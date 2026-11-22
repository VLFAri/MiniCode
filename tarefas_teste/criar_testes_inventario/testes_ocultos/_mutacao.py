"""Auxiliar de mutation testing para avaliar os TESTES que o agente escreveu (rodam em processo, sem subprocess)."""
import importlib.util
import inspect
import sys
import types
from pathlib import Path


def carregar_modulo(nome, codigo):
    modulo = types.ModuleType(nome)
    exec(compile(codigo, f"<{nome}>", "exec"), modulo.__dict__)
    return modulo


def rodar_testes_do_agente(caminho, modulo_alvo, nome_modulo):
    """Importa o arquivo de testes do agente com `nome_modulo` apontando para `modulo_alvo` e roda as funções
    test_* sem argumentos. Devolve (quantidade_de_testes, lista_de_falhas)."""
    anterior = sys.modules.get(nome_modulo)
    sys.modules[nome_modulo] = modulo_alvo
    try:
        spec = importlib.util.spec_from_file_location("testes_do_agente", caminho)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        falhas, total = [], 0
        for nome, fn in vars(mod).items():
            if not (nome.startswith("test_") and callable(fn)):
                continue
            if inspect.signature(fn).parameters:      # depende de fixture: ignorado
                continue
            total += 1
            try:
                fn()
            except BaseException as e:
                falhas.append((nome, type(e).__name__))
        return total, falhas
    finally:
        if anterior is None:
            sys.modules.pop(nome_modulo, None)
        else:
            sys.modules[nome_modulo] = anterior


def mutar(codigo, antigo, novo):
    assert antigo in codigo, antigo
    return codigo.replace(antigo, novo, 1)
