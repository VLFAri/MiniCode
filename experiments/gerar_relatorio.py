"""Uso: python experiments/gerar_relatorio.py   (gera docs/resultados.md com os números reais)"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.avaliador.relatorio import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
