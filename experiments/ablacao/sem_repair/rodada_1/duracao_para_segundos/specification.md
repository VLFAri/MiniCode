# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string like '1h30m15s' into seconds.

## Parameters / Requirements
- **Function Name:** `para_segundos`
- **Input Type:** String
- **Output Type:** Integer representing the total number of seconds
- **Input Format:** The input string should contain a combination of hours (`h`), minutes (`m`), and seconds (`s`). The format must follow these rules:
  - Hours, minutes, and seconds can be included in any order, but each unit must be specified only once.
  - Each unit is represented by a single character followed by a letter indicating the unit type (`h`, `m`, or `s`).
  - There should be no spaces between numbers and their corresponding units.
  - Examples of valid inputs include `'1h30m15s'`, `'2h'`, `'90m'`, `'45s'`.
- **Constraints:**
  - The function should handle large numbers of seconds without losing precision.
  - The function should raise a `ValueError` if the input string is empty or does not conform to the expected format.

## Acceptance Criteria
- The function correctly converts strings with hours, minutes, and seconds into the equivalent number of seconds.
- The function raises a `ValueError` for invalid input formats, including empty strings.
- The function passes the following tests:
  ```python
  assert para_segundos('') == ValueError
  assert para_segundos('1h') == 3600
  assert para_segundos('1m') == 60
  assert para_segundos('1s') == 1
  assert para_segundos('2h30m') == 9000
  assert para_segundos('45m30s') == 2730
  assert para_segundos('1h2m3s') == 4323
  ```

Arquivos do projeto:
(vazio)