import pytest
from datas_br import eh_data_valida

@pytest.mark.parametrize("d", ["29/02/2024", "31/12/1999", "01/01/2000", "28/02/2023", "30/04/2024"])
def test_validas(d):
    assert eh_data_valida(d) is True

@pytest.mark.parametrize("d", ["29/02/2023", "31/04/2024", "01/13/2024", "00/01/2024", "1/1/2024",
                               "01-01-2024", "2024/01/01", "", "32/01/2024", "29/02/1900"])
def test_invalidas(d):
    assert eh_data_valida(d) is False
