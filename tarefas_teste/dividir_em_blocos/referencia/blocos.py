def dividir(lista, n):
    if n <= 0:
        raise ValueError("n deve ser positivo")
    return [list(lista[i:i + n]) for i in range(0, len(lista), n)]
