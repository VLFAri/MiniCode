import pytest
from rpn import avaliar_rpn

def test_soma():
    assert avaliar_rpn("3 4 +") == 7

def test_composta():
    assert avaliar_rpn("5 1 2 + 4 * + 3 -") == 14

def test_divisao():
    assert avaliar_rpn("6 3 /") == 2

def test_decimais():
    assert avaliar_rpn("1.5 2 *") == 3

@pytest.mark.parametrize("expr", ["", "1 +", "1 2", "a b +", "1 2 ^"])
def test_invalidas(expr):
    with pytest.raises(ValueError):
        avaliar_rpn(expr)

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        avaliar_rpn("1 0 /")
