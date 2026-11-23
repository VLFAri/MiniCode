Based on the provided specification and project files, here is a step-by-step plan to create a test file `tests/test_inventario.py` using the pytest framework:

### Step-by-Step Plan

1. **Set Up Environment**
   - Ensure that the pytest framework is installed. If not, install it via pip:
     ```bash
     pip install pytest
     ```

2. **Create Test Directory Structure**
   - Create a directory named `tests` if it does not already exist.
     ```bash
     mkdir -p tests
     ```

3. **Create Test File**
   - Create a new Python file named `test_inventario.py` inside the `tests` directory.
     ```bash
     touch tests/test_inventario.py
     ```

4. **Import Necessary Modules**
   - Import the `Inventario` class from `inventario.py` and the `pytest` module in the test file.
     ```python
     from inventario import Inventario
     import pytest
     ```

5. **Define Setup and Teardown Functions (Optional)**
   - Define a setup function to initialize the `Inventario` object before each test.
   - Define a teardown function to clean up after each test if needed.
     ```python
     @pytest.fixture
     def inventario():
         return Inventario()
     ```

6. **Write Tests for Each Method**
   - Write individual tests for each method in the `Inventario` class.
   - Cover both normal and edge cases for each method.

7. **Test `add_item` Method**
   - Test adding items with positive quantities.
   - Test adding items with zero or negative quantities.
     ```python
     def test_add_item(inventario):
         # Normal case
         inventario.add_item("apple", 10)
         assert inventario.get_quantity("apple") == 10

         # Edge case: add zero quantity
         inventario.add_item("apple", 0)
         assert inventario.get_quantity("apple") == 10

         # Edge case: add negative quantity
         with pytest.raises(ValueError):
             inventario.add_item("apple", -1)
     ```

8. **Test `remove_item` Method**
   - Test removing items with positive quantities.
   - Test attempting to remove more items than are available.
     ```python
     def test_remove_item(inventario):
         # Normal case
         inventario.add_item("banana", 20)
         inventario.remove_item("banana", 10)
         assert inventario.get_quantity("banana") == 10

         # Edge case: remove more than available
         with pytest.raises(ValueError):
             inventario.remove_item("banana", 20)
     ```

9. **Test `get_quantity` Method**
   - Test getting the quantity of existing items.
   - Test getting the quantity of non-existent items.
     ```python
     def test_get_quantity(inventario):
         # Normal case
         inventario.add_item("orange", 15)
         assert inventario.get_quantity("orange") == 15

         # Edge case: get quantity of non-existent item
         assert inventario.get_quantity("grape") == 0
     ```

10. **Run Tests**
    - Run the tests using the pytest command.
      ```bash
      pytest tests/test_inventario.py
      ```

11. **Review and Refine Tests**
    - Review the output of the tests to ensure all tests pass.
    - Refine tests as necessary to cover all edge cases and error conditions.

### Example of Full Test File

Here is an example of what the full `test_inventario.py` file might look like:

```python
from inventario import Inventario
import pytest

@pytest.fixture
def inventario():
    return Inventario()

def test_add_item(inventario):
    # Normal case
    inventario.add_item("apple", 10)
    assert inventario.get_quantity("apple") == 10

    # Edge case: add zero quantity
    inventario.add_item("apple", 0)
    assert inventario.get_quantity("apple") == 10

    # Edge case: add negative quantity
    with pytest.raises(ValueError):
        inventario.add_item("apple", -1)

def test_remove_item(inventario):
    # Normal case
    inventario.add_item("banana", 20)
    inventario.remove_item("banana", 10)
    assert inventario.get_quantity("banana") == 10

    # Edge case: remove more than available
    with pytest.raises(ValueError):
        inventario.remove_item("banana", 20)

def test_get_quantity(inventario):
    # Normal case
    inventario.add_item("orange", 15)
    assert inventario.get_quantity("orange") == 15

    # Edge case: get quantity of non-existent item
    assert inventario.get_quantity("grape") == 0
```

This plan ensures comprehensive testing of the `Inventario` class while adhering to the requirements and constraints specified.