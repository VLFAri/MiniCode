"""Avaliação de nível 1 do gerador de especificações: o modelo produz specs que o AGENTE aceita?

Métricas (todas automáticas):
  valida_agente   : passa no `validar_spec` do GeradorSpec (o portão real do agente)
  valida_estrita  : além disso, tem >= 3 critérios, exemplos concretos, sem código de implementação, só stdlib
  tentativas_media: quantas chamadas o GeradorSpec precisa (até 3), exatamente como no agente
"""
from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path

from src.spec.gerador import GeradorSpec, limpar_cercas, validar_spec
from src.spec.qualidade import (FORA_DE_ESCOPO, itens_criterios, sem_cerca_externa,
                                tem_codigo_de_implementacao, validar_spec_estrita)


def analisar_spec(texto: str) -> dict:
    spec = sem_cerca_externa(texto)
    itens = itens_criterios(spec)
    problemas = validar_spec_estrita(texto or "")
    return {
        "valida_agente": not validar_spec(limpar_cercas(texto or "")),
        "valida_estrita": not problemas,
        "n_criterios": len(itens),
        "criterios_com_exemplo": sum("`" in i for i in itens),
        "tem_codigo": tem_codigo_de_implementacao(spec),
        "fora_de_escopo": bool(FORA_DE_ESCOPO.search(spec)),
        "tokens_aprox": len(spec) / 3.2,
        "problemas": problemas,
    }


def resumir_analises(analises: list) -> dict:
    n = len(analises)
    if n == 0:
        return {"n": 0}
    media = lambda k: sum(a[k] for a in analises) / n
    return {
        "n": n,
        "valida_agente": media("valida_agente"),
        "valida_estrita": media("valida_estrita"),
        "criterios_medio": media("n_criterios"),
        "criterios_com_exemplo_medio": media("criterios_com_exemplo"),
        "com_codigo_de_implementacao": media("tem_codigo"),
        "fora_de_escopo": media("fora_de_escopo"),
        "tokens_medio": media("tokens_aprox"),
        "problemas_mais_comuns": Counter(p for a in analises for p in a["problemas"]).most_common(5),
    }


def como_lote(modelo):
    """Usa gerar_lote se o modelo tiver (LocalSpecModel); senão, um prompt por vez (endpoint 14B)."""
    return getattr(modelo, "gerar_lote", None) or (lambda prompts: [modelo.complete(p) for p in prompts])


def avaliar_primeira_tentativa(modelo, prompts: list) -> dict:
    textos = como_lote(modelo)(prompts)
    return resumir_analises([analisar_spec(t) for t in textos])


class _Contador:
    def __init__(self, llm):
        self.llm, self.chamadas = llm, 0

    def complete(self, prompt, system_prompt=None):
        self.chamadas += 1
        return self.llm.complete(prompt, system_prompt=system_prompt) if system_prompt else self.llm.complete(prompt)


def avaliar_com_tentativas(modelo, itens: list, max_tentativas: int = 3) -> dict:
    """Roda o GeradorSpec REAL do agente (com reenvio do motivo da rejeição) e mede sucesso e tentativas."""
    sucessos, tentativas = 0, []
    for tarefa, contexto in itens:
        c = _Contador(modelo)
        try:
            GeradorSpec(c, max_tentativas=max_tentativas).gerar_spec(tarefa, contexto)
            sucessos += 1
        except RuntimeError:
            pass
        tentativas.append(c.chamadas)
    n = len(itens)
    return {"n": n, "taxa_sucesso": sucessos / n if n else 0.0, "tentativas_media": sum(tentativas) / n if n else 0.0}


def carregar_teste(caminho: str) -> list:
    return [json.loads(l) for l in Path(caminho).read_text(encoding="utf-8").splitlines() if l.strip()]


def avaliar_modelo(modelo, linhas: list, com_tentativas: bool = False) -> dict:
    metricas = avaliar_primeira_tentativa(modelo, [l["messages"][0]["content"] for l in linhas])
    if com_tentativas:
        metricas["agente"] = avaliar_com_tentativas(modelo, [(l["task"], l["contexto"]) for l in linhas])
    return metricas


def main(argv=None) -> int:
    from src.spec.modelo_local import MODELO_SPEC_PADRAO, criar_llm_spec

    ap = argparse.ArgumentParser(description="Nível 1: avalia o gerador de specs (base, lora ou teacher=Qwen-14B) no test.jsonl")
    ap.add_argument("--test", default="dataset_tratado/test.jsonl")
    ap.add_argument("--modo", choices=["base", "lora", "teacher"], required=True)
    ap.add_argument("--modelo", default=MODELO_SPEC_PADRAO)
    ap.add_argument("--adapter")
    ap.add_argument("--quant4bit", action="store_true")
    ap.add_argument("--com-tentativas", action="store_true", help="também mede sucesso/tentativas via GeradorSpec (3x mais lento)")
    ap.add_argument("--saida", default="experiments/results/spec_{modo}.json")
    args = ap.parse_args(argv)

    if args.modo == "teacher":
        from src.modelo.cliente_llm import LLMClient
        modelo = LLMClient(max_tokens=2048)
    else:
        modelo = criar_llm_spec(args.modo, args.modelo, args.adapter, args.quant4bit)

    metricas = avaliar_modelo(modelo, carregar_teste(args.test), args.com_tentativas)
    if args.modo == "teacher":    # o relatório precisa dizer QUAL modelo serviu de referência (14B da disciplina ou substituto local)
        metricas["modelo_referencia"] = f"{modelo.model} ({modelo.backend})"
    destino = Path(args.saida.format(modo=args.modo))
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(metricas, indent=2, ensure_ascii=False), encoding="utf-8")
    print(json.dumps(metricas, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
