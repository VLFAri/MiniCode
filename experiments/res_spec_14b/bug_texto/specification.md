# Specification

## Objective
Implement two functions in `texto.py` that correctly identify palindromes and count vowels in Portuguese text, considering case insensitivity, spaces, punctuation for the palindrome check, and including uppercase and accented vowels for the vowel counting.

## Parameters / Requirements
- **Function Name:** `eh_palindromo`
  - **Input Type:** `str`
  - **Constraints:** The input string can contain any characters, including spaces, numbers, and special characters.
  - **Behavior:** The function should return `True` if the input string is a palindrome when ignoring case, spaces, and punctuation. Otherwise, it should return `False`.
  
- **Function Name:** `contar_vogais`
  - **Input Type:** `str`
  - **Constraints:** The input string can contain any characters, but only letters from the Portuguese alphabet will be considered for vowel counting.
  - **Behavior:** The function should return an integer representing the total number of vowels in the input string, including uppercase and accented vowels.

## Acceptance Criteria
- **Test Case 1:** For `eh_palindromo("Anotaram a data da maratona")`, the output should be `True`.
- **Test Case 2:** For `eh_palindromo("Was it a car or a cat I saw?")`, the output should be `True`.
- **Test Case 3:** For `eh_palindromo("Hello World!")`, the output should be `False`.
- **Test Case 4:** For `contar_vogais("Árvore")`, the output should be `3`.
- **Test Case 5:** For `contar_vogais("Testando Acêntuação")`, the output should be `8`.
- **Test Case 6:** For `contar_vogais("12345")`, the output should be `0`.

These criteria must be met to ensure the functions operate as intended under various conditions.