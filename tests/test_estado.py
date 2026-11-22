import pytest
from src.agente.estado import GerenciadorEstado


@pytest.fixture
def ge(tmp_path):
    return GerenciadorEstado("tarefa", tmp_path, max_reparos=2)


def preparar_ate_implementing(ge):
    (ge.minicode_dir / "specification.md").write_text("spec")
    ge.mudar_estado("SPECIFIED")
    (ge.minicode_dir / "plan.md").write_text("1. plano")
    ge.mudar_estado("PLANNED")
    ge.mudar_estado("IMPLEMENTING")


def test_nao_salta_etapas(ge):
    with pytest.raises(RuntimeError, match="transição proibida"):
        ge.mudar_estado("IMPLEMENTING")


def test_specified_exige_arquivo(ge):
    with pytest.raises(RuntimeError, match="specification.md"):
        ge.mudar_estado("SPECIFIED")


def test_planned_exige_plano(ge):
    (ge.minicode_dir / "specification.md").write_text("spec")
    ge.mudar_estado("SPECIFIED")
    with pytest.raises(RuntimeError, match="plan.md"):
        ge.mudar_estado("PLANNED")


def test_done_exige_testes_executados(ge):
    preparar_ate_implementing(ge)
    ge.mudar_estado("VERIFYING")
    with pytest.raises(RuntimeError, match="testes executados"):
        ge.mudar_estado("DONE")


def test_done_proibido_com_testes_falhando(ge):
    preparar_ate_implementing(ge)
    ge.mudar_estado("VERIFYING")
    ge.registrar_testes(False, "falhou")
    with pytest.raises(RuntimeError, match="aprovados"):
        ge.mudar_estado("DONE")


def test_done_proibido_se_houve_escrita_apos_testes(ge):
    preparar_ate_implementing(ge)
    ge.mudar_estado("VERIFYING")
    ge.registrar_testes(True)
    ge.registrar_alteracao("x.py")
    with pytest.raises(RuntimeError, match="após a última execução"):
        ge.mudar_estado("DONE")


def test_done_com_testes_aprovados(ge):
    preparar_ate_implementing(ge)
    ge.mudar_estado("VERIFYING")
    ge.registrar_testes(True)
    ge.mudar_estado("DONE")
    assert ge.estado_atual == "DONE"


def test_repairing_exige_falha_e_respeita_limite(ge):
    preparar_ate_implementing(ge)
    ge.mudar_estado("VERIFYING")
    with pytest.raises(RuntimeError, match="só ocorre após testes que falharam"):
        ge.mudar_estado("REPAIRING")
    for _ in range(2):
        ge.registrar_testes(False)
        ge.mudar_estado("REPAIRING")
        ge.mudar_estado("VERIFYING")
    ge.registrar_testes(False)
    with pytest.raises(RuntimeError, match="limite"):
        ge.mudar_estado("REPAIRING")


def test_failed_so_via_falhar(ge):
    with pytest.raises(RuntimeError, match="falhar"):
        ge.mudar_estado("FAILED")
    ge.falhar("erro qualquer")
    assert ge.estado_atual == "FAILED"
    ge.falhar("de novo")
    assert ge.extras["error"] == "erro qualquer"


def test_extras_persistem(ge):
    ge.salvar_estado({"a": 1})
    ge.salvar_estado({"b": 2})
    assert ge.extras == {"a": 1, "b": 2}