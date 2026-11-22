from pathlib import Path

import pytest
from src.avaliador.tarefas import listar_tarefas, validar_tarefa

RAIZ = Path(__file__).resolve().parent.parent
TAREFAS = RAIZ / "tarefas_teste"
SEMENTES = RAIZ / "tarefas_semente.txt"


def test_ha_tarefas_de_todos_os_tipos_pedidos_no_enunciado():
    import json
    tipos = {t["tipo"] for t in json.loads((TAREFAS / "indice.json").read_text())}
    assert {"funcao", "bug", "api", "testes", "validacao", "refatoracao"} <= tipos
    assert len(listar_tarefas(TAREFAS)) >= 20


@pytest.mark.parametrize("dir_tarefa", listar_tarefas(TAREFAS), ids=lambda d: d.name)
def test_tarefa_e_valida(dir_tarefa):
    """Os testes ocultos falham no projeto inicial e passam com a solução de referência."""
    r = validar_tarefa(dir_tarefa)
    assert r["falha_sem_referencia"], f"{r['tarefa']}: os testes ocultos já passam sem a solução"
    assert r["passa_com_referencia"], f"{r['tarefa']}: a solução de referência não passa nos testes ocultos"


def test_tarefas_de_avaliacao_nao_repetem_as_sementes_de_treino():
    """As tarefas de avaliação não podem ser as mesmas usadas para treinar o gerador de specs."""
    if not SEMENTES.exists():
        pytest.skip("tarefas_semente.txt ausente")
    from src.spec.dataset import carregar_tarefas, filtrar_sementes, similaridade
    sementes, _ = filtrar_sementes(carregar_tarefas([SEMENTES]))
    for d in listar_tarefas(TAREFAS):
        texto = (d / "tarefa.txt").read_text()
        assert max(similaridade(texto, s) for s in sementes) < 0.6, d.name


def test_tarefa_nao_vaza_a_solucao_para_o_agente():
    """O agente só enxerga projeto/: nada de testes ocultos ou referência lá dentro."""
    for d in listar_tarefas(TAREFAS):
        proj = d / "projeto"
        if proj.is_dir():
            nomes = {p.name for p in proj.rglob("*")}
            assert "_ocultos" not in nomes and "test_oculto.py" not in nomes
