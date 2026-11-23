# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
- **Function Name:** `aplicar_desconto`
- **Input Parameters:**
  - `valor`: The original price as a float.
  - `percentual`: The discount percentage as an integer.
- **Constraints:**
  - If `valor` is negative or `percentual` is outside the range of 0 to 100, raise a `ValueError`.
  - The result should be rounded to two decimal places.
- **Existing Functions:**
  - `preco_vip`: Applies a 20% discount.
  - `preco_normal`: Applies a 5% discount.
  - `preco_promocao`: Applies a 30% discount.

## Acceptance Criteria
- The `aplicar_desconto` function must correctly apply discounts based on the provided parameters.
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions must use the `aplicar_desconto` function without changing their current behavior.
- Test cases should verify that:
  - Discounts are applied correctly for valid inputs.
  - A `ValueError` is raised when invalid inputs are provided (negative `valor` or `percentual` out of 0 to 100 range).
  - Results are rounded to two decimal places.
- Example test cases:
  - `assert aplicar_desconto(100, 20) == 80.00`
  - `assert aplicar_desconto(100, 5) == 95.00`
  - `assert aplicar_desconto(100, 30) == 70.00`
  - `assert aplicar_desconto(-100, 20) == ValueError`
  - `assert aplicar_desconto(100, 101) == ValueError`

This specification ensures that the refactored code adheres to the requirements while maintaining the functionality of the original code.