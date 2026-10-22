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

        llm = LLMClient()  # novo cliente por tarefa => contadores por tarefa
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

        # Preserva o rastro (state.json, actions.jsonl, spec, plano) para auditoria
        destino = saida / dir_tarefa.name
        if destino.exists():
            shutil.rmtree(destino)
        shutil.copytree(projeto / ".minicode", destino)

    return {
        "task": dir_tarefa.name,
        "success": sucesso,
        "first_attempt_success": bool(estado.get("first_attempt_success")),
        "iterations": estado.get("repair_attempts", 0) + 1,  # ciclos de verificação
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


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Avalia o MiniCode em um conjunto de tarefas")
    parser.add_argument("tarefas", help="Diretório com as tarefas")
    parser.add_argument("--saida", default="experiments/resultados", help="Onde guardar os resultados")
    parser.add_argument("--max-reparos", type=int, default=3)
    parser.add_argument("--max-iteracoes", type=int, default=15)
    args = parser.parse_args(argv)

    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)

    resultados = []
    for d in sorted(Path(args.tarefas).iterdir()):
        if not (d / "tarefa.txt").exists():
            continue
        print(f"\n##### {d.name} #####")
        resultados.append(avaliar_tarefa(d, saida, args.max_reparos, args.max_iteracoes))

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

if __name__ == "__main__":
    sys.exit(main())