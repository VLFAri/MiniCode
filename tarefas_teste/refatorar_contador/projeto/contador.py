_contagem = 0


def incrementar(passo=1):
    global _contagem
    _contagem += passo
    return _contagem


def valor():
    return _contagem


def zerar():
    global _contagem
    _contagem = 0
