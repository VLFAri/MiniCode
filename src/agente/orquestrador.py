import json
import re
from pathlib import Path

from src.agente.estado import GerenciadorEstado
from src.ferramentas.registro import RegistroFerramentas
from src.modelo.cliente_llm import LLMClient
from src.spec.gerador import GeradorSpec, limpar_cercas

FERRAMENTAS_ESCRITA = {"write_file", "create_file", "replace_text"}
FERRAMENTAS_DO_HARNESS = {"run_tests"}
MAX_VIOLACOES = 3
MAX_SAIDA = 4000
MAX_CHAMADAS_POR_TURNO = 3
LIMITE_AVISO_REPETICAO = 3
LIMITE_ABORTAR_REPETICAO = 5
MARCA_REPARO = "Os testes FALHARAM"
MAX_ARQUIVOS_NO_REPARO = 3
MAX_CHARS_POR_ARQUIVO = 2500
LIMITE_MESMO_ERRO_AVISO = 2
LIMITE_MESMO_ERRO_ABORTAR = 4

PROMPT_SISTEMA = """Você é o MiniCode, um agente de programação. Você modifica o projeto \
usando APENAS as ferramentas abaixo. Os testes são executados pelo sistema, não por você.

Ferramentas disponíveis:
{ferramentas}

Regras:
- O projeto é 100% PYTHON. Não crie arquivos de outras linguagens ou ecossistemas (nada de .js, .ts, .java, \
.go, .rb, .php, package.json, pom.xml, Cargo.toml, go.mod). Não há Node.js, Java, Go, Ruby, PHP, npm, yarn, \
pip ou qualquer instalador disponível neste ambiente: só o interpretador Python e sua biblioteca padrão.
- Use caminhos relativos à raiz do projeto.
- Depois de implementar, crie ou atualize testes pytest em tests/ (ex.: tests/test_<modulo>.py) que \
verifiquem o comportamento pedido. O sistema só aceita a tarefa se o pytest ENCONTRAR testes e todos \
passarem: um projeto sem testes conta como falha.
- Os testes importam o código a partir da raiz do projeto (ex.: from modulo import funcao).
- NÃO execute o pytest: o sistema roda os testes sozinho quando você responder finish e lhe devolve o erro.
- SEGURANÇA: NUNCA escreva em nenhum arquivo comandos ou chamadas perigosas: rm -rf, sudo, shutdown, reboot, \
kill, chmod 777, os.system, os.remove, shutil.rmtree, subprocess, eval, exec etc. O sistema recusa a gravação e \
aborta a tarefa se você insistir. Se a tarefa exigir isso, responda finish sem escrever nada.
- Os testes rodam ISOLADOS: sem rede externa (apenas loopback), sem criar processos (subprocess, os.system) \
e sem escrever fora do projeto. Código que viole isso é recusado ou falha: use mocks para HTTP/rede.
- Use APENAS a biblioteca padrão do Python (os, re, json, unittest, datetime, etc.). Bibliotecas externas \
(pandas, numpy, requests, flask...) NÃO estão instaladas no ambiente de testes e a importação falhará.
- Escreva testes SIMPLES e determinísticos. Evite rede e serviços externos; se precisar, use unittest.mock \
e lembre de importar tudo o que usar (ex.: import socket).
- Ao corrigir erros, corrija TODOS os problemas que enxergar de uma vez. Se o arquivo tiver mais de um \
problema, reescreva-o inteiro com write_file em vez de várias pequenas substituições.

Formato: responda SOMENTE com objetos JSON, um por linha, no máximo 3 por resposta (executados em ordem), \
sem texto fora do JSON:
{{"tool": "<nome>", "args": {{...}}}}

Quando terminar as alterações, responda:
{{"tool": "finish", "args": {{}}}}
"""


class Orquestrador:
    def __init__(
        self,
        tarefa: str,
        project_root=".",
        registro: RegistroFerramentas = None,
        llm: LLMClient = None,
        max_iteracoes: int = 15,
        max_reparos: int = 5,
    ):
        self.tarefa = tarefa
        self.project_root = Path(project_root).resolve()
        self.max_iteracoes = max_iteracoes
        self.estado = GerenciadorEstado(tarefa, self.project_root, max_reparos=max_reparos)
        self.minicode_dir = self.estado.minicode_dir
        self.llm = llm or LLMClient()
        self.registro = registro or RegistroFerramentas(self.project_root)
        self.gerador = GeradorSpec(self.llm, log=self.estado.log_acao)
        self.violacoes = 0


    @staticmethod
    def _extrair_chamadas(texto: str) -> list:
        texto = texto.replace("```json", "").replace("```", "")
        decoder = json.JSONDecoder()
        chamadas, pos, primeiro_erro = [], 0, None

        while len(chamadas) < MAX_CHAMADAS_POR_TURNO:
            ini = texto.find("{", pos)
            if ini == -1:
                break
            try:
                obj, fim = decoder.raw_decode(texto, ini)
            except json.JSONDecodeError as e:
                primeiro_erro = primeiro_erro or f"JSON inválido: {e}"
                pos = ini + 1
                continue
            pos = fim
            if isinstance(obj, dict) and "tool" in obj:
                chamadas.append(obj)

        if not chamadas:
            raise ValueError(primeiro_erro or "nenhuma ação JSON com o campo 'tool' foi encontrada")
        return chamadas

    @staticmethod
    def _eh_comando_de_teste(args: dict) -> bool:
        cmd = str(args.get("command", "")).strip().lower()
        return cmd.startswith(("pytest", "python -m pytest", "python3 -m pytest"))

    @staticmethod
    def _cauda(texto, limite: int) -> str:
        texto = str(texto).strip()
        if len(texto) <= limite:
            return texto
        cauda = texto[-limite:]
        if "\n" in cauda:
            cauda = cauda.split("\n", 1)[1]
        return "...\n" + cauda

    @staticmethod
    def _truncar(texto, limite: int = MAX_SAIDA) -> str:
        texto = str(texto)
        if len(texto) <= limite:
            return texto
        return texto[:limite] + f"\n... [truncado, {len(texto) - limite} caracteres omitidos]"


    def _ciclo_agente(self, messages: list) -> bool:
        permitidas = [n for n in self.registro.nomes() if n not in FERRAMENTAS_DO_HARNESS]
        historico = []

        for i in range(self.max_iteracoes):
            resposta = self.llm.chat(messages)
            messages.append({"role": "assistant", "content": resposta})

            try:
                chamadas = self._extrair_chamadas(resposta)
            except ValueError as e:
                self.estado.log_acao("format_error", error=str(e), response=resposta[:500])
                print(f"  [resposta do LLM fora do formato JSON: {e}]")
                messages.append({
                    "role": "user",
                    "content": f"Resposta inválida ({e}). Responda apenas com objetos JSON, um por linha: "
                               '{"tool": "...", "args": {...}}.',
                })
                continue

            resultados = []
            terminou = False

            for chamada in chamadas:
                nome = chamada.get("tool")
                args = chamada.get("args") or {}
                if not isinstance(args, dict):
                    args = {}

                if nome == "finish":
                    terminou = True
                    break

                if nome not in permitidas:
                    self.estado.log_acao("invalid_tool", tool=str(nome))
                    resultados.append(f"Ferramenta '{nome}' não disponível. Use uma de: {permitidas} ou 'finish'.")
                    continue

                if nome == "run_command" and self._eh_comando_de_teste(args):
                    self.estado.log_acao("blocked_test_command", command=args.get("command"))
                    print("  [run_command] BLOQUEADO: testes são executados pelo sistema")
                    resultados.append(
                        "Resultado de run_command [ERRO]: não execute o pytest. O sistema roda os testes "
                        "automaticamente quando você responder finish e lhe mostra os erros."
                    )
                    continue

                resultado = self.registro.executar(nome, args)
                ok = bool(resultado.get("ok"))
                saida = resultado.get("saida", "")
                self.estado.log_acao(
                    "tool_call", tool=nome, args=self._truncar(json.dumps(args, ensure_ascii=False), 500),
                    ok=ok, result=self._truncar(saida, 500),
                )

                print(f"  [{nome}] {'OK' if ok else 'ERRO'} {args.get('path', args.get('command', ''))}")
                if not ok:
                    print("      " + self._cauda(saida, 300).replace("\n", "\n      "))

                if ok and nome in FERRAMENTAS_ESCRITA:
                    self.estado.registrar_alteracao(args.get("path", "?"))

                if not ok and saida.startswith("BLOQUEADO pela segurança: conteúdo rejeitado"):
                    self.violacoes += 1
                    self.estado.log_acao("security_violation", tool=nome, count=self.violacoes)
                    if self.violacoes >= MAX_VIOLACOES:
                        raise RuntimeError(
                            f"Abortado por segurança: {self.violacoes} tentativas de gravar código perigoso."
                        )

                resultados.append(f"Resultado de {nome} [{'OK' if ok else 'ERRO'}]:\n{self._truncar(saida)}")
                historico.append(f"{nome}:{json.dumps(args, sort_keys=True, ensure_ascii=False)}")

            if terminou:
                self.estado.log_acao("finish", iteration=i + 1)
                return True

            if historico:
                repeticoes = 1
                while repeticoes < len(historico) and historico[-1 - repeticoes] == historico[-1]:
                    repeticoes += 1
                if repeticoes >= LIMITE_ABORTAR_REPETICAO:
                    self.estado.log_acao("loop_detected", action=historico[-1][:200], repetitions=repeticoes)
                    print(f"  [loop detectado: a mesma ação foi repetida {repeticoes}x; encerrando o ciclo]")
                    return False
                if repeticoes >= LIMITE_AVISO_REPETICAO:
                    resultados.append(
                        f"AVISO: você repetiu a mesma ação {repeticoes} vezes com o mesmo resultado. "
                        "Mude de abordagem (leia o arquivo, corrija o código) ou responda finish."
                    )

            messages.append({"role": "user", "content": "\n\n".join(resultados)})

        self.estado.log_acao("iteration_limit", limit=self.max_iteracoes)
        return False

    def _snapshot_arquivos(self, saida_testes: str) -> str:
        alterados = sorted(self.estado.arquivos_alterados, key=lambda p: (p not in saida_testes, p))
        partes = []
        for caminho in alterados[:MAX_ARQUIVOS_NO_REPARO]:
            res = self.registro.executar("read_file", {"path": caminho})
            if res.get("ok"):
                partes.append(f"### {caminho}\n{self._truncar(res.get('saida', ''), MAX_CHARS_POR_ARQUIVO)}")
        return "\n\n".join(partes)

    @staticmethod
    def _podar_feedbacks_antigos(messages: list):
        for m in messages:
            if m["role"] == "user" and m["content"].startswith(MARCA_REPARO):
                m["content"] = "[feedback de reparo anterior omitido; veja o mais recente abaixo]"

    @staticmethod
    def _assinatura_erro(saida: str) -> str:
        """
        Resume a FALHA (não a saída inteira) para comparar reparos consecutivos: as linhas que o
        pytest marca com 'E ' (a exceção e sua mensagem) mais a lista de testes que falharam,
        ignorando números de linha e espaços, que mudam a cada reescrita sem mudar a causa.
        """
        linhas_e = re.findall(r"^E\s+(.*)$", saida, flags=re.MULTILINE)
        falharam = re.findall(r"^FAILED\s+(\S+)", saida, flags=re.MULTILINE)
        resumo = " | ".join(linhas_e[:6]) + " :: " + ",".join(sorted(falharam))
        return re.sub(r"\s+", " ", re.sub(r"\b\d+\b", "N", resumo)).strip()

    def _verificar_arquivos_alterados(self):
        for caminho in sorted(self.estado.arquivos_alterados):
            res = self.registro.executar("read_file", {"path": caminho})
            if not res.get("ok"):
                continue
            achados = self.registro.ctx.conteudo.problemas(caminho, res.get("saida", ""))
            if achados:
                raise RuntimeError(
                    f"Testes não executados: '{caminho}' contém código perigoso ({'; '.join(achados)})."
                )

    def _executar_testes(self) -> tuple:
        self._verificar_arquivos_alterados()
        res = self.registro.executar("run_tests", {})
        if not res.get("ok"):
            raise RuntimeError(f"Não foi possível executar os testes: {res.get('saida', '')}")
        passou = bool(res.get("passou"))
        saida = res.get("saida", "")
        self.estado.registrar_testes(passou, saida)
        return passou, saida, res.get("codigo")


    def executar(self) -> bool:
        print(f"\n=== [MiniCode] Tarefa: '{self.tarefa}' ===")
        print(f"Projeto: {self.project_root}")

        try:
            perigos = self.registro.ctx.conteudo.perigos_em_texto(self.tarefa)
            if perigos:
                self.estado.log_acao("request_refused", reasons=perigos)
                raise RuntimeError("Pedido recusado por segurança: " + "; ".join(perigos) + ".")

            contexto = self.registro.executar("list_files", {}).get("saida", "")

            print("A gerar especificação...")
            spec = self.gerador.gerar_spec(self.tarefa, contexto)
            (self.minicode_dir / "specification.md").write_text(spec, encoding="utf-8")
            self.estado.mudar_estado("SPECIFIED")

            print("A gerar plano...")
            plano = self.gerador.gerar_plano(spec, contexto)
            (self.minicode_dir / "plan.md").write_text(plano, encoding="utf-8")
            self.estado.mudar_estado("PLANNED")

            self.estado.mudar_estado("IMPLEMENTING")
            messages = [
                {"role": "system", "content": PROMPT_SISTEMA.format(
                    ferramentas=self.registro.descricoes(excluir=FERRAMENTAS_DO_HARNESS))},
                {"role": "user", "content": (
                    f"Tarefa: {self.tarefa}\n\n{spec}\n\nPlano:\n{plano}\n\n"
                    f"Arquivos do projeto:\n{contexto}\n\nComece a implementação."
                )},
            ]
            self._ciclo_agente(messages)

            assinatura_anterior, repeticoes_mesmo_erro = None, 0
            while True:
                self.estado.mudar_estado("VERIFYING")
                print("A executar testes...")
                passou, saida, codigo = self._executar_testes()

                if passou:
                    self.estado.mudar_estado("DONE")
                    break

                assinatura = self._assinatura_erro(saida)
                if assinatura and assinatura == assinatura_anterior:
                    repeticoes_mesmo_erro += 1
                else:
                    repeticoes_mesmo_erro = 1
                assinatura_anterior = assinatura

                if repeticoes_mesmo_erro >= LIMITE_MESMO_ERRO_ABORTAR:
                    self.estado.falhar(
                        f"O mesmo erro se repetiu em {repeticoes_mesmo_erro} reparos seguidos sem ser "
                        "corrigido; abortado para não desperdiçar tentativas."
                    )
                    self.estado.log_acao("same_error_abort", signature=assinatura[:300], count=repeticoes_mesmo_erro)
                    break

                if self.estado.tentativas_reparo >= self.estado.max_reparos:
                    self.estado.falhar(
                        f"Testes continuam falhando após {self.estado.tentativas_reparo} reparo(s)."
                    )
                    break

                self.estado.mudar_estado("REPAIRING")
                print(f"Testes falharam. Reparo {self.estado.tentativas_reparo}/{self.estado.max_reparos}...")
                print("  " + self._cauda(saida, 700).replace("\n", "\n  "))
                modulo_ausente = re.search(r"No module named '([\w.]+)'", saida)
                if codigo == 5:
                    feedback = (
                        "O pytest NÃO ENCONTROU NENHUM TESTE, e sem testes a tarefa não pode ser aceita. "
                        "Crie agora um arquivo de testes pytest, por exemplo tests/test_<modulo>.py, com "
                        "funções test_* que verifiquem o que foi pedido (importando o código da raiz do "
                        "projeto), e responda 'finish' ao terminar."
                    )
                elif modulo_ausente:
                    feedback = (
                        f"A biblioteca '{modulo_ausente.group(1)}' NÃO está instalada e NUNCA estará: o "
                        "ambiente de testes só tem a biblioteca padrão do Python. Reescreva o código e os "
                        "testes (com write_file) sem usar essa biblioteca, usando apenas módulos padrão "
                        "(ou unittest.mock quando precisar simular algo), e responda 'finish' ao terminar."
                    )
                else:
                    aviso_repeticao = ""
                    if repeticoes_mesmo_erro >= LIMITE_MESMO_ERRO_AVISO:
                        aviso_repeticao = (
                            f"\nATENÇÃO: este é O MESMO ERRO de {repeticoes_mesmo_erro} tentativas seguidas — "
                            "sua última alteração NÃO corrigiu a causa raiz, só mudou algo próximo do sintoma. "
                            "Pare de fazer ajustes pontuais nesse mesmo ponto. Leia o traceback com atenção: "
                            "ele diz o tipo da exceção e a linha exata. Se necessário, reescreva a função "
                            "inteira do zero com uma lógica diferente, em vez de repetir a mesma tentativa.\n"
                        )
                    feedback = (
                        f"{MARCA_REPARO} (tentativa de reparo {self.estado.tentativas_reparo}/"
                        f"{self.estado.max_reparos}).{aviso_repeticao} Saída do pytest:\n"
                        f"{self._truncar(saida, 3000)}\n\n"
                        f"Conteúdo ATUAL dos arquivos que você alterou:\n{self._snapshot_arquivos(saida)}\n\n"
                        "Identifique TODOS os problemas (imports faltando, nomes errados, asserções incorretas), "
                        "corrija-os de uma vez e responda 'finish' ao terminar."
                    )
                self._podar_feedbacks_antigos(messages)
                messages.append({"role": "user", "content": feedback})
                self._ciclo_agente(messages)

        except KeyboardInterrupt:
            self.estado.falhar("Interrompido pelo usuário (Ctrl+C)")
            print("\n⏹  Execução interrompida. O estado foi salvo em .minicode/state.json.")
        except Exception as e:
            self.estado.falhar(str(e))
            print(f"\n❌ [Erro Crítico] O agente falhou: {e}")

        sucesso = self.estado.estado_atual == "DONE"
        metricas = {
            "success": sucesso,
            "first_attempt_success": sucesso and self.estado.tentativas_reparo == 0,
        }
        metricas.update(self.llm.metricas())
        self.estado.salvar_estado(metricas)

        if sucesso:
            print("\n🎉 Tarefa concluída e verificada com sucesso.")
        return sucesso