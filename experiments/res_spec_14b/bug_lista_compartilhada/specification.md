# Specification

## Objective
The objective is to correct a shared state issue in the `carrinho.py` file where independent calls to the `adicionar(item)` function are modifying the same shopping cart object. This correction should be made while maintaining the current function signature, ensuring that the `carrinho` parameter remains optional and that when provided, the item is added to it and the same object is returned.

## Parameters / Requirements
- **Function Name**: `adicionar`
- **Parameters**:
  - `item`: The item to be added to the shopping cart. Type: Any.
  - `carrinho` (optional): The shopping cart to which the item will be added. Type: List or any collection type.
- **Behavior**:
  - If `carrinho` is not provided, a new empty list should be used as the shopping cart.
  - If `carrinho` is provided, the item should be appended to this list.
  - The function should return the modified `carrinho`.
- **Constraints**:
  - The function must handle cases where multiple items are added in sequence without an explicit `carrinho` parameter.
  - The function must ensure thread safety if called concurrently from different threads.

## Acceptance Criteria
- **Test Case 1**: When `adicionar(item)` is called with no `carrinho` parameter, a new empty list should be created, the item should be added to it, and the list should be returned.
- **Test Case 2**: When `adicionar(item)` is called with an existing `carrinho`, the item should be appended to this `carrinho`, and the updated `carrinho` should be returned.
- **Test Case 3**: Multiple calls to `adicionar(item)` without an explicit `carrinho` parameter should result in each call creating its own separate shopping cart.
- **Test Case 4**: Concurrent calls to `adicionar(item)` with an explicit `carrinho` parameter should not cause race conditions or data corruption.
- **Test Case 5**: The function should maintain its original signature and behavior when `carrinho` is provided, ensuring backward compatibility.