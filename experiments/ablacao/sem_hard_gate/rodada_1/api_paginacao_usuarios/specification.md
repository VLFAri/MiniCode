# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py` para retornar uma lista paginada de usuários.

## Parameters / Requirements
- **Entrada**: Os parâmetros de entrada são passados via dicionário `query`, contendo os seguintes campos:
  - `page`: Número da página solicitada (padrão 1).
  - `page_size`: Tamanho da página (padrão 20, máximo 100).

- **Tipos**:
  - `page`: String ou inteiro.
  - `page_size`: String ou inteiro.

- **Restrições**:
  - `page` deve ser convertido para um número inteiro maior ou igual a 1.
  - `page_size` deve ser convertido para um número inteiro entre 20 e 100 (inclusive).

- **Regras de Negócio**:
  - Se `page` ou `page_size` não forem válidos (não inteiros, menores que 1, ou `page_size` acima de 100), a rota deve retornar um status HTTP 400 Bad Request com um dicionário JSON contendo uma mensagem de erro.

## Acceptance Criteria
- A rota GET /users deve aceitar parâmetros `page` e `page_size`.
- Deve retornar um status HTTP 200 OK com um dicionário JSON contendo as chaves `page`, `page_size`, `total` (total de usuários) e `items` (itens da página atual).
- Se `page` ou `page_size` forem inválidos, a rota deve retornar um status HTTP 400 Bad Request com um dicionário JSON contendo uma chave `erro` com a mensagem de erro.
- Para páginas além do final da lista de usuários, a resposta deve conter `items` como uma lista vazia.