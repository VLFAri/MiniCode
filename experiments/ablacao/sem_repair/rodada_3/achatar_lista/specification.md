# Specification

## Objective
The primary objective is to create a Python script named `achatar.py` that includes a function called `achatar(items)` which takes nested lists and tuples of any depth as input and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` accepts a single parameter `items`, which can be a nested structure containing lists and/or tuples. The nesting can be of any depth.
- **Output**: The function should return a single-level list containing all elements from the input structure, maintaining their original order. If the input contains strings, these strings should not be split into individual characters but should remain as single elements in the output list.
- **Types**: The input can be a list or tuple, and it may contain other lists, tuples, or strings. The output must always be a list.
- **Constraints**: The function should handle large inputs efficiently without causing memory issues or excessive processing time.

## Acceptance Criteria
- The function should correctly flatten any given nested list/tuple structure while preserving the order of elements.
- Strings within the input structure should not be split; they should remain as single elements in the output list.
- The function should pass the following automated tests:
  - Test Case 1: Input is `[1, [2, 3], 4]`. Expected Output: `[1, 2, 3, 4]`.
  - Test Case 2: Input is `([1, 2], [3, [4, 5]], 6)`. Expected Output: `[1, 2, 3, 4, 5, 6]`.
  - Test Case 3: Input is `[[[1, 'two'], 3], ['four', 5]]`. Expected Output: `[1, 'two', 3, 'four', 5]`.

Arquivos do projeto:
(vazio)