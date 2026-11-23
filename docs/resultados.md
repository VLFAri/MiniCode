# Resultados experimentais

Arquivo gerado por `python experiments/gerar_relatorio.py`; todos os números vêm dos arquivos de resultado.

## 1. Nível 1: gerador de especificações (base × fine-tuned × Qwen-14B)

_(ainda não executado: arquivo `experiments/results/spec_colab.json` não encontrado)_

## 2. Nível 2: agente completo com cada gerador de especificação

| Gerador de especificação | HiddenSuccessRate | TaskSuccessRate | FirstAttemptSuccess | SpecFirstTryValid | AverageSpecAttempts | AverageIterations | AverageLLMCalls |
|---|---|---|---|---|---|---|---|
| Qwen-14B | 0.32 | 0.36 | 0.32 | 1.00 | 1.00 | 2.41 | 4.68 |
| modelo base | 0.36 | 0.41 | 0.27 | 1.00 | 1.00 | 2.59 | 3.95 |
| fine-tuned (QLoRA) | 0.38 | 0.31 | 0.08 | 1.00 | 1.00 | 2.92 | 4.31 |

Modelo principal do agente (plano, código e reparo) em cada execução: Qwen-14B: Qwen/Qwen2.5-14B-Instruct-AWQ; modelo base: Qwen/Qwen2.5-14B-Instruct-AWQ; fine-tuned (QLoRA): Qwen/Qwen2.5-14B-Instruct-AWQ.

## 3. Ablação

_(ainda não executado: arquivo `experiments/ablacao/*/rodada_*/resultados.json` não encontrado)_

