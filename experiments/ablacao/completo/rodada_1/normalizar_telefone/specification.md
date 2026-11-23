# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of either 10 digits (including DDD and a fixed line number of 8 digits) or 11 digits (including DDD and a mobile number starting with 9). If the input does not conform to these requirements, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number. This string may contain spaces, parentheses, and hyphens.
- **Output**: A string representing the normalized phone number in the format `+55DDDNUMBER`.
- **Constraints**:
  - The input string can start with `+55`, which should be removed before processing.
  - The output string must be exactly 13 characters long for a mobile number (including the `+55` prefix) or 12 characters long for a fixed-line number (excluding the `+55` prefix).
  - The output string must include the DDD (area code) followed by the phone number.
  - The phone number must be either 10 digits (for fixed lines) or 11 digits (for mobiles starting with 9).

## Acceptance Criteria
- Given an input string `'(67) 99999-1234'`, the function should return `'+5567999991234'`.
- Given an input string `'+55 (67) 99999 1234'`, the function should return `'+5567999991234'`.
- Given an input string `'(67) 999991234'`, the function should return `'+5567999991234'`.
- Given an input string `'(67) 99999123'`, the function should raise a `ValueError`.
- Given an input string `'(67) 9999912345'`, the function should raise a `ValueError`.
- Given an input string `'(67) 99999123456'`, the function should raise a `ValueError`.

Arquivos do projeto:
(vazio)