"""Tabelas de resultados (sem dependência do agente nem de bibliotecas de LLM)."""
from __future__ import annotations

import json
import statistics
from pathlib import Path

METRICAS = ["HiddenSuccessRate", "FalseSuccessRate", "TaskSuccessRate", "FirstAttemptSuccess",
            "AverageIterations", "AverageLLMCalls"]


def media_e_desvio(valores: list):
    return statistics.fmean(valores), (statistics.stdev(valores) if len(valores) > 1 else None)


def tabela_markdown(por_config: dict) -> str:
    """por_config: {nome: [resumo_rodada1, resumo_rodada2, ...]} -> tabela com média (± desvio se houver >1 rodada)."""
    linhas = ["| Configuração | " + " | ".join(METRICAS) + " |", "|---|" + "---|" * len(METRICAS)]
    for nome, rodadas in por_config.items():
        celulas = []
        for m in METRICAS:
            valores = [r[m] for r in rodadas if m in r]
            if not valores:
                celulas.append("n/d")
                continue
            media, desvio = media_e_desvio(valores)
            celulas.append(f"{media:.2f}" + (f" ± {desvio:.2f}" if desvio is not None else ""))
        linhas.append(f"| {nome} (n={len(rodadas)} rodada(s)) | " + " | ".join(celulas) + " |")
    return "\n".join(linhas)


def carregar_ablacao(saida: str) -> dict:
    """Reconstrói {config: [resumos]} a partir de uma pasta já executada (para o relatório)."""
    por_config = {}
    for d in sorted(Path(saida).glob("*/rodada_*/resultados.json")):
        por_config.setdefault(d.parent.parent.name, []).append(json.loads(d.read_text(encoding="utf-8"))["summary"])
    return por_config
