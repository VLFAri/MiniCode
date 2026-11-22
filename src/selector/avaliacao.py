"""Avaliação de nível 1: acurácia do seletor de ferramentas no conjunto de teste."""
from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path

from src.selector.prompt import parse_saida


def avaliar_predicoes(golds: list, preds: list) -> dict:
    """golds: [{"tool","path"}]; preds: [{"tool","path"} | None] (None = saída inválida)."""
    n = len(golds)
    if n == 0:
        return {"n": 0}
    validas = sum(p is not None for p in preds)
    tool_ok = sum(p is not None and p["tool"] == g["tool"] for g, p in zip(golds, preds))
    exato = sum(p is not None and p["tool"] == g["tool"] and p.get("path") == g.get("path")
                for g, p in zip(golds, preds))
    por_gold, acertos = Counter(g["tool"] for g in golds), Counter()
    confusao = defaultdict(Counter)
    for g, p in zip(golds, preds):
        previsto = p["tool"] if p is not None else "<invalido>"
        confusao[g["tool"]][previsto] += 1
        acertos[g["tool"]] += previsto == g["tool"]
    maioria = por_gold.most_common(1)[0][1] / n
    return {
        "n": n,
        "json_valido": validas / n,
        "tool_accuracy": tool_ok / n,
        "tool_path_accuracy": exato / n,
        "baseline_classe_majoritaria": maioria,
        "recall_por_ferramenta": {t: acertos[t] / c for t, c in sorted(por_gold.items())},
        "confusao": {g: dict(c) for g, c in confusao.items()},
    }


def carregar_teste(caminho: str) -> list:
    return [json.loads(l) for l in Path(caminho).read_text(encoding="utf-8").splitlines() if l.strip()]


def avaliar_seletor(seletor, exemplos: list) -> dict:
    golds, preds = [], []
    for ex in exemplos:
        golds.append(parse_saida(ex["messages"][2]["content"]))
        try:
            preds.append(seletor.predict(ex["messages"][1]["content"]))
        except Exception:
            preds.append(None)
    return avaliar_predicoes(golds, preds)


def main(argv=None) -> int:
    from src.selector.seletor import MODELO_PEQUENO_PADRAO, criar_seletor

    ap = argparse.ArgumentParser(description="Nível 1: avalia o seletor (base, lora ou teacher) no test.jsonl")
    ap.add_argument("--test", default="datasets/test.jsonl")
    ap.add_argument("--modo", choices=["base", "lora", "teacher"], required=True)
    ap.add_argument("--modelo", default=MODELO_PEQUENO_PADRAO)
    ap.add_argument("--adapter", help="pasta do adapter LoRA (modo lora)")
    ap.add_argument("--saida", default="experiments/results/selector_{modo}.json")
    args = ap.parse_args(argv)

    metricas = avaliar_seletor(criar_seletor(args.modo, args.modelo, args.adapter), carregar_teste(args.test))
    destino = Path(args.saida.format(modo=args.modo))
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(metricas, indent=2, ensure_ascii=False), encoding="utf-8")
    for k in ("n", "json_valido", "tool_accuracy", "tool_path_accuracy", "baseline_classe_majoritaria"):
        print(f"{k}: {metricas[k]:.3f}" if isinstance(metricas[k], float) else f"{k}: {metricas[k]}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
