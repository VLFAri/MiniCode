def eh_palindromo(s):
    return s == s[::-1]


def contar_vogais(s):
    return sum(1 for c in s if c in "aeiou")
