# Specification

## Objective
Implementar uma função que calcule a frequência de palavras em um texto fornecido como entrada.

## Parameters / Requirements
- A função `frequencia_palavras` recebe um único parâmetro: `texto` (string), representando o texto de entrada.
- O texto deve ser convertido para minúsculas antes de processá-lo.
- As palavras devem ser separadas pelo caractere espaço (' ') e ignoradas as pontuações (`.,!?;:`).
- Se o texto for vazio, a função retorna um dicionário vazio.

## Acceptance Criteria
- `frequencia_palavras("Hello world!")` retorna `{ 'hello': 1, 'world': 1 }`
- `frequencia_palavras("Python is fun")` retorna `{ 'python': 1, 'is': 1, 'fun': 1 }`
- `frequencia_palavras("")` retorna `{ }`
- `frequencia_palavras("One two three one two")` retorna `{ 'one': 2, 'two': 2, 'three': 1 }`
- `frequencia_palavras("With punctuation! And numbers 123.")` retorna `{ 'with': 1, 'punctuation': 1, 'and': 1, 'numbers': 1, '123': 1 }`
- `frequencia_palavras("CAPITALIZATION")` retorna `{ 'capitalization': 1 }`
- `frequencia_palavras("ALL CAPS")` retorna `{ 'all': 1, 'caps': 1 }`
- `frequencia_palavras("lowercase")` retorna `{ 'lowercase': 1 }`
- `frequencia_palavras("UPPERCASE")` retorna `{ 'uppercase': 1 }`
- `frequencia_palavras("Mixed CASE")` retorna `{ 'mixed': 1, 'case': 1 }`
- `frequencia_palavras("No words here!")` retorna `{ }`
- `frequencia_palavras("Spaces only")` retorna `{ }`
- `frequencia_palavras("Punctuation marks: !@#$%^&*()_+-=[]{}|\\;',.<>?/`) retorna `{ 'punctuationmarks': 1 }`