def adicionar(item, carrinho=[]):
    carrinho.append(item)
    return carrinho


def total(carrinho):
    return sum(i["preco"] * i["qtd"] for i in carrinho)
