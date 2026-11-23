# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which returns `True` if the input string is a valid date in the format `dd/mm/yyyy` (with leading zeros, e.g., `05/03/2024`), considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input**: A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output**: A boolean value (`True` or `False`) indicating whether the provided date string is valid according to the specified rules.
- **Constraints**:
  - The day (`dd`) must be between 01 and 31 inclusive.
  - The month (`mm`) must be between 01 and 12 inclusive.
  - The year (`yyyy`) must be between 1900 and 2099 inclusive.
  - The date must adhere to the actual number of days in each month, including leap years for February.
- **Leap Year Rule**: A year is considered a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, but 1900 was not.

## Acceptance Criteria
- The function should correctly identify valid dates, including those in February during a leap year.
- The function should return `False` for invalid dates such as February 30th, non-existent months like 13, and invalid days like 32.
- The function should handle edge cases such as the minimum and maximum years within the specified range.
- The function should be tested with a variety of inputs, including valid and invalid dates, to ensure correctness.
- The implementation should be efficient and concise, avoiding unnecessary complexity.

Arquivos do projeto:
(vazio)