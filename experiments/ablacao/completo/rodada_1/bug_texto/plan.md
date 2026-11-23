Based on the provided specification and project files, here's a step-by-step plan to implement the required functionality:

### Step-by-Step Plan

1. **Review the Current Code**:
   - Open the `texto.py` file and review the current implementations of `eh_palindromo` and `contar_vogais`.

2. **Define Helper Functions**:
   - Create helper functions to clean the text before checking for palindromes and counting vowels. This will make the main functions cleaner and more readable.

3. **Implement `eh_palindromo` Function**:
   - Modify the `eh_palindromo` function to ignore case, spaces, and punctuation.
   - Use a helper function to preprocess the input string by removing non-alphabetic characters and converting it to lowercase.

4. **Implement `contar_vogais` Function**:
   - Update the `contar_vogais` function to count both uppercase and accented vowels.
   - Use a helper function to identify and count all types of vowels in the input string.

5. **Create or Update Tests**:
   - Write unit tests for both functions using a testing framework like `unittest` or `pytest`.
   - Ensure the tests cover various cases, including edge cases and special characters.

6. **Run and Debug Tests**:
   - Execute the tests to verify that both functions behave as expected.
   - Debug any issues that arise during testing.

7. **Document Changes**:
   - Add comments to the code explaining the changes made and how each function works.
   - Document the tests and their purpose.

### Detailed Steps

#### Step 1: Review the Current Code
- Examine the existing `eh_palindromo` and `contar_vogais` functions in `texto.py`.

#### Step 2: Define Helper Functions
```python
import re

def preprocess_text(text):
    # Remove non-alphabetic characters and convert to lowercase
    return re.sub(r'[^a-zA-Z]', '', text).lower()

def count_vowels(text):
    # Count all types of vowels including accented ones
    vowels = set('aeiouAEIOUáéíóúâêîôûãẽĩõũ')
    return sum(1 for char in text if char in vowels)
```

#### Step 3: Implement `eh_palindromo` Function
```python
def eh_palindromo(text):
    processed_text = preprocess_text(text)
    return processed_text == processed_text[::-1]
```

#### Step 4: Implement `contar_vogais` Function
```python
def contar_vogais(text):
    return count_vowels(text)
```

#### Step 5: Create or Update Tests
```python
import unittest

class TestTextFunctions(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("Anotaram a data da maratona"))
        self.assertFalse(eh_palindromo("Hello World"))

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Testando Acêntuação"), 8)
        self.assertEqual(contar_vogais("HELLO WORLD"), 3)

if __name__ == '__main__':
    unittest.main()
```

#### Step 6: Run and Debug Tests
- Execute the tests using a command like `python -m unittest texto_test.py`.
- Fix any failing tests by revising the implementation of the functions.

#### Step 7: Document Changes
- Add comments to explain the preprocessing steps and vowel counting logic.
- Document the test cases and their expected outcomes.

By following this plan, you should be able to modify the `texto.py` file to meet the requirements specified in the problem statement.