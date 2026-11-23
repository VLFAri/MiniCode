# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py` para retornar uma lista paginada de usuários.

## Parameters / Requirements
- **Entrada**: Os parâmetros de entrada são passados via dicionário `query`, contendo os seguintes campos:
  - `page`: Número da página solicitada (padrão = 1).
  - `page_size`: Tamanho da página (padrão = 20, máximo = 100).

- **Tipo dos Parâmetros**:
  - `page`: Deve ser convertido para inteiro.
  - `page_size`: Deve ser convertido para inteiro.

- **Restrições**:
  - `page` deve ser maior que zero.
  - `page_size` deve estar entre 1 e 100 inclusive.

- **Regras de Negócio**:
  - Se os valores de `page` ou `page_size` não forem válidos (não inteiros, menores que 1, ou `page_size` acima de 100), a função deve retornar um status HTTP 400 Bad Request com um dicionário contendo a mensagem de erro.
  - Se a página solicitada estiver além do número total de páginas, a função deve retornar uma lista vazia para `items`.

## Acceptance Criteria
- A função deve aceitar parâmetros de entrada via dicionário `query`.
- A função deve converter os valores de `page` e `page_size` para inteiros.
- A função deve validar os valores de `page` e `page_size` conforme as restrições mencionadas.
- A função deve retornar um JSON com os seguintes campos:
  - `page`: Número da página atual.
  - `page_size`: Tamanho da página.
  - `total`: Total de usuários disponíveis.
  - `items`: Lista de usuários na página solicitada.
- Em caso de erros de validação, a função deve retornar um JSON com o campo `erro` contendo a mensagem de erro e um status HTTP 400 Bad Request.
- Para páginas além do número total de páginas, a função deve retornar um JSON com `page`, `page_size`, `total` corretamente calculados e `items` como uma lista vazia.