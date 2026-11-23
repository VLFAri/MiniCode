# Specification

## Objective
Implement a Python script named `intervalos.py` that includes a function `mesclar_intervalos(lista)` which takes an unordered list of tuples representing intervals and returns a sorted list of merged intervals.

## Parameters / Requirements
- **Input**: A list of tuples where each tuple represents an interval with two integers `(start, end)`. The input list can be unordered and may contain overlapping or adjacent intervals.
- **Output**: A sorted list of tuples representing the merged intervals. The output should be ordered based on the start value of each interval.
- **Constraints**:
  - Each interval is represented as a tuple `(start, end)` where `start <= end`.
  - Intervals can overlap or touch at their endpoints.
  - The function should handle empty lists gracefully.
- **Rules**:
  - If intervals overlap or touch, they should be merged into a single interval.
  - The resulting list must be sorted in ascending order by the start value of each interval.

## Acceptance Criteria
- The function `mesclar_intervalos(lista)` should correctly merge overlapping or adjacent intervals from the input list.
- The function should return a sorted list of tuples representing the merged intervals.
- Test cases should include:
  - Overlapping intervals.
  - Adjacent intervals.
  - Non-overlapping and non-adjacent intervals.
  - Empty input list.
- All tests should pass without errors or exceptions.

Arquivos do projeto:
(vazio)