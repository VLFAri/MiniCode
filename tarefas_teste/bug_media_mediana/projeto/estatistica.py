def media(valores):
    return sum(valores) / (len(valores) - 1)


def mediana(valores):
    ordenados = sorted(valores)
    meio = len(ordenados) // 2
    return ordenados[meio]
