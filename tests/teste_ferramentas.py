import pytest
from src.ferramentas.registro import RegistroFerramentas


@pytest.fixture
def reg(tmp_path):
    (tmp_path / "a.py").write_text("def f():\n    return 1\n")
    return RegistroFerramentas(tmp_path)


def test_list_e_read(reg):
    assert "a.py" in reg.executar("list_files", {})["saida"]
    assert "return 1" in reg.executar("read_file", {"path": "a.py"})["saida"]


def test_write_cria_diretorios(reg, tmp_path):
    r = reg.executar("write_file", {"path": "pkg/novo.py", "content": "x = 1\n"})
    assert r["ok"] and (tmp_path / "pkg" / "novo.py").exists()


def test_create_file_nao_sobrescreve(reg):
    assert not reg.executar("create_file", {"path": "a.py", "content": "x"})["ok"]


def test_replace_text_exige_ocorrencia_unica(reg, tmp_path):
    assert reg.executar("replace_text", {"path": "a.py", "old": "return 1", "new": "return 2"})["ok"]
    assert "return 2" in (tmp_path / "a.py").read_text()
    assert not reg.executar("replace_text", {"path": "a.py", "old": "inexistente", "new": "y"})["ok"]


def test_search_code(reg):
    assert "a.py:1" in reg.executar("search_code", {"pattern": "def f"})["saida"]


def test_escrita_fora_do_projeto_bloqueada(reg, tmp_path):
    r = reg.executar("write_file", {"path": "../fora.txt", "content": "x"})
    assert not r["ok"] and "BLOQUEADO" in r["saida"]
    assert not (tmp_path.parent / "fora.txt").exists()


def test_ler_env_bloqueado(reg, tmp_path):
    (tmp_path / ".env").write_text("TOKEN=abc")
    r = reg.executar("read_file", {"path": ".env"})
    assert not r["ok"] and "abc" not in r["saida"]
    assert ".env" not in reg.executar("list_files", {})["saida"].split()


def test_run_command_perigoso_bloqueado(reg):
    for cmd in ("sudo ls", "rm -rf /", "shutdown now"):
        assert not reg.executar("run_command", {"command": cmd})["ok"]


def test_argumentos_invalidos(reg):
    assert not reg.executar("read_file", {})["ok"]
    assert not reg.executar("read_file", {"path": "a.py", "x": 1})["ok"]
    assert not reg.executar("ferramenta_inexistente", {})["ok"]


def test_run_tests_veredito_real(reg, tmp_path):
    r = reg.executar("run_tests", {})
    assert r["ok"] and r["passou"] is False
    (tmp_path / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    assert reg.executar("run_tests", {})["passou"] is True
    (tmp_path / "test_ok.py").write_text("def test_ok():\n    assert False\n")
    assert reg.executar("run_tests", {})["passou"] is False


def test_descricoes_excluem_run_tests(reg):
    assert "run_tests" not in reg.descricoes(excluir={"run_tests"})
    assert "read_file" in reg.descricoes(excluir={"run_tests"})


def test_replace_text_mostra_o_conteudo_real_quando_o_trecho_nao_existe(reg, tmp_path):
    r = reg.executar("replace_text", {"path": "a.py", "old": "trecho inexistente", "new": "x"})
    assert not r["ok"]
    assert "NÃO existe" in r["saida"] and "def f():" in r["saida"] and "write_file" in r["saida"]


def test_replace_text_com_varias_ocorrencias_orienta_o_modelo(reg, tmp_path):
    (tmp_path / "b.py").write_text("x = 1\nx = 1\n")
    r = reg.executar("replace_text", {"path": "b.py", "old": "x = 1", "new": "x = 2"})
    assert not r["ok"] and "2 vezes" in r["saida"]
    assert (tmp_path / "b.py").read_text() == "x = 1\nx = 1\n"