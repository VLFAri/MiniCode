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
  - The function should return a list of lists, where each sublist represents a block of the original list.
  - If the last block does not reach the size `n`, it should still be included in the returned list.

## Acceptance Criteria
- The function should correctly divide the input list into blocks of size `n`.
- The original list should remain unchanged after the function execution.
- If `n <= 0`, the function should raise a `ValueError`.
- The function should handle empty lists gracefully, returning an empty list of lists.
- Test cases should include scenarios with different types of elements in the list, varying sizes of `n`, and edge cases like `n = 1` and `n > len(list)`.

Arquivos do projeto:
(vazio)