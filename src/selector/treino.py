"""Tokenização do dataset de treino com máscara de loss: só a RESPOSTA (o JSON da ferramenta) conta."""
from __future__ import annotations


def tokenizar_exemplo(tok, messages: list, max_len: int) -> dict:
    """messages = [system, user, assistant]. O prompt (system+user) recebe label -100, que o PyTorch
    ignora no cálculo da loss; assim o modelo aprende a RESPONDER, não a decorar o enunciado."""
    prompt = tok.apply_chat_template(messages[:2], tokenize=False, add_generation_prompt=True)
    resposta = messages[2]["content"] + tok.eos_token
    prompt_ids = tok(prompt, add_special_tokens=False)["input_ids"]
    resposta_ids = tok(resposta, add_special_tokens=False)["input_ids"]
    ids = prompt_ids + resposta_ids
    return {
        "input_ids": ids,
        "attention_mask": [1] * len(ids),
        "labels": [-100] * len(prompt_ids) + resposta_ids,
        "truncado": len(ids) > max_len,   # o notebook DESCARTA estes exemplos em vez de cortá-los
    }
