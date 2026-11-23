Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Criação do Ambiente de Desenvolvimento:**
   - Crie um novo diretório para o projeto.
   - Inicialize um ambiente virtual (`venv`) para o projeto.
   - Instale as dependências necessárias (por exemplo, `pytest` para testes).

2. **Estrutura de Arquivos:**
   - Crie os seguintes arquivos e diretórios:
     - `src/`: Diretório principal onde a implementação da função será colocada.
     - `tests/`: Diretório onde os testes serão escritos.
     - `requirements.txt`: Arquivo para listar as dependências do projeto.

3. **Implementação da Função `dias_entre`:**
   - No arquivo `src/dias_entre.py`, implemente a função `dias_entre` que recebe duas strings de data no formato "AAAA-MM-DD" e retorna a diferença absoluta em dias entre elas.
   - Use o módulo `datetime` para manipulação de datas.
   - Implemente a validação das entradas para garantir que estejam no formato correto e sejam datas válidas.
   - Trate possíveis erros de entrada lançando um `ValueError` quando necessário.

4. **Testes Automatizados:**
   - No diretório `tests/`, crie um arquivo `test_dias_entre.py`.
   - Escreva testes unitários para a função `dias_entre` utilizando o framework `pytest`.
   - Inclua testes para casos de uso comuns, datas extremas, e entradas inválidas.
   - Certifique-se de que todos os cenários de teste cobrem os requisitos e critérios de aceitação.

5. **Execução dos Testes:**
   - Execute os testes automatizados para verificar a funcionalidade da função `dias_entre`.
   - Corrija quaisquer falhas encontradas durante a execução dos testes.

6. **Documentação:**
   - Adicione documentação ao código fonte da função `dias_entre` para explicar seu propósito, parâmetros e retorno.
   - Documente os testes escritos para cada caso de uso.

7. **Validação Final:**
   - Revisite o código e os testes para garantir que todos os requisitos foram atendidos.
   - Certifique-se de que a função `dias_entre` funciona corretamente para todas as entradas válidas e lança `ValueError` para entradas inválidas.

### Exemplo de Estrutura de Arquivos

```
project/
│
├── src/
│   └── dias_entre.py
│
├── tests/
│   └── test_dias_entre.py
│
└── requirements.txt
```

Este plano fornece uma estrutura clara para implementar a função `dias_entre` e garantir sua qualidade através de testes automatizados.