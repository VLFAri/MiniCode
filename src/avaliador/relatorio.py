"""Monta docs/resultados.md SÓ com números que existem nos arquivos de resultado (nada é preenchido à mão).

Fontes (geradas pelo notebook e pelos scripts de avaliação):
  experiments/results/spec_colab.json          nível 1: modelo base x fine-tuned x Qwen-14B  (notebooks/train.ipynb)
  experiments/res_spec_{14b,base,lora}/        nível 2: agente completo com cada gerador de spec  (main.py --avaliar)
  experiments/ablacao/<config>/rodada_N/       ablação  (experiments/ablacao.py)
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.avaliador.tabelas import carregar_ablacao, tabela_markdown

PENDENTE = "_(ainda não executado: arquivo `{}` não encontrado)_"


def _ler(caminho: Path):
    return json.loads(caminho.read_text(encoding="utf-8")) if caminho.exists() else None


def tabela_nivel1(dados: dict) -> str:
    linhas = ["| Modelo | Spec válida p/ o agente | Spec válida (estrita) | Critérios (média) | Com código de implementação |",
              "|---|---|---|---|---|"]
    nomes = {"base": "modelo base (baseline)", "finetuned": "mesmo modelo + QLoRA", "qwen14b": "Qwen-14B (referência)"}
    if (dados.get("qwen14b") or {}).get("modelo_referencia"):
        nomes["qwen14b"] = f"referência: {dados['qwen14b']['modelo_referencia']}"
    n = None
    for chave, nome in nomes.items():
        m = dados.get(chave)
        if not m:
            linhas.append(f"| {nome} | n/d | n/d | n/d | n/d |")
            continue
        n = n or m.get("n")
        linhas.append(f"| {nome} | {m['valida_agente']:.2f} | {m['valida_estrita']:.2f} | "
                      f"{m['criterios_medio']:.1f} | {m['com_codigo_de_implementacao']:.2f} |")
    return "\n".join(linhas) + (f"\n\nExemplos no conjunto de teste: {n}." if n else "")


def tabela_agente(por_nome: dict) -> str:
    colunas = ["HiddenSuccessRate", "TaskSuccessRate", "FirstAttemptSuccess", "SpecFirstTryValid",
               "AverageSpecAttempts", "AverageIterations", "AverageLLMCalls"]
    linhas = ["| Gerador de especificação | " + " | ".join(colunas) + " |", "|---|" + "---|" * len(colunas)]
    for nome, resumo in por_nome.items():
        linhas.append(f"| {nome} | " + " | ".join(f"{resumo[c]:.2f}" if c in resumo else "n/d" for c in colunas) + " |")
    return "\n".join(linhas)


def gerar(raiz: str = ".", saida: str = "docs/resultados.md") -> str:
    raiz = Path(raiz)
    partes = ["# Resultados experimentais", "",
              "Arquivo gerado por `python experiments/gerar_relatorio.py`; todos os números vêm dos arquivos de resultado.", ""]

    partes += ["## 1. Nível 1: gerador de especificações (base × fine-tuned × Qwen-14B)", ""]
    colab = _ler(raiz / "experiments/results/spec_colab.json")
    teacher = _ler(raiz / "experiments/results/spec_teacher.json")      # experiments/eval_spec.py --modo teacher
    if teacher and (not colab or not colab.get("qwen14b")):
        colab = {**(colab or {}), "qwen14b": teacher}
    partes += [tabela_nivel1(colab) if colab else PENDENTE.format("experiments/results/spec_colab.json"), ""]
    if (raiz / "experiments/results/spec_loss.png").exists():
        partes += ["![loss](../experiments/results/spec_loss.png)", ""]

    partes += ["## 2. Nível 2: agente completo com cada gerador de especificação", ""]
    nivel2, modelos = {}, {}
    for nome, pasta in (("Qwen-14B", "res_spec_14b"), ("modelo base", "res_spec_base"), ("fine-tuned (QLoRA)", "res_spec_lora")):
        d = _ler(raiz / "experiments" / pasta / "resultados.json")
        if d:
            nivel2[nome] = d["summary"]
            modelos[nome] = sorted({r["llm_model"] for r in d.get("results", []) if r.get("llm_model")})
    partes += [tabela_agente(nivel2) if nivel2 else PENDENTE.format("experiments/res_spec_*/resultados.json"), ""]
    if any(modelos.values()):   # o modelo PRINCIPAL (plano, código, reparo) pode não ser o 14B da disciplina
        partes += ["Modelo principal do agente (plano, código e reparo) em cada execução: "
                   + "; ".join(f"{n}: {', '.join(m) or 'n/d'}" for n, m in modelos.items()) + ".", ""]

    partes += ["## 3. Ablação", ""]
    ablacao = carregar_ablacao(str(raiz / "experiments/ablacao"))
    partes += [tabela_markdown(ablacao) if ablacao else PENDENTE.format("experiments/ablacao/*/rodada_*/resultados.json"), ""]

    texto = "\n".join(partes) + "\n"
    destino = raiz / saida
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(texto, encoding="utf-8")
    return texto


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Gera docs/resultados.md a partir dos arquivos de resultado")
    ap.add_argument("--raiz", default=".")
    ap.add_argument("--saida", default="docs/resultados.md")
    args = ap.parse_args(argv)
    print(gerar(args.raiz, args.saida))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
