# Specification

## Objective
Implementar uma função `transposta(m)` no arquivo `matriz.py` que recebe uma matriz representada como uma lista de listas e retorna a matriz transposta. A função deve lidar corretamente com matrizes vazias e matrizes onde as linhas têm tamanhos diferentes.

## Parameters / Requirements
- **Entrada**: Uma matriz `m` representada como uma lista de listas.
  - Exemplo de entrada válida: `[[1, 2], [3, 4]]`
  - Exemplo de entrada inválida: `[[1, 2], [3, 4, 5]]` (por causa dos tamanhos diferentes das linhas)
- **Saída**: A matriz transposta da entrada original.
  - Para uma matriz vazia, a função deve retornar `[]`.
- **Restrições**:
  - Se as linhas da matriz tiverem tamanhos diferentes, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve retornar a matriz transposta corretamente para entradas válidas.
- A função deve retornar `[]` quando a entrada for uma matriz vazia.
- A função deve lançar um `ValueError` se as linhas da matriz tiverem tamanhos diferentes.

Arquivos do projeto:
(vazio)