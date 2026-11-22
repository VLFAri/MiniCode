"""Formato ÚNICO do seletor de ferramentas, compartilhado por dataset, treino e inferência.

Se o prompt usado no treino diferir do usado na inferência, o modelo fine-tuned degrada em silêncio;
por isso tudo passa por `mensagens()` e `rotulo()`.
"""
from __future__ import annotations

import json

# run_tests fica de fora: quem executa os testes é o harness, não o LLM
FERRAMENTAS_SELETOR = (
    "list_files", "read_file", "write_file", "create_file", "replace_text",
    "search_code", "git_diff", "run_command", "finish",
)

PROMPT_SELETOR = (
    "Você é o seletor de ferramentas do MiniCode. Dado o estado atual do agente, responda SOMENTE "
    'com um JSON {"tool": "<nome>", "path": "<arquivo ou null>"} indicando a PRÓXIMA ação.\n'
    "Ferramentas: " + ", ".join(FERRAMENTAS_SELETOR) + ".\n"
    "Use 'finish' quando a implementação estiver completa, para o sistema rodar os testes."
)


def mensagens(features: str) -> list:
    """Entrada do modelo (system + user), idêntica no treino e na inferência."""
    return [
        {"role": "system", "content": PROMPT_SELETOR},
        {"role": "user", "content": features},
    ]


def rotulo(tool: str, path=None) -> str:
    """Saída esperada do modelo, serializada de forma determinística."""
    return json.dumps({"tool": tool, "path": path if isinstance(path, str) else None}, ensure_ascii=False)


def parse_saida(texto: str):
    """Extrai {"tool", "path"} da resposta do modelo; None se não houver JSON válido com 'tool'."""
    texto = (texto or "").replace("```json", "").replace("```", "")
    decoder = json.JSONDecoder()
    pos = 0
    while True:
        ini = texto.find("{", pos)
        if ini == -1:
            return None
        try:
            obj, fim = decoder.raw_decode(texto, ini)
        except json.JSONDecodeError:
            pos = ini + 1
            continue
        if isinstance(obj, dict) and isinstance(obj.get("tool"), str):
            caminho = obj.get("path")
            return {"tool": obj["tool"], "path": caminho if isinstance(caminho, str) else None}
        pos = fim
