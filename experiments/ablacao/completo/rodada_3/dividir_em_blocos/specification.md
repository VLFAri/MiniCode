# Specification

## Objective
Implement a Python function named `divide` that takes a list and an integer `n`, divides the list into blocks of size `n` (the last block can be smaller if the list size is not perfectly divisible by `n`), and returns a list of these blocks without altering the original list. If `n` is less than or equal to zero, raise a `ValueError`.

## Parameters / Requirements
- **Input Parameters**:
  - `lista`: A list of any type (e.g., integers, strings).
  - `n`: An integer representing the desired block size.
- **Constraints**:
  - The input list must not be modified.
  - The value of `n` must be greater than zero; otherwise, a `ValueError` should be raised.
- **Behavioral Requirements**:
  - The function should return a list of lists where each sublist represents a block of the original list with a maximum size of `n`.
  - If the last block is smaller than `n`, it should still be included in the returned list.

## Acceptance Criteria
- The function should handle empty lists correctly, returning an empty list of lists.
- The function should raise a `ValueError` when `n` is less than or equal to zero.
- The function should preserve the order of elements from the original list in the output list of blocks.
- The function should work with lists containing any type of elements.
- Test cases should include scenarios with different types of elements in the list, including empty lists, lists with a single element, and lists where the length is not perfectly divisible by `n`.

Arquivos do projeto:
(vazio)