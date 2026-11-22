import pytest
from telefone import normalizar_telefone

def test_celular_formatado():
    assert normalizar_telefone("(67) 99999-1234") == "+5567999991234"

def test_celular_puro():
    assert normalizar_telefone("67999991234") == "+5567999991234"

def test_com_prefixo():
    assert normalizar_telefone("+55 67 99999-1234") == "+5567999991234"

def test_fixo():
    assert normalizar_telefone("(67) 3333-4444") == "+556733334444"

@pytest.mark.parametrize("t", ["123", "abc", "", "(67) 89999-1234", "679999912345", "+55 67 9999-12"])
def test_invalidos(t):
    with pytest.raises(ValueError):
        normalizar_telefone(t)
