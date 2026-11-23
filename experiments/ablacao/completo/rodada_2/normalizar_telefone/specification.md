# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of exactly 10 digits (including DDD and a fixed line number of 8 digits) or 11 digits (including DDD and a mobile number starting with 9). If the input does not conform to these requirements, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number. This string may contain spaces, parentheses, and hyphens.
- **Output**: A string in the format `+55DDDNUMBER`, where `DDD` represents the area code and `NUMBER` represents the phone number.
- **Constraints**:
  - The input string can start with `+55`.
  - The function should remove any leading `+55` from the input string before processing.
  - The function should handle various separators such as spaces, parentheses, and hyphens.
  - The output must be exactly 13 characters long for valid inputs.
  - Valid phone numbers must have either 10 digits (fixed lines) or 11 digits (mobiles).
  - Mobile numbers must start with the digit `9`.
  - Invalid inputs should result in a `ValueError` being raised.

## Acceptance Criteria
- Given a valid Brazilian phone number with spaces, parentheses, or hyphens, the function should return the number in the format `+55DDDNUMBER`.
- Given an invalid input (e.g., too many or too few digits), the function should raise a `ValueError`.
- The function should correctly handle inputs starting with `+55` by removing this prefix before validation.
- The function should pass the following tests:
  - Input: `'67999991234'` -> Output: `'+5567999991234'`
  - Input: `'(67) 99999-1234'` -> Output: `'+5567999991234'`
  - Input: `'999991234'` -> Raises: `ValueError`
  - Input: `'+5567999991234'` -> Output: `'+5567999991234'`

Arquivos do projeto:
(vazio)