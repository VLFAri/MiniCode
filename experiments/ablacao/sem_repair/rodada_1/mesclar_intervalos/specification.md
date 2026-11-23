# Specification

## Objective
Implement a Python script named `intervalos.py` that contains a function `mesclar_intervalos(lista)` which takes a list of tuples representing intervals and merges overlapping or adjacent intervals.

## Parameters / Requirements
- **Input**: A list of tuples `(start, end)` where `start` and `end` are integers. The list may be unordered.
- **Output**: A list of merged intervals in ascending order.
- **Constraints**:
  - Each tuple represents an interval `[start, end]`.
  - Intervals can overlap or touch each other.
  - The function should handle empty lists and lists with a single interval correctly.
- **Types**:
  - Input: List[Tuple[int, int]]
  - Output: List[Tuple[int, int]]

## Acceptance Criteria
- The function should return the correct merged intervals for given inputs.
- The output intervals should be sorted in ascending order.
- Test cases should include:
  - Overlapping intervals.
  - Adjacent intervals.
  - Single interval.
  - Empty input list.
- The solution should pass the following tests:
  ```python
  def test_mesclar_intervalos():
      assert mesclar_intervalos([(1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]
      assert mesclar_intervalos([(5, 5), (1, 3), (2, 6), (8, 10)]) == [(1, 6), (8, 10)]
      assert mesclar_intervalos([(1, 4), (4, 5)]) == [(1, 5)]
      assert mesclar_intervalos([]) == []
      assert mesclar_intervalos([(1, 2)]) == [(1, 2)]
  ```

Arquivos do projeto:
(vazio)