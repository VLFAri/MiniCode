"""Constrói o dataset de tool selection a partir dos rastros (.minicode/) de execuções do teacher.

Entrada : experiments/resultados/<tarefa>/{state.json, actions.jsonl} + resultados.json (opcional)
Saída   : train.jsonl / val.jsonl / test.jsonl (formato de chat) + stats.json

Decisões de qualidade documentadas em stats.json: quais tarefas foram descartadas e por quê, quantos
exemplos duplicados saíram e como ficou a distribuição de ferramentas em cada split.
"""
from __future__ import annotations

import argparse
import json
import random
from collections import Counter
from pathlib import Path

from src.selector.prompt import FERRAMENTAS_SELETOR, mensagens, rotulo

# eventos que indicam uma execução "suja" do teacher (loops, tentativas de burlar a segurança)
EVENTOS_DESCARTAM_TAREFA = {
    "loop_detected": "loop_detectado",
    "same_error_abort": "mesmo_erro_repetido",
    "security_violation": "violacao_seguranca",
    "request_refused": "pedido_recusado",
}


def _ler_jsonl(caminho: Path) -> list:
    if not caminho.exists():
        return []
    return [json.loads(l) for l in caminho.read_text(encoding="utf-8").splitlines() if l.strip()]


def _ocultos(dir_resultados: Path) -> dict:
    """task -> hidden_pass, lido do resultados.json gerado pelo avaliador (se existir)."""
    arq = dir_resultados / "resultados.json"
    if not arq.exists():
        return {}
    dados = json.loads(arq.read_text(encoding="utf-8"))
    return {r["task"]: r.get("hidden_pass") for r in dados.get("results", [])}


def motivo_descarte(estado: dict, eventos: list, hidden_pass, exigir_ocultos: bool):
    """None se a execução serve como fonte de exemplos; senão, o motivo do descarte."""
    sucesso = estado.get("success", estado.get("state") == "DONE")
    if not sucesso:
        return "tarefa_nao_concluida"
    if hidden_pass is False:
        return "testes_ocultos_falharam"
    if exigir_ocultos and hidden_pass is not True:
        return "sem_resultado_dos_testes_ocultos"
    for ev in eventos:
        if ev.get("type") in EVENTOS_DESCARTAM_TAREFA:
            return EVENTOS_DESCARTAM_TAREFA[ev["type"]]
    return None


def extrair_exemplos(eventos: list) -> list:
    """Pares (features, label) válidos, na ordem em que o teacher decidiu."""
    pares = []
    for ev in eventos:
        if ev.get("type") != "selector_example":
            continue
        label = ev.get("label") or {}
        if not ev.get("features") or label.get("tool") not in FERRAMENTAS_SELETOR:
            continue
        pares.append((ev["features"], label["tool"], label.get("path")))
    return pares


def dividir_por_tarefa(tarefas: list, seed: int = 42, frac_val: float = 0.15, frac_test: float = 0.15) -> dict:
    """Divide por TAREFA (nunca por passo): passos da mesma tarefa são quase iguais entre si, e
    separá-los entre treino e teste vazaria o gabarito para o conjunto de teste."""
    tarefas = sorted(set(tarefas))
    random.Random(seed).shuffle(tarefas)
    n = len(tarefas)
    n_test = max(1, round(n * frac_test)) if n >= 3 else 0
    n_val = max(1, round(n * frac_val)) if n >= 3 else 0
    return {
        "test": tarefas[:n_test],
        "val": tarefas[n_test:n_test + n_val],
        "train": tarefas[n_test + n_val:],
    }


def construir(dirs_resultados: list, saida: str, seed: int = 42, exigir_ocultos: bool = False) -> dict:
    saida = Path(saida)
    saida.mkdir(parents=True, exist_ok=True)

    por_tarefa = {}                      # tarefa -> lista de (features, tool, path)
    descartadas, vistas = {}, set()
    for d in map(Path, dirs_resultados):
        ocultos = _ocultos(d)
        for dir_tarefa in sorted(p for p in d.iterdir() if (p / "actions.jsonl").exists()):
            nome = dir_tarefa.name
            vistas.add(nome)
            estado = json.loads((dir_tarefa / "state.json").read_text(encoding="utf-8"))
            eventos = _ler_jsonl(dir_tarefa / "actions.jsonl")
            motivo = motivo_descarte(estado, eventos, ocultos.get(nome), exigir_ocultos)
            if motivo:
                descartadas.setdefault(nome, []).append(motivo)
                continue
            por_tarefa.setdefault(nome, []).extend(extrair_exemplos(eventos))

    divisao = dividir_por_tarefa(list(por_tarefa), seed)
    stats = {
        "tarefas_vistas": len(vistas),
        "tarefas_usadas": len(por_tarefa),
        "tarefas_descartadas": descartadas,
        "duplicados_removidos": 0,
        "splits": {},
    }
    for split, tarefas in divisao.items():
        unicos, vistos = [], set()
        for t in tarefas:
            for features, tool, path in por_tarefa[t]:
                chave = (features, tool, path)
                if chave in vistos:
                    stats["duplicados_removidos"] += 1
                    continue
                vistos.add(chave)
                unicos.append({
                    "task": t,
                    "messages": mensagens(features) + [{"role": "assistant", "content": rotulo(tool, path)}],
                })
        (saida / f"{split}.jsonl").write_text(
            "".join(json.dumps(ex, ensure_ascii=False) + "\n" for ex in unicos), encoding="utf-8")
        contagem = Counter(json.loads(ex["messages"][2]["content"])["tool"] for ex in unicos)
        stats["splits"][split] = {"tarefas": len(tarefas), "exemplos": len(unicos), "por_ferramenta": dict(contagem)}

    (saida / "stats.json").write_text(json.dumps(stats, indent=2, ensure_ascii=False), encoding="utf-8")
    return stats


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Gera train/val/test do seletor de ferramentas a partir dos rastros do teacher")
    ap.add_argument("--resultados", nargs="+", default=["experiments/resultados"],
                    help="um ou mais diretórios gerados por `minicode --avaliar`")
    ap.add_argument("--saida", default="datasets")
    ap.add_argument("--seed", type=int, default=42)
    ap.add_argument("--exigir-ocultos", action="store_true",
                    help="só aceita tarefas cujos testes ocultos passaram (recomendado)")
    args = ap.parse_args(argv)

    stats = construir(args.resultados, args.saida, args.seed, args.exigir_ocultos)
    print(f"tarefas: {stats['tarefas_usadas']} usadas de {stats['tarefas_vistas']} "
          f"({len(stats['tarefas_descartadas'])} descartadas); duplicados removidos: {stats['duplicados_removidos']}")
    for split, d in stats["splits"].items():
        print(f"  {split:<5} tarefas={d['tarefas']:<3} exemplos={d['exemplos']:<5} {d['por_ferramenta']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
