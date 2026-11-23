# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
- **Function Name:** `aplicar_desconto`
- **Parameters:**
  - `valor`: The original price value as a float.
  - `percentual`: The discount percentage as an integer.
- **Behavior:**
  - If `valor` is negative or `percentual` is outside the range of 0 to 100, raise a `ValueError`.
  - Otherwise, calculate the discounted price by applying the given percentage discount to the original price.
  - Round the final discounted price to two decimal places.
- **Functions to Modify:**
  - `preco_vip`: Should apply a 20% discount using `aplicar_desconto`.
  - `preco_normal`: Should apply a 5% discount using `aplicar_desconto`.
  - `preco_promocao`: Should apply a 30% discount using `aplicar_desconto`.

## Acceptance Criteria
- The `aplicar_desconto` function must correctly handle negative values and percentages outside the valid range by raising a `ValueError`.
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions must use the `aplicar_desconto` function without changing their current behavior.
- Test cases should verify that:
  - `aplicar_desconto(100, 20)` returns `79.99`.
  - `aplicar_desconto(100, 5)` returns `95.00`.
  - `aplicar_desconto(100, 30)` returns `69.99`.
  - `aplicar_desconto(-100, 20)` raises a `ValueError`.
  - `aplicar_desconto(100, -1)` raises a `ValueError`.
  - `aplicar_desconto(100, 101)` raises a `ValueError`.
- The refactored code should maintain the same functionality as the original code but with reduced redundancy.

This specification ensures that the code is clean, maintainable, and adheres to the requirements provided by the user.