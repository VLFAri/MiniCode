# Specification

## Objective
Implement a Python function `para_segundos` that converts a duration string like '1h30m15s' into seconds.

## Parameters / Requirements
- **Function Name:** `para_segundos`
- **Input Type:** String
- **Output Type:** Integer representing the total number of seconds
- **Valid Input Format:** The input string should contain any combination of hours (`h`), minutes (`m`), and seconds (`s`). These units must be in the order of hours, minutes, and then seconds, without spaces between them. For example, valid inputs include '2h', '90m', '45s', and '1h30m15s'.
- **Invalid Inputs:** Any string that does not conform to the above format should raise a `ValueError`.

## Acceptance Criteria
- The function correctly converts strings with hours, minutes, and seconds into their equivalent in seconds.
- The function raises a `ValueError` for empty strings or strings that do not follow the specified format.
- Test cases should cover various scenarios including valid durations, invalid formats, and edge cases such as single unit durations and empty strings.

Arquivos do projeto:
(vazio)