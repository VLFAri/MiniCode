def achatar(itens):
    resultado = []
    for item in itens:
        if isinstance(item, (list, tuple)):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado
