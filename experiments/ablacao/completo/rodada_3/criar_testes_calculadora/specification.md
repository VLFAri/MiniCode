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
  - The tests should verify that the functions perform the correct arithmetic operations.
  - The tests should also verify the handling of exceptions, specifically `ZeroDivisionError`.

## Acceptance Criteria
- The file `tests/test_calculadora.py` should contain test cases for each of the functions `somar`, `subtrair`, and `dividir`.
- Each test case should use assertions to validate the output of the functions.
- There should be a specific test case for the `dividir` function to ensure it raises a `ZeroDivisionError` when attempting to divide by zero.
- All tests should pass when run with `pytest`.
- The original `calculadora.py` file should not be modified.