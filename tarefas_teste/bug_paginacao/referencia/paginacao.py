def paginar(itens, pagina, tamanho):
    if pagina < 1 or tamanho < 1:
        raise ValueError("pagina e tamanho devem ser >= 1")
    inicio = (pagina - 1) * tamanho
    return itens[inicio:inicio + tamanho]
