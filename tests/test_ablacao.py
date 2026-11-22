import json

import pytest
from src.agente.estado import GerenciadorEstado
from src.agente.orquestrador import PROMPT_SISTEMA, PROMPT_SISTEMA_SO_PROMPT, Orquestrador
from tests.test_orquestrador import FakeLLM, LLMEspiao, chamada

SOMA_ERRADA = "def soma(a, b):\n    return a - b\n"
TESTE_SOMA = "from soma import soma\n\ndef test_soma():\n    assert soma(2, 3) == 5\n"


def estado_json(p):
    return json.loads((p / ".minicode" / "state.json").read_text())


def test_gate_de_done_so_desliga_quando_pedido(tmp_path):
    for flag, deve_falhar in ((True, True), (False, False)):
        ge = GerenciadorEstado("t", tmp_path / str(flag), hard_gates=flag)
        (ge.minicode_dir / "specification.md").write_text("s")
        ge.mudar_estado("SPECIFIED")
        (ge.minicode_dir / "plan.md").write_text("1. p")
        ge.mudar_estado("PLANNED")
        ge.mudar_estado("IMPLEMENTING")
        ge.mudar_estado("VERIFYING")
        if deve_falhar:
            with pytest.raises(RuntimeError, match="testes executados"):
                ge.mudar_estado("DONE")
        else:
            ge.mudar_estado("DONE")
            assert ge.estado_atual == "DONE"


def test_transicoes_continuam_obrigatorias_sem_hard_gate(tmp_path):
    ge = GerenciadorEstado("t", tmp_path, hard_gates=False)
    with pytest.raises(RuntimeError, match="transição proibida"):
        ge.mudar_estado("DONE")


def test_com_hard_gate_codigo_errado_nao_vira_done(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_soma.py").write_text(TESTE_SOMA)
    llm = FakeLLM([chamada("write_file", path="soma.py", content=SOMA_ERRADA), chamada("finish")] * 3)
    assert Orquestrador("soma", tmp_path, llm=llm, max_reparos=0).executar() is False
    assert estado_json(tmp_path)["state"] == "FAILED" and estado_json(tmp_path)["hard_gates"] is True


def test_sem_hard_gate_o_agente_declara_sucesso_sem_rodar_testes(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_soma.py").write_text(TESTE_SOMA)
    llm = FakeLLM([chamada("write_file", path="soma.py", content=SOMA_ERRADA), chamada("finish")])
    assert Orquestrador("soma", tmp_path, llm=llm, hard_gates=False).executar() is True
    s = estado_json(tmp_path)
    assert s["state"] == "DONE" and s["tests_run"] == 0 and s["hard_gates"] is False


def test_sem_hard_gate_o_prompt_pede_testes_e_expoe_run_tests(tmp_path):
    llm = LLMEspiao([chamada("finish")])
    Orquestrador("soma", tmp_path, llm=llm, hard_gates=False).executar()
    sistema = llm.historicos[-1][0]["content"]
    assert "run_tests" in sistema and "EXECUTE os testes" in sistema and "NÃO execute o pytest" not in sistema
    llm2 = LLMEspiao([chamada("finish")])
    Orquestrador("soma", tmp_path / "b", llm=llm2).executar()
    assert "NÃO execute o pytest" in llm2.historicos[-1][0]["content"]
    assert PROMPT_SISTEMA != PROMPT_SISTEMA_SO_PROMPT


def test_sem_hard_gate_o_modelo_consegue_chamar_run_tests(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_soma.py").write_text(TESTE_SOMA)
    llm = FakeLLM([chamada("write_file", path="soma.py", content=SOMA_ERRADA), chamada("run_tests"), chamada("finish")])
    Orquestrador("soma", tmp_path, llm=llm, hard_gates=False).executar()
    chamadas = [json.loads(l) for l in (tmp_path / ".minicode" / "actions.jsonl").read_text().splitlines()]
    assert any(a["type"] == "tool_call" and a["tool"] == "run_tests" for a in chamadas)
    assert not any(a["type"] == "invalid_tool" for a in chamadas)


# ---------------------------------------------------------------- runner de ablação e relatório
def _resumo(hidden, falso):
    return {"HiddenSuccessRate": hidden, "FalseSuccessRate": falso, "TaskSuccessRate": 1.0,
            "FirstAttemptSuccess": 0.5, "AverageIterations": 2.0, "AverageLLMCalls": 8.0}


def test_tabela_media_e_desvio():
    from src.avaliador.ablacao import tabela_markdown
    t = tabela_markdown({"completo": [_resumo(0.8, 0.0), _resumo(0.6, 0.2)], "sem_hard_gate": [_resumo(0.5, 0.4)]})
    assert "completo (n=2 rodada(s))" in t and "0.70 ± 0.14" in t
    assert "sem_hard_gate (n=1 rodada(s))" in t and "0.50 |" in t and "±" not in t.split("sem_hard_gate")[1]


def test_false_success_rate_conta_done_com_ocultos_reprovados():
    from src.avaliador.avaliador import resumir
    base = {"first_attempt_success": True, "iterations": 1, "llm_calls": 2}
    r = resumir([{**base, "success": True, "hidden_pass": True}, {**base, "success": True, "hidden_pass": False},
                 {**base, "success": False, "hidden_pass": False}, {**base, "success": True, "hidden_pass": None}])
    assert abs(r["HiddenSuccessRate"] - 1 / 3) < 1e-9 and abs(r["FalseSuccessRate"] - 1 / 3) < 1e-9


def test_ablacao_roda_as_tres_configuracoes_com_os_parametros_certos(tmp_path, monkeypatch):
    from src.avaliador import ablacao
    t = tmp_path / "tarefas" / "t1"
    t.mkdir(parents=True)
    (t / "tarefa.txt").write_text("x")
    vistos = []

    def falso(d, saida, max_reparos, max_iteracoes, hard_gates=True, **kw):
        vistos.append((max_reparos, hard_gates))
        return {"task": d.name, "success": True, "first_attempt_success": True, "iterations": 1, "llm_calls": 3,
                "hidden_pass": hard_gates}

    monkeypatch.setattr("src.avaliador.ablacao.avaliar_tarefa", falso)
    por_config = ablacao.rodar(str(tmp_path / "tarefas"), str(tmp_path / "abl"), list(ablacao.CONFIGS), 2, 10)
    assert vistos == [(3, True)] * 2 + [(0, True)] * 2 + [(3, False)] * 2
    assert por_config["sem_hard_gate"][0]["HiddenSuccessRate"] == 0.0
    assert (tmp_path / "abl" / "ablacao.md").exists()
    assert set(ablacao.carregar_ablacao(str(tmp_path / "abl"))) == set(ablacao.CONFIGS)


def test_relatorio_so_usa_numeros_existentes(tmp_path):
    from src.avaliador.relatorio import gerar
    vazio = gerar(str(tmp_path))
    assert vazio.count("ainda não executado") == 3
    (tmp_path / "experiments" / "results").mkdir(parents=True)
    m = {"n": 5, "valida_agente": 0.2, "valida_estrita": 0.1, "criterios_medio": 2.5, "com_codigo_de_implementacao": 0.6}
    ft = {**m, "valida_agente": 0.9, "valida_estrita": 0.8, "criterios_medio": 4.5, "com_codigo_de_implementacao": 0.0}
    (tmp_path / "experiments" / "results" / "spec_colab.json").write_text(json.dumps({"base": m, "finetuned": ft, "qwen14b": None}))
    txt = gerar(str(tmp_path))
    assert "| modelo base (baseline) | 0.20 | 0.10 |" in txt and "| mesmo modelo + QLoRA | 0.90 | 0.80 |" in txt
    assert "| Qwen-14B (referência) | n/d |" in txt and txt.count("ainda não executado") == 2


def test_relatorio_declara_o_modelo_de_referencia_quando_nao_e_o_14b(tmp_path):
    from src.avaliador.relatorio import gerar
    (tmp_path / "experiments" / "results").mkdir(parents=True)
    m = {"n": 5, "valida_agente": 0.2, "valida_estrita": 0.1, "criterios_medio": 2.5, "com_codigo_de_implementacao": 0.6}
    (tmp_path / "experiments" / "results" / "spec_colab.json").write_text(json.dumps({"base": m, "finetuned": m, "qwen14b": None}))
    (tmp_path / "experiments" / "results" / "spec_teacher.json").write_text(
        json.dumps({**m, "valida_agente": 0.95, "modelo_referencia": "qwen2.5:14b-instruct (local)"}))
    txt = gerar(str(tmp_path))
    assert "referência: qwen2.5:14b-instruct (local) | 0.95 |" in txt and "Qwen-14B (referência)" not in txt


def test_relatorio_lista_o_modelo_principal_do_agente(tmp_path):
    from src.avaliador.relatorio import gerar
    d = tmp_path / "experiments" / "res_spec_base"
    d.mkdir(parents=True)
    d.joinpath("resultados.json").write_text(json.dumps({
        "summary": {"HiddenSuccessRate": 0.4},
        "results": [{"llm_model": "qwen2.5-coder:7b"}, {"llm_model": "qwen2.5-coder:7b"}, {"llm_model": None}]}))
    txt = gerar(str(tmp_path))
    assert "modelo base: qwen2.5-coder:7b" in txt


def test_avaliacao_do_teacher_registra_o_modelo_usado(tmp_path, monkeypatch):
    from src.spec import avaliacao
    from tests.test_spec import SPEC_BOA

    class Fake:
        model, backend = "qwen2.5:14b", "local"

        def __init__(self, **kw):
            pass

        def complete(self, prompt, system_prompt=None):
            return SPEC_BOA

    monkeypatch.setattr("src.modelo.cliente_llm.LLMClient", Fake)
    teste = tmp_path / "test.jsonl"
    teste.write_text(json.dumps({"task": "t", "contexto": "(vazio)", "messages": [{"role": "user", "content": "p"}, {"role": "assistant", "content": "x"}]}) + "\n")
    saida = tmp_path / "spec_teacher.json"
    assert avaliacao.main(["--modo", "teacher", "--test", str(teste), "--saida", str(saida)]) == 0
    dados = json.loads(saida.read_text())
    assert dados["modelo_referencia"] == "qwen2.5:14b (local)" and dados["valida_estrita"] == 1.0
