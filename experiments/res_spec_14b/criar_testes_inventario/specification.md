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
    - Returns the current quantity of a given item in the inventory.
- **Constraints**:
  - Item names must be strings.
  - Quantities must be integers.
  - Non-positive quantities should raise an error or handle appropriately when adding/removing items.
  - Attempting to remove more items than are available should also raise an error or handle appropriately.

## Acceptance Criteria
- The test file should include tests for each method in the `Inventario` class.
- Tests should cover normal cases, edge cases, and error conditions.
- All tests should pass without any failures.
- The test file should not modify the `inventario.py` file.
- Tests should be clear, concise, and well-documented.
- Use appropriate assertions to verify the correctness of each method's behavior.
- Include setup and teardown functions if necessary to ensure the inventory is reset between tests.