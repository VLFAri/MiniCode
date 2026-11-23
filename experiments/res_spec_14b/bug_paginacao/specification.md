# Specification

## Objective
Implementar uma função `paginar` que retorna a página correta de uma lista de itens com base nos parâmetros fornecidos. A função deve ser 1-indexada, ou seja, a página 1 deve retornar os primeiros itens da lista.

## Parameters / Requirements
- **itens**: Uma lista de objetos ou valores que serão paginados.
- **pagina**: Um número inteiro representando a página desejada. Deve ser 1-indexado (ou seja, a primeira página é 1).
- **tamanho**: Um número inteiro representando o número de itens por página.

Restrições:
- Se `pagina` ou `tamanho` forem menores que 1, a função deve lançar um `ValueError`.
- Páginas além do final da lista devem retornar uma lista vazia.

## Acceptance Criteria
- A função deve aceitar uma lista de itens e retornar a página correta com base no tamanho da página e na página desejada.
- A função deve lançar um `ValueError` se `pagina` ou `tamanho` forem menores que 1.
- A função deve retornar uma lista vazia para páginas além do final da lista.
- A função deve ser 1-indexada, ou seja, a página 1 deve retornar os primeiros itens da lista.

Esses critérios podem ser verificados através de testes automatizados que incluem casos de uso como entradas inválidas, páginas fora do intervalo válido e páginas válidas dentro do intervalo.