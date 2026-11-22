import re


def frequencia_palavras(texto):
    contagem = {}
    for palavra in re.findall(r"\w+", texto.lower()):
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem
