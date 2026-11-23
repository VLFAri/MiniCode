# Specification

## Objective
Implementar uma função `paginar` que recebe uma lista de itens (`itens`), um número inteiro representando a página (`pagina`) e outro número inteiro representando o tamanho da página (`tamanho`). A função deve retornar uma lista contendo apenas os itens da página solicitada, considerando que a primeira página é 1-indexada.

## Parameters / Requirements
- **Entrada:** Uma lista de objetos (`itens`), dois números inteiros positivos (`pagina` e `tamanho`).
- **Restrições:** 
  - Se `pagina` ou `tamanho` forem menores que 1, levantar `ValueError`.
  - Se `pagina` for maior que a quantidade total de páginas possíveis, retornar uma lista vazia.
- **Saída:** Uma lista contendo os itens da página solicitada, ou uma lista vazia se a página não existir.

## Acceptance Criteria
- `paginar([1, 2, 3], 1, 2)` retorna `[1, 2]`
- `paginar(['a', 'b', 'c'], 2, 1)` retorna `['b']`
- `paginar([], 1, 1)` retorna `[]`
- `paginar([10, 20, 30], 1, 5)` retorna `[10, 20, 30]`
- `paginar([10, 20, 30], 2, 1)` retorna `[]`
- `paginar([10, 20, 30], 3, 1)` retorna `[]`
- `paginar([10, 20, 30], 4, 1)` lança `ValueError`
- `paginar([10, 20, 30], 0, 1)` lança `ValueError`
- `paginar([10, 20, 30], -1, 1)` lança `ValueError`
- `paginar([10, 20, 30], 1, 0)` lança `ValueError`
- `paginar([10, 20, 30], 1, 6)` lança `ValueError`