import os
from dotenv import load_dotenv
from openai import OpenAI

URL_PADRAO = "https://llm.liaufms.org/v1/qwen2-5-14b-instruct-awq"
MODELO_PADRAO = "Qwen/Qwen2.5-14B-Instruct-AWQ"


class LLMClient:

    def __init__(
        self,
        temperature: float = 0.1,
        max_tokens: int = 2048,
        timeout: float = 120.0,
        max_retries: int = 3,
    ):
        load_dotenv()
        token = os.getenv("MINICODE_API_KEY") or os.getenv("TOKEN")
        if not token:
            raise ValueError(
                "Chave da API não encontrada. Defina MINICODE_API_KEY no ambiente ou no .env."
            )

        self.model = os.getenv("MINICODE_MODEL", MODELO_PADRAO)
        self.temperature = temperature
        self.max_tokens = max_tokens

        self.client = OpenAI(
            base_url=os.getenv("MINICODE_BASE_URL", URL_PADRAO),
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
        }