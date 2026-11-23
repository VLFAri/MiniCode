# Specification

## Objective
Create a test file `tests/test_inventario.py` using the `pytest` framework to test the `Inventario` class from `inventario.py`. The tests should cover the functionalities of adding items, removing items, checking quantities, handling non-existent items, adding with non-positive quantities, and removing more than what is currently in stock.

## Parameters / Requirements
- **File**: `inventario.py`
  - Contains the `Inventario` class which has methods for managing an inventory such as adding items, removing items, and checking quantities.
- **Test File**: `tests/test_inventario.py`
  - Should be written using the `pytest` framework.
  - Must not modify the original `inventario.py` file.

## Acceptance Criteria
- Tests should be able to add items to the inventory.
- Tests should be able to remove items from the inventory.
- Tests should be able to check the quantity of an existing item.
- Tests should handle cases where an item does not exist in the inventory.
- Tests should fail when attempting to add an item with a non-positive quantity.
- Tests should fail when attempting to remove more items than are currently in stock.
- All tests should pass without modifying the original `inventario.py` file.
- Tests should be clear, concise, and well-documented.