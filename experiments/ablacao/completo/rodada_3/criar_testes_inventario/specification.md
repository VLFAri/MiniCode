# Specification

## Objective
Create a test file `tests/test_inventario.py` using the pytest framework to test the `Inventario` class from `inventario.py`. The tests should cover the functionalities of adding items, removing items, checking quantities, handling non-existent items, adding items with non-positive quantities, and removing more items than are available in stock.

## Parameters / Requirements
- **File**: `inventario.py`
  - Contains the `Inventario` class which has methods for managing an inventory such as adding items, removing items, and checking quantities.
- **Test File**: `tests/test_inventario.py`
  - Should be written using the pytest framework.
  - Must not modify the original `inventario.py` file.
- **Methods to Test**:
  - `add_item(item_name, quantity)`
    - Adds a specified quantity of an item to the inventory.
  - `remove_item(item_name, quantity)`
    - Removes a specified quantity of an item from the inventory.
  - `get_quantity(item_name)`
    - Returns the quantity of a given item in the inventory.
- **Constraints**:
  - Item names must be strings.
  - Quantities must be integers.
  - Non-existent items should return a specific value or raise an exception when queried.
  - Adding items with non-positive quantities should either fail silently or raise an appropriate error.
  - Removing more items than are available in stock should either fail silently or raise an appropriate error.

## Acceptance Criteria
- The test file should include tests for each method described above.
- Tests should verify that:
  - Items can be added to the inventory correctly.
  - Items can be removed from the inventory correctly.
  - The correct quantity is returned when querying an existing item.
  - An appropriate response is given when querying a non-existent item.
  - Attempts to add items with non-positive quantities are handled appropriately.
  - Attempts to remove more items than are available in stock are handled appropriately.
- All tests should pass without modifying the original `inventario.py` file.
- The test file should be well-organized and readable, following best practices for writing tests.