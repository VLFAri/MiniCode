# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando a expressão RPN, onde os tokens são separados por espaços.
- **Tokens**: Os tokens podem ser números inteiros ou decimais, ou um dos seguintes operadores: `+`, `-`, `*`, `/`.
- **Restrições**:
  - A expressão deve ser válida, ou seja, não pode estar vazia, conter tokens desconhecidos, ou ter um número incorreto de operandos para os operadores presentes.
  - Deve lançar um `ValueError` se a expressão for inválida.
  - Deve lançar um `ZeroDivisionError` se ocorrer uma tentativa de divisão por zero.

## Acceptance Criteria
- A função deve aceitar uma string de entrada e retornar o resultado da avaliação da expressão RPN.
- Se a expressão for inválida, a função deve lançar um `ValueError`.
- Se houver uma tentativa de divisão por zero, a função deve lançar um `ZeroDivisionError`.
- A função deve ser capaz de lidar com números inteiros e decimais corretamente.
- Testes automatizados devem verificar que a função funciona conforme esperado para uma variedade de entradas válidas e inválidas.

Arquivos do projeto:
(vazio)