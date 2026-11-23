# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py` para retornar uma lista paginada de usuários.

## Parameters / Requirements
- **Entrada**: Os parâmetros de entrada são passados via dicionário `query`, contendo os seguintes campos:
  - `page`: Número da página solicitada (padrão = 1).
  - `page_size`: Tamanho da página (padrão = 20, máximo = 100).

- **Restrições**:
  - `page` e `page_size` podem ser fornecidos como strings ou inteiros.
  - `page_size` não pode exceder 100.
  - `page` e `page_size` devem ser números inteiros positivos.

- **Regras de Negócio**:
  - Se nenhum valor for fornecido para `page` e `page_size`, os padrões serão usados.
  - Se valores inválidos forem fornecidos (não inteiros, menores que 1, ou `page_size` acima de 100), a rota deve retornar um código de status 400 e uma mensagem de erro.

## Acceptance Criteria
- A rota GET /users deve aceitar parâmetros `page` e `page_size`.
- Deve retornar um JSON com os seguintes campos:
  - `"page"`: Número da página atual.
  - `"page_size"`: Tamanho da página.
  - `"total"`: Total de usuários disponíveis.
  - `"items"`: Lista de usuários na página solicitada.
- Se os valores de `page` ou `page_size` forem inválidos, a rota deve retornar um JSON com o campo `"erro"` contendo uma mensagem de erro e um código de status HTTP 400.
- Para páginas além do total de páginas disponíveis, a rota deve retornar um JSON válido com `"items"` como uma lista vazia.