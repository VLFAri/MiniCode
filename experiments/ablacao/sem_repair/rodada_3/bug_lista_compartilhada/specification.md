# Specification

## Objective
The objective is to correct a bug in the `carrinho.py` file where independent calls to the `adicionar(item)` function share the same cart object. The solution should maintain the current function signature, ensuring that the `carrinho` parameter remains optional. When provided, the `item` should be added to the specified cart and the same cart object should be returned.

## Parameters / Requirements
- **Function Name:** `adicionar`
- **Parameters:**
  - `item`: The item to be added to the cart. This can be of any type but typically would be an object representing a product or service.
  - `carrinho` (optional): The cart object to which the item will be added. If not provided, a new cart should be created and used.
- **Behavior:**
  - If `carrinho` is not provided, a new cart should be created internally.
  - Each call to `adicionar(item)` should operate on its own instance of the cart unless a specific cart is passed as an argument.
  - The function should return the cart object to allow method chaining if needed.

## Acceptance Criteria
- Independent calls to `adicionar(item)` should not affect each other's carts when no `carrinho` is explicitly provided.
- When a `carrinho` is provided, the `item` should be added to that specific cart.
- The function should handle cases where `carrinho` is not provided by creating a new cart internally.
- The function signature should remain unchanged: `def adicionar(item, carrinho=None):`.
- Test cases should verify that items are correctly added to the appropriate cart and that separate calls do not interfere with each other's carts.