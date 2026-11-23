# Specification

## Objective
Implement a Python function named `divide` that takes a list and an integer `n`, divides the list into blocks of size `n` (the last block can be smaller if the list size is not perfectly divisible by `n`), and returns a list of these blocks without altering the original list. If `n` is less than or equal to zero, raise a `ValueError`.

## Parameters / Requirements
- **Input Parameters**:
  - `lista`: A list of any type (e.g., integers, strings).
  - `n`: An integer representing the desired block size.
- **Constraints**:
  - The input list must not be modified.
  - If `n <= 0`, the function should raise a `ValueError`.
- **Behavioral Requirements**:
  - The function should return a list of lists where each sublist represents a block of the original list.
  - Each block should have exactly `n` elements, except possibly the last one which may contain fewer elements if the total number of elements in the original list is not perfectly divisible by `n`.

## Acceptance Criteria
- The function should correctly divide the list into blocks of size `n`.
- The function should handle cases where `n` is less than or equal to zero by raising a `ValueError`.
- The function should not modify the original list.
- The function should pass the following tests:
  ```python
  def test_divide():
      assert divide([1, 2, 3, 4, 5], 2) == [[1, 2], [3, 4], [5]]
      assert divide(['a', 'b', 'c', 'd', 'e'], 3) == [['a', 'b', 'c'], ['d', 'e']]
      assert divide([], 5) == []
      try:
          divide([1, 2, 3], 0)
      except ValueError:
          pass
      else:
          assert False, "Expected ValueError"
  ```

Arquivos do projeto:
(vazio)