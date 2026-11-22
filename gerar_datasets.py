"""Uso (na raiz do repositório):

    export MINICODE_API_KEY=...            # teacher = Qwen-14B da disciplina
    python gerar_datasets.py --expandir 60 # (opcional) mais tarefas
    python gerar_datasets.py               # gera raw_specs.jsonl e dataset_tratado/{train,val,test}.jsonl

    python gerar_datasets.py --teacher ollama --ollama-modelo qwen2.5-coder:7b   # alternativa local
    python gerar_datasets.py --etapa tratar                                      # só refaz o filtro/split a partir do cache

O import abaixo NÃO tem fallback: se `src` não for encontrado, o script falha em vez de gerar dados no formato errado.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.spec.dataset import main  # noqa: E402

if __name__ == "__main__":
    raise SystemExit(main())
