# Specification

## Objective
Implement a module named `palavras.py` containing a function `frequencia_palavras(texto)` that returns a dictionary with the count of each word in the input text. The words should be converted to lowercase and punctuation should be ignored. If the input text is empty, the function should return an empty dictionary.

## Parameters / Requirements
- **Input Parameter**: `texto` (string)
  - The input parameter is a string representing the text from which word frequencies will be calculated.
  - Constraints: The text can contain any printable ASCII characters including letters, numbers, spaces, and punctuation marks.
- **Output**: Dictionary
  - The output is a dictionary where keys are unique words (in lowercase) and values are the counts of these words in the input text.
  - Constraints: The dictionary should not include any punctuation marks as part of the keys.

## Acceptance Criteria
- The function should correctly convert all words to lowercase.
- Punctuation marks should be ignored when counting words.
- The function should handle empty strings by returning an empty dictionary.
- Test cases should verify that the function works correctly for various inputs, including those with punctuation and mixed case letters.

Arquivos do projeto:
(vazio)