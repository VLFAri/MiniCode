"""Modelo pequeno (base ou base + LoRA) usado como gerador de especificações no lugar do Qwen-14B.

Expõe a mesma interface que o `GeradorSpec` espera de um LLM: `complete(prompt, system_prompt=None)`.
"""
from __future__ import annotations

import os
import time

MODELO_SPEC_PADRAO = "Qwen/Qwen2.5-Coder-1.5B-Instruct"


class LocalSpecModel:
    def __init__(self, modelo: str = None, adapter: str = None, quant4bit: bool = False,
                 max_new_tokens: int = 1400, model=None, tokenizer=None):
        import torch

        self.torch = torch
        self.max_new_tokens = max_new_tokens
        if model is None:
            from transformers import AutoModelForCausalLM, AutoTokenizer

            modelo = modelo or os.getenv("MINICODE_SPEC_MODEL", MODELO_SPEC_PADRAO)
            tokenizer = AutoTokenizer.from_pretrained(modelo)
            cuda = torch.cuda.is_available()
            if quant4bit:   # mesma quantização do treino QLoRA
                from transformers import BitsAndBytesConfig
                bnb = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4",
                                         bnb_4bit_compute_dtype=torch.float16, bnb_4bit_use_double_quant=True)
                model = AutoModelForCausalLM.from_pretrained(modelo, quantization_config=bnb, device_map={"": 0})
            else:
                model = AutoModelForCausalLM.from_pretrained(modelo, torch_dtype=torch.float16 if cuda else torch.float32)
                model.to("cuda" if cuda else "cpu")
            if adapter:
                from peft import PeftModel
                model = PeftModel.from_pretrained(model, adapter)
        self.model, self.tok = model, tokenizer
        if self.tok.pad_token is None:
            self.tok.pad_token = self.tok.eos_token
        self.chamadas = 0
        self.segundos = 0.0

    def _texto(self, prompt: str, system_prompt: str = None) -> str:
        msgs = ([{"role": "system", "content": system_prompt}] if system_prompt else []) + \
               [{"role": "user", "content": prompt}]
        return self.tok.apply_chat_template(msgs, tokenize=False, add_generation_prompt=True)

    def gerar_lote(self, prompts: list, tamanho: int = 4, system_prompt: str = None) -> list:
        """Geração gulosa em lotes (padding à esquerda), bem mais rápida que um prompt por vez."""
        torch, saidas = self.torch, []
        self.model.eval()
        lado, self.tok.padding_side = self.tok.padding_side, "left"
        try:
            for i in range(0, len(prompts), tamanho):
                textos = [self._texto(p, system_prompt) for p in prompts[i:i + tamanho]]
                entrada = self.tok(textos, return_tensors="pt", padding=True, add_special_tokens=False).to(self.model.device)
                inicio = time.time()
                with torch.no_grad():
                    gerado = self.model.generate(**entrada, max_new_tokens=self.max_new_tokens, do_sample=False,
                                                 pad_token_id=self.tok.pad_token_id)
                self.segundos += time.time() - inicio
                self.chamadas += len(textos)
                novos = gerado[:, entrada["input_ids"].shape[1]:]
                saidas += [self.tok.decode(n, skip_special_tokens=True) for n in novos]
        finally:
            self.tok.padding_side = lado
        return saidas

    def complete(self, prompt: str, system_prompt: str = None) -> str:
        return self.gerar_lote([prompt], 1, system_prompt)[0]

    def metricas(self) -> dict:
        return {"llm_calls": self.chamadas, "seconds": round(self.segundos, 1)}


def criar_llm_spec(modo: str, modelo: str = None, adapter: str = None, quant4bit: bool = False):
    """nenhum -> None (o agente usa o Qwen-14B) | base -> modelo pequeno puro | lora -> modelo + adapter."""
    if modo in (None, "nenhum"):
        return None
    if modo == "base":
        return LocalSpecModel(modelo, quant4bit=quant4bit)
    if modo == "lora":
        if not adapter:
            raise ValueError("o modo 'lora' exige --spec-adapter (pasta do adapter treinado)")
        return LocalSpecModel(modelo, adapter, quant4bit=quant4bit)
    raise ValueError(f"modo desconhecido: {modo}")
