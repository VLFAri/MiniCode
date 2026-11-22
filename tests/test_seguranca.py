import pytest
from src.ferramentas.base import ValidadorCaminho, ValidadorComando, ViolacaoSeguranca, ambiente_seguro


@pytest.fixture
def vc(tmp_path):
    return ValidadorCaminho(tmp_path)


def test_caminho_dentro_do_projeto(vc, tmp_path):
    assert vc.resolver("a/b.py") == (tmp_path / "a" / "b.py").resolve()


@pytest.mark.parametrize("p", ["../fora.txt", "/etc/passwd", "a/../../x", ""])
def test_caminho_fora_do_projeto(vc, p):
    with pytest.raises(ViolacaoSeguranca):
        vc.resolver(p)


def test_symlink_para_fora(vc, tmp_path):
    fora = tmp_path.parent / "segredo.txt"
    fora.write_text("x")
    (tmp_path / "link").symlink_to(fora)
    with pytest.raises(ViolacaoSeguranca):
        vc.resolver("link")


@pytest.mark.parametrize("p", [".git/config", ".minicode/state.json"])
def test_escrita_em_protegidos(vc, p):
    with pytest.raises(ViolacaoSeguranca):
        vc.resolver(p, escrita=True)
    vc.resolver(p)


def test_env_bloqueado_em_leitura_e_escrita(vc):
    for escrita in (True, False):
        with pytest.raises(ViolacaoSeguranca):
            vc.resolver(".env", escrita=escrita)
    vc.resolver(".env.example")


@pytest.mark.parametrize("cmd", [
    "sudo ls", "rm -rf /", "shutdown now", "reboot", "pytest; rm -rf /", "pytest && ls",
    "pytest | cat", "pytest > out.txt", "curl http://x", "bash -c ls", "ls", "python script.py",
    "git push", "git diff --output=x", "pytest --basetemp=/tmp/x", "", "pytest $(whoami)",
])
def test_comandos_bloqueados(cmd):
    with pytest.raises(ViolacaoSeguranca):
        ValidadorComando().validar(cmd)


@pytest.mark.parametrize("cmd", ["pytest", "pytest -q tests/", "python -m pytest -x", "git diff", "git status"])
def test_comandos_permitidos(cmd):
    assert ValidadorComando().validar(cmd)


def test_ambiente_sem_segredos(monkeypatch):
    monkeypatch.setenv("MINICODE_API_KEY", "segredo")
    monkeypatch.setenv("TOKEN", "segredo")
    env = ambiente_seguro()
    assert "MINICODE_API_KEY" not in env and "TOKEN" not in env


@pytest.mark.parametrize("cmd", [
    "npm install", "npm test", "npx jest", "yarn add express", "pnpm install", "node index.js",
    "pip install requests", "pip3 install fastapi", "poetry install", "conda install numpy",
    "cargo build", "go run main.go", "mvn test", "gradle build", "dotnet run", "ruby script.rb",
    "php index.php", "java Main", "make build", "cmake .",
])
def test_gerenciadores_e_runtimes_nao_suportados(cmd):
    with pytest.raises(ViolacaoSeguranca, match="não está disponível"):
        ValidadorComando().validar(cmd)