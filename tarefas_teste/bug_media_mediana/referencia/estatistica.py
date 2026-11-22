def media(valores):
    if not valores:
        raise ValueError("lista vazia")
    return sum(valores) / len(valores)


def mediana(valores):
    if not valores:
        raise ValueError("lista vazia")
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    if len(ordenados) % 2:
        return ordenados[meio]
    return (ordenados[meio - 1] + ordenados[meio]) / 2
