# Arquitetura

```
 USER ─► Orquestrador ─► GeradorSpec ─► spec.md, plan.md          (LLM só propõe texto)
              │
              ├─► LLM ──JSON{tool,args}──► Validadores ──► Ferramentas ──► resultado ─► LLM
              │                                │ recusa
              │                                └──► ViolacaoSeguranca (3 → FAILED)
              └─► GerenciadorEstado (hard gates) ─► .minicode/{state.json, actions.jsonl}
```

## Máquina de estados

| De | Para | Pré-condição imposta por código |
|---|---|---|
| RECEIVED | SPECIFIED | `specification.md` existe e não é vazio |
| SPECIFIED | PLANNED | `plan.md` existe e não é vazio |
| PLANNED | IMPLEMENTING | spec **e** plano presentes |
| IMPLEMENTING | VERIFYING | (o sistema roda o pytest) |
| VERIFYING | DONE | testes executados, **aprovados** e sem alterações posteriores |
| VERIFYING | REPAIRING | última execução falhou e `tentativas < max_reparos` |
| REPAIRING | VERIFYING | — |
| qualquer | FAILED | só via `falhar(motivo)`: limite de reparos, mesmo erro repetido, violação, exceção |

Qualquer transição fora da tabela levanta `RuntimeError("Hard Gate violado ...")`. Os testes em `tests/test_estado.py`
cobrem cada caso.

## Ciclo de execução

1. Recusa pedidos perigosos antes de chamar o LLM.
2. `GeradorSpec.gerar_spec` (até 3 tentativas, com validação do formato) e `gerar_plano` (lista numerada).
3. Ciclo do agente: o LLM responde até 3 chamadas JSON por turno; cada uma é validada e executada; o resultado volta ao LLM.
4. `finish` → o sistema roda `run_tests` na sandbox. Falhou → `REPAIRING` com saída do pytest e conteúdo atual dos arquivos.
5. Para quando: testes passam (`DONE`), limite de reparos, mesmo erro repetido, loop de ações, ou violações de segurança.

## Rastro (`.minicode/actions.jsonl`)

Eventos: `transition`, `tool_call`, `run_tests`, `spec_attempt`, `invalid_tool`, `blocked_test_command`,
`security_violation`, `request_refused`, `loop_detected`, `same_error_abort`.

## Parte 2: onde o modelo especializado entra

```
tarefa + contexto (list_files) ──► [Qwen-14B | modelo pequeno + LoRA] ──► especificação
                                          ▲ só esta função muda; plano, código e reparo ficam no Qwen-14B
```

* `GeradorSpec(llm, llm_spec=...)`: `llm_spec` é usado **apenas** para a spec; se faltar, usa-se o LLM principal.
* O treino e a inferência usam o mesmo `PROMPT_SPEC` (`tests/test_spec.py` garante que o dataset o respeita).
* Dataset: `src/spec/dataset.py`. O teacher recebe um system prompt com as regras do harness; o aluno não o vê.
* Avaliação nível 1: `src/spec/avaliacao.py`; nível 2: `main.py --avaliar --spec-model ...`; ablação: `src/avaliador/ablacao.py`.

## Ablação "regra no prompt × hard gate"

`Orquestrador(hard_gates=False)` remove só o gate `VERIFYING → DONE`: o prompt passa a **pedir** que o modelo rode os
testes (a ferramenta `run_tests` fica disponível), mas `finish` vira `DONE` sem conferência. Sucesso real é medido pelos
testes ocultos; `FalseSuccessRate` mede quantas vezes o agente declarou sucesso sem merecer.
