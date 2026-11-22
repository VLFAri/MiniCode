import pytest
from texto import contar_vogais, eh_palindromo

@pytest.mark.parametrize("s", ["Anotaram a data da maratona", "A man, a plan, a canal: Panama", "", "a"])
def test_palindromos(s):
    assert eh_palindromo(s) is True

@pytest.mark.parametrize("s", ["abc", "Python", "ab"])
def test_nao_palindromos(s):
    assert eh_palindromo(s) is False

def test_vogais_maiusculas():
    assert contar_vogais("AEIOU") == 5

def test_vogais_acentuadas():
    assert contar_vogais("áéíóú âêô ãõ") == 10

def test_sem_vogais():
    assert contar_vogais("xyz") == 0
    assert contar_vogais("") == 0
