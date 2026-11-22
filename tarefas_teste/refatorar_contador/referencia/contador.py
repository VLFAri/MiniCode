class Contador:
    def __init__(self):
        self._valor = 0

    def incrementar(self, passo=1):
        self._valor += passo
        return self._valor

    def valor(self):
        return self._valor

    def zerar(self):
        self._valor = 0


_padrao = Contador()


def incrementar(passo=1):
    return _padrao.incrementar(passo)


def valor():
    return _padrao.valor()


def zerar():
    _padrao.zerar()
