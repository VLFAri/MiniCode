def adicionar(item, carrinho=None):
    if carrinho is None:
        carrinho = []
    carrinho.append(item)
    return carrinho


def total(carrinho):
    return sum(i["preco"] * i["qtd"] for i in carrinho)
