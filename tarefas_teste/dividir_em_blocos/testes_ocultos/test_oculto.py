import pytest
from blocos import dividir

def test_com_resto():
    assert dividir([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]

def test_exato():
    assert dividir([1, 2, 3, 4], 2) == [[1, 2], [3, 4]]

def test_n_maior_que_lista():
    assert dividir([1, 2], 5) == [[1, 2]]

def test_vazia():
    assert dividir([], 3) == []

@pytest.mark.parametrize("n", [0, -1])
def test_n_invalido(n):
    with pytest.raises(ValueError):
        dividir([1], n)

def test_nao_altera_original():
    base = [1, 2, 3]
    dividir(base, 2)
    assert base == [1, 2, 3]
