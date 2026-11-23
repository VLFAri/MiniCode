# Specification

## Objective
Implementar uma função `paginar` que retorna a página correta de uma lista de itens, considerando um índice baseado em 1 para as páginas.

## Parameters / Requirements
- **itens**: Uma lista de objetos ou valores que serão paginados.
- **pagina**: Um número inteiro representando a página desejada. Deve ser maior ou igual a 1.
- **tamanho**: Um número inteiro representando o tamanho da página. Deve ser maior ou igual a 1.

Restrições:
- Se `pagina` ou `tamanho` forem menores que 1, a função deve lançar um `ValueError`.
- Se `pagina` for além do final da lista de itens, a função deve retornar uma lista vazia.

## Acceptance Criteria
- A função deve aceitar uma lista de itens e retornar a página correta com base nos parâmetros `pagina` e `tamanho`.
- A função deve lançar um `ValueError` se `pagina` ou `tamanho` forem menores que 1.
- A função deve retornar uma lista vazia se `pagina` for além do final da lista de itens.
- A função deve ser 1-indexada, ou seja, a página 1 deve retornar os primeiros itens.
- Testes automatizados devem verificar corretamente essas condições.