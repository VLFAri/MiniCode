from __future__ import annotations

import re

SECOES_OBRIGATORIAS = ("# Specification", "## Objective", "## Parameters", "## Acceptance Criteria")

PROMPT_SPEC = """Você é um engenheiro de software especialista em Spec-Driven Development.
Transforme o pedido numa especificação técnica formal, em Markdown, seguindo EXATAMENTE este formato:

# Specification

## Objective
(objetivo principal)

## Parameters / Requirements
(entradas, tipos, restrições e regras de negócio)

## Acceptance Criteria
(critérios claros e verificáveis por testes automatizados)

Arquivos do projeto:
{contexto}

Pedido do utilizador: {tarefa}
"""

PROMPT_PLANO = """Com base na especificação e nos arquivos do projeto, crie um plano numerado,
passo a passo, do que deve ser programado. Inclua a criação ou atualização dos testes.

Arquivos do projeto:
{contexto}

{spec}
"""


def limpar_cercas(texto: str) -> str:
    texto = texto.strip()
    texto = re.sub(r"^```[a-zA-Z]*\s*\n", "", texto)
    texto = re.sub(r"\n```\s*$", "", texto)
    return texto.strip()


def validar_spec(texto: str) -> list:
    problemas = []
    for secao in SECOES_OBRIGATORIAS:
        if secao.lower() not in texto.lower():
            problemas.append(f"seção ausente: '{secao}'")

    partes = re.split(r"##\s*Acceptance Criteria", texto, flags=re.IGNORECASE)
    if len(partes) < 2 or len(partes[1].strip()) < 10:
        problemas.append("a seção 'Acceptance Criteria' está vazia")
    return problemas


class GeradorSpec:
    def __init__(self, llm, log=None, max_tentativas: int = 3):
        self.llm = llm
        self.log = log or (lambda *a, **k: None)
        self.max_tentativas = max_tentativas

    def gerar_spec(self, tarefa: str, contexto: str) -> str:
        prompt = PROMPT_SPEC.format(tarefa=tarefa, contexto=contexto)
        problemas = []
        for tentativa in range(1, self.max_tentativas + 1):
            extra = ""
            if problemas:
                extra = f"\n\nA tentativa anterior foi rejeitada: {'; '.join(problemas)}. Corrija."
            spec = limpar_cercas(self.llm.complete(prompt + extra))
            problemas = validar_spec(spec)
            self.log("spec_attempt", attempt=tentativa, problems=problemas)
            if not problemas:
                return spec
        raise RuntimeError(f"Não foi possível gerar uma especificação válida: {problemas}")

    def gerar_plano(self, spec: str, contexto: str) -> str:
        plano = limpar_cercas(self.llm.complete(PROMPT_PLANO.format(spec=spec, contexto=contexto)))
        if not re.search(r"^\s*\d+[\.\)]", plano, flags=re.MULTILINE):
            raise RuntimeError("O plano gerado não é uma lista numerada.")
        return plano