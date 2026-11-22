# Uso de ferramentas de IA

O enunciado permite e incentiva o uso de ferramentas de IA; o aluno continua responsável por todo o código entregue.
Este arquivo descreve **como** foram usadas. Revise e complete as partes marcadas com `PREENCHER` antes de entregar.

## Ferramentas

* **Claude (Anthropic), via chat web/app** — assistente de revisão, implementação e documentação.
* PREENCHER: outras ferramentas usadas (Claude Code, Copilot, ChatGPT...) e em quais etapas.

## O que o assistente fez

**Parte 1 (v1)** — PREENCHER: como a v1 foi construída (quais partes escritas à mão, quais com ajuda de IA).

**Parte 2 (v2)**

* Revisão do código da v1 e dos scripts de dados/notebook que o aluno já tinha. Apontou: dataset fora do formato do agente
  (0 de 121 specs passavam no `validar_spec`), teacher e aluno sendo o mesmo modelo, contexto fixo no prompt, sementes fora
  do escopo do harness e notebook sem célula de treino.
* Implementação (com testes automatizados): pipeline de dataset (`src/spec/dataset.py`, `gerar_datasets.py`), validação
  de qualidade das specs (`src/spec/qualidade.py`), tokenização com máscara de loss, notebook de treino QLoRA, modelo local
  integrado ao `GeradorSpec`, avaliação em dois níveis, testes ocultos, ablação (flag `hard_gates`), relatório automático.
* Criação das 22 tarefas de `tarefas_teste/` com testes ocultos e soluções de referência, validadas por `src.avaliador.tarefas`.
* Redação de README, `docs/architecture.md`, modelo do relatório e roteiro do vídeo.

## O que o assistente NÃO fez

* Não executou o teacher (Qwen-14B), o treino no Colab nem as avaliações: **nenhum resultado numérico foi produzido ou
  inventado pelo assistente**. Os números de `docs/resultados.md` vêm dos arquivos gerados pelas execuções do aluno.
* Não gravou o vídeo.

## O que o aluno fez e validou

PREENCHER (exemplos): gerou o dataset com o teacher e inspecionou amostras; revisou `stats.json`; treinou no Colab;
rodou as avaliações e a ablação; leu e entende cada módulo (máquina de estados, validadores, LoRA/QLoRA); ajustou
prompts/limites; corrigiu erros encontrados.

## Verificação

Os testes automatizados (`pytest tests/`) cobrem o harness, a segurança, o dataset, a avaliação e a ablação. O notebook
de treino só pode ser verificado executando-o no Colab.
