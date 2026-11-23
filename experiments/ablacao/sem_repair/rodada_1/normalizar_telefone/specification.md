# Specification

## Objective
The objective is to create a Python function named `normalizar_telefone` that takes a Brazilian phone number as input and returns it in the international format `+55DDDNUMBER`. The function should remove spaces, parentheses, and hyphens from the input string. If the input starts with `+55`, this prefix should be removed before validation. The resulting phone number must consist of exactly 10 digits (including DDD and a fixed line number of 8 digits) or 11 digits (including DDD and a mobile number starting with 9). If the input does not conform to these requirements, the function should raise a `ValueError`.

## Parameters / Requirements
- **Input**: A string representing a Brazilian phone number. This string may contain spaces, parentheses, and hyphens.
- **Output**: A string representing the normalized phone number in the format `+55DDDNUMBER`.
- **Constraints**:
  - The input string can start with `+55`, which should be removed before processing.
  - The final output must be exactly 12 characters long, including the `+55` prefix.
  - The phone number must either have 10 digits (excluding DDD) or 11 digits (excluding DDD).
  - The phone number must start with `9` if it's a mobile number.

## Acceptance Criteria
- The function should correctly normalize phone numbers according to the specified rules.
- The function should handle various formats of input strings, including those with spaces, parentheses, and hyphens.
- The function should raise a `ValueError` for invalid inputs that do not match the specified constraints.
- The function should be tested with a variety of valid and invalid inputs to ensure correctness.

Arquivos do projeto:
(vazio)