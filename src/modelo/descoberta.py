"""Descoberta de modelos em servidores locais compatíveis com OpenAI (Ollama, LM Studio, llama.cpp).

Módulo leve de propósito: não importa `openai`, então scripts como `gerar_datasets.py` podem usá-lo sem a biblioteca.
"""
import json
import re
import urllib.error
import urllib.request

URL_LOCAL_PADRAO = "http://localhost:11434/v1"


def listar_modelos(base_url: str, timeout: float = 5.0) -> list:
    """Nomes dos modelos instalados (GET {base_url}/models). Lista vazia se o servidor estiver inacessível."""
    try:
        req = urllib.request.Request(base_url.rstrip("/") + "/models")
        with urllib.request.urlopen(req, timeout=timeout) as r:
            dados = json.loads(r.read().decode("utf-8"))
        return [m["id"] for m in dados.get("data", []) if "id" in m]
    except (urllib.error.URLError, OSError, ValueError, KeyError):
        return []


def tamanho_em_bilhoes(nome: str) -> float:
    achado = re.search(r"(\d+(?:\.\d+)?)b\b", nome.lower())
    return float(achado.group(1)) if achado else 0.0


def escolher_modelo_qwen(modelos: list):
    """Entre os modelos Qwen instalados, o MAIOR (agentes dependem muito do tamanho); None se não houver."""
    qwen = [m for m in modelos if "qwen" in m.lower()]
    return max(qwen, key=tamanho_em_bilhoes) if qwen else None
