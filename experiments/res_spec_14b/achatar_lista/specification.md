# Specification

## Objective
The objective is to create a Python script named `achatar.py` that includes a function called `achatar(items)` which accepts nested lists and tuples of any depth and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` will receive a single parameter `items`, which can be a nested structure containing lists, tuples, and strings.
  - The input can contain multiple levels of nesting.
  - The input may include strings, which should not be split or flattened.
- **Output**: A single-level list containing all elements from the input structure, maintaining the original order.
- **Constraints**:
  - The function must handle arbitrarily deep nesting.
  - The function should preserve the order of elements as they appear in the input structure.
  - Strings within the input should be treated as atomic elements and not split into individual characters.

## Acceptance Criteria
- The function `achatar(items)` should return a correctly flattened list when given a nested structure as input.
- The function should pass the following tests:
  - `assert achatar([1, 2, [3, 4], 5]) == [1, 2, 3, 4, 5]`
  - `assert achatar([(1, 2), [3, [4, 5]]]) == [1, 2, 3, 4, 5]`
  - `assert achatar(['abc', ['d', 'e'], 'f']) == ['abc', 'd', 'e', 'f']`
  - `assert achatar([[], [], []]) == []`
  - `assert achatar([1, [2, [3, [4, [5]]]]]) == [1, 2, 3, 4, 5]`

Arquivos do projeto:
(vazio)