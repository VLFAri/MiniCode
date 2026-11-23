# Specification

## Objective
The objective is to correct a shared state issue in the `carrinho.py` file where independent calls to the `adicionar(item)` function are modifying the same shopping cart object. This correction should be made while maintaining the current function signature, ensuring that the `carrinho` parameter remains optional and that when provided, the item is added to it and the same object is returned.

## Parameters / Requirements
- **Function Name**: `adicionar`
- **Parameters**:
  - `item`: The item to be added to the shopping cart. It can be of any type but typically represents an item for sale.
  - `carrinho` (optional): The shopping cart object to which the item will be added. If not provided, a new shopping cart object should be created and used.
- **Behavior**:
  - When `carrinho` is not provided, a new instance of the shopping cart should be created internally.
  - When `carrinho` is provided, the item should be added to this specific shopping cart.
  - The function should return the `carrinho` object after adding the item.
- **Constraints**:
  - The function must handle cases where multiple items are added through separate calls correctly, without affecting each other's state if different carts are used.
  - The function should be able to handle concurrent calls safely, avoiding race conditions.

## Acceptance Criteria
- Independent calls to `adicionar(item)` with or without specifying a `carrinho` should not affect each other's state.
- The function should create a new shopping cart if no `carrinho` is specified.
- The function should add the item to the specified `carrinho` if one is provided.
- The function should return the modified `carrinho` object.
- The function should pass unit tests verifying its behavior under various scenarios including concurrency.
- The function should maintain its current signature, allowing for optional `carrinho` parameter.