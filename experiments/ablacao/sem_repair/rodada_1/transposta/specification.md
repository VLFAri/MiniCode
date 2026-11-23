# Specification

## Objective
Implementar uma função `transposta` no arquivo `matriz.py` que recebe uma matriz representada como uma lista de listas e retorna a matriz transposta. A função deve lidar corretamente com matrizes vazias e matrizes onde as linhas têm tamanhos diferentes.

## Parameters / Requirements
- **Entrada**: Uma matriz representada como uma lista de listas (`list[list]`).
  - Exemplo de entrada válida: `[[1, 2], [3, 4]]`
  - Exemplo de entrada inválida: `[[1, 2], [3, 4, 5]]` (por causa dos tamanhos diferentes das sublistas)
- **Saída**: A matriz transposta da entrada fornecida.
  - Para uma matriz vazia, a função deve retornar uma lista vazia `[]`.
- **Exceção**: Se as sublistas da entrada não tiverem o mesmo tamanho, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- A função deve retornar a matriz transposta corretamente para entradas válidas.
- A função deve retornar uma lista vazia `[]` quando a entrada for uma lista vazia.
- A função deve lançar uma exceção `ValueError` se as sublistas da entrada não tiverem o mesmo tamanho.

Arquivos do projeto:
(vazio)