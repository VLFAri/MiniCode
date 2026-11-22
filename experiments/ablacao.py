"""Uso: python experiments/ablacao.py --tarefas tarefas_teste --repeticoes 3"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.avaliador.ablacao import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
