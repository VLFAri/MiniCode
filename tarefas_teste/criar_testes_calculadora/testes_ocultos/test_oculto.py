from pathlib import Path

import sys
from pathlib import Path as _P

import pytest

sys.path.insert(0, str(_P(__file__).parent))
from _mutacao import carregar_modulo, mutar, rodar_testes_do_agente

RAIZ = Path.cwd()
TESTES = RAIZ / "tests" / "test_calculadora.py"
ORIGINAL = (RAIZ / "calculadora.py").read_text()

MUTANTES = {
    "somar_subtrai": mutar(ORIGINAL, "return a + b", "return a - b"),
    "subtrair_soma": mutar(ORIGINAL, "return a - b", "return a + b"),
    "dividir_multiplica": mutar(ORIGINAL, "return a / b", "return a * b"),
    "dividir_excecao_errada": mutar(ORIGINAL, "ZeroDivisionError(", "ValueError("),
}


def test_arquivo_de_testes_existe_e_calculadora_nao_mudou():
    assert TESTES.is_file(), "tests/test_calculadora.py não foi criado"
    assert ORIGINAL.count("def ") == 3 and "return a + b" in ORIGINAL


def test_testes_passam_no_codigo_correto():
    total, falhas = rodar_testes_do_agente(TESTES, carregar_modulo("calculadora", ORIGINAL), "calculadora")
    assert total >= 3, "poucos testes"
    assert falhas == []


@pytest.mark.parametrize("nome", sorted(MUTANTES))
def test_testes_detectam_mutante(nome):
    total, falhas = rodar_testes_do_agente(TESTES, carregar_modulo("calculadora", MUTANTES[nome]), "calculadora")
    assert falhas, f"os testes do agente NÃO detectaram o defeito '{nome}'"
