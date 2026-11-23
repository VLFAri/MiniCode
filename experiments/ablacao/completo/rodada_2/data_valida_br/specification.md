# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which returns `True` if the input string is a valid date in the format `dd/mm/yyyy` (with leading zeros, e.g., `05/03/2024`), considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input**: A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output**: A boolean value (`True` or `False`) indicating whether the provided date is valid according to the specified rules.
- **Constraints**:
  - The day (`dd`) must be between 01 and 31 inclusive.
  - The month (`mm`) must be between 01 and 12 inclusive.
  - The year (`yyyy`) must be between 1900 and 2099 inclusive.
  - The date must adhere to the actual number of days in each month, including leap years for February.
- **Leap Year Rule**: A year is considered a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, but 1900 was not.

## Acceptance Criteria
- The function should correctly validate dates within the specified range and format.
- The function should return `True` for valid dates such as `05/03/2024`, `28/02/2024`, and `29/02/2024`.
- The function should return `False` for invalid dates such as `30/02/2024`, `31/04/2024`, and `00/00/0000`.
- The function should handle edge cases like `01/01/1900` and `31/12/2099` correctly.
- The function should be tested with at least 10 different valid and invalid date strings to ensure correctness.
- The code should be well-documented and include comments explaining the logic used for validation.

Arquivos do projeto:
(vazio)