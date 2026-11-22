import re
from datetime import date

_FORMATO = re.compile(r"^\d{2}/\d{2}/\d{4}$")


def eh_data_valida(texto):
    if not isinstance(texto, str) or not _FORMATO.match(texto):
        return False
    dia, mes, ano = (int(p) for p in texto.split("/"))
    try:
        date(ano, mes, dia)
    except ValueError:
        return False
    return True
