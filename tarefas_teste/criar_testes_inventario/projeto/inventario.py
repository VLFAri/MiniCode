class Inventario:
    def __init__(self):
        self._itens = {}

    def adicionar(self, item, qtd=1):
        if qtd <= 0:
            raise ValueError("quantidade deve ser positiva")
        self._itens[item] = self._itens.get(item, 0) + qtd

    def remover(self, item, qtd=1):
        if self._itens.get(item, 0) < qtd:
            raise ValueError("estoque insuficiente")
        self._itens[item] -= qtd

    def quantidade(self, item):
        return self._itens.get(item, 0)
