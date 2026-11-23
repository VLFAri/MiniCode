# Specification

## Objective
Implement a Python function named `divide` that takes a list and an integer `n`, divides the list into blocks of size `n` (the last block can be smaller if the list size is not perfectly divisible by `n`), and returns a list of these blocks without altering the original list. If `n` is less than or equal to zero, raise a `ValueError`.

## Parameters / Requirements
- **Input Parameters**:
  - `lista`: A list of any type (e.g., integers, strings).
  - `n`: An integer representing the desired block size.
- **Output**:
  - A list of lists where each sublist represents a block of the original list with size `n` (except possibly the last one).
- **Constraints**:
  - The input `lista` must be a valid Python list.
  - The input `n` must be an integer.
  - If `n <= 0`, the function should raise a `ValueError`.
- **Business Rules**:
  - The function should preserve the order of elements from the original list in the output blocks.
  - The original list should remain unchanged after the function execution.

## Acceptance Criteria
- The function should correctly divide the list into blocks of size `n` and return them as a list of lists.
- The function should raise a `ValueError` if `n` is less than or equal to zero.
- The function should not modify the original list.
- The function should handle edge cases such as empty lists and very small lists appropriately.
- Test cases should include scenarios with different types of elements in the list, positive and negative values for `n`, and edge cases like empty lists and lists with sizes not perfectly divisible by `n`.