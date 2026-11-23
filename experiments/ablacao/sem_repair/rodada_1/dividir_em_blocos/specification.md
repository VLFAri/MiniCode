# Specification

## Objective
Implement a Python function named `divide` that takes a list and an integer `n`, divides the list into blocks of size `n` (the last block can be smaller if the list size is not perfectly divisible by `n`), and returns a list of these blocks without altering the original list. If `n` is less than or equal to zero, raise a `ValueError`.

## Parameters / Requirements
- **Input Parameters**:
  - `lista`: A list of any type (e.g., integers, strings).
  - `n`: An integer representing the desired block size.
- **Constraints**:
  - The input list must not be modified.
  - `n` must be a positive integer; otherwise, a `ValueError` should be raised.
- **Behavioral Requirements**:
  - The function should handle empty lists gracefully.
  - The function should return a list of lists where each sublist represents a block of the original list.
  - If `n` is greater than the length of the list, the function should return a single block containing the entire list.

## Acceptance Criteria
- The function should correctly divide the list into blocks of size `n`.
- The function should raise a `ValueError` if `n` is less than or equal to zero.
- The function should pass the following tests:
  ```python
  def test_divide():
      assert divide([], 2) == []
      assert divide([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
      assert divide([1, 2, 3, 4, 5, 6], 3) == [[1, 2, 3], [4, 5, 6]]
      assert divide([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]
      try:
          divide([1, 2, 3], 0)
          assert False, "Expected ValueError"
      except ValueError:
          pass
  ```

Arquivos do projeto:
(vazio)