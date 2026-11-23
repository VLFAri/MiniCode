# Specification

## Objective
Implementar uma função `paginar` que retorna a página correta de uma lista de itens, considerando um índice baseado em 1 para as páginas.

## Parameters / Requirements
- **itens**: Uma lista de objetos ou valores que serão paginados.
- **pagina**: Um número inteiro representando a página desejada. Deve ser maior ou igual a 1. Valores menores que 1 devem lançar um `ValueError`.
- **tamanho**: Um número inteiro representando o tamanho da página. Deve ser maior ou igual a 1. Valores menores que 1 devem lançar um `ValueError`.

## Acceptance Criteria
- A função deve retornar a página correta com base no índice baseado em 1.
- Se a página ou o tamanho da página for menor que 1, a função deve lançar um `ValueError`.
- Se a página solicitada estiver além do final da lista de itens, a função deve retornar uma lista vazia.

Essa especificação deve guiar a implementação da função `paginar` de forma que atenda aos requisitos e critérios de aceitação mencionados.