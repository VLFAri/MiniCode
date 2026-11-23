# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string like '1h30m15s' into seconds.

## Parameters / Requirements
- **Function Name:** `para_segundos`
- **Input Type:** String
- **Output Type:** Integer representing the total number of seconds
- **Valid Input Format:** The input string should contain any combination of hours (h), minutes (m), and seconds (s) in that order without spaces. Examples include '2h', '90m', '45s', and '1h30m15s'.
- **Invalid Input Handling:** If the input string is empty or does not conform to the specified format, the function should raise a `ValueError`.

## Acceptance Criteria
- The function correctly converts valid input strings into their equivalent total seconds.
- The function raises a `ValueError` for empty strings or strings that do not follow the specified format.
- The implementation includes clear comments and follows PEP8 guidelines for code style.
- Unit tests are provided to verify the correctness of the function under various scenarios including edge cases.

Arquivos do projeto:
(vazio)