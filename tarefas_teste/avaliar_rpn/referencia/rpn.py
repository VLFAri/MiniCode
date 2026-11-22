OPERADORES = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}


def avaliar_rpn(expressao):
    pilha = []
    tokens = expressao.split()
    if not tokens:
        raise ValueError("expressão vazia")
    for token in tokens:
        if token in OPERADORES:
            if len(pilha) < 2:
                raise ValueError("operandos insuficientes")
            b, a = pilha.pop(), pilha.pop()
            pilha.append(OPERADORES[token](a, b))
        else:
            try:
                pilha.append(float(token))
            except ValueError:
                raise ValueError(f"token inválido: {token}")
    if len(pilha) != 1:
        raise ValueError("operandos sobrando")
    return pilha[0]
