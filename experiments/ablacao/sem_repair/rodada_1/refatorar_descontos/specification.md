# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
The function `aplicar_desconto` should accept two parameters:
- `valor`: A float representing the original price.
- `percentual`: An integer representing the discount percentage.

The function should adhere to the following rules:
- If `valor` is negative or `percentual` is outside the range of 0 to 100, raise a `ValueError`.
- The result should be rounded to two decimal places.

The refactored functions `preco_vip`, `preco_normal`, and `preco_promocao` should use `aplicar_desconto` without changing their current behavior.

## Acceptance Criteria
The acceptance criteria for this specification include:
- The `aplicar_desconto` function must correctly calculate the discounted value based on the provided `valor` and `percentual`.
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions must call `aplicar_desconto` with the appropriate arguments and return values that match their previous behavior.
- Test cases should verify that:
  - `aplicar_desconto` raises a `ValueError` when given invalid inputs (negative `valor` or `percentual` out of range).
  - `aplicar_desconto` returns the correct discounted value rounded to two decimal places for valid inputs.
  - The refactored functions (`preco_vip`, `preco_normal`, `preco_promocao`) produce the same output as before refactoring.