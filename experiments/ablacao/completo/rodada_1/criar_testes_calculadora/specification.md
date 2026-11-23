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
  - For the `dividir` function, there should be a specific test case to check if a `ZeroDivisionError` is raised when attempting to divide by zero.
- **Regras de Negócio**:
  - The tests should not modify the original `calculadora.py` file.
  - All tests should be written in the `tests/test_calculadora.py` file.

## Acceptance Criteria
- The `tests/test_calculadora.py` file contains test cases for each of the functions `somar`, `subtrair`, and `dividir`.
- Each test case should verify that the corresponding function performs its operation correctly.
- There should be a test case specifically designed to check if a `ZeroDivisionError` is raised when the `dividir` function attempts to divide by zero.
- All tests should pass when run with `pytest`.
- The original `calculadora.py` file remains unchanged.