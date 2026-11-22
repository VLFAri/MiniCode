def paginar(itens, pagina, tamanho):
    inicio = pagina * tamanho
    fim = inicio + tamanho
    return itens[inicio:fim]
