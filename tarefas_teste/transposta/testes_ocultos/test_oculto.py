import pytest
from matriz import transposta

def test_retangular():
    assert transposta([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

def test_quadrada():
    assert transposta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_vazia():
    assert transposta([]) == []

def test_irregular():
    with pytest.raises(ValueError):
        transposta([[1, 2], [3]])

def test_nao_altera_original():
    m = [[1, 2], [3, 4]]
    transposta(m)
    assert m == [[1, 2], [3, 4]]
