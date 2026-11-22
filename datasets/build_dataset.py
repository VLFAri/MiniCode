"""Uso: python datasets/build_dataset.py --resultados experiments/resultados --exigir-ocultos

Não crie datasets/__init__.py: o nome colidiria com a biblioteca `datasets` do Hugging Face.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.selector.dataset import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
