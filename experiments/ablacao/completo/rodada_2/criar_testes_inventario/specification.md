# Specification

## Objective
Create a `tests/test_inventario.py` file with pytest tests for the `Inventario` class defined in `inventario.py`. The tests should cover the functionalities of adding items, removing items, checking quantities, handling non-existent items, adding items with non-positive quantities, and removing more items than are available in stock.

## Parameters / Requirements
- **File**: `inventario.py`
  - Contains the `Inventario` class which has methods to add items, remove items, check quantities, etc.
- **Test File**: `tests/test_inventario.py`
  - Should contain pytest tests that verify the functionality of the `Inventario` class.
- **Methods to Test**:
  - `add_item(item_name, quantity)`
    - Adds an item to the inventory.
  - `remove_item(item_name, quantity)`
    - Removes an item from the inventory.
  - `get_quantity(item_name)`
    - Returns the quantity of a given item in the inventory.
- **Constraints**:
  - The `quantity` parameter must be a positive integer when calling `add_item`.
  - The `quantity` parameter must not exceed the current stock when calling `remove_item`.

## Acceptance Criteria
- The `tests/test_inventario.py` file should include the following tests:
  - Test that verifies adding an item increases its quantity correctly.
  - Test that verifies removing an item decreases its quantity correctly.
  - Test that verifies `get_quantity` returns the correct quantity for existing items.
  - Test that verifies attempting to get the quantity of a non-existent item raises an appropriate error.
  - Test that verifies adding an item with a non-positive quantity raises an appropriate error.
  - Test that verifies removing more items than are available in stock raises an appropriate error.
- All tests should pass without any errors or failures.
- The original `inventario.py` file should remain unchanged.