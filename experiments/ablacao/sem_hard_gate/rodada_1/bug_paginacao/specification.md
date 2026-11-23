# Specification

## Objective
Implementar uma função `paginar` que retorna a página correta de uma lista de itens com base nos parâmetros fornecidos. A função deve ser 1-indexada, ou seja, a página 1 deve retornar os primeiros itens da lista.

## Parameters / Requirements
- **itens**: Uma lista de objetos ou valores que serão paginados.
- **pagina**: Um número inteiro representando a página desejada. Deve ser 1-indexado.
- **tamanho**: Um número inteiro representando o tamanho da página, ou seja, quantos itens cada página deve conter.

Restrições:
- Se `pagina` ou `tamanho` forem menores que 1, a função deve lançar um `ValueError`.
- Páginas além do final da lista devem retornar uma lista vazia.

## Acceptance Criteria
- A função deve retornar a página correta quando chamada com parâmetros válidos.
- A função deve lançar um `ValueError` se `pagina` ou `tamanho` forem menores que 1.
- A função deve retornar uma lista vazia para páginas além do final da lista.
- A função deve ser 1-indexada, ou seja, a página 1 deve retornar os primeiros itens da lista.

Essa especificação fornece as diretrizes necessárias para implementar a função `paginar` de acordo com os requisitos fornecidos pelo usuário.