import pytest
import cadastro

@pytest.fixture
def limpo():
    cadastro.USUARIOS.clear()
    yield cadastro
    cadastro.USUARIOS.clear()

def test_cadastro_valido_guarda_em_minusculas(limpo):
    r = cadastro.cadastrar("Ana", "Ana@Exemplo.COM")
    assert r["email"] == "ana@exemplo.com" and r["nome"] == "Ana"
    assert "ana@exemplo.com" in cadastro.USUARIOS

@pytest.mark.parametrize("email", ["", "abc", "a@b", "a b@c.com", "@c.com", "a@.com", "a@@c.com"])
def test_email_invalido(limpo, email):
    with pytest.raises(ValueError):
        cadastro.cadastrar("Ana", email)
    assert cadastro.USUARIOS == {}

@pytest.mark.parametrize("nome", ["", "   "])
def test_nome_vazio(limpo, nome):
    with pytest.raises(ValueError):
        cadastro.cadastrar(nome, "ana@exemplo.com")
    assert cadastro.USUARIOS == {}

def test_duplicado_ignora_maiusculas(limpo):
    cadastro.cadastrar("Ana", "ana@exemplo.com")
    with pytest.raises(ValueError):
        cadastro.cadastrar("Outra", "ANA@exemplo.com")
    assert len(cadastro.USUARIOS) == 1
