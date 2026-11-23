# Specification

## Objective
The objective is to create a Python script named `achatar.py` that includes a function called `achatar(items)` which takes nested lists and tuples of any depth as input and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` accepts a single parameter `items`, which can be a nested structure containing lists, tuples, and strings.
  - The nesting can go to any depth.
  - The input must be valid Python data structures.
- **Output**: A single flat list where all elements from the input structure are included in the order they appear, except for strings which should not be split into individual characters.
- **Constraints**:
  - The function should handle large inputs efficiently.
  - The function should preserve the order of elements as they appear in the input structure.
  - The function should not modify the original input structure.

## Acceptance Criteria
- The function `achatar(items)` should pass the following tests:
  - Test Case 1: Input is `[1, [2, 3], 4]`. Expected Output: `[1, 2, 3, 4]`.
  - Test Case 2: Input is `([1, 2], 3, ('a', 'b'))`. Expected Output: `[1, 2, 3, 'a', 'b']`.
  - Test Case 3: Input is `[[[1]], 2]`. Expected Output: `[1, 2]`.
  - Test Case 4: Input is `['abc', [1, 2]]`. Expected Output: `['abc', 1, 2]`.
  - Test Case 5: Input is `[(1, 2), ['a', 'b']]`. Expected Output: `[1, 2, 'a', 'b']`.

Arquivos do projeto:
(vazio)