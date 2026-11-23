# Specification

## Objective
Implement a module named `palavras.py` which contains a function `frequencia_palavras(texto)` that returns a dictionary with the count of each word in the input text. The words should be converted to lowercase and punctuation should be ignored. If the input text is empty, the function should return an empty dictionary.

## Parameters / Requirements
- **Input Parameter**: `texto` (string)
  - The input parameter is a string representing the text from which word frequencies will be calculated.
- **Output**: Dictionary
  - The output is a dictionary where keys are unique words (in lowercase) and values are the counts of these words in the input text.
- **Constraints**:
  - The function must ignore punctuation marks when processing the text.
  - The function should convert all words to lowercase before counting them.
  - An empty input string should result in an empty dictionary being returned.

## Acceptance Criteria
- The function correctly converts all words to lowercase.
- Punctuation marks are properly ignored during word counting.
- The function accurately counts the occurrences of each word in the input text.
- For an empty input string, the function returns an empty dictionary.
- Test cases should include:
  - A sentence with multiple words and punctuation.
  - An empty string.
  - A string containing only punctuation.
  - A string with repeated words in different cases and punctuation.

Arquivos do projeto:
(vazio)