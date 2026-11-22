def aplicar_desconto(valor, percentual):
    if valor < 0:
        raise ValueError("valor negativo")
    if not 0 <= percentual <= 100:
        raise ValueError("percentual inválido")
    return round(valor - valor * percentual / 100, 2)


def preco_vip(valor):
    return aplicar_desconto(valor, 20)


def preco_normal(valor):
    return aplicar_desconto(valor, 5)


def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
