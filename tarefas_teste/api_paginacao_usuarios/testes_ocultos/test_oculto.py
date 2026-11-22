import pytest
import app

def ids(corpo):
    return [u["id"] for u in corpo["items"]]

def test_padrao():
    status, corpo = app.handle("GET", "/users")
    assert status == 200
    assert corpo["page"] == 1 and corpo["page_size"] == 20 and corpo["total"] == 50
    assert ids(corpo) == list(range(1, 21))

def test_pagina_parcial_com_texto():
    status, corpo = app.handle("GET", "/users", {"page": "3", "page_size": "20"})
    assert status == 200 and ids(corpo) == list(range(41, 51))

def test_inteiros_e_tamanho_menor():
    status, corpo = app.handle("GET", "/users", {"page": 2, "page_size": 10})
    assert status == 200 and ids(corpo) == list(range(11, 21)) and corpo["page_size"] == 10

def test_alem_do_fim():
    status, corpo = app.handle("GET", "/users", {"page": "4"})
    assert status == 200 and corpo["items"] == [] and corpo["total"] == 50

def test_limite_maximo_aceito():
    status, corpo = app.handle("GET", "/users", {"page_size": "100"})
    assert status == 200 and len(corpo["items"]) == 50

@pytest.mark.parametrize("query", [{"page_size": "101"}, {"page": "0"}, {"page": "-1"}, {"page": "abc"},
                                   {"page_size": "0"}, {"page_size": "x"}, {"page": "1.5"}])
def test_invalidos_devolvem_400(query):
    status, corpo = app.handle("GET", "/users", query)
    assert status == 400 and "erro" in corpo

def test_outras_rotas_intactas():
    assert app.handle("GET", "/")[0] == 200
