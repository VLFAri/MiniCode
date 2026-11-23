# Specification

## Objective
Implement a Python script named `intervalos.py` that includes a function `mesclar_intervalos(lista)` which takes a list of tuples representing intervals and merges overlapping or adjacent intervals.

## Parameters / Requirements
- **Input**: A list of tuples `(start, end)` where `start` and `end` are integers. The list may be unordered and can contain up to 1000 intervals.
- **Output**: A list of merged intervals in ascending order.
- **Constraints**:
  - Each interval is represented as a tuple `(start, end)` where `start <= end`.
  - Intervals can overlap or touch each other.
  - The function should handle edge cases such as empty lists or lists with only one interval.
  
## Acceptance Criteria
- The function should correctly merge all overlapping or adjacent intervals.
- The output intervals should be sorted in ascending order based on the start value.
- The function should pass the following test cases:
  ```python
  assert mesclar_intervalos([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]
  assert mesclar_intervalos([(1, 4), (4, 5)]) == [(1, 5)]
  assert mesclar_intervalos([]) == []
  assert mesclar_intervalos([(5, 5)]) == [(5, 5)]
  ```

Arquivos do projeto:
(vazio)