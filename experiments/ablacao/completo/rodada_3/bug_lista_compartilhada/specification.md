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
1. When calling `adicionar(item)` multiple times without providing a `carrinho`, each call should operate on a separate shopping cart.
2. When calling `adicionar(item, carrinho)` multiple times with the same `carrinho` object, all calls should modify the same shopping cart.
3. The function should handle cases where `carrinho` is not provided correctly by creating a new empty list each time.
4. The function should pass unit tests verifying the above criteria.
5. The code should maintain readability and adhere to good coding practices.