"""Validação do PRÓPRIO conjunto de tarefas: um teste oculto mal escrito invalida toda a avaliação.

Para cada tarefa (pasta com tarefa.txt, projeto/ opcional, testes_ocultos/ e referencia/):
  - os testes ocultos têm de FALHAR no projeto inicial (senão a tarefa já nasce resolvida);
  - os testes ocultos têm de PASSAR com a solução de referência sobreposta ao projeto.

Uso: PYTHONPATH=. python -m src.avaliador.tarefas tarefas_teste
"""
from __future__ import annotations

import shutil
import sys
import tempfile
from pathlib import Path

from src.ferramentas.registro import RegistroFerramentas


def listar_tarefas(raiz) -> list:
    return sorted(d for d in Path(raiz).iterdir() if (d / "tarefa.txt").exists())


def rodar_ocultos(dir_tarefa: Path, projeto: Path) -> bool:
    shutil.copytree(dir_tarefa / "testes_ocultos", projeto / "_ocultos", dirs_exist_ok=True)
    res = RegistroFerramentas(projeto).executar("run_tests", {"target": "_ocultos"})
    return bool(res.get("ok") and res.get("passou"))


def _projeto_temporario(dir_tarefa: Path, tmp: str, com_referencia: bool) -> Path:
    projeto = Path(tmp) / ("com_ref" if com_referencia else "sem_ref")
    if (dir_tarefa / "projeto").is_dir():
        shutil.copytree(dir_tarefa / "projeto", projeto)
    else:
        projeto.mkdir()
    if com_referencia:
        shutil.copytree(dir_tarefa / "referencia", projeto, dirs_exist_ok=True)
    return projeto


def validar_tarefa(dir_tarefa) -> dict:
    dir_tarefa = Path(dir_tarefa)
    with tempfile.TemporaryDirectory() as tmp:
        sem = rodar_ocultos(dir_tarefa, _projeto_temporario(dir_tarefa, tmp, False))
        com = rodar_ocultos(dir_tarefa, _projeto_temporario(dir_tarefa, tmp, True))
    return {"tarefa": dir_tarefa.name, "falha_sem_referencia": not sem, "passa_com_referencia": com,
            "ok": (not sem) and com}


def main(argv=None) -> int:
    raiz = (argv or sys.argv[1:] or ["tarefas_teste"])[0]
    resultados = [validar_tarefa(d) for d in listar_tarefas(raiz)]
    for r in resultados:
        print(("OK   " if r["ok"] else "ERRO ") + r["tarefa"],
              "" if r["ok"] else f"(falha sem ref: {r['falha_sem_referencia']}, passa com ref: {r['passa_com_referencia']})")
    print(f"{sum(r['ok'] for r in resultados)}/{len(resultados)} tarefas válidas")
    return 0 if all(r["ok"] for r in resultados) else 1


if __name__ == "__main__":
    raise SystemExit(main())
