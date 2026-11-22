import contador
from contador import Contador

def test_instancias_independentes():
    a, b = Contador(), Contador()
    a.incrementar()
    a.incrementar(5)
    assert a.valor() == 6 and b.valor() == 0

def test_zerar_instancia():
    c = Contador()
    c.incrementar(3)
    c.zerar()
    assert c.valor() == 0

def test_funcoes_de_modulo_continuam():
    contador.zerar()
    contador.incrementar()
    contador.incrementar(2)
    assert contador.valor() == 3
    contador.zerar()
    assert contador.valor() == 0

def test_modulo_e_instancia_nao_se_misturam():
    contador.zerar()
    c = Contador()
    c.incrementar(10)
    assert contador.valor() == 0
