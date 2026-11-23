# Specification

## Objective
Implement a Python script named `intervalos.py` that contains a function `mesclar_intervalos(lista)` which takes an unordered list of tuples representing intervals and returns a sorted list of merged intervals.

## Parameters / Requirements
- **Input**: A list of tuples where each tuple represents an interval with two integer values `(start, end)`. The input list can be unordered and may contain overlapping or adjacent intervals.
- **Output**: A sorted list of tuples representing the merged intervals. The output should be ordered based on the start value of each interval.
- **Constraints**:
  - Each interval is represented as a tuple `(start, end)` where `start <= end`.
  - Intervals can overlap or touch at their endpoints.
  - The function should handle empty lists gracefully.
- **Rules**:
  - If intervals overlap or touch, they should be merged into a single interval.
  - The resulting list must be sorted in ascending order based on the start value of each interval.

## Acceptance Criteria
- The function `mesclar_intervalos(lista)` should correctly merge overlapping or adjacent intervals from the input list.
- The function should return a list of tuples where each tuple represents a merged interval.
- The returned list should be sorted in ascending order based on the start value of each interval.
- Test cases should include:
  - Overlapping intervals.
  - Adjacent intervals.
  - Non-overlapping and non-adjacent intervals.
  - Empty input list.
- The implementation should pass all unit tests designed to verify these criteria.

Arquivos do projeto:
(vazio)