# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando a expressão RPN, onde os tokens são separados por espaços.
- **Tokens**: Os tokens podem ser números inteiros ou decimais, ou um dos seguintes operadores: `+`, `-`, `*`, `/`.
- **Restrições**:
  - A expressão deve ser válida, ou seja, não pode estar vazia, conter tokens desconhecidos, ou ter operandos faltando ou sobrando.
  - Deve lançar um `ValueError` para expressões inválidas.
  - Deve lançar um `ZeroDivisionError` se a divisão por zero for tentada.

## Acceptance Criteria
- A função deve aceitar uma string de entrada e retornar o resultado da avaliação da expressão RPN.
- Se a expressão for inválida, a função deve lançar um `ValueError`.
- Se a divisão por zero for tentada, a função deve lançar um `ZeroDivisionError`.
- A implementação deve incluir testes automatizados para verificar o comportamento da função em diferentes casos de uso.

Arquivos do projeto:
(vazio)