import pytest
from datas import dias_entre

def test_mesmo_dia():
    assert dias_entre("2024-03-01", "2024-03-01") == 0

def test_ordem_normal():
    assert dias_entre("2024-01-01", "2024-01-31") == 30

def test_ordem_invertida():
    assert dias_entre("2024-01-31", "2024-01-01") == 30

def test_ano_bissexto():
    assert dias_entre("2024-02-28", "2024-03-01") == 2
    assert dias_entre("2023-02-28", "2023-03-01") == 1

@pytest.mark.parametrize("d", ["2024-13-01", "abc", "2024/01/01", "2024-02-30", ""])
def test_invalidas(d):
    with pytest.raises(ValueError):
        dias_entre(d, "2024-01-01")
