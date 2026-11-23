# Specification

## Objective
The objective is to correct two functions in the `texto.py` file: `eh_palindromo`, which should ignore case, spaces, and punctuation when determining if a string is a palindrome, and `contar_vogais`, which should count uppercase vowels and accented characters as well.

## Parameters / Requirements
- **Function: `eh_palindromo(texto)`**
  - Input: `texto` (string)
  - Output: boolean (True if `texto` is a palindrome, False otherwise)
  - Constraints:
    - The function must be case-insensitive.
    - The function must ignore spaces and punctuation.
- **Function: `contar_vogais(texto)`**
  - Input: `texto` (string)
  - Output: integer representing the number of vowels in `texto`
  - Constraints:
    - Vowels include 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ'.
    - The function should count all occurrences of these vowels in the input string.

## Acceptance Criteria
- The `eh_palindromo` function should return True for strings that are palindromes, ignoring case, spaces, and punctuation.
- The `contar_vogais` function should accurately count all instances of vowels, including uppercase and accented characters, in the input string.
- Both functions should pass the following tests:
  - For `eh_palindromo`:
    ```python
    assert eh_palindromo("Anotaram a data da maratona") == True
    assert eh_palindromo("Was it a car or a cat I saw?") == True
    assert eh_palindromo("No lemon, no melon") == True
    ```
  - For `contar_vogais`:
    ```python
    assert contar_vogais("aeiouAEIOUáéíóúâêôãõ") == 20
    assert contar_vogais("") == 0
    assert contar_vogais("Testando a função") == 6
    ```

These criteria ensure that the functions behave as expected under various conditions and inputs.