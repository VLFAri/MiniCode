"""Cliente do LLM do agente (API compatível com a da OpenAI).

Dois backends, escolhidos EXPLICITAMENTE por `MINICODE_BACKEND` (nunca por fallback silencioso, para que um
experimento não rode com um modelo diferente do que o relatório diz):

  remoto (padrão) : Qwen-14B da disciplina. Exige MINICODE_API_KEY.
  local           : servidor local compatível com OpenAI (Ollama :11434, LM Studio :1234, llama.cpp :8080).
                    Detecta sozinho um modelo Qwen instalado; MINICODE_MODEL força um nome específico.

Variáveis (podem ir no .env, que NÃO deve ser versionado):
  MINICODE_BACKEND=local
  MINICODE_BASE_URL=http://localhost:11434/v1     # opcional no backend local
  MINICODE_MODEL=qwen2.5-coder:7b                 # opcional: sem isso, escolhe o maior Qwen instalado

Diagnóstico:  PYTHONPATH=. python -m src.modelo.cliente_llm
"""
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.modelo.descoberta import URL_LOCAL_PADRAO, escolher_modelo_qwen, listar_modelos  # noqa: F401

URL_PADRAO = "https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq"
MODELO_PADRAO = "Qwen/Qwen2.5-14B-Instruct-AWQ"
BACKENDS = ("remoto", "local")


class LLMClient:

    def __init__(
        self,
        temperature: float = 0.1,
        max_tokens: int = 2048,
        timeout: float = None,
        max_retries: int = 3,
    ):
        load_dotenv()
        self.backend = (os.getenv("MINICODE_BACKEND") or "remoto").strip().lower()
        if self.backend not in BACKENDS:
            raise ValueError(f"MINICODE_BACKEND inválido: {self.backend!r}. Use um de {BACKENDS}.")

        if self.backend == "local":
            base_url = os.getenv("MINICODE_BASE_URL", URL_LOCAL_PADRAO)
            token = os.getenv("MINICODE_API_KEY") or "local"      # servidores locais ignoram a chave
            modelo = os.getenv("MINICODE_MODEL") or escolher_modelo_qwen(listar_modelos(base_url))
            if not modelo:
                raise ValueError(
                    f"Nenhum modelo Qwen encontrado em {base_url}. Verifique se o servidor está rodando "
                    "(ex.: `ollama serve`), instale um (`ollama pull qwen2.5-coder:7b`) ou defina MINICODE_MODEL."
                )
            timeout = 600.0 if timeout is None else timeout       # modelo local em CPU/GPU modesta é lento
        else:
            base_url = os.getenv("MINICODE_BASE_URL", URL_PADRAO)
            token = os.getenv("MINICODE_API_KEY") or os.getenv("TOKEN")
            if not token:
                raise ValueError(
                    "Chave da API não encontrada. Defina MINICODE_API_KEY no ambiente ou no .env "
                    "(ou use um modelo local com MINICODE_BACKEND=local)."
                )
            modelo = os.getenv("MINICODE_MODEL", MODELO_PADRAO)
            timeout = 120.0 if timeout is None else timeout

        self.base_url = base_url
        self.model = modelo
        self.temperature = temperature
        self.max_tokens = max_tokens

        self.client = OpenAI(
            base_url=base_url,
            api_key=token,
            timeout=timeout,
            max_retries=max_retries,
        )

        self.chamadas = 0
        self.tokens_prompt = 0
        self.tokens_resposta = 0

    def chat(self, messages: list, temperature: float = None, max_tokens: int = None) -> str:
        resp = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature if temperature is None else temperature,
            max_tokens=max_tokens or self.max_tokens,
        )

        self.chamadas += 1
        if resp.usage:
            self.tokens_prompt += resp.usage.prompt_tokens or 0
            self.tokens_resposta += resp.usage.completion_tokens or 0

        return resp.choices[0].message.content or ""

    def complete(self, prompt: str, system_prompt: str = None) -> str:
        messages = []
        if system_prompt:
            messages.append({"role": "system", "content": system_prompt})
        messages.append({"role": "user", "content": prompt})
        return self.chat(messages)

    def metricas(self) -> dict:
        return {
            "llm_calls": self.chamadas,
            "prompt_tokens": self.tokens_prompt,
            "completion_tokens": self.tokens_resposta,
            "llm_backend": self.backend,     # fica no state.json: o resultado diz com que modelo foi obtido
            "llm_model": self.model,
        }


def main() -> int:
    """Diagnóstico: mostra o backend, os modelos encontrados e faz uma chamada de teste."""
    load_dotenv()
    backend = (os.getenv("MINICODE_BACKEND") or "remoto").lower()
    print(f"backend: {backend}")
    if backend == "local":
        base = os.getenv("MINICODE_BASE_URL", URL_LOCAL_PADRAO)
        modelos = listar_modelos(base)
        print(f"servidor: {base}\nmodelos instalados: {modelos or '(nenhum / servidor inacessível)'}")
        print(f"Qwen escolhido: {os.getenv('MINICODE_MODEL') or escolher_modelo_qwen(modelos)}")
    try:
        llm = LLMClient(max_tokens=32)
        print(f"modelo em uso: {llm.model}\nresposta: {llm.complete('Responda apenas: ok')!r}")
        return 0
    except Exception as e:
        print(f"FALHA: {type(e).__name__}: {e}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
