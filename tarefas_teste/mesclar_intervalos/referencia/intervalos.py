def mesclar_intervalos(lista):
    resultado = []
    for inicio, fim in sorted(lista):
        if resultado and inicio <= resultado[-1][1]:
            resultado[-1] = (resultado[-1][0], max(resultado[-1][1], fim))
        else:
            resultado.append((inicio, fim))
    return resultado
