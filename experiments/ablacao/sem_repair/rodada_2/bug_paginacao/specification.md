# Specification

## Objective
Implement a function `paginar(itens, pagina, tamanho)` that correctly returns the items for the specified page in a 1-indexed manner. If `pagina` or `tamanho` is less than 1, raise a `ValueError`. For pages beyond the last page, return an empty list.

## Parameters / Requirements
- **itens**: A list of items to be paginated.
- **pagina**: An integer representing the page number to retrieve. It should be 1-indexed (i.e., the first page is page 1).
- **tamanho**: An integer representing the size of each page.
- **Constraints**:
  - `pagina` and `tamanho` must be positive integers.
  - If `pagina` or `tamanho` is less than 1, the function should raise a `ValueError`.
  - If the requested page is beyond the last page, the function should return an empty list.

## Acceptance Criteria
- The function should correctly return the items for the specified page when `pagina` is 1 or greater and `tamanho` is greater than 0.
- The function should raise a `ValueError` if `pagina` or `tamanho` is less than 1.
- The function should return an empty list if the requested page is beyond the last page.
- The function should be tested with various inputs to ensure it behaves as expected under different conditions.