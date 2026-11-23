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
  - The function must handle cases where multiple items are added in quick succession without affecting each other's state.
  - The function should maintain its current behavior if `carrinho` is explicitly passed.

## Acceptance Criteria
- **Test Case 1**: When `adicionar(item)` is called with no `carrinho` argument, a new empty list should be created and the item should be added to it.
  - Input: `adicionar('apple')`
  - Expected Output: `['apple']`
- **Test Case 2**: When `adicionar(item)` is called with an existing `carrinho`, the item should be added to the provided `carrinho`.
  - Input: `adicionar('banana', ['orange'])`
  - Expected Output: `['orange', 'banana']`
- **Test Case 3**: Multiple independent calls to `adicionar(item)` should not affect each other's `carrinho` states.
  - Input: 
    ```python
    cart1 = ['item1']
    cart2 = ['item2']
    adicionar('item3')
    adicionar('item4', cart1)
    adicionar('item5', cart2)
    ```
  - Expected Output:
    - `adicionar('item3')`: `['item3']`
    - `adicionar('item4', cart1)`: `['item1', 'item4']`
    - `adicionar('item5', cart2)`: `['item2', 'item5']`

These criteria ensure that the function behaves correctly under various conditions and maintains the integrity of separate shopping carts when called independently.