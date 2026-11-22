"""Tokenização para SFT com máscara de loss: só a resposta (a spec) é treinada."""
from __future__ import annotations


def tokenizar_exemplo(tok, messages: list, max_len: int) -> dict:
    """messages = [user, assistant]. O prompt recebe label -100 (ignorado pela loss); a spec + EOS é treinada.
    O prompt é montado com o MESMO apply_chat_template da inferência (inclusive o system padrão do Qwen)."""
    prompt = tok.apply_chat_template(messages[:-1], tokenize=False, add_generation_prompt=True)
    resposta = messages[-1]["content"] + tok.eos_token
    prompt_ids = tok(prompt, add_special_tokens=False)["input_ids"]
    resposta_ids = tok(resposta, add_special_tokens=False)["input_ids"]
    ids = prompt_ids + resposta_ids
    return {
        "input_ids": ids,
        "attention_mask": [1] * len(ids),
        "labels": [-100] * len(prompt_ids) + resposta_ids,
        "truncado": len(ids) > max_len,   # o notebook DESCARTA estes exemplos: cortar ensinaria specs incompletas
    }
