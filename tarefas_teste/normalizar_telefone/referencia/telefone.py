import re


def normalizar_telefone(texto):
    limpo = re.sub(r"[\s()\-]", "", texto)
    if limpo.startswith("+55"):
        limpo = limpo[3:]
    if not limpo.isdigit() or len(limpo) not in (10, 11):
        raise ValueError("telefone inválido")
    if len(limpo) == 11 and limpo[2] != "9":
        raise ValueError("celular deve começar com 9")
    return "+55" + limpo
