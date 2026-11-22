def preco_vip(valor):
    if valor < 0:
        raise ValueError("valor negativo")
    return round(valor - valor * 20 / 100, 2)


def preco_normal(valor):
    if valor < 0:
        raise ValueError("valor negativo")
    return round(valor - valor * 5 / 100, 2)


def preco_promocao(valor):
    if valor < 0:
        raise ValueError("valor negativo")
    return round(valor - valor * 30 / 100, 2)
