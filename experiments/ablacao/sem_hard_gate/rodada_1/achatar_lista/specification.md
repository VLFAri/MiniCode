# Specification

## Objective
The primary objective is to create a Python script named `achatar.py` that includes a function `achatar(items)` which accepts nested lists and tuples of any depth and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` will receive a single argument `items`, which can be a nested structure containing lists, tuples, and strings.
- **Output**: The function should return a single-level list containing all elements from the input structure, preserving the order of elements.
- **Constraints**:
  - The input can contain multiple levels of nesting.
  - Strings within the input should not be split or flattened; they should remain as single elements in the output.
  - The function must handle empty inputs gracefully.

## Acceptance Criteria
- The function should correctly flatten any given nested structure into a single-level list.
- The function should preserve the order of elements as they appear in the input.
- The function should not alter or split strings present in the input.
- The function should pass the following automated tests:
  ```python
  assert achatar([1, [2, 3], 4]) == [1, 2, 3, 4]
  assert achatar((1, (2,), [3, [4]])) == [1, 2, 3, 4]
  assert achatar(['a', ['b', 'c'], ('d', 'e')]) == ['a', 'b', 'c', 'd', 'e']
  assert achatar([]) == []
  assert achatar(('a',)) == ['a']
  ```

Arquivos do projeto:
(vazio)