# Specification

## Objective
Implement a module named `palavras.py` which contains a function `frequencia_palavras(texto)` that returns a dictionary with the count of each word in the input text. The words should be converted to lowercase and punctuation should be ignored. If the input text is empty, the function should return an empty dictionary.

## Parameters / Requirements
- **Input Parameter**: `texto` (string)
  - The input parameter is a string representing the text from which word frequencies will be calculated.
  - The text may contain any printable ASCII characters, including letters, numbers, spaces, and punctuation marks.
- **Output**: Dictionary
  - The output is a dictionary where keys are unique words (in lowercase) and values are the counts of these words in the input text.
  - The dictionary should be empty if the input text is empty or consists only of whitespace and/or punctuation.

## Acceptance Criteria
- The function should correctly convert all words to lowercase.
- Punctuation marks should be ignored when counting words.
- Whitespace should not affect the word count (i.e., multiple spaces between words should be treated as a single space).
- The function should handle empty strings and strings containing only whitespace and/or punctuation by returning an empty dictionary.
- The function should be efficient and able to process large texts without significant performance degradation.
- Test cases should include:
  - A text with multiple words and punctuation.
  - An empty text.
  - A text with only whitespace and punctuation.
  - A text with repeated words and punctuation.

Arquivos do projeto:
(vazio)