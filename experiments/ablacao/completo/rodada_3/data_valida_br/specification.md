# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which evaluates whether the input string `texto` is a valid date in the format `dd/mm/yyyy` (including leading zeros). The function should return `True` if the date is valid, considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input**: A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output**: A boolean value (`True` or `False`) indicating whether the input string represents a valid date.
- **Constraints**:
  - The day (`dd`) must be between 01 and 31.
  - The month (`mm`) must be between 01 and 12.
  - The year (`yyyy`) must be within a reasonable range (e.g., 1900 to 2100).
  - Leap years must be correctly identified and handled.
- **Rules of Business**:
  - February can have 29 days only in leap years.
  - Other months follow standard rules regarding the number of days they contain.

## Acceptance Criteria
- The function `eh_data_valida(texto)` should correctly identify invalid dates such as "30/02/2024" or "31/04/2024".
- The function should handle leap years correctly, meaning "29/02/2024" should return `True`.
- The function should validate dates outside of February with the correct number of days, e.g., "31/01/2024" should return `True`, but "31/04/2024" should return `False`.
- The function should return `False` for any date outside the specified constraints (e.g., "32/01/2024", "00/00/0000").
- The function should be tested with at least 10 different inputs covering all edge cases and typical scenarios.

Arquivos do projeto:
(vazio)