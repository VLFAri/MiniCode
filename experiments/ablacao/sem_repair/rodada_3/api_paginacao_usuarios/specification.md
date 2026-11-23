# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py` para retornar uma lista paginada de usuários.

## Parameters / Requirements
- **Entrada**: Os parâmetros de entrada são passados via dicionário `query`, contendo os seguintes campos:
  - `page`: Número da página solicitada (padrão: 1).
  - `page_size`: Tamanho da página (padrão: 20, máximo: 100).

- **Tipo dos Parâmetros**:
  - `page`: Deve ser convertido para inteiro.
  - `page_size`: Deve ser convertido para inteiro.

- **Restrições**:
  - `page` deve ser maior que zero.
  - `page_size` deve estar entre 1 e 100.

- **Regras de Negócio**:
  - Se `page` ou `page_size` não forem válidos (não inteiros, menores que 1, ou `page_size` acima de 100), a rota deve retornar um status HTTP 400 Bad Request com um dicionário JSON contendo uma mensagem de erro.

## Acceptance Criteria
- A rota GET /users deve aceitar parâmetros `page` e `page_size`.
- A resposta deve conter os seguintes campos no formato JSON:
  - `page`: Número da página atual.
  - `page_size`: Tamanho da página.
  - `total`: Total de usuários disponíveis.
  - `items`: Lista de usuários na página solicitada.
- Se os parâmetros `page` ou `page_size` forem inválidos, a resposta deve ser um status HTTP 400 Bad Request com um dicionário JSON contendo uma mensagem de erro.
- Para páginas além do final da lista de usuários, a resposta deve conter `items` como uma lista vazia.