from pathlib import Path

import sys
from pathlib import Path as _P

import pytest

sys.path.insert(0, str(_P(__file__).parent))
from _mutacao import carregar_modulo, mutar, rodar_testes_do_agente

RAIZ = Path.cwd()
TESTES = RAIZ / "tests" / "test_inventario.py"
ORIGINAL = (RAIZ / "inventario.py").read_text()

MUTANTES = {
    "adicionar_subtrai": mutar(ORIGINAL, ".get(item, 0) + qtd", ".get(item, 0) - qtd"),
    "sem_validar_qtd": mutar(ORIGINAL, "if qtd <= 0:", "if False:"),
    "remover_sem_guarda": mutar(ORIGINAL, "< qtd:", "< -1:"),
    "remover_soma": mutar(ORIGINAL, "self._itens[item] -= qtd", "self._itens[item] += qtd"),
    "inexistente_nao_zero": mutar(ORIGINAL, "return self._itens.get(item, 0)", "return self._itens.get(item, 1)"),
}


def test_arquivo_de_testes_existe():
    assert TESTES.is_file(), "tests/test_inventario.py não foi criado"


def test_testes_passam_no_codigo_correto():
    total, falhas = rodar_testes_do_agente(TESTES, carregar_modulo("inventario", ORIGINAL), "inventario")
    assert total >= 4, "poucos testes"
    assert falhas == []


@pytest.mark.parametrize("nome", sorted(MUTANTES))
def test_testes_detectam_mutante(nome):
    total, falhas = rodar_testes_do_agente(TESTES, carregar_modulo("inventario", MUTANTES[nome]), "inventario")
    assert falhas, f"os testes do agente NÃO detectaram o defeito '{nome}'"
