"""Estudo de ablação: cada configuração roda as MESMAS tarefas e o sucesso é medido pelos testes ocultos.

Configurações (o que muda em relação a `completo`):
  completo      : spec + plano + hard gates + repair loop (padrão)
  sem_repair    : max_reparos=0 (a primeira falha dos testes encerra a tarefa)
  sem_hard_gate : a regra "rode os testes antes de terminar" vira só instrução no prompt; DONE sem conferência
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.avaliador.avaliador import avaliar_tarefa, checar_infra, resumir
from src.avaliador.tabelas import (METRICAS, carregar_ablacao, media_e_desvio,  # noqa: F401  (reexportados)
                                   tabela_markdown)

CONFIGS = {
    "completo": {"max_reparos": 3, "hard_gates": True},
    "sem_repair": {"max_reparos": 0, "hard_gates": True},
    "sem_hard_gate": {"max_reparos": 3, "hard_gates": False},
}
def rodar(dir_tarefas: str, saida: str, configs: list, repeticoes: int, max_iteracoes: int, **extra) -> dict:
    saida = Path(saida)
    por_config = {}
    for nome in configs:
        cfg = CONFIGS[nome]
        por_config[nome] = []
        for rep in range(1, repeticoes + 1):
            destino = saida / nome / f"rodada_{rep}"
            destino.mkdir(parents=True, exist_ok=True)
            resultados = []
            for d in sorted(Path(dir_tarefas).iterdir()):
                if not (d / "tarefa.txt").exists():
                    continue
                print(f"\n##### [{nome} #{rep}] {d.name} #####")
                resultados.append(avaliar_tarefa(d, destino, cfg["max_reparos"], max_iteracoes,
                                                 hard_gates=cfg["hard_gates"], **extra))
                checar_infra(resultados)      # levanta InfraestruturaIndisponivel: não faz sentido comparar configurações assim
            resumo = resumir(resultados)
            (destino / "resultados.json").write_text(
                json.dumps({"config": nome, "summary": resumo, "results": resultados}, indent=2, ensure_ascii=False),
                encoding="utf-8")
            por_config[nome].append(resumo)
    tabela = tabela_markdown(por_config)
    (saida / "ablacao.md").write_text(tabela + "\n", encoding="utf-8")
    return por_config


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Roda a ablação (completo / sem_repair / sem_hard_gate) nas tarefas")
    ap.add_argument("--tarefas", default="tarefas_teste")
    ap.add_argument("--saida", default="experiments/ablacao")
    ap.add_argument("--configs", nargs="+", choices=sorted(CONFIGS), default=list(CONFIGS))
    ap.add_argument("--repeticoes", type=int, default=1, help="o agente é estocástico: use >= 3 para reportar média e desvio")
    ap.add_argument("--max-iteracoes", type=int, default=15)
    args = ap.parse_args(argv)
    rodar(args.tarefas, args.saida, args.configs, args.repeticoes, args.max_iteracoes)
    print("\n" + (Path(args.saida) / "ablacao.md").read_text(encoding="utf-8"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())