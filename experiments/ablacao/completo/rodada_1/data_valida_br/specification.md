# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which returns `True` if the input string is a valid date in the format `dd/mm/yyyy` (with leading zeros, e.g., `05/03/2024`), considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input**: A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output**: A boolean value (`True` or `False`) indicating whether the provided date is valid according to the specified rules.
- **Constraints**:
  - The day (`dd`) must be between 01 and 31.
  - The month (`mm`) must be between 01 and 12.
  - The year (`yyyy`) must be within a reasonable range (e.g., 1900 to 2100).
  - Leap years should be correctly identified and handled.
- **Rules of Business**:
  - February can have 29 days only in leap years.
  - Other months should have the correct number of days based on their month number.

## Acceptance Criteria
- The function `eh_data_valida(texto)` should return `True` for valid dates and `False` for invalid ones.
- Test cases should cover all possible scenarios including edge cases such as leap years, maximum and minimum days per month, and out-of-range values.
- The implementation should be efficient and handle large inputs without performance degradation.
- The code should be well-documented with clear comments explaining each part of the logic.

Arquivos do projeto:
(vazio)