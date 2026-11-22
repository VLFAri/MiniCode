import re

_PADRAO = re.compile(r"^(?:(\d+)h)?(?:(\d+)m)?(?:(\d+)s)?$")


def para_segundos(texto):
    achado = _PADRAO.match(texto)
    if not texto or achado is None:
        raise ValueError(f"duração inválida: {texto!r}")
    horas, minutos, segundos = (int(g or 0) for g in achado.groups())
    return horas * 3600 + minutos * 60 + segundos
