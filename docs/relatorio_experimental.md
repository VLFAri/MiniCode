# Relatório experimental (Parte 2)

> Os números vêm de [`resultados.md`](resultados.md) (gerado por `python experiments/gerar_relatorio.py`). Onde está
> `PREENCHER`, escreva com base nos seus resultados: nada abaixo afirma resultado que ainda não foi medido.

## 1. Pergunta e hipótese

**Pergunta.** É possível especializar uma LLM pequena para executar melhor uma função específica do agente?

**Função escolhida.** Geração de especificação (`task + contexto → spec`).

**Hipótese.** Após o fine-tuning com QLoRA, o Qwen2.5-Coder-1.5B-Instruct gera especificações que o agente aceita já na
primeira tentativa (`validar_spec`) e que cumprem critérios de qualidade (critérios de aceitação verificáveis com exemplos
concretos, sem código de implementação, só biblioteca padrão), em taxa maior que o mesmo modelo sem treino e próxima à do
Qwen-14B. **Hipótese do nível 2:** esse ganho local melhora a `HiddenSuccessRate` do agente completo. (Pode não melhorar:
reporte o que medir.)

## 2. Dataset

Preencher com os valores de `dataset_tratado/stats.json`:

| Item | Valor |
|---|---|
| Origem das tarefas | `tarefas_semente.txt` (+ tarefas geradas pelo teacher com `--expandir`) |
| Teacher | Qwen-14B (endpoint da disciplina) — PREENCHER se usou outro |
| Geração | prompt real do agente + system prompt privilegiado (regras do harness), até 3 tentativas com reamostragem |
| Filtragem | validação estrita (`src/spec/qualidade.py`): formato do agente, ≥ 3 critérios, exemplos concretos, sem código de implementação, só stdlib, tamanho |
| Sementes excluídas | reservadas do enunciado, fora do escopo (frameworks, outras linguagens), quase duplicadas |
| Formato | `{task, contexto, messages:[user, assistant]}` em JSONL |
| Quantidade | PREENCHER (`itens_validos` de `stats.json`) |
| Split | PREENCHER (tarefas/exemplos de train, val, test; **por tarefa**, sem vazamento) |

Limitações a discutir: tamanho do conjunto de teste; viés do teacher; contextos sintéticos; sementes parecidas entre si.

## 3. Modelo e LoRA/QLoRA

`Qwen/Qwen2.5-Coder-1.5B-Instruct`, base congelada em 4 bits (NF4) no QLoRA.

Em vez de atualizar `W ∈ ℝ^{d×d}`, aprende-se `ΔW = BA`, com `B ∈ ℝ^{d×r}`, `A ∈ ℝ^{r×d}` e `r ≪ d`; a saída é
`W' = W + (α/r)·BA`. `W` tem `d²` parâmetros e `BA` tem `2rd` (para `d = 1536` e `r = 16`: 2,36 M contra 49 mil, cerca de
2%). `B` começa em zero, então o modelo com LoRA é idêntico ao base antes do treino, e a comparação base × fine-tuned usa o
mesmo objeto. No QLoRA a matriz congelada fica quantizada em 4 bits e só `A` e `B` são treinados em 16 bits.

Configuração: PREENCHER (r, α, dropout, módulos-alvo, épocas, learning rate, batch efetivo, `MAX_LEN`; ver o notebook).

## 4. Treinamento

PREENCHER: figura `experiments/results/spec_loss.png` (loss de treino × época e de validação × época), época do melhor
checkpoint, sinais de overfitting.

## 5. Resultados

Nível 1 (tarefa especializada), nível 2 (agente completo) e ablação: copie as tabelas de [`resultados.md`](resultados.md).
Para cada uma, escreva: o que mudou, o tamanho da amostra, a variação entre rodadas e se a diferença é conclusiva.

## 6. Ablação

Componentes comparados: `completo`, `sem_repair` (`max_reparos=0`) e `sem_hard_gate` (regra só no prompt). Interprete
principalmente `HiddenSuccessRate` e `FalseSuccessRate`. PREENCHER.

## 7. Respostas às questões do enunciado

| # | Pergunta | Evidência a usar | Resposta |
|---|---|---|---|
| 1 | Quanto a LLM faz sozinha e quanto depende do harness? | `sem_hard_gate` e `sem_repair` × `completo` | PREENCHER |
| 2 | Spec-Driven Development melhora a execução? | `SpecFirstTryValid`, relação entre spec válida e `HiddenSuccessRate` por tarefa | PREENCHER |
| 3 | Pedir a regra × impor a regra? | `completo` × `sem_hard_gate`, `FalseSuccessRate` | PREENCHER |
| 4 | O feedback dos testes permite auto-correção? | `completo` × `sem_repair`, `FirstAttemptSuccess` × `TaskSuccessRate` | PREENCHER |
| 5 | O fine-tuning melhorou o modelo? | tabela do nível 1 | PREENCHER |
| 6 | O ganho local virou ganho no agente? | tabela do nível 2 | PREENCHER |
| 7 | Modelo pequeno especializado compete com o maior? | nível 1 e 2, coluna Qwen-14B | PREENCHER |
| 8 | Quais componentes mais impactaram? | todas as tabelas | PREENCHER |

## 8. Ameaças à validade

Poucas tarefas; agente estocástico (use `--repeticoes`); teacher e juiz de qualidade serem heurísticos (`validar_spec_estrita`
mede forma, não correção semântica); testes ocultos escritos pelo mesmo grupo; geração gulosa vs. amostrada.
