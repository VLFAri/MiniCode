"""Seletores de próxima ferramenta: modelo pequeno local (base ou base+LoRA) e Qwen-14B como referência."""
from __future__ import annotations

import os
import time

from src.selector.prompt import PROMPT_SELETOR, mensagens, parse_saida

MODELO_PEQUENO_PADRAO = "Qwen/Qwen2.5-1.5B-Instruct"


class LocalSelector:
    """Modelo pequeno do Hugging Face, opcionalmente com adapter LoRA. Decodificação gulosa."""

    def __init__(self, modelo: str = None, adapter: str = None, max_new_tokens: int = 48,
                 model=None, tokenizer=None):
        import torch

        self.torch = torch
        self.max_new_tokens = max_new_tokens
        if model is None:
            from transformers import AutoModelForCausalLM, AutoTokenizer

            modelo = modelo or os.getenv("MINICODE_SELECTOR_MODEL", MODELO_PEQUENO_PADRAO)
            tokenizer = AutoTokenizer.from_pretrained(modelo)
            dtype = torch.float16 if torch.cuda.is_available() else torch.float32
            model = AutoModelForCausalLM.from_pretrained(modelo, torch_dtype=dtype)
            if adapter:
                from peft import PeftModel

                model = PeftModel.from_pretrained(model, adapter)
            model.to("cuda" if torch.cuda.is_available() else "cpu")
        self.model, self.tok = model, tokenizer
        self.chamadas = 0
        self.segundos = 0.0

    def gerar(self, features: str) -> str:
        torch = self.torch
        self.model.eval()
        prompt = self.tok.apply_chat_template(mensagens(features), tokenize=False, add_generation_prompt=True)
        entrada = self.tok(prompt, return_tensors="pt", add_special_tokens=False).to(self.model.device)
        inicio = time.time()
        with torch.no_grad():
            saida = self.model.generate(
                **entrada, max_new_tokens=self.max_new_tokens, do_sample=False,
                pad_token_id=self.tok.pad_token_id or self.tok.eos_token_id,
            )
        self.segundos += time.time() - inicio
        self.chamadas += 1
        return self.tok.decode(saida[0][entrada["input_ids"].shape[1]:], skip_special_tokens=True)

    def predict(self, features: str):
        return parse_saida(self.gerar(features))


class TeacherSelector:
    """Qwen-14B (endpoint da disciplina) respondendo zero-shot à mesma tarefa: referência do nível 1."""

    def __init__(self, llm):
        self.llm = llm

    def predict(self, features: str):
        return parse_saida(self.llm.complete(features, system_prompt=PROMPT_SELETOR))


def criar_seletor(modo: str, modelo: str = None, adapter: str = None):
    """nenhum -> None | base -> modelo pequeno puro | lora -> modelo + adapter | teacher -> Qwen-14B."""
    if modo in (None, "nenhum"):
        return None
    if modo == "base":
        return LocalSelector(modelo)
    if modo == "lora":
        if not adapter:
            raise ValueError("o modo 'lora' exige --selector-adapter (pasta do adapter treinado)")
        return LocalSelector(modelo, adapter)
    if modo == "teacher":
        from src.modelo.cliente_llm import LLMClient

        return TeacherSelector(LLMClient(max_tokens=64))
    raise ValueError(f"modo de seletor desconhecido: {modo}")
