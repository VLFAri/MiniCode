from palavras import frequencia_palavras

def test_basico():
    assert frequencia_palavras("a b a") == {"a": 2, "b": 1}

def test_maiusculas_e_pontuacao():
    assert frequencia_palavras("Olá, olá! Mundo.") == {"olá": 2, "mundo": 1}

def test_vazio():
    assert frequencia_palavras("") == {}

def test_espacos_extras():
    assert frequencia_palavras("  x   x ") == {"x": 2}
