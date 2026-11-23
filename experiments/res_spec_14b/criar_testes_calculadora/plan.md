Based on the provided specification and project files, here's a step-by-step plan to create test cases for the functions `somar`, `subtrair`, and `dividir` in `calculadora.py`.

### Step-by-Step Plan

1. **Set Up Environment**
   - Ensure Python and pytest are installed.
   - Create a directory structure if necessary, with `calculadora.py` and `tests/test_calculadora.py`.

2. **Import Necessary Libraries**
   - Open `tests/test_calculadora.py` and import the necessary modules from `calculadora.py`.
   - Import `pytest` for writing test cases.

3. **Define Test Cases for `somar` Function**
   - Write test cases to cover different scenarios such as positive numbers, negative numbers, and zero.
   - Example: `test_somar_positive_numbers`, `test_somar_negative_numbers`, `test_somar_with_zero`.

4. **Define Test Cases for `subtrair` Function**
   - Similarly, write test cases for the `subtrair` function covering various scenarios.
   - Example: `test_subtrair_positive_numbers`, `test_subtrair_negative_numbers`, `test_subtrair_with_zero`.

5. **Define Test Cases for `dividir` Function**
   - Write test cases for the `dividir` function, ensuring to cover division by zero.
   - Example: `test_dividir_normal_cases`, `test_dividir_with_zero_division_error`.

6. **Handle Division By Zero Error**
   - Specifically, write a test case to ensure that `dividir` raises a `ZeroDivisionError` when the divisor is zero.
   - Example: `test_dividir_raises_ZeroDivisionError`.

7. **Run Tests**
   - Use pytest to run all the test cases.
   - Verify that all tests pass successfully.

8. **Document Test Cases**
   - Ensure each test case is clearly named and documented to indicate what scenario it covers.

### Detailed Steps

#### Step 1: Set Up Environment
Ensure you have Python and pytest installed. If not, install pytest using pip:

```bash
pip install pytest
```

#### Step 2: Import Necessary Libraries
In `tests/test_calculadora.py`, import the necessary functions from `calculadora.py` and import `pytest`.

```python
from calculadora import somar, subtrair, dividir
import pytest
```

#### Step 3: Define Test Cases for `somar`
Write test cases for the `somar` function.

```python
def test_somar_positive_numbers():
    assert somar(1, 2) == 3

def test_somar_negative_numbers():
    assert somar(-1, -2) == -3

def test_somar_with_zero():
    assert somar(0, 0) == 0
```

#### Step 4: Define Test Cases for `subtrair`
Write test cases for the `subtrair` function.

```python
def test_subtrair_positive_numbers():
    assert subtrair(3, 1) == 2

def test_subtrair_negative_numbers():
    assert subtrair(-2, -1) == -1

def test_subtrair_with_zero():
    assert subtrair(0, 0) == 0
```

#### Step 5: Define Test Cases for `dividir`
Write test cases for the `dividir` function, including handling division by zero.

```python
def test_dividir_normal_cases():
    assert dividir(6, 2) == 3
    assert dividir(-6, 2) == -3
    assert dividir(6, -2) == -3
    assert dividir(-6, -2) == 3

def test_dividir_with_zero_division_error():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
```

#### Step 6: Handle Division By Zero Error
Ensure there is a specific test case to check the handling of `ZeroDivisionError`.

```python
def test_dividir_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
```

#### Step 7: Run Tests
Use pytest to run all the test cases.

```bash
pytest tests/test_calculadora.py
```

#### Step 8: Document Test Cases
Ensure each test case is clearly named and documented to indicate what scenario it covers.

By following this plan, you will have comprehensive test coverage for the functions in `calculadora.py`, ensuring they behave correctly under various conditions.