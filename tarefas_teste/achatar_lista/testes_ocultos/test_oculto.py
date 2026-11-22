from achatar import achatar

def test_profundo():
    assert achatar([1, [2, [3, [4]]], 5]) == [1, 2, 3, 4, 5]

def test_strings_nao_sao_achatadas():
    assert achatar(["ab", ["c"]]) == ["ab", "c"]

def test_vazia():
    assert achatar([]) == []

def test_tuplas():
    assert achatar((1, (2, 3), [4])) == [1, 2, 3, 4]

def test_listas_vazias_aninhadas():
    assert achatar([[], [[]], 1]) == [1]
