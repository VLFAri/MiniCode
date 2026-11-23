# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string into seconds.

## Parameters / Requirements
- **Input**: A string representing a duration in the format of hours ('h'), minutes ('m'), and seconds ('s') in that order without spaces. The input can be empty or invalid.
- **Output**: An integer representing the total number of seconds corresponding to the input duration.
- **Exceptions**:
  - If the input is an empty string or does not follow the specified format, raise a `ValueError`.

## Acceptance Criteria
- The function should correctly parse strings like '1h30m15s' and return the equivalent duration in seconds.
- The function must handle valid combinations of hours, minutes, and seconds.
- The function should raise a `ValueError` for empty strings or strings that do not conform to the expected format.
- Test cases should include valid inputs, empty strings, and invalid formats to ensure the function behaves as expected.

Arquivos do projeto:
(vazio)