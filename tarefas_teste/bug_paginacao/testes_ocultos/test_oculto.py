import pytest
from paginacao import paginar

DADOS = list(range(10))

def test_primeira_pagina():
    assert paginar(DADOS, 1, 3) == [0, 1, 2]

def test_pagina_do_meio():
    assert paginar(DADOS, 2, 3) == [3, 4, 5]

def test_ultima_pagina_parcial():
    assert paginar(DADOS, 4, 3) == [9]

def test_alem_do_fim():
    assert paginar(DADOS, 5, 3) == []

@pytest.mark.parametrize("pagina, tamanho", [(0, 3), (-1, 3), (1, 0), (1, -2)])
def test_invalidos(pagina, tamanho):
    with pytest.raises(ValueError):
        paginar(DADOS, pagina, tamanho)
