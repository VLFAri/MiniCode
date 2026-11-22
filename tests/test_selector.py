import json

import pytest
from src.agente.orquestrador import Orquestrador
from src.avaliador.avaliador import avaliar_tarefa, resumir
from src.ferramentas.registro import RegistroFerramentas
from src.selector.avaliacao import avaliar_predicoes, avaliar_seletor
from src.selector.dataset import construir, dividir_por_tarefa, motivo_descarte
from src.selector.prompt import FERRAMENTAS_SELETOR, PROMPT_SELETOR, mensagens, parse_saida, rotulo
from tests.test_orquestrador import FakeLLM, LLMEspiao, chamada

SOMA_OK = "def soma(a, b):\n    return a + b\n"
SOMA_ERRADA = "def soma(a, b):\n    return a - b\n"
TESTE_SOMA = "from soma import soma\n\ndef test_soma():\n    assert soma(2, 3) == 5\n"


@pytest.fixture
def projeto(tmp_path):
    (tmp_path / "tests").mkdir()
    (tmp_path / "tests" / "test_soma.py").write_text(TESTE_SOMA)
    return tmp_path


def acoes(projeto):
    return [json.loads(l) for l in (projeto / ".minicode" / "actions.jsonl").read_text().splitlines()]


def exemplos(projeto):
    return [a for a in acoes(projeto) if a["type"] == "selector_example"]


class SeletorFalso:
    def __init__(self, previsao):
        self.previsao = previsao
        self.chamadas = 0

    def predict(self, features):
        self.chamadas += 1
        if isinstance(self.previsao, Exception):
            raise self.previsao
        return self.previsao


# ---------------------------------------------------------------- formato compartilhado
def test_lista_de_ferramentas_do_seletor_acompanha_o_registro(tmp_path):
    """Se uma ferramenta nova for criada e esquecida aqui, o seletor nunca a escolheria."""
    do_registro = set(RegistroFerramentas(tmp_path).nomes()) - {"run_tests"}
    assert set(FERRAMENTAS_SELETOR) == do_registro | {"finish"}
    assert all(f in PROMPT_SELETOR for f in FERRAMENTAS_SELETOR)


def test_rotulo_e_parse_saida_sao_inversos():
    assert parse_saida(rotulo("read_file", "a.py")) == {"tool": "read_file", "path": "a.py"}
    assert parse_saida(rotulo("finish")) == {"tool": "finish", "path": None}
    assert parse_saida('```json\n{"tool": "list_files"}\n```') == {"tool": "list_files", "path": None}
    assert parse_saida('Resposta: {"tool": "search_code", "path": 3}') == {"tool": "search_code", "path": None}


@pytest.mark.parametrize("lixo", ["", None, "sem json", '{"sem_tool": 1}', '{"tool": ', '{"tool": 5}'])
def test_parse_saida_rejeita_lixo(lixo):
    assert parse_saida(lixo) is None


def test_mensagens_tem_system_e_user():
    m = mensagens("ESTADO")
    assert [x["role"] for x in m] == ["system", "user"] and m[1]["content"] == "ESTADO"


# ---------------------------------------------------------------- orquestrador registra exemplos
def test_cada_decisao_do_teacher_vira_um_exemplo(projeto):
    llm = FakeLLM([chamada("read_file", path="tests/test_soma.py"),
                   chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    ex = exemplos(projeto)
    assert [(e["label"]["tool"], e["label"]["path"]) for e in ex] == [
        ("read_file", "tests/test_soma.py"), ("write_file", "soma.py"), ("finish", None)]
    assert "FASE: IMPLEMENTING" in ex[0]["features"] and "TESTES: nunca executados" in ex[0]["features"]
    assert "HISTORICO:\n(nenhuma)" in ex[0]["features"]
    # o histórico do passo seguinte enxerga a ação anterior e o resultado dela
    assert "1. read_file tests/test_soma.py -> OK" in ex[1]["features"]
    assert "2. write_file soma.py -> OK" in ex[2]["features"]
    assert "ALTERADOS: soma.py" in ex[2]["features"]


def test_exemplos_do_reparo_trazem_fase_e_erro_do_pytest(projeto):
    llm = FakeLLM([chamada("write_file", path="soma.py", content=SOMA_ERRADA), chamada("finish"),
                   chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm).executar() is True
    reparo = [e for e in exemplos(projeto) if "FASE: REPAIRING" in e["features"]]
    assert reparo and all("TESTES: falharam" in e["features"] for e in reparo)
    assert all("ERRO_PYTEST: (nenhum)" not in e["features"] for e in reparo)


def test_chamadas_invalidas_ou_bloqueadas_nao_geram_exemplo(projeto):
    llm = FakeLLM([chamada("run_tests"), chamada("run_command", command="pytest -q"),
                   chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    Orquestrador("soma", projeto, llm=llm).executar()
    assert [e["label"]["tool"] for e in exemplos(projeto)] == ["write_file", "finish"]


def test_features_nao_vazam_credenciais(projeto):
    (projeto / ".env").write_text("TOKEN=abc")
    llm = FakeLLM([chamada("finish")])
    Orquestrador("soma", projeto, llm=llm, max_reparos=0).executar()
    assert all("TOKEN=abc" not in e["features"] and ".env" not in e["features"].split() for e in exemplos(projeto))


# ---------------------------------------------------------------- integração do seletor
def test_dica_do_seletor_chega_ao_llm_sem_poluir_o_historico(projeto):
    llm = LLMEspiao([chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    sel = SeletorFalso({"tool": "write_file", "path": "soma.py"})
    assert Orquestrador("soma", projeto, llm=llm, selector=sel).executar() is True
    h0, h1 = llm.historicos[0], llm.historicos[1]
    assert "SELETOR" in h0[-1]["content"] and "'write_file'" in h0[-1]["content"] and "soma.py" in h0[-1]["content"]
    assert "SELETOR" in h1[-1]["content"]
    assert "SELETOR" not in h1[1]["content"]     # mensagens antigas ficam limpas
    s = json.loads((projeto / ".minicode" / "state.json").read_text())
    assert s["selector_calls"] == 2 and s["selector_followed"] == 1  # 1ª ação seguiu; 'finish' != 'write_file'


def test_sem_seletor_o_prompt_nao_muda(projeto):
    llm = LLMEspiao([chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    Orquestrador("soma", projeto, llm=llm).executar()
    assert all("SELETOR" not in m["content"] for h in llm.historicos for m in h)
    assert "selector_calls" not in json.loads((projeto / ".minicode" / "state.json").read_text())


def test_seletor_que_falha_nao_derruba_o_agente(projeto):
    llm = FakeLLM([chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    sel = SeletorFalso(RuntimeError("GPU sem memória"))
    assert Orquestrador("soma", projeto, llm=llm, selector=sel).executar() is True
    assert any(a["type"] == "selector_error" and "GPU" in a["error"] for a in acoes(projeto))


@pytest.mark.parametrize("previsao", [None, "lixo", {"tool": "run_tests"}, {"tool": "inventada"}, {}])
def test_previsao_invalida_e_ignorada(projeto, previsao):
    llm = LLMEspiao([chamada("write_file", path="soma.py", content=SOMA_OK), chamada("finish")])
    assert Orquestrador("soma", projeto, llm=llm, selector=SeletorFalso(previsao)).executar() is True
    assert all("SELETOR" not in m["content"] for h in llm.historicos for m in h)
    assert any(a["type"] == "selector_invalid" for a in acoes(projeto))


# ---------------------------------------------------------------- métricas do nível 1
def test_avaliar_predicoes_calcula_acuracias_e_baseline():
    golds = [{"tool": "read_file", "path": "a.py"}, {"tool": "write_file", "path": "a.py"},
             {"tool": "finish", "path": None}, {"tool": "finish", "path": None}]
    preds = [{"tool": "read_file", "path": "b.py"},      # tool certa, caminho errado
             None,                                       # saída inválida
             {"tool": "finish", "path": None},
             {"tool": "finish", "path": None}]
    m = avaliar_predicoes(golds, preds)
    assert m["n"] == 4 and m["json_valido"] == 0.75
    assert m["tool_accuracy"] == 0.75 and m["tool_path_accuracy"] == 0.5
    assert m["baseline_classe_majoritaria"] == 0.5
    assert m["recall_por_ferramenta"]["finish"] == 1.0 and m["recall_por_ferramenta"]["write_file"] == 0.0
    assert m["confusao"]["write_file"] == {"<invalido>": 1}
    assert avaliar_predicoes([], []) == {"n": 0}


def test_avaliar_seletor_usa_o_formato_do_dataset():
    ex = [{"messages": mensagens("E1") + [{"role": "assistant", "content": rotulo("finish")}]}]

    class Eco:
        def predict(self, features):
            assert features == "E1"
            return {"tool": "finish", "path": None}

    assert avaliar_seletor(Eco(), ex)["tool_path_accuracy"] == 1.0


# ---------------------------------------------------------------- dataset
def _ex(features, tool, path=None):
    return {"type": "selector_example", "features": features, "label": {"tool": tool, "path": path}}


def _criar_execucao(raiz, nome, exemplos, success=True, extra_eventos=()):
    d = raiz / nome
    d.mkdir(parents=True)
    (d / "state.json").write_text(json.dumps({"success": success, "state": "DONE" if success else "FAILED"}))
    linhas = list(exemplos) + [{"type": e} for e in extra_eventos]
    (d / "actions.jsonl").write_text("".join(json.dumps(l) + "\n" for l in linhas))


@pytest.fixture
def resultados(tmp_path):
    raiz = tmp_path / "res"
    raiz.mkdir()
    for i in range(10):
        _criar_execucao(raiz, f"t{i}", [_ex(f"estado {i}a", "read_file", "a.py"),
                                        _ex(f"estado {i}b", "write_file", "a.py"),
                                        _ex(f"estado {i}b", "write_file", "a.py"),   # duplicado exato
                                        _ex(f"estado {i}c", "finish")])
    _criar_execucao(raiz, "falhou", [_ex("x", "finish")], success=False)
    _criar_execucao(raiz, "loop", [_ex("y", "read_file", "a.py")], extra_eventos=["loop_detected"])
    _criar_execucao(raiz, "ocultos", [_ex("z", "finish")])
    (raiz / "resultados.json").write_text(json.dumps({"results": [{"task": "ocultos", "hidden_pass": False}]}))
    return raiz


def test_dataset_filtra_tarefas_ruins_e_remove_duplicados(resultados, tmp_path):
    st = construir([str(resultados)], str(tmp_path / "out"))
    assert st["tarefas_vistas"] == 13 and st["tarefas_usadas"] == 10
    assert st["tarefas_descartadas"] == {"falhou": ["tarefa_nao_concluida"], "loop": ["loop_detectado"],
                                         "ocultos": ["testes_ocultos_falharam"]}
    assert st["duplicados_removidos"] == 10
    assert sum(s["exemplos"] for s in st["splits"].values()) == 30


def test_dataset_divide_por_tarefa_sem_vazamento(resultados, tmp_path):
    out = tmp_path / "out"
    construir([str(resultados)], str(out))
    por_split = {}
    for split in ("train", "val", "test"):
        linhas = [json.loads(l) for l in (out / f"{split}.jsonl").read_text().splitlines()]
        por_split[split] = {l["task"] for l in linhas}
        assert linhas
    assert not (por_split["train"] & por_split["val"] or por_split["train"] & por_split["test"]
                or por_split["val"] & por_split["test"])
    assert len(por_split["train"] | por_split["val"] | por_split["test"]) == 10


def test_dataset_usa_o_mesmo_formato_da_inferencia(resultados, tmp_path):
    out = tmp_path / "out"
    construir([str(resultados)], str(out))
    ex = json.loads((out / "train.jsonl").read_text().splitlines()[0])
    assert ex["messages"][:2] == mensagens(ex["messages"][1]["content"])
    assert parse_saida(ex["messages"][2]["content"])["tool"] in FERRAMENTAS_SELETOR


def test_dataset_e_deterministico_e_exigir_ocultos_descarta_sem_resultado(resultados, tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    construir([str(resultados)], str(a), seed=7)
    construir([str(resultados)], str(b), seed=7)
    assert (a / "test.jsonl").read_text() == (b / "test.jsonl").read_text()
    st = construir([str(resultados)], str(tmp_path / "c"), exigir_ocultos=True)
    assert st["tarefas_usadas"] == 0     # nenhuma tarefa tem hidden_pass == True nesse fixture


def test_divisao_com_poucas_tarefas_nao_cria_splits_vazios_de_teste():
    pequeno = dividir_por_tarefa(["a", "b"])
    assert pequeno["test"] == [] and pequeno["val"] == [] and sorted(pequeno["train"]) == ["a", "b"]
    d = dividir_por_tarefa([f"t{i}" for i in range(20)])
    assert len(d["test"]) == 3 and len(d["val"]) == 3 and len(d["train"]) == 14


def test_motivo_descarte_ordem_de_prioridade():
    assert motivo_descarte({"success": False}, [], None, False) == "tarefa_nao_concluida"
    assert motivo_descarte({"success": True}, [], False, False) == "testes_ocultos_falharam"
    assert motivo_descarte({"success": True}, [], None, True) == "sem_resultado_dos_testes_ocultos"
    assert motivo_descarte({"success": True}, [{"type": "security_violation"}], True, True) == "violacao_seguranca"
    assert motivo_descarte({"success": True}, [{"type": "tool_call"}], True, True) is None


# ---------------------------------------------------------------- testes ocultos no avaliador
def _tarefa(tmp_path, ocultos=True):
    t = tmp_path / "tarefa_soma"
    (t / "projeto" / "tests").mkdir(parents=True)
    # o agente "escreve" um teste trivial: passa mesmo com a solução errada
    (t / "projeto" / "tests" / "test_trivial.py").write_text("def test_trivial():\n    assert True\n")
    (t / "tarefa.txt").write_text("Crie soma(a, b)")
    if ocultos:
        (t / "testes_ocultos").mkdir()
        (t / "testes_ocultos" / "test_oculto.py").write_text(TESTE_SOMA)
    return t


def _avaliar(monkeypatch, tmp_path, codigo, **kw):
    llm = FakeLLM([chamada("write_file", path="soma.py", content=codigo), chamada("finish")])
    monkeypatch.setattr("src.avaliador.avaliador.LLMClient", lambda: llm)
    return avaliar_tarefa(_tarefa(tmp_path, **kw), tmp_path / "saida", 1, 10)


def test_testes_ocultos_pegam_solucao_errada_que_passa_nos_proprios_testes(monkeypatch, tmp_path):
    r = _avaliar(monkeypatch, tmp_path, SOMA_ERRADA)
    assert r["success"] is True and r["hidden_pass"] is False


def test_testes_ocultos_confirmam_solucao_correta(monkeypatch, tmp_path):
    r = _avaliar(monkeypatch, tmp_path, SOMA_OK)
    assert r["success"] is True and r["hidden_pass"] is True


def test_tarefa_sem_testes_ocultos_retorna_none(monkeypatch, tmp_path):
    assert _avaliar(monkeypatch, tmp_path, SOMA_OK, ocultos=False)["hidden_pass"] is None


def test_resumir_inclui_taxas_novas_apenas_quando_existem():
    base = {"success": True, "first_attempt_success": True, "iterations": 1, "llm_calls": 2}
    assert "HiddenSuccessRate" not in resumir([base])
    r = resumir([{**base, "hidden_pass": True, "selector_calls": 4, "selector_followed": 3},
                 {**base, "hidden_pass": False, "selector_calls": 4, "selector_followed": 1},
                 {**base, "hidden_pass": None}])
    assert r["HiddenSuccessRate"] == 0.5 and r["SelectorFollowRate"] == 0.5


# ---------------------------------------------------------------- tokenização do treino
class TokenizadorFalso:
    """Um 'token' por caractere; o suficiente para verificar a máscara de loss."""
    eos_token = "#"

    def apply_chat_template(self, msgs, tokenize=False, add_generation_prompt=False):
        assert not tokenize and add_generation_prompt
        return "".join(f"<{m['role']}>{m['content']}" for m in msgs) + "<assistant>"

    def __call__(self, texto, add_special_tokens=True):
        assert add_special_tokens is False
        return {"input_ids": [ord(c) for c in texto]}


def test_tokenizacao_mascara_o_prompt_e_treina_so_a_resposta():
    from src.selector.treino import tokenizar_exemplo

    msgs = mensagens("ESTADO") + [{"role": "assistant", "content": rotulo("finish")}]
    t = TokenizadorFalso()
    out = tokenizar_exemplo(t, msgs, max_len=10_000)
    treinados = [i for i, l in zip(out["input_ids"], out["labels"]) if l != -100]
    assert "".join(map(chr, treinados)) == rotulo("finish") + "#"       # resposta + EOS
    n_prompt = len(t.apply_chat_template(msgs[:2], add_generation_prompt=True))
    assert out["labels"][:n_prompt] == [-100] * n_prompt
    assert len(out["input_ids"]) == len(out["labels"]) == len(out["attention_mask"])
    assert out["truncado"] is False
    assert tokenizar_exemplo(t, msgs, max_len=10)["truncado"] is True
