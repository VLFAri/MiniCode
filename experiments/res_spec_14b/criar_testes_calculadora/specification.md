# Specification

## Objective
Create test cases for the functions `somar`, `subtrair`, and `dividir` in the file `calculadora.py`. The tests should be written in the file `tests/test_calculadora.py` using the pytest framework. Additionally, include a test case to handle division by zero (`ZeroDivisionError`) without altering the original `calculadora.py` file.

## Parameters / Requirements
- **Entradas**: Numbers (integers or floats) passed as arguments to the functions `somar`, `subtrair`, and `dividir`.
- **Tipos**: The inputs and outputs of these functions should be either integers or floats.
- **Restrições**: 
  - The function `somar(a, b)` should return the sum of `a` and `b`.
  - The function `subtrair(a, b)` should return the result of subtracting `b` from `a`.
  - The function `dividir(a, b)` should return the result of dividing `a` by `b`, except when `b` is zero, in which case it should raise a `ZeroDivisionError`.
- **Regras de Negócio**:
  - Test cases must cover various scenarios including positive numbers, negative numbers, zero, and edge cases like division by zero.

## Acceptance Criteria
- The test cases should be able to verify that each function behaves correctly according to its defined behavior.
- Tests should be written using the pytest framework.
- Each test case should be clearly named and documented to indicate what scenario it covers.
- A specific test case should exist to check the handling of `ZeroDivisionError` in the `dividir` function.
- All tests should pass successfully when run against the `calculadora.py` file.