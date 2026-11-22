from datetime import datetime


def _converter(texto):
    return datetime.strptime(texto, "%Y-%m-%d").date()


def dias_entre(d1, d2):
    return abs((_converter(d2) - _converter(d1)).days)
