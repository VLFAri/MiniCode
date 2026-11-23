# Specification

## Objective
Implementar uma função `achatar` que aceite listas e tuplas aninhadas de qualquer profundidade e retorne uma única lista contendo todos os elementos dessas estruturas, mantendo a ordem original.

## Parameters / Requirements
- A função deve receber como parâmetro uma lista ou tupla qualquer.
- Os elementos da lista/tupla podem ser outros tipos de dados, incluindo outras listas/tuplas.
- Strings devem permanecer como elementos individuais da lista final.
- A função deve ignorar objetos não iteráveis (como dicionários, módulos, etc.).

## Acceptance Criteria
- `achatar([1, [2, 3], 4])` retorna `[1, 2, 3, 4]`
- `achatar(['a', ['b', 'c'], ('d',)])` retorna `['a', 'b', 'c', 'd']`
- `achatar([[1, 2], [3, 4]])` retorna `[1, 2, 3, 4]`
- `achatar(('x', ('y',), ['z']))` retorna `['x', 'y', 'z']`
- `achatar([])` retorna `[]`
- `achatar([None])` retorna `[None]`
- `achatar([True, False])` retorna `[True, False]`
- `achatar([1, [2, [3, [4]]]])` retorna `[1, 2, 3, 4]`
- `achatar([1, [2, [3, [4, [5]]]]])` retorna `[1, 2, 3, 4, 5]`
- `achatar([1, [2, [3, [4, [5, [6]]]]]])` retorna `[1, 2, 3, 4, 5, 6]`
- `achatar([1, [2, [3, [4, [5, [6, [7]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13]]]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14]]]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14, [15]]]]]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14, [15, [16]]]]]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]`
- `achatar([1, [2, [3, [4, [5, [6, [7, [8, [9, [10, [11, [12, [13, [14, [15, [16, [17]]]]]]]]]]]]]]]]])` retorna `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,