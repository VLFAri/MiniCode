import argparse
import json
import shutil
import sys
import tempfile
import time
from pathlib import Path

from src.agente.orquestrador import Orquestrador
from src.modelo.cliente_llm import LLMClient
from src.selector.seletor import criar_seletor
from src.spec.modelo_local import criar_llm_spec

def rodar_testes_ocultos(dir_tarefa: Path, projeto: Path, agente):
    """Critério de sucesso INDEPENDENTE do agente.

    O agente escreve os próprios testes, então 'DONE' só prova que esses testes passam (testes triviais
    passam). Se a tarefa trouxer `testes_ocultos/`, eles são copiados para o projeto SÓ depois que o
    agente terminou (ele nunca os vê) e executados na mesma sandbox. None = tarefa sem testes ocultos.
    """
    ocultos = dir_tarefa / "testes_ocultos"
    if not ocultos.is_dir():
        return None
    try:
        agente._verificar_arquivos_alterados()  # nunca executa código que a segurança rejeitaria
        shutil.copytree(ocultos, projeto / "_ocultos", dirs_exist_ok=True)
        res = agente.registro.executar("run_tests", {"target": "_ocultos"})
        return bool(res.get("ok") and res.get("passou"))
    except Exception:
        return False


def avaliar_tarefa(dir_tarefa: Path, saida: Path, max_reparos: int, max_iteracoes: int, selector=None, llm_spec=None,
                   hard_gates: bool = True) -> dict:
    tarefa = (dir_tarefa / "tarefa.txt").read_text(encoding="utf-8").strip()

    with tempfile.TemporaryDirectory() as tmp:
        projeto = Path(tmp) / "projeto"
        if (dir_tarefa / "projeto").is_dir():
            shutil.copytree(dir_tarefa / "projeto", projeto)
        else:                                   # tarefas "do zero" não precisam de projeto/ (git não versiona pasta vazia)
            projeto.mkdir()

        llm = LLMClient()  # novo cliente por tarefa => contadores por tarefa
        inicio = time.time()
        agente = Orquestrador(
            tarefa, project_root=projeto, llm=llm,
            max_reparos=max_reparos, max_iteracoes=max_iteracoes, selector=selector, llm_spec=llm_spec, hard_gates=hard_gates,
        )
        sucesso = agente.executar()
        segundos = time.time() - inicio
        hidden_pass = rodar_testes_ocultos(dir_tarefa, projeto, agente)

        estado = json.loads((projeto / ".minicode" / "state.json").read_text(encoding="utf-8"))
        acoes = (projeto / ".minicode" / "actions.jsonl").read_text(encoding="utf-8").splitlines()
        eventos = [json.loads(a) for a in acoes]
        tool_calls = sum(1 for a in eventos if a.get("type") == "tool_call")
        tentativas_spec = [a for a in eventos if a.get("type") == "spec_attempt"]

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
        "hidden_pass": hidden_pass,
        "hard_gates": hard_gates,
        "llm_model": estado.get("llm_model"),
        "spec_attempts": len(tentativas_spec),
        "spec_first_try_valid": bool(tentativas_spec) and not tentativas_spec[0].get("problems"),
        "selector_calls": estado.get("selector_calls"),
        "selector_followed": estado.get("selector_followed"),
    }


def resumir(resultados: list) -> dict:
    n = len(resultados)
    if n == 0:
        return {}
    resumo = {
        "tasks": n,
        "TaskSuccessRate": sum(r["success"] for r in resultados) / n,
        "FirstAttemptSuccess": sum(r["first_attempt_success"] for r in resultados) / n,
        "AverageIterations": sum(r["iterations"] for r in resultados) / n,
        "AverageLLMCalls": sum(r["llm_calls"] for r in resultados) / n,
    }
    ocultos = [r["hidden_pass"] for r in resultados if r.get("hidden_pass") is not None]
    if ocultos:  # taxa de sucesso medida por testes que o agente nunca viu
        resumo["HiddenSuccessRate"] = sum(ocultos) / len(ocultos)
    if ocultos:  # o agente disse DONE mas os testes ocultos reprovaram: o que um hard gate de verdade deveria evitar
        conhecidos = [r for r in resultados if r.get("hidden_pass") is not None]
        resumo["FalseSuccessRate"] = sum(bool(r["success"]) and not r["hidden_pass"] for r in conhecidos) / len(conhecidos)
    com_spec = [r for r in resultados if r.get("spec_attempts")]
    if com_spec:  # qualidade da especificação medida DENTRO do agente
        resumo["AverageSpecAttempts"] = sum(r["spec_attempts"] for r in com_spec) / len(com_spec)
        resumo["SpecFirstTryValid"] = sum(r["spec_first_try_valid"] for r in com_spec) / len(com_spec)
    chamadas = sum(r.get("selector_calls") or 0 for r in resultados)
    if chamadas:
        resumo["SelectorFollowRate"] = sum(r.get("selector_followed") or 0 for r in resultados) / chamadas
    return resumo


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Avalia o MiniCode em um conjunto de tarefas")
    parser.add_argument("tarefas", help="Diretório com as tarefas")
    parser.add_argument("--saida", default="experiments/resultados", help="Onde guardar os resultados")
    parser.add_argument("--max-reparos", type=int, default=3)
    parser.add_argument("--max-iteracoes", type=int, default=15)
    parser.add_argument("--selector", choices=["nenhum", "base", "lora"], default="nenhum",
                        help="seletor de ferramentas (modelo pequeno) usado para guiar o agente")
    parser.add_argument("--selector-modelo", default=None)
    parser.add_argument("--selector-adapter", default=None)
    parser.add_argument("--spec-model", choices=["nenhum", "base", "lora"], default="nenhum",
                        help="modelo pequeno que gera a ESPECIFICAÇÃO no lugar do Qwen-14B")
    parser.add_argument("--spec-modelo", default=None)
    parser.add_argument("--spec-adapter", default=None)
    parser.add_argument("--sem-hard-gates", action="store_true",
                        help="SÓ PARA ABLAÇÃO: desliga o gate VERIFYING->DONE (a regra vira instrução no prompt)")
    parser.add_argument("--spec-4bit", action="store_true", help="carrega o modelo em 4 bits (use se o adapter foi treinado com QLoRA; exige GPU)")
    args = parser.parse_args(argv)
    seletor = criar_seletor(args.selector, args.selector_modelo, args.selector_adapter)
    llm_spec = criar_llm_spec(args.spec_model, args.spec_modelo, args.spec_adapter, quant4bit=args.spec_4bit)
    extra = {k: v for k, v in (("selector", seletor), ("llm_spec", llm_spec)) if v}
    if args.sem_hard_gates:
        extra["hard_gates"] = False

    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)

    resultados = []
    for d in sorted(Path(args.tarefas).iterdir()):
        if not (d / "tarefa.txt").exists():
            continue
        print(f"\n##### {d.name} #####")
        resultados.append(avaliar_tarefa(d, saida, args.max_reparos, args.max_iteracoes, **extra))

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