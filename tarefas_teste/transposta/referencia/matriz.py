def transposta(m):
    if not m:
        return []
    if any(len(linha) != len(m[0]) for linha in m):
        raise ValueError("linhas com tamanhos diferentes")
    return [list(coluna) for coluna in zip(*m)]
