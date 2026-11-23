# Specification

## Objective
Implementar duas funções no arquivo `texto.py`: `eh_palindromo` e `contar_vogais`. Ambas funções devem ignorar maiúsculas, espaços e pontuação ao avaliar se uma string é um palíndromo ou contar as vogais presentes nessa string.

## Parameters / Requirements
- **Função `eh_palindromo(texto)`**:
  - Recebe uma string como parâmetro.
  - Retorna `True` se a string for um palíndromo (igual quando lida da esquerda para direita e vice-versa), considerando apenas letras minúsculas e sem espaços ou pontuação.
  - Exemplos:
    - `eh_palindromo("Anotaram a data da maratona")` retorna `True`
    - `eh_palindromo("Ola mundo!")` retorna `False`

- **Função `contar_vogais(texto)`**:
  - Recebe uma string como parâmetro.
  - Retorna o número total de vogais presentes na string, considerando tanto letras minúsculas quanto maiúsculas e acentuadas.
  - Exemplos:
    - `contar_vogais("Anotaram a data da maratona")` retorna `10`
    - `contar_vogais("Python é incrível!")` retorna `9`

## Acceptance Criteria
- `eh_palindromo("Anotaram a data da maratona")` retorna `True`
- `eh_palindromo("Ola mundo!")` retorna `False`
- `contar_vogais("Anotaram a data da maratona")` retorna `10`
- `contar_vogais("Python é incrível!")` retorna `9`
- `contar_vogais("1234567890")` retorna `0`
- `contar_vogais("AEIOUaeiou")` retorna `10`
- `contar_vogais("abcdeFGHIJKLMNOPQRSTUVWXYZ")` retorna `5`
- `contar_vogais("aBcDeFgHiJkLmNoPqRsTuVwXyZ")` retorna `21`
- `contar_vogais("AeIoU")` retorna `5`
- `contar_vogais("")` retorna `0`
- `contar_vogais("1234567890!@#$%^&*()_+-=[]{}|\\;',.<>?/` retorna `0`
- `contar_vogais("Um palíndromo é uma frase que pode ser lida da mesma forma tanto da esquerda para direita quanto da direita para esquerda.")` retorna `20`