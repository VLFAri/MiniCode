import re

_PADRAO = re.compile(r"^(?:[A-Za-z]{3}-?\d{4}|[A-Za-z]{3}\d[A-Za-z]\d{2})$")


def validar_placa(texto):
    return isinstance(texto, str) and _PADRAO.match(texto) is not None
