# Specification

## Objective
The objective is to create a Python script named `achatar.py` that includes a function called `achatar(items)` which takes nested lists and tuples of any depth as input and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` accepts a single parameter `items`, which can be a nested structure containing lists, tuples, and strings. The nesting can be of any depth.
- **Output**: The function should return a single-level list containing all elements from the input structure, maintaining their original order. If the input contains strings, these should not be split into individual characters but treated as single elements.
- **Types**: The input can be a list or tuple, and it may contain other lists, tuples, and strings. The output must always be a list.
- **Constraints**: The function should handle large inputs efficiently without causing memory issues or excessive processing time.

## Acceptance Criteria
- The function should correctly flatten any given nested list or tuple structure while keeping strings intact.
- The function should maintain the order of elements as they appear in the input structure.
- The function should pass the following tests:
  - Test 1: Input `[1, [2, 3], 4]` should result in `[1, 2, 3, 4]`.
  - Test 2: Input `([1, 2], [3, 4])` should result in `[1, 2, 3, 4]`.
  - Test 3: Input `[[[1]], 2]` should result in `[1, 2]`.
  - Test 4: Input `[1, 'abc', [2, 3]]` should result in `[1, 'abc', 2, 3]`.
  - Test 5: Input `[1, ('a', 'b'), 2]` should result in `[1, 'a', 'b', 2]`.

Arquivos do projeto:
(vazio)