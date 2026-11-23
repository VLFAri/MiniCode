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
  - Se `page` ou `page_size` forem inválidos (não inteiros, menores que 1, ou `page_size` acima de 100), a rota deve retornar um status HTTP 400 Bad Request com um dicionário JSON contendo uma mensagem de erro.
  - Para páginas além do final da lista de usuários, a resposta deve conter uma lista vazia de itens.

## Acceptance Criteria
- A rota GET /users deve aceitar parâmetros `page` e `page_size`.
- Deve validar os parâmetros conforme as restrições definidas.
- Em caso de parâmetros válidos, deve retornar um status HTTP 200 OK com um dicionário JSON contendo os campos `page`, `page_size`, `total` (total de usuários disponíveis) e `items` (itens da página solicitada).
- Em caso de parâmetros inválidos, deve retornar um status HTTP 400 Bad Request com um dicionário JSON contendo uma mensagem de erro.
- Testes automatizados devem verificar corretamente todas as condições listadas acima.