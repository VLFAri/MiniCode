# Specification

## Objective
The objective is to correct a shared state issue in the `carrinho.py` file where independent calls to the `adicionar(item)` function are modifying the same shopping cart object. This correction should be made while maintaining the current function signature, ensuring that the `carrinho` parameter remains optional and that when provided, the item is added to it and the same object is returned.

## Parameters / Requirements
- **Function Name**: `adicionar`
- **Parameters**:
  - `item`: The item to be added to the shopping cart. Type: Any.
  - `carrinho` (optional): The shopping cart to which the item will be added. Type: List or any collection type that supports adding items.
- **Behavior**:
  - If `carrinho` is not provided, a new empty list should be used as the shopping cart.
  - If `carrinho` is provided, the item should be added to this specific shopping cart.
  - The function should return the modified shopping cart.
- **Constraints**:
  - The function signature must remain unchanged.
  - The solution should avoid sharing mutable state between different calls to `adicionar`.

## Acceptance Criteria
- Independent calls to `adicionar(item)` with no `carrinho` argument should each operate on a separate, newly created shopping cart.
- Calls to `adicionar(item, carrinho)` should modify the provided `carrinho`.
- The function should correctly handle cases where `carrinho` is not provided by creating a new empty list.
- Test cases should verify that:
  - Different calls to `adicionar(item)` without a `carrinho` argument do not share state.
  - Providing a `carrinho` argument results in modifications to that specific `carrinho`.
  - The function returns the correct shopping cart after adding an item.
- All tests should pass without any assertion errors, indicating that the function behaves as expected under all specified conditions.