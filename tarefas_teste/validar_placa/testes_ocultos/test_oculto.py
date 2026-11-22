import pytest
from placas import validar_placa

@pytest.mark.parametrize("p", ["ABC-1234", "ABC1234", "abc1234", "ABC1D23", "abc1d23"])
def test_validas(p):
    assert validar_placa(p) is True

@pytest.mark.parametrize("p", ["AB1234", "ABC12345", "1BC1D23", "ABC-1D23", "ABCD123", "", "ABC 1234", None, 1234567])
def test_invalidas(p):
    assert validar_placa(p) is False
