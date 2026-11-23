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
  - For the `dividir` function, there should be a specific test case to check the behavior when dividing by zero.
- **Regras de Negócio**:
  - The test cases should cover various scenarios including positive numbers, negative numbers, and zero.
  - The test case for division by zero should verify that a `ZeroDivisionError` is raised.

## Acceptance Criteria
- The file `tests/test_calculadora.py` should contain test cases for each of the functions `somar`, `subtrair`, and `dividir`.
- Each test case should be clearly named and describe the scenario it is testing.
- Test cases should include assertions to validate the output of the functions.
- A specific test case should be included to verify the behavior of the `dividir` function when the divisor is zero.
- All tests should pass when run with the pytest framework.
- The original `calculadora.py` file should not be modified.