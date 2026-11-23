# Specification

## Objective
The objective is to correct two functions in the `texto.py` file: `eh_palindromo`, which should ignore case, spaces, and punctuation when determining if a string is a palindrome, and `contar_vogais`, which should count uppercase vowels and accented vowels.

## Parameters / Requirements
- **Function: `eh_palindromo(texto)`**
  - Input: `texto` (string)
  - Output: boolean indicating whether the input text is a palindrome or not.
  - Constraints:
    - The function must be case-insensitive.
    - The function must ignore spaces and punctuation.
- **Function: `contar_vogais(texto)`**
  - Input: `texto` (string)
  - Output: integer representing the total number of vowels in the input text.
  - Constraints:
    - Vowels include 'a', 'e', 'i', 'o', 'u'.
    - Uppercase vowels ('A', 'E', 'I', 'O', 'U') must also be counted.
    - Accented vowels ('á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ') must also be counted.

## Acceptance Criteria
- The `eh_palindromo` function should return `True` for strings that are palindromes, ignoring case, spaces, and punctuation.
- The `contar_vogais` function should accurately count all instances of vowels, including uppercase and accented vowels, in the input string.
- Both functions should pass the following tests:
```python
def test_eh_palindromo():
    assert eh_palindromo("Anotaram a data da maratona") == True
    assert eh_palindromo("Was it a car or a cat I saw?") == True
    assert eh_palindromo("No lemon, no melon") == True
    assert eh_palindromo("Hello World!") == False

def test_contar_vogais():
    assert contar_vogais("aeiouAEIOUáéíóúâêôãõ") == 20
    assert contar_vogais("Python Programming") == 4
```
These tests ensure that the functions behave as expected under various conditions.