"""Dataset para especializar um modelo pequeno na GERAÇÃO DE ESPECIFICAÇÕES do MiniCode.

Princípios (cada um corrige um problema do script anterior):
  1. O prompt do aluno é EXATAMENTE o `PROMPT_SPEC` do agente (mesmo template, contexto no mesmo formato de
     `list_files`). Treino e inferência veem a mesma entrada. Sem fallback silencioso: se o import falhar, o
     script falha.
  2. O teacher (Qwen-14B) recebe, além do prompt, um system prompt PRIVILEGIADO com as restrições do harness
     (só stdlib, pytest, sem código de implementação...). O aluno não vê esse system prompt: ele aprende a
     produzir a resposta "como se" soubesse das regras (destilação de contexto).
  3. Só entram specs que passam na validação ESTRITA (formato do agente + conteúdo), com reamostragem.
  4. Sementes fora do escopo do harness, quase duplicadas ou vindas do enunciado ficam de fora (e são listadas).
  5. A divisão train/val/test é por TAREFA.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

from src.spec.gerador import PROMPT_SPEC
from src.spec.qualidade import sem_cerca_externa, validar_spec_estrita

SYSTEM_TEACHER = """Você escreve especificações técnicas para um agente de programação (Spec-Driven Development).

Ambiente onde o código será implementado e testado:
- Python 3 com SOMENTE a biblioteca padrão; nada de instalar pacotes, rede, bancos ou serviços externos (se a tarefa citar algo assim, simule em memória com a biblioteca padrão).
- A verificação é feita com pytest, sem interface gráfica.

Regras da especificação:
- Escreva em português, em Markdown, EXATAMENTE com as seções: "# Specification", "## Objective", "## Parameters / Requirements" e "## Acceptance Criteria", nessa ordem.
- Defina o nome do arquivo/módulo, os nomes e as assinaturas (com tipos) das funções ou classes, e o comportamento em casos de borda e de erro (qual exceção).
- Em "Acceptance Criteria" liste de 4 a 8 critérios verificáveis por testes automatizados; cada um com um exemplo concreto de entrada e saída entre crases, por exemplo: `soma(2, 3)` retorna `5`.
- NÃO inclua código de implementação: nada de corpos de função nem blocos de código com lógica. Descreva só o comportamento.
- Responda apenas com a especificação, sem texto antes nem depois."""

PROMPT_EXPANDIR = """Gere {n} pedidos de programação NOVOS, um por linha, sem numeração nem marcadores, em português.
Cada pedido deve ser uma tarefa pequena, verificável por testes automatizados e implementável só com a biblioteca padrão do Python (sem frameworks, rede ou bancos externos). Varie as categorias: algoritmos, estruturas de dados, validação de dados, manipulação de strings, utilitários, classes pequenas, correção de bug em código existente, refatoração.

Exemplos do estilo desejado:
{exemplos}

Não repita assuntos já cobertos."""

# --- sementes que não servem para treinar este agente -------------------------------------------
RESERVADAS_ENUNCIADO = re.compile(r"fatorial|GET\s*/users|/health", re.IGNORECASE)
FORA_DE_ESCOPO_TAREFA = re.compile(
    r"fastapi|flask|django|pydantic|redis|\bs3\b|\bpdf\b|\bjwt\b|nullpointer|numpy|pandas|boto|\bjava\b|node|npm|react",
    re.IGNORECASE)

# Formatos plausíveis da saída de `list_files` (ver tools.ListFiles); "(vazio)" é o mais comum
CONTEXTOS = ["(vazio)"] * 3 + [
    "README.md", "main.py", "main.py\ntests/test_main.py",
    "src/__init__.py\nsrc/main.py\ntests/test_main.py", "utils.py\ntests/test_utils.py",
    "app.py\nmodels.py\ntests/test_app.py",
]


def _palavras(t: str) -> set:
    return set(re.findall(r"\w+", t.lower()))


def similaridade(a: str, b: str) -> float:
    pa, pb = _palavras(a), _palavras(b)
    return len(pa & pb) / len(pa | pb) if pa | pb else 0.0


def carregar_tarefas(caminhos: list) -> list:
    tarefas = []
    for c in map(Path, caminhos):
        if not c.exists():
            raise FileNotFoundError(f"arquivo de tarefas não encontrado: {c}")
        tarefas += [l.strip() for l in c.read_text(encoding="utf-8").splitlines()
                    if l.strip() and not l.strip().startswith("#")]
    return tarefas


def filtrar_sementes(tarefas: list, limite_similaridade: float = 0.8) -> tuple:
    """(válidas, {motivo: [tarefas]}). Mantém a primeira de cada grupo de quase duplicadas."""
    validas, excluidas = [], defaultdict(list)
    for t in tarefas:
        if RESERVADAS_ENUNCIADO.search(t):
            excluidas["reservada_do_enunciado"].append(t)
        elif FORA_DE_ESCOPO_TAREFA.search(t):
            excluidas["fora_do_escopo_stdlib"].append(t)
        elif any(similaridade(t, v) >= limite_similaridade for v in validas):
            excluidas["quase_duplicada"].append(t)
        else:
            validas.append(t)
    return validas, dict(excluidas)


def contexto_para(tarefa: str, k: int, seed: int) -> str:
    base = int(hashlib.sha256(f"{seed}|{tarefa}".encode()).hexdigest(), 16)
    return CONTEXTOS[(base + k) % len(CONTEXTOS)]


def montar_itens(tarefas: list, contextos_por_tarefa: int, seed: int) -> list:
    return [(t, contexto_para(t, k, seed)) for t in tarefas for k in range(contextos_por_tarefa)]


# --- teachers ---------------------------------------------------------------------------------
class TeacherOllama:
    """Qwen local via API compatível com OpenAI do Ollama. modelo="auto" usa o MAIOR Qwen instalado."""

    def __init__(self, modelo: str = "auto", temperatura: float = 0.4, timeout: int = 300,
                 url: str = "http://localhost:11434/v1/chat/completions"):
        self.temperatura, self.timeout, self.url = temperatura, timeout, url
        if modelo == "auto":
            from src.modelo.descoberta import escolher_modelo_qwen, listar_modelos, tamanho_em_bilhoes
            base = url.rsplit("/chat/completions", 1)[0]
            modelo = escolher_modelo_qwen(listar_modelos(base))
            if not modelo:
                raise ValueError(f"nenhum modelo Qwen encontrado em {base}: o Ollama está rodando (`ollama serve`)? "
                                 "Instale um (`ollama pull qwen2.5-coder:7b`) ou informe --ollama-modelo <nome>")
            print(f"teacher local: {modelo}")
            if tamanho_em_bilhoes(modelo) and tamanho_em_bilhoes(modelo) <= 3:
                print("  AVISO: teacher pequeno (<= 3B). Se o aluno for o 1.5B, os rótulos não serão melhores que o "
                      "que ele já produz (autodestilação); prefira um modelo maior.")
        self.modelo = modelo

    def complete(self, prompt: str, system_prompt: str = None) -> str:
        msgs = ([{"role": "system", "content": system_prompt}] if system_prompt else []) + \
               [{"role": "user", "content": prompt}]
        corpo = json.dumps({"model": self.modelo, "messages": msgs, "temperature": self.temperatura}).encode()
        req = urllib.request.Request(self.url, data=corpo, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                return json.loads(r.read().decode())["choices"][0]["message"]["content"]
        except urllib.error.HTTPError as e:
            raise RuntimeError(f"o Ollama respondeu {e.code} para o modelo '{self.modelo}': "
                               f"{e.read()[:200].decode(errors='replace')} (ele está instalado? veja `ollama list`)") from e
        except urllib.error.URLError as e:
            raise RuntimeError(f"falha de conexão com o Ollama em {self.url}: {e.reason}") from e


class Teacher14B:
    """Qwen-14B do endpoint da disciplina (credencial via MINICODE_API_KEY)."""

    def __init__(self, temperatura: float = 0.4):
        from src.modelo.cliente_llm import LLMClient
        self.llm = LLMClient(temperature=temperatura, max_tokens=2048)

    def complete(self, prompt: str, system_prompt: str = None) -> str:
        return self.llm.complete(prompt, system_prompt=system_prompt)


def criar_teacher(nome: str, ollama_modelo: str):
    return Teacher14B() if nome == "llm14b" else TeacherOllama(ollama_modelo)


# --- etapa 0 (opcional): mais sementes ---------------------------------------------------------
def expandir_sementes(teacher, alvo: int, existentes: list, seed: int = 42, rodadas: int = 10, por_rodada: int = 25) -> list:
    """Pede ao teacher tarefas novas até somar `alvo`, descartando as fora de escopo e as parecidas."""
    rng = random.Random(seed)
    atuais = list(existentes)
    novas = []
    for _ in range(rodadas):
        if len(novas) >= alvo:
            break
        exemplos = "\n".join(rng.sample(existentes, min(12, len(existentes))))
        bruto = teacher.complete(PROMPT_EXPANDIR.format(n=por_rodada, exemplos=exemplos))
        candidatas = [re.sub(r"^\s*(?:[-*•]|\d+[.)])\s*", "", l).strip() for l in bruto.splitlines()]
        validas, _ = filtrar_sementes(atuais + [c for c in candidatas if len(c) >= 20])
        aceitas = validas[len(atuais):]          # filtrar_sementes mantém a ordem: as novas vêm depois
        novas += aceitas
        atuais += aceitas
    return novas[:alvo]


# --- etapa 1: geração bruta com cache ------------------------------------------------------------
def ler_cache(caminho: Path) -> dict:
    cache = defaultdict(list)
    if caminho.exists():
        for l in caminho.read_text(encoding="utf-8").splitlines():
            if l.strip():
                r = json.loads(l)
                cache[(r["task"], r["contexto"])].append(r)
    return cache


def gerar_dados_brutos(itens: list, teacher, caminho_cache: Path, max_tentativas: int = 3,
                       teacher_nome: str = "") -> None:
    """Para cada (tarefa, contexto): amostra specs até uma passar na validação estrita (ou esgotar as tentativas).
    Cada tentativa é gravada: reexecutar retoma de onde parou e o log mostra por que specs foram recusadas."""
    cache = ler_cache(caminho_cache)
    falhas_seguidas = 0
    with open(caminho_cache, "a", encoding="utf-8") as f:
        for i, (tarefa, ctx) in enumerate(itens, 1):
            feitas = cache.get((tarefa, ctx), [])
            if len(feitas) >= max_tentativas or any(not validar_spec_estrita(t["raw_spec"]) for t in feitas):
                continue
            print(f"[{i}/{len(itens)}] {tarefa[:80]}")
            prompt = PROMPT_SPEC.format(tarefa=tarefa, contexto=ctx)
            problemas = validar_spec_estrita(feitas[-1]["raw_spec"]) if feitas else []
            for n in range(len(feitas) + 1, max_tentativas + 1):
                extra = f"\n\nA tentativa anterior foi rejeitada: {'; '.join(problemas)}. Corrija." if problemas else ""
                try:
                    bruto = teacher.complete(prompt + extra, SYSTEM_TEACHER)
                except Exception as e:
                    falhas_seguidas += 1
                    print(f"  [ERRO] {e}")
                    if falhas_seguidas >= 3:
                        raise RuntimeError("teacher inacessível (3 falhas seguidas); verifique chave/rede/Ollama") from e
                    break
                falhas_seguidas = 0
                f.write(json.dumps({"task": tarefa, "contexto": ctx, "attempt": n, "teacher": teacher_nome,
                                    "raw_spec": bruto}, ensure_ascii=False) + "\n")
                f.flush()
                problemas = validar_spec_estrita(bruto)
                if not problemas:
                    break


# --- etapa 2: filtro, formato de chat e split por tarefa --------------------------------------------------
def dividir_por_tarefa(tarefas: list, seed: int, frac_val: float, frac_test: float) -> dict:
    """Divide por TAREFA: variações da mesma tarefa nunca ficam em splits diferentes."""
    tarefas = sorted(set(tarefas))
    random.Random(seed).shuffle(tarefas)
    n = len(tarefas)
    n_test = max(1, round(n * frac_test)) if n >= 3 else 0
    n_val = max(1, round(n * frac_val)) if n >= 3 else 0
    return {"test": tarefas[:n_test], "val": tarefas[n_test:n_test + n_val], "train": tarefas[n_test + n_val:]}


def tratar_e_dividir(itens: list, caminho_cache: Path, pasta_saida: Path, seed: int = 42,
                     frac_val: float = 0.10, frac_test: float = 0.15) -> dict:
    cache = ler_cache(caminho_cache)
    pasta_saida.mkdir(parents=True, exist_ok=True)
    linhas, motivos, primeira_valida, sem_geracao = [], Counter(), [], 0
    for tarefa, ctx in itens:
        tentativas = sorted(cache.get((tarefa, ctx), []), key=lambda r: r["attempt"])
        if not tentativas:
            sem_geracao += 1
            continue
        problemas_por_tentativa = [validar_spec_estrita(t["raw_spec"]) for t in tentativas]
        primeira_valida.append(not problemas_por_tentativa[0])
        aceita = next((t for t, p in zip(tentativas, problemas_por_tentativa) if not p), None)
        if aceita is None:
            motivos.update(problemas_por_tentativa[-1])
            continue
        spec = sem_cerca_externa(aceita["raw_spec"])
        while "\n\n\n" in spec:
            spec = spec.replace("\n\n\n", "\n\n")
        linhas.append({
            "task": tarefa, "contexto": ctx,
            "messages": [{"role": "user", "content": PROMPT_SPEC.format(tarefa=tarefa, contexto=ctx)},
                         {"role": "assistant", "content": spec}],
        })

    divisao = dividir_por_tarefa([l["task"] for l in linhas], seed, frac_val, frac_test)
    stats = {
        "itens": len(itens), "sem_geracao": sem_geracao, "itens_validos": len(linhas),
        "descartados_por_motivo": dict(motivos),
        "teacher_primeira_tentativa_valida": (sum(primeira_valida) / len(primeira_valida)) if primeira_valida else None,
        "splits": {},
    }
    for nome, tarefas in divisao.items():
        conjunto = set(tarefas)
        linhas_split = [l for l in linhas if l["task"] in conjunto]
        (pasta_saida / f"{nome}.jsonl").write_text(
            "".join(json.dumps(l, ensure_ascii=False) + "\n" for l in linhas_split), encoding="utf-8")
        tam = [len(l["messages"][1]["content"]) / 3.2 for l in linhas_split]   # ~tokens
        stats["splits"][nome] = {"tarefas": len(tarefas), "exemplos": len(linhas_split),
                                 "tokens_resposta_medio": round(sum(tam) / len(tam)) if tam else 0}
    (pasta_saida / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    return stats


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Gera train/validation/test de especificações a partir de tarefas-semente")
    ap.add_argument("--tarefas", nargs="+", default=["tarefas_semente.txt"])
    ap.add_argument("--cache", default="raw_specs.jsonl")
    ap.add_argument("--saida", default="dataset_tratado")
    ap.add_argument("--teacher", choices=["llm14b", "ollama"], default="llm14b",
                    help="llm14b = endpoint da disciplina (MINICODE_API_KEY); ollama = modelo local")
    ap.add_argument("--ollama-modelo", default="auto",
                    help="nome do `ollama list`; 'auto' usa o maior Qwen instalado (use um MAIOR que o aluno)")
    ap.add_argument("--etapa", choices=["gerar", "tratar", "tudo"], default="tudo")
    ap.add_argument("--tentativas", type=int, default=3)
    ap.add_argument("--contextos-por-tarefa", type=int, default=1)
    ap.add_argument("--expandir", type=int, default=0, help="pede ao teacher N tarefas novas (salvas em tarefas_expandidas.txt)")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--frac-val", type=float, default=0.10)
    ap.add_argument("--frac-test", type=float, default=0.15)
    args = ap.parse_args(argv)

    teacher = None
    if args.etapa in ("gerar", "tudo"):
        try:
            teacher = criar_teacher(args.teacher, args.ollama_modelo)
        except (ValueError, ImportError) as e:
            print(f"Não foi possível preparar o teacher '{args.teacher}': {type(e).__name__}: {e}\n"
                  "  - Qwen-14B da disciplina: defina MINICODE_API_KEY (e `pip install -r requirements.txt`).\n"
                  "  - Qwen que você já tem instalado: python gerar_datasets.py --teacher ollama "
                  "[--ollama-modelo <nome do `ollama list`>]\n"
                  "  - Só refazer filtro/split de um raw_specs.jsonl existente: --etapa tratar")
            return 2

    try:
        tarefas = carregar_tarefas(args.tarefas)
    except FileNotFoundError as e:
        print(f"{e}\n  pasta atual : {Path.cwd()}\n  código em   : {Path(__file__).resolve().parents[2]}\n"
              "  Rode na raiz do repositório (onde está tarefas_semente.txt) ou informe --tarefas <caminho>.")
        return 2
    validas, excluidas = filtrar_sementes(tarefas)
    if args.expandir and teacher:
        novas = expandir_sementes(teacher, args.expandir, validas, args.seed)
        Path("tarefas_expandidas.txt").write_text("\n".join(novas) + "\n", encoding="utf-8")
        validas += novas
        print(f"{len(novas)} tarefas novas geradas (tarefas_expandidas.txt)")
    print(f"sementes: {len(tarefas)} lidas, {len(validas)} usadas; excluídas: "
          f"{ {m: len(v) for m, v in excluidas.items()} }")
    itens = montar_itens(validas, args.contextos_por_tarefa, args.seed)

    if teacher:
        nome = args.teacher if args.teacher == "llm14b" else f"ollama:{args.ollama_modelo}"
        gerar_dados_brutos(itens, teacher, Path(args.cache), args.tentativas, nome)
    if args.etapa in ("tratar", "tudo"):
        stats = tratar_e_dividir(itens, Path(args.cache), Path(args.saida), args.seed, args.frac_val, args.frac_test)
        stats["sementes_excluidas"] = excluidas
        (Path(args.saida) / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nválidos: {stats['itens_validos']}/{stats['itens']} | teacher 1ª tentativa válida: "
              f"{stats['teacher_primeira_tentativa_valida']}")
        print("motivos de descarte:", stats["descartados_por_motivo"])
        for nome, d in stats["splits"].items():
            print(f"  {nome:<5} tarefas={d['tarefas']:<4} exemplos={d['exemplos']:<4} ~tokens/resposta={d['tokens_resposta_medio']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
