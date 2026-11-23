# Specification

## Objective
O objetivo deste bloco é criar uma função `dividir` no arquivo `blocos.py`, que recebe duas entradas: uma lista e um número `n`. A função deve dividir a lista em blocos de tamanho `n` e retornar uma nova lista contendo esses blocos, mantendo a ordem original da lista original.

## Parameters / Requirements
- **Entrada 1**: Uma lista qualquer (lista).
- **Entrada 2**: Um número inteiro positivo (`n`) que representa o tamanho dos blocos.
- **Restrições**:
  - `n` deve ser maior que zero.
  - Se `n` for igual ou menor que zero, deve lançar um `ValueError`.
- **Regras de negócio**:
  - O último bloco pode ter menos elementos do que o primeiro bloco se `n` não for divisível pelo tamanho da lista.
  - Os blocos devem ser exatamente de tamanho `n`.

## Acceptance Criteria
Os seguintes critérios devem ser atendidos para considerar a especificação concluída:

1. A função `dividir` deve funcionar corretamente para listas vazias e com apenas um elemento.
2. A função deve dividir a lista em blocos de tamanho `n` e retornar a lista de blocos, mantendo a ordem original da lista original.
3. Se `n` for menor ou igual a zero, a função deve lançar um `ValueError`.
4. Os blocos devem ser exatamente de tamanho `n`.

## Arquivos do projeto
(vazio)

Pedido do utilizador: Crie blocos.py com a função dividir(lista, n) que divida a lista em blocos de tamanho n (o último pode ser menor) e devolva a lista de blocos, sem alterar a lista original. Se n for menor ou igual a zero, lance ValueError.