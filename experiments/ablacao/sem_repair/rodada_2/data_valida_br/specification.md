# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which returns `True` if the input string is a valid date in the format `dd/mm/yyyy` (with leading zeros, e.g., `05/03/2024`), considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input**: A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output**: A boolean value (`True` or `False`) indicating whether the provided date string is valid according to the specified rules.
- **Constraints**:
  - The day (`dd`) must be between 01 and 31 inclusive.
  - The month (`mm`) must be between 01 and 12 inclusive.
  - The year (`yyyy`) must be between 1900 and 2100 inclusive.
  - The date must adhere to the actual number of days in each month, including leap years for February.
- **Leap Year Rule**: A year is considered a leap year if it is divisible by 4, except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, but 1900 was not.

## Acceptance Criteria
- The function should correctly validate dates within the specified range and format.
- The function should return `True` for valid dates and `False` for invalid dates.
- Test cases should include:
  - Valid dates (e.g., `05/03/2024`, `29/02/2024`)
  - Invalid dates due to incorrect day ranges (e.g., `32/01/2024`, `00/00/2024`)
  - Invalid dates due to incorrect month ranges (e.g., `01/13/2024`, `01/00/2024`)
  - Invalid dates due to incorrect year ranges (e.g., `01/01/1899`, `01/01/2101`)
  - Dates with correct day ranges but incorrect month ranges (e.g., `29/02/2021`, `29/02/2023`)
- The implementation should be able to pass automated tests based on these criteria.

Arquivos do projeto:
(vazio)