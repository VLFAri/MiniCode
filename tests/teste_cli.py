import json
from pathlib import Path

from src.cli.main import main, resumir

RAIZ = Path(__file__).resolve().parent.parent


def test_recusa_rodar_no_codigo_do_proprio_minicode(capsys):
    assert main(["x", "--project", str(RAIZ)]) == 1
    assert "próprio MiniCode" in capsys.readouterr().out


def test_cria_o_diretorio_do_projeto_se_nao_existir(tmp_path, monkeypatch):
    alvo = tmp_path / "novo_projeto"

    class Falso:
        def __init__(self, *a, **k):
            pass

        def executar(self):
            return True

    monkeypatch.setattr("src.cli.main.Orquestrador", Falso)
    assert main(["tarefa", "--project", str(alvo)]) == 0
    assert alvo.is_dir()


def test_resumir_calcula_as_metricas_do_enunciado():
    r = resumir([
        {"success": True, "first_attempt_success": True, "iterations": 1, "llm_calls": 4},
        {"success": True, "first_attempt_success": False, "iterations": 3, "llm_calls": 10},
        {"success": False, "first_attempt_success": False, "iterations": 6, "llm_calls": 20},
        {"success": False, "first_attempt_success": False, "iterations": 6, "llm_calls": 26},
    ])
    assert r["TaskSuccessRate"] == 0.5 and r["FirstAttemptSuccess"] == 0.25
    assert r["AverageIterations"] == 4 and r["AverageLLMCalls"] == 15
    assert resumir([]) == {}


def test_modo_avaliar_percorre_as_tarefas_e_grava_resultados(tmp_path, monkeypatch):
    for nome in ("t1", "t2"):
        (tmp_path / "tarefas" / nome / "projeto").mkdir(parents=True)
        (tmp_path / "tarefas" / nome / "tarefa.txt").write_text("faça algo")
    (tmp_path / "tarefas" / "ignorada").mkdir()

    chamadas = []

    def falso(dir_tarefa, saida, max_reparos, max_iteracoes):
        chamadas.append(dir_tarefa.name)
        return {"task": dir_tarefa.name, "success": True, "first_attempt_success": True,
                "iterations": 1, "llm_calls": 3, "seconds": 0.1}

    monkeypatch.setattr("src.cli.main.avaliar_tarefa", falso)
    saida = tmp_path / "res"
    assert main(["--avaliar", str(tmp_path / "tarefas"), "--saida", str(saida)]) == 0
    assert chamadas == ["t1", "t2"]
    dados = json.loads((saida / "resultados.json").read_text())
    assert dados["summary"]["TaskSuccessRate"] == 1.0 and len(dados["results"]) == 2