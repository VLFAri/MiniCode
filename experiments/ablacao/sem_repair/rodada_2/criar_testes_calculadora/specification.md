# Specification

## Objective
Create test cases for the functions `somar`, `subtrair`, and `dividir` in the file `calculadora.py`. The tests should be written in the file `tests/test_calculadora.py` using the pytest framework. Additionally, include a test case to handle division by zero (`ZeroDivisionError`) without altering the original `calculadora.py` file.

## Parameters / Requirements
- **Entradas**: Numbers (integers or floats) passed as arguments to the functions `somar`, `subtrair`, and `dividir`.
- **Tipos**: The inputs should be of type `int` or `float`.
- **Restrições**: 
  - The function `somar` should accept two numbers and return their sum.
  - The function `subtrair` should accept two numbers and return the difference between them.
  - The function `dividir` should accept two numbers and return the result of dividing the first number by the second number.
  - The function `dividir` should raise a `ZeroDivisionError` if the second number is zero.
- **Regras de Negócio**:
  - The tests should cover all possible scenarios including edge cases like division by zero.

## Acceptance Criteria
- The file `tests/test_calculadora.py` should contain test cases for each function in `calculadora.py`.
- Each test case should be clearly named and describe what scenario it is testing.
- Test cases should include assertions to verify the correctness of the results returned by the functions.
- A specific test case should be included to check that a `ZeroDivisionError` is raised when attempting to divide by zero.
- All tests should pass when run with `pytest`.
- No changes should be made to the `calculadora.py` file.