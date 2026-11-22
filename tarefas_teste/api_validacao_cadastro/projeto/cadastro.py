USUARIOS = {}


def cadastrar(nome, email):
    USUARIOS[email] = {"nome": nome, "email": email}
    return USUARIOS[email]
