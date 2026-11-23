# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string like '1h30m15s' into seconds.

## Parameters / Requirements
- **Function Name:** `para_segundos`
- **Input Type:** String
- **Output Type:** Integer representing the total number of seconds
- **Input Format:** The input string should contain a combination of hours (`h`), minutes (`m`), and seconds (`s`). The format must follow these rules:
  - Hours, minutes, and seconds can be included in any order but must be specified in the order `h`, `m`, `s`.
  - Each unit is represented by a single character followed by a digit or digits (e.g., `1h`, `2m`, `3s`).
  - There should be no spaces between characters.
  - The function should handle empty strings and invalid formats by raising a `ValueError`.

## Acceptance Criteria
- The function correctly converts valid duration strings to their equivalent in seconds.
- The function raises a `ValueError` for empty strings or strings with an invalid format.
- Test cases should include valid inputs, empty strings, and invalid inputs to ensure the function behaves as expected.

Arquivos do projeto:
(vazio)