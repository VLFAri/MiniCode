# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of either 10 digits (including DDD and a fixed line number of 8 digits) or 11 digits (including DDD and a mobile number starting with 9). If the input does not conform to these requirements, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number.
- **Output**: A string representing the normalized phone number in the international format `+55DDDNUMBER`.
- **Constraints**:
  - The input string may contain spaces, parentheses, and hyphens.
  - If the input starts with `+55`, this prefix should be removed before processing.
  - The output must be exactly 13 characters long for valid inputs.
  - Valid phone numbers must have either 10 digits (fixed line) or 11 digits (mobile).
  - Mobile numbers start with the digit `9`.
  - Fixed lines consist of 10 digits including the DDD.

## Acceptance Criteria
- The function should correctly normalize phone numbers according to the specified rules.
- The function should handle various formats of input strings, including those with spaces, parentheses, and hyphens.
- The function should validate the length and structure of the phone number and raise a `ValueError` if the input does not meet the specified criteria.
- Test cases should include valid and invalid phone numbers to ensure the function behaves as expected.

Arquivos do projeto:
(vazio)