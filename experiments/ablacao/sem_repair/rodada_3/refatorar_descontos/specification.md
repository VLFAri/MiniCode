# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
- **Function Name:** `aplicar_desconto`
- **Parameters:**
  - `valor`: A float representing the original price.
  - `percentual`: An integer representing the discount percentage.
- **Behavior:**
  - The function should apply the specified discount to the given value.
  - If the `valor` is negative or if the `percentual` is outside the range of 0 to 100, the function should raise a `ValueError`.
  - The result should be rounded to two decimal places.
- **Functions to Modify:**
  - `preco_vip`: Should use `aplicar_desconto` with a 20% discount.
  - `preco_normal`: Should use `aplicar_desconto` with a 5% discount.
  - `preco_promocao`: Should use `aplicar_desconto` with a 30% discount.

## Acceptance Criteria
- The `aplicar_desconto` function should correctly handle positive values for `valor` and valid percentages for `percentual`.
- The `aplicar_desconto` function should raise a `ValueError` when `valor` is negative or `percentual` is outside the range of 0 to 100.
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions should use the `aplicar_desconto` function without changing their current behavior.
- Test cases should verify that the rounding to two decimal places works as expected.
- Test cases should also verify that invalid inputs trigger the correct exceptions.