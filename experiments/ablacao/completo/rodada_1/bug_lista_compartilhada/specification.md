# Specification

## Objective
The objective is to correct a bug in the `carrinho.py` file where independent calls to the `adicionar(item)` function share the same cart object. The solution should maintain the current function signature, ensuring that the `carrinho` parameter remains optional. When provided, the `item` should be added to the specified cart and the same cart object should be returned.

## Parameters / Requirements
- **Function Name**: `adicionar`
- **Parameters**:
  - `item`: The item to be added to the cart. This can be of any type but typically represents an object or product.
  - `carrinho` (optional): The cart object to which the item will be added. If not provided, a new cart should be created and used.
- **Behavior**:
  - If `carrinho` is not provided, a new cart should be created internally.
  - Each call to `adicionar(item)` should operate on its own cart instance if `carrinho` is not provided.
  - If `carrinho` is provided, the `item` should be added to this specific cart.
  - The function should return the cart object after adding the item.

## Acceptance Criteria
1. Independent calls to `adicionar(item)` without providing a `carrinho` parameter should each operate on their own cart instances.
2. Providing a `carrinho` parameter should add the `item` to the specified cart.
3. The function should return the cart object after adding the item.
4. Test cases should verify that:
   - Items added without specifying a cart are stored in separate carts.
   - Items added with a specified cart are stored in the correct cart.
   - The function returns the correct cart object after each operation.
5. The function signature should remain unchanged, maintaining the optional nature of the `carrinho` parameter.