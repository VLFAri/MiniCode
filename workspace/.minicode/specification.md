# Specification

## Objective
Implement a Python script that uses the QuickSort algorithm to sort three different lists.

## Parameters / Requirements
The implementation should include two files:
1. `quick_sort.py`: This file will contain the QuickSort algorithm and a function to sort the provided lists.
2. `tests/test_quick_sort.py`: This file will contain unit tests to verify the correctness of the sorting function.

### quick_sort.py
- The script must define a function named `quick_sort` which takes a single argument: a list of integers.
- The function should return the sorted list in ascending order.
- The script should be able to handle three predefined lists stored in variables.

### tests/test_quick_sort.py
- The tests should validate the functionality of the `quick_sort` function.
- Each test case should use one of the predefined lists from `quick_sort.py`.

## Acceptance Criteria
The following criteria must be met for the solution to be considered acceptable:
- The `quick_sort` function correctly sorts each of the three lists.
- The sorting is done using the QuickSort algorithm.
- Unit tests in `tests/test_quick_sort.py` pass without any errors or failures.
- The code is well-documented with comments explaining the purpose of the function and how it works.
- The solution is efficient and handles edge cases such as empty lists or lists with duplicate values.