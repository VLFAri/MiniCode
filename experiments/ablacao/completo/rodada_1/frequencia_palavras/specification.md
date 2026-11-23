# Specification

## Objective
Implement a module named `palavras.py` which contains a function `frequencia_palavras(texto)` that returns a dictionary with the count of each word in the input text. The words should be converted to lowercase and punctuation should be ignored. If the input text is empty, the function should return an empty dictionary.

## Parameters / Requirements
- **Input Parameter**: `texto` (string)
  - The input parameter is a string representing the text from which word frequencies will be calculated.
  - The text may contain any printable ASCII characters including letters, numbers, spaces, and punctuation marks.
  - The function should handle both uppercase and lowercase letters appropriately, converting all words to lowercase.
  - Punctuation marks should be ignored when counting words. This includes but is not limited to commas, periods, exclamation points, question marks, quotation marks, etc.
  - The function should gracefully handle an empty string as input, returning an empty dictionary.

## Acceptance Criteria
- The function `frequencia_palavras(texto)` must correctly convert all words in the input text to lowercase.
- The function must ignore punctuation when counting words.
- The function must return a dictionary where keys are unique words (in lowercase) and values are the counts of those words in the input text.
- If the input text is empty, the function must return an empty dictionary.
- The implementation should be efficient and able to process large texts without significant performance degradation.
- The function should be thoroughly tested using automated tests to ensure it meets the specified requirements.

Arquivos do projeto:
(vazio)