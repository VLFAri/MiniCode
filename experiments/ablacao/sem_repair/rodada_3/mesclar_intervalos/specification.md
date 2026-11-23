# Specification

## Objective
Implement a Python script named `intervalos.py` that includes a function `mesclar_intervalos(lista)` which takes a list of tuples representing intervals and merges overlapping or adjacent intervals.

## Parameters / Requirements
- **Input**: A list of tuples `(start, end)` where `start` and `end` are integers. The input list may be unordered.
- **Output**: A list of merged intervals in ascending order.
- **Constraints**:
  - Each tuple represents an interval `[start, end]`.
  - Intervals can overlap or touch each other.
  - The output should contain the minimum number of non-overlapping intervals covering all input intervals.
- **Types**:
  - Input: List[Tuple[int, int]]
  - Output: List[Tuple[int, int]]

## Acceptance Criteria
- The function should correctly merge intervals as described in the requirements.
- The function should handle edge cases such as empty lists, single-element lists, and lists with no overlapping intervals.
- The function should be tested with automated tests to ensure it meets the acceptance criteria.
- Example test cases:
  - Input: `[(1, 3), (2, 6), (8, 10)]`
    - Expected Output: `[(1, 6), (8, 10)]`
  - Input: `[(1, 4), (4, 5)]`
    - Expected Output: `[(1, 5)]`
  - Input: `[]`
    - Expected Output: `[]`

Arquivos do projeto:
(vazio)