# Specification

## Objective
Implement a Python function named `divide` that takes a list and an integer `n`, divides the list into blocks of size `n` (the last block can be smaller if the list size is not perfectly divisible by `n`), and returns a list of these blocks without altering the original list. If `n` is less than or equal to zero, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input Parameters**:
  - `lista`: A list of any type (e.g., integers, strings).
  - `n`: An integer representing the desired block size.
- **Output**:
  - A list of lists where each sublist represents a block of the original list with size `n` (except possibly the last one which may be smaller).
- **Constraints**:
  - The input list can contain up to 10^6 elements.
  - The value of `n` must be a positive integer greater than zero; otherwise, a `ValueError` should be raised.

## Acceptance Criteria
- The function should correctly divide the input list into blocks of size `n`.
- The function should return a list of lists where each sublist contains exactly `n` elements from the original list, except possibly the last sublist which may contain fewer elements.
- If `n` is less than or equal to zero, the function should raise a `ValueError`.
- The original list should remain unchanged after the function executes.
- The function should handle edge cases such as empty lists and very large lists efficiently.
- Test cases should include scenarios with different types of elements in the list, varying sizes of `n`, and edge cases like empty lists and lists where the length is not perfectly divisible by `n`.