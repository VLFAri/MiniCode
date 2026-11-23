# Specification

## Objective
The primary objective is to create a Python script named `achatar.py` that includes a function `achatar(items)` which accepts nested lists and tuples of any depth and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` will receive a single argument `items`, which can be a nested structure containing lists, tuples, and strings.
- **Output**: The function should return a single-level list containing all elements from the input structure, maintaining their original order. If the input contains strings, these should not be split into individual characters but rather treated as single elements.
- **Types**: The input can be a list or tuple, and it may contain other lists, tuples, and strings. The output must always be a list.
- **Constraints**: The function should handle structures of arbitrary depth and size efficiently without causing memory issues or performance degradation.

## Acceptance Criteria
- The function should correctly flatten nested lists and tuples while preserving the order of elements.
- Strings within the input structure should not be split; they should be included as single elements in the output list.
- The function should pass the following automated tests:
  - Test Case 1: Input is `[1, 2, [3, 4], (5, 6)]`. Expected Output: `[1, 2, 3, 4, 5, 6]`.
  - Test Case 2: Input is `[(1, 2), [3, 4], 5]`. Expected Output: `[1, 2, 3, 4, 5]`.
  - Test Case 3: Input is `['abc', [1, 2], (3, 4)]`. Expected Output: `['abc', 1, 2, 3, 4]`.
  - Test Case 4: Input is `[[[1]], 2, ('a', 'b')]`. Expected Output: `[1, 2, 'a', 'b']`.

Arquivos do projeto:
(vazio)