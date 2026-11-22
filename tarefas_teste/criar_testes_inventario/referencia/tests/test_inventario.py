import pytest
from inventario import Inventario


def test_adicionar_e_quantidade():
    inv = Inventario()
    inv.adicionar("maca", 3)
    inv.adicionar("maca")
    assert inv.quantidade("maca") == 4


def test_item_inexistente_tem_zero():
    assert Inventario().quantidade("pera") == 0


def test_remover():
    inv = Inventario()
    inv.adicionar("maca", 5)
    inv.remover("maca", 2)
    assert inv.quantidade("maca") == 3


def test_remover_alem_do_estoque():
    inv = Inventario()
    inv.adicionar("maca", 1)
    with pytest.raises(ValueError):
        inv.remover("maca", 2)
    assert inv.quantidade("maca") == 1


def test_adicionar_quantidade_nao_positiva():
    inv = Inventario()
    with pytest.raises(ValueError):
        inv.adicionar("maca", 0)
    with pytest.raises(ValueError):
        inv.adicionar("maca", -1)
