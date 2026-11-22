"""Uso: python experiments/eval_selector.py --modo base|lora|teacher [--adapter pasta]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.selector.avaliacao import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
