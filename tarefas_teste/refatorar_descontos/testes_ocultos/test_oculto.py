import ast
from pathlib import Path

import pytest
import preco

@pytest.mark.parametrize("f, entrada, esperado", [
    (preco.preco_vip, 100, 80.0), (preco.preco_normal, 100, 95.0), (preco.preco_promocao, 100, 70.0),
    (preco.preco_vip, 19.99, 15.99), (preco.preco_promocao, 0, 0.0),
])
def test_comportamento_preservado(f, entrada, esperado):
    assert f(entrada) == esperado

@pytest.mark.parametrize("f", [preco.preco_vip, preco.preco_normal, preco.preco_promocao])
def test_negativo_continua_invalido(f):
    with pytest.raises(ValueError):
        f(-1)

def test_aplicar_desconto():
    assert preco.aplicar_desconto(200, 10) == 180.0
    assert preco.aplicar_desconto(50, 0) == 50.0
    assert preco.aplicar_desconto(50, 100) == 0.0

@pytest.mark.parametrize("valor, pct", [(-1, 10), (10, -1), (10, 101)])
def test_aplicar_desconto_invalido(valor, pct):
    with pytest.raises(ValueError):
        preco.aplicar_desconto(valor, pct)

def test_duplicacao_removida():
    arvore = ast.parse(Path(preco.__file__).read_text())
    assert sum(isinstance(n, ast.Raise) for n in ast.walk(arvore)) <= 2, "a validação ainda está duplicada"
