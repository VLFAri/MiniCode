# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string like '1h30m15s' into seconds.

## Parameters / Requirements
- **Function Name:** `para_segundos`
- **Input Type:** String
- **Output Type:** Integer representing the total number of seconds
- **Input Format:** The input string should contain a combination of hours (`h`), minutes (`m`), and seconds (`s`). These units must be in the order of hours, minutes, and then seconds, without any spaces between them. For example, valid inputs include `'2h'`, `'90m'`, `'45s'`, and `'1h30m15s'`.
- **Constraints:** The function should handle empty strings and invalid formats by raising a `ValueError`.

## Acceptance Criteria
- The function correctly converts valid duration strings to their equivalent in seconds.
- The function raises a `ValueError` for empty strings or strings with an invalid format.
- The function is tested with various valid and invalid inputs to ensure correctness.

Arquivos do projeto:
(vazio)