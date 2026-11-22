import pytest
from estatistica import media, mediana

def test_media():
    assert media([1, 2, 3]) == 2
    assert media([2]) == 2
    assert media([1, 2]) == 1.5

def test_mediana_impar():
    assert mediana([3, 1, 2]) == 2

def test_mediana_par():
    assert mediana([1, 2, 3, 4]) == 2.5
    assert mediana([4, 1, 3, 2]) == 2.5

@pytest.mark.parametrize("f", [media, mediana])
def test_vazia(f):
    with pytest.raises(ValueError):
        f([])

def test_nao_altera_lista():
    v = [3, 1, 2]
    mediana(v)
    media(v)
    assert v == [3, 1, 2]
