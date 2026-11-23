# Specification

## Objective
Implement two functions in `texto.py` that correctly identify palindromes and count vowels in Portuguese text. The `eh_palindromo` function should ignore case, spaces, and punctuation. The `contar_vogais` function should count both lowercase and uppercase vowels, including accented characters.

## Parameters / Requirements
- **Function:** `eh_palindromo(texto)`
  - **Input:** `texto` (string)
  - **Output:** boolean indicating whether the input string is a palindrome when ignoring case, spaces, and punctuation.
- **Function:** `contar_vogais(texto)`
  - **Input:** `texto` (string)
  - **Output:** integer representing the total number of vowels in the input string, including uppercase and accented vowels.

### Constraints
- The `eh_palindromo` function must treat the following strings as palindromes:
  - "Anotaram a data da maratona"
  - "Socorram-me subi no onibus em Marrocos"
- The `contar_vogais` function must correctly count vowels in the following examples:
  - Input: "Olá Mundo!"
    - Expected Output: 3 (O, á, o)
  - Input: "Árvore"
    - Expected Output: 4 (Á, á, o, e)

## Acceptance Criteria
- The `eh_palindromo` function should return `True` for all valid palindrome inputs and `False` otherwise.
- The `contar_vogais` function should return the correct count of vowels for any given input string.
- Both functions should be tested with at least 5 different inputs to ensure correctness.
- All tests should pass without any errors or exceptions.