# Specification

## Objective
Implementar uma função `paginar(itens, pagina, tamanho)` que seja 1-indexada, retornando a página correta dos itens fornecidos. A função deve lançar `ValueError` se a página ou o tamanho forem menores que 1. Para páginas além do final da lista de itens, a função deve retornar uma lista vazia.

## Parameters / Requirements
- **itens**: Uma lista de objetos (por exemplo, strings, números, etc.) que serão paginados.
- **pagina**: Um número inteiro representando a página desejada. Deve ser 1-indexado (ou seja, a primeira página é 1).
- **tamanho**: Um número inteiro representando o tamanho da página (número de itens por página).

Restrições:
- Se `pagina` ou `tamanho` forem menores que 1, a função deve lançar `ValueError`.
- Se `pagina` for além do final da lista de itens, a função deve retornar uma lista vazia.

## Acceptance Criteria
- A função deve aceitar uma lista de itens e retornar a página correta baseada nos parâmetros `pagina` e `tamanho`.
- A função deve lançar `ValueError` se `pagina` ou `tamanho` forem menores que 1.
- A função deve retornar uma lista vazia se `pagina` for além do final da lista de itens.
- Testes automatizados devem verificar que a função retorna os resultados esperados para diferentes entradas.