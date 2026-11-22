import pytest
from calculadora import dividir, somar, subtrair


def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0


def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(0, 4) == -4


def test_dividir():
    assert dividir(6, 3) == 2
    assert dividir(1, 4) == 0.25


def test_dividir_por_zero():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
