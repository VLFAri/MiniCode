# Specification

## Objective
Create a `tests/test_inventario.py` file with pytest tests for the `Inventario` class defined in `inventario.py`. The tests should cover the functionalities of adding items, removing items, checking quantities, handling non-existent items, adding items with non-positive quantities, and removing more items than are in stock.

## Parameters / Requirements
- **File**: `inventario.py`
  - Contains the `Inventario` class which has methods to manage an inventory such as adding items, removing items, and checking quantities.
- **Test File**: `tests/test_inventario.py`
  - Should contain pytest tests that validate the functionality of the `Inventario` class.
- **Methods to Test**:
  - `add_item(item_name, quantity)`
    - Adds a specified quantity of an item to the inventory.
  - `remove_item(item_name, quantity)`
    - Removes a specified quantity of an item from the inventory.
  - `get_quantity(item_name)`
    - Returns the quantity of a specific item in the inventory.
- **Constraints**:
  - The `quantity` parameter must be a positive integer when calling `add_item`.
  - The `quantity` parameter must not exceed the current quantity of the item when calling `remove_item`.

## Acceptance Criteria
- The `tests/test_inventario.py` file should include the following tests:
  - Test that verifies adding an item increases its quantity in the inventory.
  - Test that verifies removing an item decreases its quantity in the inventory.
  - Test that verifies getting the quantity of an existing item returns the correct value.
  - Test that verifies attempting to get the quantity of a non-existent item raises an appropriate error.
  - Test that verifies adding an item with a non-positive quantity raises an appropriate error.
  - Test that verifies attempting to remove more items than are in stock raises an appropriate error.
- All tests should pass without any errors or failures.
- The tests should be written using the pytest framework.
- The original `inventario.py` file should not be modified.