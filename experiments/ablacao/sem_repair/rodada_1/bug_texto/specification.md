# Specification

## Objective
The objective is to correct two functions in the `texto.py` file: `eh_palindromo`, which should ignore case, spaces, and punctuation when determining if a string is a palindrome, and `contar_vogais`, which should count both lowercase and uppercase vowels, including accented characters.

## Parameters / Requirements
- **Function: `eh_palindromo(texto)`**
  - Input: `texto` (string)
  - Output: boolean (True if `texto` is a palindrome, False otherwise)
  - Constraints:
    - The function must be case-insensitive.
    - The function must ignore spaces and punctuation.
- **Function: `contar_vogais(texto)`**
  - Input: `texto` (string)
  - Output: integer representing the total number of vowels in `texto`
  - Constraints:
    - Vowels include 'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ'.
    - The function must count all occurrences of these vowels in the input string.

## Acceptance Criteria
- The `eh_palindromo` function should return True for strings that are palindromes, ignoring case, spaces, and punctuation. For example, "Anotaram a data da maratona" should return True.
- The `contar_vogais` function should accurately count all instances of vowels, including accented ones, in the input string. For example, "Árvore" should return 3 (counting 'Á', 'o', 'e').

These criteria can be verified through automated tests that check the output of each function against known inputs and expected outputs.