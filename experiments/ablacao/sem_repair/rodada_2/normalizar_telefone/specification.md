# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of exactly 10 digits (including DDD and fixed line number) or 11 digits (including DDD and mobile number starting with 9). If the input does not conform to these requirements, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number. This string may contain spaces, parentheses, and hyphens.
- **Output**: A string representing the normalized phone number in the international format `+55DDDNUMBER`.
- **Constraints**:
  - The input string can start with `+55`, which should be removed before processing.
  - The output string must have exactly 10 digits for fixed lines or 11 digits for mobile numbers.
  - Mobile numbers must start with the digit `9`.
  - Fixed lines will have 8 digits after the DDD.
- **Types**:
  - Input: `str`
  - Output: `str`

## Acceptance Criteria
- Given an input string `'(67) 99999-1234'`, the function should return `'+5567999991234'`.
- Given an input string `'99999-1234'`, the function should return `'+55999991234'`.
- Given an input string `'+55 (67) 99999-1234'`, the function should return `'+5567999991234'`.
- Given an invalid input string `'(67) 99999-123'`, the function should raise a `ValueError`.
- Given an invalid input string `'(67) 999991234'`, the function should raise a `ValueError`.

Arquivos do projeto:
(vazio)