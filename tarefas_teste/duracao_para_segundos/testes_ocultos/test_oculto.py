import pytest
from duracao import para_segundos

@pytest.mark.parametrize("texto, esperado", [
    ("1h30m", 5400), ("45s", 45), ("2h", 7200), ("1h1m1s", 3661), ("90m", 5400), ("0s", 0),
])
def test_validas(texto, esperado):
    assert para_segundos(texto) == esperado

@pytest.mark.parametrize("texto", ["", "abc", "1x", "h", "1s30m", "1h 30m", "-5s", "1.5h"])
def test_invalidas(texto):
    with pytest.raises(ValueError):
        para_segundos(texto)
