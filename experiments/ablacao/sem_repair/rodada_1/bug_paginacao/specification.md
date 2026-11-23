# Specification

## Objective
Implementar uma função `paginar` que retorna a página correta de uma lista de itens, considerando um índice baseado em 1 para as páginas.

## Parameters / Requirements
- **itens**: Lista de objetos ou valores que serão paginados.
- **pagina**: Número da página desejada. Deve ser um número inteiro positivo. A primeira página é 1.
- **tamanho**: Número de itens por página. Deve ser um número inteiro positivo.

Restrições:
- Se `pagina` ou `tamanho` forem menores que 1, a função deve lançar um `ValueError`.
- Para páginas além do final da lista de itens, a função deve retornar uma lista vazia.

## Acceptance Criteria
- A função deve aceitar uma lista de itens e dois parâmetros inteiros (`pagina`, `tamanho`) e retornar a página correta de itens.
- A função deve lançar `ValueError` se `pagina` ou `tamanho` forem menores que 1.
- A função deve retornar uma lista vazia para páginas além do final da lista de itens.
- A função deve ser implementada no arquivo `paginacao.py`.