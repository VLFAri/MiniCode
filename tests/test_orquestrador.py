import json

import pytest
from src.agente.orquestrador import PROMPT_SISTEMA, Orquestrador
from tests.test_gerador import SPEC_OK

TESTE_SOMA = "from soma import soma\n\ndef test_soma():\n    assert soma(2, 3) == 5\n"


def chamada(tool, **args):
    return json.dumps({"tool": tool, "args": args})


class FakeLLM:
    def __init__(self, respostas_chat):
        self.respostas_chat = list(respostas_chat)
        self.chamadas = 0

    def complete(self, prompt, system_prompt=None):
        self.chamadas += 1
        return SPEC_OK if "Specification" in prompt and "Pedido" in prompt else "1. implementar\n2. testar"

    def chat(self, messages, **kw):
        self.chamadas += 1
        return self.respostas_chat.pop(0) if self.respostas_chat else chamada("finish")

    def metricas(self):
        return {"llm_calls": self.chamadas, "prompt_tokens": 0, "completion_tokens": 0}


class LLMEspiao(FakeLLM):
    def __init__(self, respostas):
        super().__init__(respostas)
        self.historicos = []

    def chat(self, messages, **kw):
        self.historicos.append([dict(m) for m in messages])
        return super().chat(messages, **kw)


@pytest.fixture
def projeto(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_soma.py").write_text(TESTE_SOMA)
    return tmp_path


def estado_json(projeto):
    return json.loads((projeto / ".minicode" / "state.json").read_text())


def acoes(projeto):
    return [json.loads(l) for l in (projeto / ".minicode" / "actions.jsonl").read_text().splitlines()]


def test_sucesso_na_primeira_tentativa(projeto):
    llm = FakeLLM([chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n"),
                   chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    s = estado_json(projeto)
    assert s["state"] == "DONE" and s["first_attempt_success"] is True and s["repair_attempts"] == 0
    assert s["files_changed"] == ["soma.py"]
    assert (projeto / ".minicode" / "specification.md").exists() and (projeto / ".minicode" / "plan.md").exists()


def test_repair_loop_corrige_erro(projeto):
    llm = FakeLLM([
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a - b\n"), chamada("finish"),
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n"), chamada("finish"),
    ])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    s = estado_json(projeto)
    assert s["repair_attempts"] == 1 and s["first_attempt_success"] is False and s["tests_run"] == 2
    estados = [a["to"] for a in acoes(projeto) if a["type"] == "transition"]
    assert estados == ["SPECIFIED", "PLANNED", "IMPLEMENTING", "VERIFYING", "REPAIRING", "VERIFYING", "DONE"]


def test_falha_apos_limite_de_reparos(projeto):
    erro = chamada("write_file", path="soma.py", content="def soma(a, b):\n    return 0\n")
    llm = FakeLLM([erro, chamada("finish")] * 5)
    assert Orquestrador("soma", projeto, llm=llm, max_reparos=2).executar() is False
    s = estado_json(projeto)
    assert s["state"] == "FAILED" and s["repair_attempts"] == 2 and "reparo" in s["error"]


def test_llm_nao_consegue_chamar_run_tests(projeto):
    llm = FakeLLM([chamada("run_tests"), chamada("finish")] * 3)
    Orquestrador("soma", projeto, llm=llm, max_reparos=1).executar()
    assert any(a["type"] == "invalid_tool" for a in acoes(projeto))
    assert not any(a["type"] == "tool_call" and a["tool"] == "run_tests" for a in acoes(projeto))


def test_comando_perigoso_do_llm_e_bloqueado(projeto):
    llm = FakeLLM([chamada("run_command", command="rm -rf /"), chamada("finish")] * 3)
    Orquestrador("soma", projeto, llm=llm, max_reparos=1).executar()
    chamadas = [a for a in acoes(projeto) if a["type"] == "tool_call" and a["tool"] == "run_command"]
    assert chamadas and not any(a["ok"] for a in chamadas)


def test_resposta_malformada_e_limite_de_iteracoes(projeto):
    llm = FakeLLM(["não sou json"] * 50)
    Orquestrador("soma", projeto, llm=llm, max_iteracoes=3, max_reparos=0).executar()
    a = acoes(projeto)
    assert sum(1 for x in a if x["type"] == "format_error") >= 3
    assert any(x["type"] == "iteration_limit" for x in a)
    assert estado_json(projeto)["state"] == "FAILED"


def test_falha_do_llm_leva_a_failed(projeto):
    class LLMQuebrado(FakeLLM):
        def complete(self, prompt, system_prompt=None):
            raise ConnectionError("endpoint fora do ar")

    Orquestrador("soma", projeto, llm=LLMQuebrado([])).executar()
    s = estado_json(projeto)
    assert s["state"] == "FAILED" and "endpoint" in s["error"]


def test_projeto_sem_testes_agente_cria_testes_e_conclui(tmp_path):
    codigo = chamada("create_file", path="calculadora.py", content="def somar(a, b):\n    return a + b\n")
    testes = chamada("create_file", path="tests/test_calculadora.py",
                     content="from calculadora import somar\n\ndef test_somar():\n    assert somar(1, 2) == 3\n")
    llm = FakeLLM([codigo, chamada("finish"), testes, chamada("finish")])
    assert Orquestrador("Crie calculadora.py", tmp_path, llm=llm).executar() is True
    s = estado_json(tmp_path)
    assert s["state"] == "DONE" and s["repair_attempts"] == 1
    assert (tmp_path / "calculadora.py").exists() and (tmp_path / "tests" / "test_calculadora.py").exists()


def test_aviso_de_nenhum_teste_e_enviado_ao_llm(tmp_path):
    vistos = []

    class Espiao(FakeLLM):
        def chat(self, messages, **kw):
            vistos.append(messages[-1]["content"])
            return chamada("finish")

    Orquestrador("x", tmp_path, llm=Espiao([]), max_reparos=1).executar()
    assert any("NENHUM TESTE" in v for v in vistos)


def test_prompt_exige_criacao_de_testes():
    assert "tests/" in PROMPT_SISTEMA and "pytest" in PROMPT_SISTEMA


def test_extrai_varias_acoes_na_mesma_resposta():
    texto = '{"tool": "read_file", "args": {"path": "a.py"}}\n{"tool": "finish", "args": {}}'
    assert [c["tool"] for c in Orquestrador._extrair_chamadas(texto)] == ["read_file", "finish"]


def test_extrai_acao_com_cercas_e_texto_solto():
    texto = 'Vou criar o arquivo:\n```json\n{"tool": "write_file", "args": {"path": "a.py", "content": "x = {1: 2}\\n"}}\n```\nPronto!'
    chamadas = Orquestrador._extrair_chamadas(texto)
    assert len(chamadas) == 1 and chamadas[0]["args"]["content"] == "x = {1: 2}\n"


def test_extrai_no_maximo_tres_acoes_e_rejeita_lixo():
    texto = "\n".join('{"tool": "list_files", "args": {}}' for _ in range(6))
    assert len(Orquestrador._extrair_chamadas(texto)) == 3
    for ruim in ["sem json", '{"sem_tool": 1}', '{"tool": ']:
        with pytest.raises(ValueError):
            Orquestrador._extrair_chamadas(ruim)


def test_duas_acoes_numa_resposta_sao_executadas_em_ordem(projeto):
    duas = (chamada("create_file", path="soma.py", content="def soma(a, b):\n    return a + b\n")
            + "\n" + chamada("create_file", path="LEIA.md", content="ok\n"))
    llm = FakeLLM([duas, chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    assert (projeto / "soma.py").exists() and (projeto / "LEIA.md").exists()
    assert not any(a["type"] == "format_error" for a in acoes(projeto))


def test_pytest_via_run_command_e_bloqueado_pelo_harness(projeto):
    llm = FakeLLM([chamada("run_command", command="pytest tests/test_soma.py"), chamada("finish")] * 3)
    Orquestrador("soma", projeto, llm=llm, max_reparos=1).executar()
    a = acoes(projeto)
    assert any(x["type"] == "blocked_test_command" for x in a)
    assert not any(x["type"] == "tool_call" and x["tool"] == "run_command" for x in a)


def test_loop_de_acao_repetida_encerra_o_ciclo(projeto):
    llm = FakeLLM([chamada("read_file", path="nao_existe.py")] * 30)
    Orquestrador("soma", projeto, llm=llm, max_iteracoes=15, max_reparos=0).executar()
    a = acoes(projeto)
    assert any(x["type"] == "loop_detected" for x in a)
    assert sum(1 for x in a if x["type"] == "tool_call") < 15


def test_ctrl_c_salva_estado_e_nao_propaga(projeto):
    class LLMInterrompido(FakeLLM):
        def chat(self, messages, **kw):
            raise KeyboardInterrupt

    assert Orquestrador("soma", projeto, llm=LLMInterrompido([])).executar() is False
    s = estado_json(projeto)
    assert s["state"] == "FAILED" and "Ctrl+C" in s["error"]


def test_feedback_de_reparo_traz_o_conteudo_atual_dos_arquivos(projeto):
    llm = LLMEspiao([
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a - b\n"), chamada("finish"),
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n"), chamada("finish"),
    ])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    feedback = next(m["content"] for m in llm.historicos[-1] if m["content"].startswith("Os testes FALHARAM"))
    assert "### soma.py" in feedback and "return a - b" in feedback
    assert "TODOS os problemas" in feedback


def test_feedbacks_antigos_sao_podados(projeto):
    erro = chamada("write_file", path="soma.py", content="def soma(a, b):\n    return 0\n")
    llm = LLMEspiao([erro, chamada("finish")] * 6)
    Orquestrador("soma", projeto, llm=llm, max_reparos=3).executar()
    ultimo = llm.historicos[-1]
    completos = [m for m in ultimo if m["content"].startswith("Os testes FALHARAM")]
    omitidos = [m for m in ultimo if "omitido" in m["content"]]
    assert len(completos) == 1 and len(omitidos) >= 1


def test_padrao_de_reparos_e_cinco(tmp_path):
    assert Orquestrador("x", tmp_path, llm=FakeLLM([])).estado.max_reparos == 5


def test_guarda_indisponivel_leva_a_failed_sem_reparos(tmp_path):
    from src.ferramentas.registro import RegistroFerramentas
    reg = RegistroFerramentas(tmp_path)
    reg.ctx._sandbox_ok = False
    assert Orquestrador("x", tmp_path, registro=reg, llm=FakeLLM([])).executar() is False
    s = estado_json(tmp_path)
    assert s["state"] == "FAILED" and "executar os testes" in s["error"] and s["repair_attempts"] == 0


def test_modulo_ausente_gera_feedback_especifico_em_vez_de_loop(projeto):
    import re
    nome_modulo = "biblioteca_que_nao_existe_xyz"
    chamadas_llm = []

    class LLMComFalhaDeImport(FakeLLM):
        def chat(self, messages, **kw):
            chamadas_llm.append(messages[-1]["content"])
            return super().chat(messages, **kw)

    com_erro = chamada("write_file", path="soma.py", content=f"import {nome_modulo}\n\ndef soma(a, b):\n    return a + b\n")
    sem_erro = chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n")
    llm = LLMComFalhaDeImport([com_erro, chamada("finish"), sem_erro, chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    feedback = next((c for c in chamadas_llm if "biblioteca_que_nao_existe_xyz" in c and "NÃO está instalada" in c), None)
    assert feedback is not None


def test_prompt_pede_apenas_biblioteca_padrao():
    assert "biblioteca padrão" in PROMPT_SISTEMA.lower() or "biblioteca padrao" in PROMPT_SISTEMA.lower()


def test_prompt_proibe_outras_linguagens_e_instaladores():
    assert "100% PYTHON" in PROMPT_SISTEMA
    assert "npm" in PROMPT_SISTEMA and "Node.js" in PROMPT_SISTEMA


@pytest.mark.parametrize("comando", [
    "npm install", "npx jest", "yarn add express", "node index.js",
    "pip install requests", "cargo build", "go run main.go", "mvn test", "dotnet run",
])
def test_qualquer_runtime_nao_python_e_bloqueado_com_mensagem_especifica(projeto, comando):
    """Cobre a CATEGORIA inteira (gerenciadores/runtimes não-Python), não só um comando do log."""
    llm = FakeLLM([chamada("run_command", command=comando), chamada("finish")] * 3)
    Orquestrador("site", projeto, llm=llm, max_reparos=1).executar()
    chamadas = [x for x in acoes(projeto) if x["type"] == "tool_call" and x["tool"] == "run_command"]
    assert chamadas and all("não está disponível" in x["result"] for x in chamadas)


# ---------------------------------------------------------------- detecção de erro repetido entre reparos
# (cobre a CATEGORIA "o modelo trava tentando a mesma correção", não um bug de um algoritmo específico)

def test_assinatura_de_erro_ignora_numeros_de_linha_mas_distingue_excecoes():
    saida_a = "tests/test_x.py:12: in f\nE   TypeError: '<' not supported\nFAILED tests/test_x.py::test_a"
    saida_a_outra_linha = "tests/test_x.py:47: in f\nE   TypeError: '<' not supported\nFAILED tests/test_x.py::test_a"
    saida_b = "tests/test_x.py:12: in f\nE   NameError: name 'x' is not defined\nFAILED tests/test_x.py::test_a"
    assert Orquestrador._assinatura_erro(saida_a) == Orquestrador._assinatura_erro(saida_a_outra_linha)
    assert Orquestrador._assinatura_erro(saida_a) != Orquestrador._assinatura_erro(saida_b)


def test_mesmo_erro_repetido_aborta_antes_do_limite_de_reparos(projeto):
    """O modelo reescreve sempre o MESMO bug (código genérico, não amarrado a um algoritmo específico)."""
    sempre_o_mesmo_bug = chamada(
        "write_file", path="soma.py",
        content="def soma(a, b):\n    return a + indefinida_nao_existe\n",
    )
    llm = FakeLLM([sempre_o_mesmo_bug, chamada("finish")] * 10)
    assert Orquestrador("soma", projeto, llm=llm, max_reparos=5).executar() is False
    s = estado_json(projeto)
    assert s["state"] == "FAILED" and "mesmo erro" in s["error"]
    assert s["repair_attempts"] < 5
    assert any(a["type"] == "same_error_abort" for a in acoes(projeto))


def test_erros_diferentes_a_cada_reparo_nao_disparam_a_deteccao(projeto):
    """Cada reparo corrige o erro anterior mas introduz um erro NOVO e diferente: não é um loop."""
    tentativas = [
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + indefinida\n"),
        chamada("finish"),
        chamada("write_file", path="soma.py", content="def soma(a, b)\n    return a + b\n"),
        chamada("finish"),
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a - b\n"),
        chamada("finish"),
        chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n"),
        chamada("finish"),
    ]
    llm = FakeLLM(tentativas)
    assert Orquestrador("soma", projeto, llm=llm, max_reparos=5).executar() is True
    assert not any(a["type"] == "same_error_abort" for a in acoes(projeto))


def test_aviso_de_repeticao_aparece_no_feedback_a_partir_da_segunda_vez(projeto):
    sempre_o_mesmo_bug = chamada(
        "write_file", path="soma.py",
        content="def soma(a, b):\n    return a + indefinida_nao_existe\n",
    )

    vistos = []

    class Espiao(FakeLLM):
        def chat(self, messages, **kw):
            vistos.append(messages[-1]["content"])
            return super().chat(messages, **kw)

    llm = Espiao([sempre_o_mesmo_bug, chamada("finish")] * 10)
    Orquestrador("soma", projeto, llm=llm, max_reparos=5).executar()
    feedbacks = [v for v in vistos if v.startswith("Os testes FALHARAM")]
    assert len(feedbacks) >= 2
    assert "MESMO ERRO" not in feedbacks[0]
    assert "MESMO ERRO" in feedbacks[1]


def test_reparo_bem_sucedido_apos_erro_unico_nao_aciona_aviso(projeto):
    erro = chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a - b\n")
    ok = chamada("write_file", path="soma.py", content="def soma(a, b):\n    return a + b\n")

    vistos = []

    class Espiao(FakeLLM):
        def chat(self, messages, **kw):
            vistos.append(messages[-1]["content"])
            return super().chat(messages, **kw)

    llm = Espiao([erro, chamada("finish"), ok, chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    feedbacks = [v for v in vistos if v.startswith("Os testes FALHARAM")]
    assert len(feedbacks) == 1 and "MESMO ERRO" not in feedbacks[0]