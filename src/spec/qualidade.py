"""Critérios de qualidade de uma especificação, além do formato exigido pelo agente.

`validar_spec` (gerador.py) é o portão do agente: só confere as seções. Para TREINAR um modelo isso é
pouco, porque specs vazias de conteúdo também passam. A validação estrita abaixo é usada para filtrar
o dataset e para medir a qualidade do modelo.
"""
from __future__ import annotations

import re

from src.spec.gerador import limpar_cercas, validar_spec

SECOES = ("# Specification", "## Objective", "## Parameters", "## Acceptance Criteria")

# O agente só executa Python da biblioteca padrão verificado por pytest (ver ValidadorComando).
FORA_DE_ESCOPO = re.compile(
    r"\b(fastapi|flask|django|pydantic|numpy|pandas|requests|redis|boto3|reportlab|sqlalchemy|"
    r"node\.?js|npm|java|javascript|typescript)\b", re.IGNORECASE)

_BLOCO = re.compile(r"```.*?```", re.DOTALL)
_LOGICA = re.compile(r"^\s*(return|for|while|if|elif|else:|try:|except|with|raise|yield)\b|\bself\.\w+\s*=", re.MULTILINE)
_ITEM = re.compile(r"^\s*([-*•]|\d+[.)])\s+")


def sem_cerca_externa(texto: str) -> str:
    """Remove a cerca ``` que envolve a resposta INTEIRA, e só ela. `limpar_cercas` também arranca a cerca de
    fechamento de um bloco de código que termine a spec, deixando o bloco aberto e escondendo seu conteúdo."""
    t = (texto or "").strip()
    return limpar_cercas(t) if t.startswith("```") else t


def secao_criterios(spec: str) -> str:
    partes = re.split(r"##\s*Acceptance Criteria", spec, flags=re.IGNORECASE)
    return partes[1] if len(partes) > 1 else ""


def itens_criterios(spec: str) -> list:
    """Cada critério (bullet ou item numerado), juntando as linhas de continuação."""
    itens = []
    for linha in secao_criterios(spec).splitlines():
        if _ITEM.match(linha):
            itens.append(linha.strip())
        elif itens and linha.strip():
            itens[-1] += " " + linha.strip()
    return itens


def tem_codigo_de_implementacao(spec: str) -> bool:
    return any(_LOGICA.search(bloco) for bloco in _BLOCO.findall(spec))


def validar_spec_estrita(texto: str, min_chars: int = 400, max_chars: int = 4500, min_criterios: int = 3) -> list:
    """Lista de problemas (vazia = spec boa para treinar)."""
    spec = sem_cerca_externa(texto)
    problemas = list(validar_spec(limpar_cercas(texto)))   # mesma visão do GeradorSpec do agente

    if not spec.lstrip().startswith("# Specification"):
        problemas.append("não começa com '# Specification' (texto antes da spec)")
    posicoes = [spec.lower().find(s.lower()) for s in SECOES]
    if all(p >= 0 for p in posicoes) and posicoes != sorted(posicoes):
        problemas.append("seções fora de ordem")

    if len(spec) < min_chars:
        problemas.append(f"spec curta demais (< {min_chars} caracteres)")
    if len(spec) > max_chars:
        problemas.append(f"spec longa demais (> {max_chars} caracteres)")

    itens = itens_criterios(spec)
    if len(itens) < min_criterios:
        problemas.append(f"menos de {min_criterios} critérios de aceitação")
    if sum("`" in i for i in itens) < 2:
        problemas.append("critérios sem exemplos concretos (entrada/saída entre crases)")

    if tem_codigo_de_implementacao(spec):
        problemas.append("contém código de implementação (a spec diz o quê, não o como)")
    achado = FORA_DE_ESCOPO.search(spec)
    if achado:
        problemas.append(f"cita biblioteca/linguagem fora do escopo: {achado.group(0)}")
    return problemas
