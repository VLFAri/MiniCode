VOGAIS = set("aeiouáéíóúâêôãõàü")


def eh_palindromo(s):
    letras = [c for c in s.lower() if c.isalnum()]
    return letras == letras[::-1]


def contar_vogais(s):
    return sum(1 for c in s.lower() if c in VOGAIS)
