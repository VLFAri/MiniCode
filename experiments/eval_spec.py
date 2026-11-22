"""Uso: python experiments/eval_spec.py --modo base|lora|teacher [--adapter pasta] [--com-tentativas]"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src.spec.avaliacao import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
