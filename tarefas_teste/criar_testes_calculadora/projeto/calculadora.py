def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("divisão por zero")
    return a / b
