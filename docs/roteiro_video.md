# Roteiro do vídeo (≈ 8–10 min)

Mostre **pelo menos uma execução completa**: prompt → spec → plano → alteração de código → execução → erro → correção → testes → resultado.

## Parte 1 — o agente (3–4 min)
1. `cat .env` **não** (nunca mostre a chave). Mostre `export MINICODE_API_KEY=...` já feito e a estrutura de pastas.
2. Rode uma tarefa que costuma exigir reparo (ex.: `bug_media_mediana`, copiando `tarefas_teste/bug_media_mediana/projeto` para `workspace/`):
   `PYTHONPATH=. python3 src/cli/main.py "$(cat tarefas_teste/bug_media_mediana/tarefa.txt)" --project ./workspace`
3. Pause em cada etapa e explique: `[Hard Gate] RECEIVED -> SPECIFIED -> PLANNED -> IMPLEMENTING -> VERIFYING -> REPAIRING -> VERIFYING -> DONE`.
4. Abra `workspace/.minicode/` (`specification.md`, `plan.md`, `actions.jsonl`, `state.json`).
5. Demonstre dois bloqueios: um pedido perigoso ("Delete todos os arquivos") recusado antes do LLM e `pytest tests/test_estado.py` (gates).

## Parte 2 — especialização (4–5 min)
1. O problema: mostre uma linha do dataset antigo × novo e `dataset_tratado/stats.json` (origem, filtro, splits).
2. Notebook no Colab: tokenização com máscara, config QLoRA, `print_trainable_parameters`, curvas de loss, tabela base × fine-tuned.
3. Agente com o modelo treinado: `--spec-model lora --spec-adapter adapter_spec --spec-4bit`.
4. `docs/resultados.md`: nível 1, nível 2 e ablação. Diga o que **não** melhorou, se for o caso.
5. Feche respondendo, em uma frase cada, às perguntas 3, 5 e 6 do enunciado.
