import argparse
import json
import sys
from pathlib import Path

# permite `python src/cli/main.py` sem PYTHONPATH (o README da v1 promete isso): a raiz do projeto entra no caminho de imports
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.agente.orquestrador import Orquestrador
from src.avaliador.avaliador import (InfraestruturaIndisponivel, avaliar_tarefa, checar_infra,  # noqa: F401
                                     resumir)  # reexportados: usados pelo CLI e pelos testes
from src.selector.seletor import criar_seletor
from src.spec.modelo_local import criar_llm_spec


def avaliar_lote(dir_tarefas: str, dir_saida: str, max_reparos: int, max_iteracoes: int, selector=None, llm_spec=None,
                 hard_gates: bool = True) -> int:
    saida = Path(dir_saida)
    saida.mkdir(parents=True, exist_ok=True)

    extra = {k: v for k, v in (("selector", selector), ("llm_spec", llm_spec)) if v}
    if not hard_gates:
        extra["hard_gates"] = False
    resultados, parada = [], None
    for d in sorted(Path(dir_tarefas).iterdir()):
        if not (d / "tarefa.txt").exists():
            continue
        print(f"\n##### {d.name} #####")
        resultados.append(avaliar_tarefa(d, saida, max_reparos, max_iteracoes, **extra))
        try:
            checar_infra(resultados)
        except InfraestruturaIndisponivel as e:
            parada = str(e)
            break

    resumo = resumir(resultados)
    (saida / "resultados.json").write_text(
        json.dumps({"summary": resumo, "results": resultados}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    print("\n================ RESUMO ================")
    for r in resultados:
        marca = "OK  " if r["success"] else "FAIL"
        print(f"{marca} {r['task']:<28} iter={r['iterations']} llm_calls={r['llm_calls']} {r['seconds']}s")
    for k, v in resumo.items():
        print(f"{k}: {v:.2f}" if isinstance(v, float) else f"{k}: {v}")
    if parada:
        print(f"\n❌ {parada}")
        return 1
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="minicode", description="MiniCode v2 - agente de programação")
    parser.add_argument("tarefa", nargs="?", help="Tarefa em linguagem natural (se omitida, será pedida)")
    parser.add_argument("--project", default="workspace", help="Diretório do projeto a modificar (padrão: ./workspace, criado se não existir)")
    parser.add_argument("--max-reparos", type=int, default=5, help="Máximo de ciclos de reparo (padrão: 5)")
    parser.add_argument("--max-iteracoes", type=int, default=15, help="Máximo de ações do LLM por ciclo (padrão: 15)")
    parser.add_argument("--avaliar", metavar="DIR_TAREFAS", help="Modo avaliação: roda o agente em todas as tarefas do diretório")
    parser.add_argument("--saida", default="experiments/resultados", help="Onde guardar os resultados da avaliação")
    parser.add_argument("--selector", choices=["nenhum", "base", "lora"], default="nenhum",
                        help="seletor de ferramentas (modelo pequeno) que recomenda a próxima ação ao agente")
    parser.add_argument("--selector-modelo", default=None, help="modelo base do seletor (padrão: Qwen2.5-1.5B-Instruct)")
    parser.add_argument("--selector-adapter", default=None, help="pasta do adapter LoRA (obrigatório com --selector lora)")
    parser.add_argument("--spec-model", choices=["nenhum", "base", "lora"], default="nenhum",
                        help="modelo pequeno que gera a ESPECIFICAÇÃO no lugar do Qwen-14B (plano e código continuam no 14B)")
    parser.add_argument("--spec-modelo", default=None, help="modelo base do gerador de spec (padrão: Qwen2.5-Coder-1.5B-Instruct)")
    parser.add_argument("--spec-adapter", default=None, help="pasta do adapter LoRA (obrigatório com --spec-model lora)")
    parser.add_argument("--sem-hard-gates", action="store_true",
                        help="SÓ PARA ABLAÇÃO: desliga o gate VERIFYING->DONE (a regra vira instrução no prompt)")
    parser.add_argument("--spec-4bit", action="store_true", help="carrega o modelo em 4 bits (use se o adapter foi treinado com QLoRA; exige GPU)")
    args = parser.parse_args(argv)

    seletor = criar_seletor(args.selector, args.selector_modelo, args.selector_adapter)
    llm_spec = criar_llm_spec(args.spec_model, args.spec_modelo, args.spec_adapter, quant4bit=args.spec_4bit)

    if args.avaliar:
        return avaliar_lote(args.avaliar, args.saida, args.max_reparos, args.max_iteracoes, seletor, llm_spec,
                            hard_gates=not args.sem_hard_gates)

    print("=== MiniCode v2 ===")
    tarefa = args.tarefa if args.tarefa else input("> ")

    if not tarefa.strip():
        print("Nenhuma tarefa fornecida. A encerrar.")
        return 1

    project_root = Path(args.project).resolve()
    if (project_root / "src" / "agente" / "orquestrador.py").exists():
        print(f"❌ {project_root} é o código do próprio MiniCode. Use outra pasta (ex.: --project ./workspace).")
        return 1
    project_root.mkdir(parents=True, exist_ok=True)

    try:
        agente = Orquestrador(
            tarefa,
            project_root=project_root,
            max_iteracoes=args.max_iteracoes,
            max_reparos=args.max_reparos,
            selector=seletor,
            llm_spec=llm_spec,
            hard_gates=not args.sem_hard_gates,
        )
        sucesso = agente.executar()
    except Exception as e:
        print(f"\n❌ [Erro Crítico] Ocorreu um problema ao executar o agente: {e}")
        return 1

    return 0 if sucesso else 1


if __name__ == "__main__":
    sys.exit(main())