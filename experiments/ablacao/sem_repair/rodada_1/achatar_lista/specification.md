# Specification

## Objective
The primary objective is to create a Python script named `achatar.py` that includes a function `achatar(items)` which accepts nested lists and tuples of any depth and returns a flattened list containing all elements in the order they appear. The function should not flatten strings, meaning strings should remain as single elements in the output.

## Parameters / Requirements
- **Input**: The function `achatar(items)` will receive a single argument `items`, which can be a list or tuple containing nested lists and/or tuples. The nesting can be of any depth.
- **Output**: The function should return a single-level list containing all elements from the input structure, maintaining their original order. If the input contains strings, these should not be split but treated as individual elements.
- **Types**: The input can be either a list or a tuple. Elements within these structures can be of any type, including other lists or tuples.
- **Constraints**: The solution must handle arbitrarily deep nesting without performance degradation.
- **Business Rules**: Strings should not be split into individual characters; they should be treated as single elements.

## Acceptance Criteria
- The function `achatar(items)` should correctly flatten any given nested list or tuple while preserving the order of elements.
- The function should not alter strings, treating them as single elements.
- The solution should pass the following automated tests:
  - Test Case 1: Input is `[1, [2, 3], 4]`. Expected Output: `[1, 2, 3, 4]`.
  - Test Case 2: Input is `([1, 2], [3, [4, 5]], 6)`. Expected Output: `[1, 2, 3, 4, 5, 6]`.
  - Test Case 3: Input is `[[[1], 2], 3]`. Expected Output: `[1, 2, 3]`.
  - Test Case 4: Input is `['abc', ['def'], 'ghi']`. Expected Output: `['abc', 'def', 'ghi']`.

Arquivos do projeto:
(vazio)