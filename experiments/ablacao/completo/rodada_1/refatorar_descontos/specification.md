# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
- **Function Name:** `aplicar_desconto`
- **Parameters:**
  - `valor`: A float representing the original price.
  - `percentual`: An integer representing the discount percentage.
- **Behavior:**
  - The function should calculate the discounted value based on the provided parameters.
  - If `valor` is negative or `percentual` is outside the range of 0 to 100, the function should raise a `ValueError`.
  - The result should be rounded to two decimal places.

## Acceptance Criteria
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions should use the `aplicar_desconto` function without changing their current behavior.
- The `aplicar_desconto` function should handle invalid inputs by raising a `ValueError`.
- The output of each function should be rounded to two decimal places.
- Test cases should verify that the refactored functions behave as expected under various conditions, including valid and invalid input scenarios.