# Specification

## Objective
The objective is to correct two functions in the `texto.py` file: `eh_palindromo`, which should ignore case, spaces, and punctuation when determining if a string is a palindrome, and `contar_vogais`, which should count uppercase vowels and accented characters as well.

## Parameters / Requirements
- **Function:** `eh_palindromo`
  - **Input:** A single string `s`.
  - **Output:** A boolean value indicating whether the input string is a palindrome under the specified conditions.
  - **Constraints:** The function must be case-insensitive, ignore spaces and punctuation, and return `True` for strings that read the same forward and backward after normalization.
  
- **Function:** `contar_vogais`
  - **Input:** A single string `s`.
  - **Output:** An integer representing the total number of vowels in the input string, including uppercase vowels and accented characters.
  - **Constraints:** The function must recognize 'a', 'e', 'i', 'o', 'u' as well as their uppercase and accented versions ('á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ').

## Acceptance Criteria
- **Test Case for `eh_palindromo`:**
  - Input: `"Anotaram a data da maratona"`
  - Expected Output: `True`
  - Test Description: The function should correctly identify that the given string is a palindrome, ignoring spaces, punctuation, and case differences.
  
- **Test Case for `contar_vogais`:**
  - Input: `"Olá Mundo!"`
  - Expected Output: `3`
  - Test Description: The function should accurately count the number of vowels in the input string, including accented characters and uppercase vowels.

These criteria ensure that the corrected functions meet the requirements and can be verified through automated tests.