from carrinho import adicionar, total

def item(p, q=1):
    return {"preco": p, "qtd": q}

def test_chamadas_independentes():
    a = adicionar(item(1))
    b = adicionar(item(2))
    assert a is not b
    assert len(a) == 1 and len(b) == 1

def test_carrinho_informado_e_alterado_no_lugar():
    c = []
    r = adicionar(item(1), c)
    assert r is c and len(c) == 1
    adicionar(item(2), c)
    assert len(c) == 2

def test_total():
    c = []
    adicionar(item(10, 2), c)
    adicionar(item(5), c)
    assert total(c) == 25

def test_terceira_chamada_sem_vazamento():
    adicionar(item(1))
    adicionar(item(1))
    assert len(adicionar(item(1))) == 1
