# Specification

## Objective
Implementar uma função `dividir` que divide uma lista em blocos de tamanho específico (`n`) e retorna uma lista contendo esses blocos.

## Parameters / Requirements
- A função `dividir` recebe dois parâmetros: uma lista (`lista`) e um número inteiro positivo (`n`).
- Se `n` for menor ou igual a zero, a função deve lançar uma exceção `ValueError`.
- A função deve dividir a lista original em blocos de tamanho `n`, mantendo a ordem dos elementos no processo.
- O último bloco pode ter menos elementos do que o tamanho `n`, mas não mais que o comprimento da lista original.
- A função deve retornar uma nova lista contendo os blocos divididos.

## Acceptance Criteria
- `dividir([1, 2, 3, 4], 2)` retorna `[ [1, 2], [3, 4] ]`
- `dividir(['a', 'b', 'c'], 1)` retorna `[ ['a'], ['b'], ['c'] ]`
- `dividir([], 3)` retorna `[]`
- `dividir([10], 5)` retorna `[ [10] ]`
- `dividir([1, 2, 3, 4, 5], 0)` lança `ValueError("n must be positive")`
- `dividir([1, 2, 3, 4, 5], -1)` lança `ValueError("n must be positive")`
- `dividir([1, 2, 3, 4, 5], 6)` lança `ValueError("n must be less than or equal to the length of the list")`