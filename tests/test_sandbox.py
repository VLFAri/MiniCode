import pytest
from src.ferramentas.registro import RegistroFerramentas


@pytest.fixture
def ambiente(tmp_path):
    projeto = tmp_path / "proj"
    projeto.mkdir()
    return projeto, tmp_path, RegistroFerramentas(projeto)


def rodar_teste(ambiente, corpo: str, imports: str = ""):
    projeto, _, reg = ambiente
    (projeto / "test_hostil.py").write_text(f"{imports}\ndef test_x():\n    {corpo}\n")
    return reg.executar("run_tests", {})


def bloqueado(res):
    return res["ok"] and res["passou"] is False and "MiniCode sandbox" in res["saida"]


def test_escrita_fora_do_projeto_bloqueada(ambiente):
    _, raiz, _ = ambiente
    fora = raiz / "fora.txt"
    res = rodar_teste(ambiente, f'open({str(fora)!r}, "w").write("escapei")')
    assert bloqueado(res) and not fora.exists()


@pytest.mark.parametrize("corpo", [
    'os.remove({fora!r})',
    'os.rename({fora!r}, {fora!r} + ".bak")',
    'shutil.rmtree({pasta!r})',
])
def test_remocao_e_renomeacao_fora_bloqueadas(ambiente, corpo):
    _, raiz, _ = ambiente
    fora = raiz / "alvo.txt"
    fora.write_text("intacto")
    pasta = raiz / "pasta_externa"
    pasta.mkdir()
    (pasta / "a.txt").write_text("a")
    res = rodar_teste(ambiente, corpo.format(fora=str(fora), pasta=str(pasta)), "import os, shutil")
    assert bloqueado(res)
    assert fora.read_text() == "intacto" and (pasta / "a.txt").exists()


def test_subprocess_bloqueado(ambiente):
    _, raiz, _ = ambiente
    marca = raiz / "marca_subprocess"
    res = rodar_teste(ambiente, f'subprocess.run(["touch", {str(marca)!r}])', "import subprocess")
    assert bloqueado(res) and not marca.exists()


def test_os_system_bloqueado(ambiente):
    _, raiz, _ = ambiente
    marca = raiz / "marca_system"
    res = rodar_teste(ambiente, f'os.system("touch {marca}")', "import os")
    assert bloqueado(res) and not marca.exists()


def test_fork_exec_direto_bloqueado(ambiente):
    res = rodar_teste(ambiente, "_posixsubprocess.fork_exec()", "import _posixsubprocess")
    assert bloqueado(res)


def test_rede_externa_bloqueada(ambiente):
    res = rodar_teste(ambiente, 'socket.create_connection(("8.8.8.8", 53), timeout=1)', "import socket")
    assert bloqueado(res)


def test_dns_bloqueado(ambiente):
    res = rodar_teste(ambiente, 'socket.getaddrinfo("www.google.com", 80)', "import socket")
    assert bloqueado(res)


def test_leitura_de_segredos_bloqueada(ambiente):
    res = rodar_teste(ambiente, 'open(os.path.expanduser("~/.ssh/id_rsa")).read()', "import os")
    assert bloqueado(res)


def test_arquivos_protegidos_do_projeto(ambiente):
    projeto, _, _ = ambiente
    (projeto / ".git").mkdir()
    for alvo in (".git/config", ".minicode/state.json", ".env"):
        res = rodar_teste(ambiente, f'open({alvo!r}, "w").write("x")')
        assert bloqueado(res), alvo


def test_uso_legitimo_nao_e_bloqueado(ambiente):
    projeto, _, reg = ambiente
    (projeto / "test_ok.py").write_text(
        "import socket\n"
        "def test_ok(tmp_path):\n"
        "    (tmp_path / 'a.txt').write_text('x')\n"
        "    open('dentro.txt', 'w').write('y')\n"
        "    s = socket.socket(); s.bind(('127.0.0.1', 0)); s.close()\n"
        "    assert (tmp_path / 'a.txt').read_text() == 'x'\n"
    )
    res = reg.executar("run_tests", {})
    assert res["passou"] is True, res["saida"]
    assert (projeto / "dentro.txt").exists()


def test_sandbox_ativo_por_padrao(ambiente):
    assert ambiente[2].ctx.sandbox_ativo() is True


def test_falha_fechada_se_a_guarda_nao_carregar(ambiente, monkeypatch):
    projeto, _, reg = ambiente
    (projeto / "test_ok.py").write_text("def test_ok():\n    assert True\n")
    monkeypatch.setattr(reg.ctx, "_sandbox_ok", False)
    res = reg.executar("run_tests", {})
    assert res["ok"] is False and "indisponível" in res["saida"]


def test_desativacao_explicita_realmente_desliga(ambiente, monkeypatch):
    _, raiz, reg = ambiente
    fora = raiz / "fora.txt"
    monkeypatch.setenv("MINICODE_SANDBOX", "off")
    res = rodar_teste(ambiente, f'open({str(fora)!r}, "w").write("escapei")')
    assert res["passou"] is True and fora.exists()


def test_limites_de_recursos_nao_atrapalham_pytest_normal(ambiente):
    projeto, _, reg = ambiente
    (projeto / "test_ok.py").write_text("def test_ok():\n    assert sum(range(10**6)) > 0\n")
    assert reg.executar("run_tests", {})["passou"] is True