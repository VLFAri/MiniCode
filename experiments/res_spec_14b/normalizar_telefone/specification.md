# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of either 10 digits (including DDD and a fixed line number of 8 digits) or 11 digits (including DDD and a mobile number starting with 9). Any other format should result in a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number which may contain spaces, parentheses, and hyphens.
- **Output**: A string in the format `+55DDDNUMBER` where `DDD` represents the area code and `NUMBER` represents the remaining digits of the phone number.
- **Constraints**:
  - The input string can start with `+55`.
  - The function should remove any non-digit characters from the input string.
  - The output string must have exactly 12 characters if the phone number includes an area code and a fixed line number, or 13 characters if it includes an area code and a mobile number.
  - The function should raise a `ValueError` if the input does not conform to the expected formats.

## Acceptance Criteria
- The function should correctly normalize phone numbers according to the specified rules.
- The function should handle various formats of input strings, including those with spaces, parentheses, and hyphens.
- The function should validate the normalized phone number to ensure it has the correct number of digits.
- The function should raise a `ValueError` for invalid inputs.
- The function should pass the following tests:
  - `normalizar_telefone('(67) 99999-1234') == '+5567999991234'`
  - `normalizar_telefone('+55 (67) 99999-1234') == '+5567999991234'`
  - `normalizar_telefone('67 99999 1234') == '+5567999991234'`
  - `normalizar_telefone('+5567999991234') == '+5567999991234'`
  - `normalizar_telefone('67999991234') == '+5567999991234'`
  - `normalizar_telefone('+556799999123') raises ValueError`

Arquivos do projeto:
(vazio)