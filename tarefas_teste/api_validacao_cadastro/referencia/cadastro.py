import re

USUARIOS = {}
_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s.]+$")


def cadastrar(nome, email):
    if not isinstance(nome, str) or not nome.strip():
        raise ValueError("nome vazio")
    if not isinstance(email, str) or not _EMAIL.match(email):
        raise ValueError("e-mail inválido")
    chave = email.lower()
    if chave in USUARIOS:
        raise ValueError("e-mail já cadastrado")
    USUARIOS[chave] = {"nome": nome.strip(), "email": chave}
    return USUARIOS[chave]
