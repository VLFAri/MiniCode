import argparse
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

from src.agente.orquestrador import Orquestrador
from src.modelo.cliente_llm import LLMClient


def avaliar_tarefa(dir_tarefa: Path, saida: Path, max_reparos: int, max_iteracoes: int) -> dict:
    tarefa = (dir_tarefa / "tarefa.txt").read_text(encoding="utf-8").strip()

    with tempfile.TemporaryDirectory() as tmp:
        projeto = Path(tmp) / "projeto"
        shutil.copytree(dir_tarefa / "projeto", projeto)

        llm = LLMClient()
        inicio = time.time()
        agente = Orquestrador(
            tarefa, project_root=projeto, llm=llm,
            max_reparos=max_reparos, max_iteracoes=max_iteracoes,
        )
        sucesso = agente.executar()
        segundos = time.time() - inicio

        estado = json.loads((projeto / ".minicode" / "state.json").read_text(encoding="utf-8"))
        acoes = (projeto / ".minicode" / "actions.jsonl").read_text(encoding="utf-8").splitlines()
        tool_calls = sum(1 for a in acoes if json.loads(a).get("type") == "tool_call")

        destino = saida / dir_tarefa.name
        if destino.exists():
            shutil.rmtree(destino)
        shutil.copytree(projeto / ".minicode", destino)

    return {
        "task": dir_tarefa.name,
        "success": sucesso,
        "first_attempt_success": bool(estado.get("first_attempt_success")),
        "iterations": estado.get("repair_attempts", 0) + 1,
        "llm_calls": estado.get("llm_calls", 0),
        "tool_calls": tool_calls,
        "prompt_tokens": estado.get("prompt_tokens", 0),
        "completion_tokens": estado.get("completion_tokens", 0),
        "seconds": round(segundos, 1),
        "error": estado.get("error"),
    }


def resumir(resultados: list) -> dict:
    n = len(resultados)
    if n == 0:
        return {}
    return {
        "tasks": n,
        "TaskSuccessRate": sum(r["success"] for r in resultados) / n,
        "FirstAttemptSuccess": sum(r["first_attempt_success"] for r in resultados) / n,
        "AverageIterations": sum(r["iterations"] for r in resultados) / n,
        "AverageLLMCalls": sum(r["llm_calls"] for r in resultados) / n,
    }


def avaliar_lote(dir_tarefas: str, dir_saida: str, max_reparos: int, max_iteracoes: int) -> int:
    saida = Path(dir_saida)
    saida.mkdir(parents=True, exist_ok=True)

    resultados = []
    for d in sorted(Path(dir_tarefas).iterdir()):
        if not (d / "tarefa.txt").exists():
            continue
        print(f"\n##### {d.name} #####")
        resultados.append(avaliar_tarefa(d, saida, max_reparos, max_iteracoes))

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
    return 0


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="minicode", description="MiniCode v1 - agente de programação")
    parser.add_argument("tarefa", nargs="?", help="Tarefa em linguagem natural (se omitida, será pedida)")
    parser.add_argument("--project", default="workspace", help="Diretório do projeto a modificar (padrão: ./workspace, criado se não existir)")
    parser.add_argument("--max-reparos", type=int, default=5, help="Máximo de ciclos de reparo (padrão: 5)")
    parser.add_argument("--max-iteracoes", type=int, default=15, help="Máximo de ações do LLM por ciclo (padrão: 15)")
    parser.add_argument("--avaliar", metavar="DIR_TAREFAS", help="Modo avaliação: roda o agente em todas as tarefas do diretório")
    parser.add_argument("--saida", default="experiments/resultados", help="Onde guardar os resultados da avaliação")
    args = parser.parse_args(argv)

    if args.avaliar:
        return avaliar_lote(args.avaliar, args.saida, args.max_reparos, args.max_iteracoes)

    print("=== MiniCode v1 ===")
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
        )
        sucesso = agente.executar()
    except Exception as e:
        print(f"\n❌ [Erro Crítico] Ocorreu um problema ao executar o agente: {e}")
        return 1

    return 0 if sucesso else 1


if __name__ == "__main__":
    sys.exit(main())