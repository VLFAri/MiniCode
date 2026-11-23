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

| Configuração | HiddenSuccessRate | FalseSuccessRate | TaskSuccessRate | FirstAttemptSuccess | AverageIterations | AverageLLMCalls |
|---|---|---|---|---|---|---|
| completo (n=3 rodada(s)) | 0.41 ± 0.05 | 0.11 ± 0.03 | 0.50 ± 0.09 | 0.38 ± 0.03 | 2.00 ± 0.09 | 4.29 ± 0.23 |
| sem_repair (n=3 rodada(s)) | 0.33 ± 0.05 | 0.06 ± 0.03 | 0.32 ± 0.05 | 0.32 ± 0.05 | 1.00 ± 0.00 | 3.12 ± 0.20 |

