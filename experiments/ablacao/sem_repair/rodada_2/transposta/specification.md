# Specification

## Objective
Implementar uma função `transposta` no arquivo `matriz.py` que recebe uma matriz representada como uma lista de listas e retorna a matriz transposta. A função deve lidar corretamente com matrizes vazias e matrizes onde as linhas têm tamanhos diferentes.

## Parameters / Requirements
- **Entrada**: Uma matriz representada como uma lista de listas de números inteiros ou floats.
- **Saída**: A matriz transposta da entrada original.
- **Restrições**:
  - Se a matriz de entrada for vazia, a função deve retornar uma lista vazia `[]`.
  - Se as linhas da matriz de entrada tiverem tamanhos diferentes, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve retornar a matriz transposta corretamente para matrizes válidas.
- A função deve retornar uma lista vazia `[]` quando a matriz de entrada for vazia.
- A função deve lançar um `ValueError` se as linhas da matriz de entrada tiverem tamanhos diferentes.

Arquivos do projeto:
(vazio)