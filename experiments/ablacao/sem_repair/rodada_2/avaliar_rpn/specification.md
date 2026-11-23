# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando uma expressão RPN válida, onde os tokens são separados por espaços. Os tokens podem ser números inteiros ou decimais, ou um dos seguintes operadores: `+`, `-`, `*`, `/`.
- **Restrições**:
  - A função deve lançar um `ValueError` se a expressão for vazia, conter tokens desconhecidos, ou se houver operandos faltando ou sobrando.
  - A função deve lançar um `ZeroDivisionError` se a divisão por zero for tentada.

## Acceptance Criteria
- A função deve aceitar uma string de entrada e retornar o resultado da avaliação da expressão RPN.
- A função deve lançar `ValueError` para entradas inválidas conforme descrito acima.
- A função deve lançar `ZeroDivisionError` se a divisão por zero for tentada durante a avaliação da expressão.
- Deve haver testes automatizados que verifiquem corretamente cada caso de uso, incluindo entradas válidas e inválidas.

Arquivos do projeto:
(vazio)