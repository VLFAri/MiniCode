# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando a expressão RPN, onde os tokens são separados por espaços. Os tokens podem ser números inteiros ou decimais, ou os operadores `+`, `-`, `*`, `/`.
- **Saída**: O resultado da avaliação da expressão RPN como um número (inteiro ou decimal).
- **Restrições**:
  - A função deve lançar um `ValueError` se a expressão for inválida (por exemplo, vazia, token desconhecido, operandos faltando ou sobrando).
  - A função deve lançar um `ZeroDivisionError` se ocorrer uma tentativa de divisão por zero.

## Acceptance Criteria
- A função deve aceitar uma string válida de expressão RPN e retornar o valor correto da avaliação.
- A função deve lançar `ValueError` para entradas inválidas, incluindo strings vazias, tokens desconhecidos, operandos faltando ou sobrando.
- A função deve lançar `ZeroDivisionError` quando houver uma tentativa de divisão por zero.

Arquivos do projeto:
(vazio)