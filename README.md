# MiniCode versão 1

# Estrutura

```
src/
  cli/main.py            (agente + modo --avaliar)
  agente/{estado,orquestrador}.py
  ferramentas/{base,registro,tools}.py
  spec/gerador.py        modelo/cliente_llm.py
tests/
```

## Como executar

No agente, a execução é realizada pelo src/cli/main.py, que inicia o prompt e o envia para o orquestrador.

Entretanto, para maior facilidade, foi criado o arquivo code que automatiza o processo. 

Então, para inicializar o agente, pode-se executar apenas:

```bash
./code
```
ou
```bash
python3 src/cli/main.py
```

## Escopo

O MiniCode só trabalha com **projetos Python**, verificados via **pytest** com a **biblioteca padrão**.
Não há Node.js, Java, Go, Ruby, PHP, nem instaladores de pacotes (pip, npm, yarn, conda...): um pedido que
exija outra linguagem ou dependência externa precisa ser reescrito em Python puro, e o prompt do agente
já instrui isso. Comandos desses ecossistemas (`npm install`, `pip install x`, `mvn test`...) são bloqueados
com uma mensagem explicando a limitação, em vez do erro genérico de allowlist.

## Fluxo do agente

```
RECEIVED → SPECIFIED → PLANNED → IMPLEMENTING → VERIFYING ──passou──► DONE
                                                    │  ▲
                                                falhou  │
                                                    ▼  │
                                                 REPAIRING ──limite──► FAILED
```

1. **SPECIFIED**: o LLM transforma o pedido em `specification.md` (Objective, Parameters, Acceptance Criteria).
2. **PLANNED**: o LLM cria `plan.md` numerado, vendo a spec e a lista de arquivos do projeto.
3. **IMPLEMENTING**: loop em que o LLM pede uma ferramenta (JSON), o harness a valida e executa e o resultado volta ao LLM, até `finish` ou o limite de iterações.
4. **VERIFYING**: o harness executa o pytest. O veredito vem do código de saída real.
5. **REPAIRING**: se falhou, o erro do pytest volta ao LLM, que corrige; retorna a VERIFYING. Máximo de `--max-reparos`; ao estourar, `FAILED`.
   - Se o **mesmo erro** (mesma exceção, mesmos testes falhando) se repetir em reparos consecutivos, o feedback ganha um aviso explícito para o LLM mudar de estratégia em vez de insistir no mesmo ajuste pontual; se persistir por `LIMITE_MESMO_ERRO_ABORTAR` (4) reparos seguidos, a tarefa falha antes de esgotar `--max-reparos`, economizando tentativas.

## Spec-Driven Development

A implementação não começa sem especificação. `spec/gerador.py` valida a spec (seções obrigatórias,
critérios de aceitação não vazios), remove cercas de código e refaz a geração (até 3 tentativas) se inválida.
O plano precisa ser uma lista numerada.

## Agent Hardness

| Regra | Onde é imposta |
|---|---|
| Não saltar etapas (ex.: SPECIFIED → IMPLEMENTING) | matriz de transições em `estado.py` |
| `SPECIFIED`/`PLANNED`/`IMPLEMENTING` exigem `specification.md` e `plan.md` não vazios | `_checar_precondicoes` |
| **`DONE` exige testes executados, aprovados e posteriores à última escrita** | `_checar_precondicoes` |
| `REPAIRING` só após testes que falharam e dentro do limite de tentativas | `_checar_precondicoes` |
| `FAILED` só via `falhar()` (qualquer estado não terminal) | `estado.py` |
| O LLM **não pode** executar `run_tests` nem declarar sucesso | `FERRAMENTAS_DO_HARNESS` no orquestrador |
| "Nenhum teste coletado" (exit 5) não conta como aprovado | `RunTests` |
| Sem a guarda de execução ativa, o código do projeto não roda (fail-closed) | `Contexto.sandbox_ativo` |
| Código perigoso não é gravado; 3 tentativas abortam a tarefa | `ValidadorConteudo` e `_ciclo_agente` |
| Pedido com comandos perigosos é recusado antes do LLM | `executar` |
| Arquivos alterados são reescaneados antes dos testes | `_verificar_arquivos_alterados` |
| Limite de iterações e de reparos | orquestrador / estado |

O `estado_atual` nunca é atribuído fora de `mudar_estado()` / `falhar()`.

## Ferramentas

`list_files`, `read_file`, `write_file`, `create_file`, `replace_text`, `search_code`, `git_diff`,
`run_command` (allowlist) e `run_tests` (apenas harness). Saídas são truncadas para respeitar a janela de contexto.

## Segurança

Defesa em profundidade, em camadas independentes (cada uma vale mesmo se a anterior for burlada):

**1. Ferramentas (o que o agente pede)** — `ValidadorCaminho` e `ValidadorComando` em `ferramentas/base.py`
- **Caminhos**: `resolve()` + verificação de que o alvo está dentro do projeto (bloqueia `../`, caminhos absolutos e symlinks para fora). Escrita proibida em `.git/` e `.minicode/`; leitura e escrita proibidas em `.env`.
- **Comandos**: allowlist (`pytest`, `python -m pytest`, `git diff|status|log`), **sem shell**; metacaracteres (`; & | > < $ \``), `sudo`, `rm`, `shutdown`, `reboot` etc. e flags perigosas (`--output`, `--basetemp`...) são rejeitados.

**2. Código perigoso nunca é gravado (o que o agente escreve)** — `ValidadorConteudo`
- O LLM **não pode** escrever comandos perigosos em nenhum arquivo: toda gravação (`write_file`, `create_file`, `replace_text`, que valida o arquivo resultante) passa pelo scanner, e a gravação é recusada. O texto vale para **qualquer tipo de arquivo**, inclusive `.md` e `.txt`.
- **Python (análise da AST)**: `subprocess`, `ctypes`, `importlib`, `builtins`, `runpy`, `marshal`, `eval`, `exec`, `__import__`, `os.system/popen/exec*/spawn*/fork/kill`, remoção e permissões (`os.remove/unlink/rmdir/chmod/chown`, `shutil.rmtree`, `.unlink()`, `.rmdir()`), `getattr(os, "system")`, `__builtins__` e **aliases** (`import os as o`).
- **Texto de qualquer arquivo (regex)**: `rm` com opções ou em caminhos perigosos, `rmdir`, `shred`, `sudo`, `shutdown/reboot/poweroff`, `mkfs`, `dd if=`, fork bomb, `chmod 777`, `chown -R`, `curl|sh`, `kill -9`, `killall`, `systemctl stop`, `iptables`, `crontab`, equivalentes do Windows (`del /f`, `rd /s`, `format c:`).
- Clientes HTTP (`requests`, `socket`) são permitidos: a rede é bloqueada na execução.
- **Reincidência**: após 3 tentativas bloqueadas de gravar código perigoso, a tarefa é abortada em `FAILED`.
- **Pedido do usuário**: se a própria tarefa pede algo perigoso, é recusada antes de chamar o LLM, tanto em comandos (`rm -rf /`) quanto em linguagem natural, em português e inglês: destruição de arquivos ("delete todos os arquivos", "formate o disco", "desligue o computador"), elevação de privilégios ("execute como root"), malware ("crie um ransomware") e **invasão ou acesso não autorizado** ("hackeie a Nasa", "invada o servidor", "quebre a senha", "crie um exploit para essa vulnerabilidade", "ataque DDoS", "hack into..."). Pedidos legítimos parecidos ("remova elementos duplicados", "apague a função X do arquivo", "teste a segurança da autenticação", "hackathon") passam.
- **Reescaneamento**: antes de executar os testes, os arquivos alterados são verificados de novo; se algum contiver código perigoso, os testes não rodam.
- O prompt também proíbe esses comandos, mas a garantia vem do código, não do prompt.

**3. Guarda de execução (o que o código faz ao rodar)** — `GUARDA_EXECUCAO` em `ferramentas/base.py`
- O pytest roda via `python -c`, com um *audit hook* (PEP 578) instalado antes de importá-lo. Dentro do processo dos testes ficam bloqueados: escrita/remoção/renomeação **fora do projeto** (e em `.git/`, `.minicode/`, `.env`), leitura de segredos (`~/.ssh`, `~/.aws`, `/etc/shadow`...), criação de processos (`subprocess`, `os.system`, `fork`, `exec`, `ctypes`) e **toda rede que não seja loopback**, incluindo DNS.
- O `tmp_path` do pytest fica dentro do projeto (`.minicode/tmp`), então testes legítimos funcionam.
- **Fail-closed**: antes de executar testes, o harness confirma que a guarda carrega (sonda). Se não carregar, o código do projeto **não é executado** e a tarefa termina em `FAILED`. `MINICODE_SANDBOX=off` desativa a guarda (só para depuração; emite aviso).

**4. Limites e isolamento do processo**
- Timeout, limites de CPU, memória (4 GB) e tamanho de arquivo (100 MB) no subprocesso (POSIX); limite de iterações, de reparos e detecção de loop.
- Subprocessos rodam **sem variáveis** `*KEY*`, `*TOKEN*`, `*SECRET*`: o código do projeto não vê a chave da API.
- `git diff` roda com `--no-ext-diff --no-textconv`.

**Limitações conhecidas** (relevantes para o relatório)
- Não é um sandbox à prova de código **deliberadamente hostil**: o scanner é heurístico (ofuscação o contorna) e audit hooks do Python não são uma fronteira de segurança absoluta. Elas fecham o caso realista, um LLM que escreve código perigoso por engano ou por instrução maliciosa embutida em arquivos.
- Leitura de arquivos fora do projeto é permitida, exceto a lista de segredos conhecidos.
- As restrições valem para o código executado **pelo harness** (testes). Rodar manualmente o script gerado não passa pela guarda.
- Testes que dependam de rede ou de subprocessos precisam usar mocks (o prompt informa o modelo disso).
- Para isolamento forte (por exemplo, avaliar código de terceiros), execute o MiniCode dentro de um contêiner sem rede.

## Testes

`tests/` (297 testes, sem rede) cobre:
- **Estado e gates**: transições proibidas, pré-condições de `DONE`/`REPAIRING`, `falhar()`.
- **Segurança**: caminhos, comandos, scanner de conteúdo (incluindo truques como aliases e remoção de arquivos, e a ausência de falsos positivos em código legítimo), pedido perigoso recusado, reincidência, e a guarda de execução com tentativas reais de fuga (escrita fora do projeto, `os.system`, `subprocess`, rede externa, leitura de `~/.ssh`).
- **Ferramentas e gerador de spec**.
- **Orquestrador ponta a ponta com LLM falso**: sucesso, repair loop, estouro de reparos, JSON malformado, várias ações por resposta, loop repetido, Ctrl+C e falha do endpoint.

## Rastreabilidade (`.minicode/` dentro do projeto alvo)

| Arquivo | Conteúdo |
|---|---|
| `specification.md`, `plan.md` | spec e plano produzidos |
| `actions.jsonl` | transições, chamadas de ferramenta, execuções de teste, erros de formato |
| `state.json` | tarefa, estado final, arquivos alterados, nº de reparos, testes, erro, `success`, `first_attempt_success`, chamadas e tokens do LLM |

## Avaliação

O modo `--avaliar DIR` roda o agente em todas as tarefas de um diretório e reporta **TaskSuccessRate**,
**FirstAttemptSuccess**, **AverageIterations** (ciclos de verificação) e **AverageLLMCalls**, salvando
em `experiments/resultados/resultados.json` junto do rastro de cada tarefa. Cada tarefa é uma pasta:

```
<DIR>/<nome_da_tarefa>/
    tarefa.txt     pedido em linguagem natural
    projeto/       projeto inicial, com os testes que definem o sucesso
```

O agente trabalha numa cópia temporária de `projeto/`, então os originais nunca são alterados.