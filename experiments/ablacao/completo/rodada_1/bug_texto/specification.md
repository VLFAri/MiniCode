# Specification

## Objective
The objective is to correct two functions in the `texto.py` file: `eh_palindromo`, which should ignore case, spaces, and punctuation when determining if a string is a palindrome, and `contar_vogais`, which should count uppercase vowels and accented characters as well.

## Parameters / Requirements
- **Function: `eh_palindromo(texto)`**
  - Input: `texto` (string)
  - Output: boolean (True if `texto` is a palindrome, False otherwise)
  - Constraints:
    - The function must ignore case sensitivity.
    - The function must ignore spaces and punctuation marks.
- **Function: `contar_vogais(texto)`**
  - Input: `texto` (string)
  - Output: integer representing the number of vowels in the input string.
  - Constraints:
    - Vowels include 'a', 'e', 'i', 'o', 'u' both lowercase and uppercase.
    - Accented vowels such as 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ' should also be counted.

## Acceptance Criteria
- The `eh_palindromo` function should return True for strings that are palindromes, ignoring case, spaces, and punctuation.
- The `contar_vogais` function should accurately count all instances of vowels, including uppercase and accented vowels.
- Both functions should pass the following tests:
  - For `eh_palindromo("Anotaram a data da maratona")`: Expected output is `True`.
  - For `contar_vogais("Testando Acêntuação")`: Expected output is `8`.

These criteria ensure that the functions operate correctly under specified conditions and can be verified through automated testing.