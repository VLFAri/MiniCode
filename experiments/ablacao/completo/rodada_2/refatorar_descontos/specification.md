# Specification

## Objective
Refactor the `preco.py` file to eliminate code duplication by creating a function named `aplicar_desconto`. This function should be used in place of existing discount calculation logic within the functions `preco_vip`, `preco_normal`, and `preco_promocao`.

## Parameters / Requirements
- **Function Name:** `aplicar_desconto`
- **Input Parameters:**
  - `valor`: A float representing the original price.
  - `percentual`: An integer representing the discount percentage.
- **Behavioral Requirements:**
  - The function should raise a `ValueError` if the `percentual` is outside the range of 0 to 100 or if the `valor` is negative.
  - The result should be rounded to two decimal places.
- **Existing Functions to Modify:**
  - `preco_vip`: Should apply a 20% discount using `aplicar_desconto`.
  - `preco_normal`: Should apply a 5% discount using `aplicar_desconto`.
  - `preco_promocao`: Should apply a 30% discount using `aplicar_desconto`.

## Acceptance Criteria
- The `aplicar_desconto` function correctly raises a `ValueError` when given invalid input parameters.
- The `preco_vip`, `preco_normal`, and `preco_promocao` functions use the `aplicar_desconto` function without changing their current behavior.
- Test cases for each function confirm that the discounts are applied accurately and consistently with the specified percentages.
- All changes are made in the `preco.py` file only, ensuring no other files are modified.