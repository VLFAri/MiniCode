# Specification

## Objective
Implement a Python script named `datas_br.py` that includes a function `eh_data_valida(texto)` which evaluates whether the input string `texto` represents a valid date in the format `dd/mm/yyyy` (with leading zeros if necessary). The function should return `True` if the date is valid considering leap years, and `False` otherwise.

## Parameters / Requirements
- **Input:** A single string `texto` representing a date in the format `dd/mm/yyyy`.
- **Output:** A boolean value (`True` or `False`) indicating whether the provided date is valid.
- **Constraints:**
  - The day (`dd`) must be between 01 and 31 inclusive.
  - The month (`mm`) must be between 01 and 12 inclusive.
  - The year (`yyyy`) must be between 1900 and 2099 inclusive.
  - Leading zeros are allowed and required for days and months less than 10.
  - Leap years must be correctly identified and handled according to the Gregorian calendar rules.
- **Rules of Business:**
  - February can have 29 days only in leap years.
  - Other months follow standard day counts with no exceptions.

## Acceptance Criteria
- The function `eh_data_valida(texto)` should pass the following tests:
  - `eh_data_valida("01/01/2023") == True`
  - `eh_data_valida("31/12/2023") == True`
  - `eh_data_valida("29/02/2020") == True`
  - `eh_data_valida("29/02/2021") == False`
  - `eh_data_valida("30/04/2023") == True`
  - `eh_data_valida("31/04/2023") == False`
  - `eh_data_valida("01/13/2023") == False`
  - `eh_data_valida("00/01/2023") == False`
  - `eh_data_valida("01/01/1899") == False`
  - `eh_data_valida("01/01/2100") == False`

Arquivos do projeto:
(vazio)