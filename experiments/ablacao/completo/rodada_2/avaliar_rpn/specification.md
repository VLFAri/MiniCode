# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando uma expressão em RPN, onde os tokens são separados por espaços. Os tokens podem ser números inteiros ou decimais, ou um dos seguintes operadores: `+`, `-`, `*`, `/`.
- **Saída**: O resultado da avaliação da expressão RPN como um número (inteiro ou decimal).
- **Restrições**:
  - A função deve lançar um `ValueError` se a expressão for vazia, conter tokens desconhecidos, ou se houver operandos faltando ou sobrando.
  - A função deve lançar um `ZeroDivisionError` se a expressão incluir uma divisão por zero.

## Acceptance Criteria
- A função deve aceitar uma string válida em notação polonesa reversa e retornar o resultado correto da avaliação.
- A função deve lançar `ValueError` para as seguintes condições:
  - A entrada é uma string vazia.
  - A entrada contém um token que não é reconhecido como um número ou um operador válido.
  - A entrada tem menos ou mais operandos do que os operadores presentes na expressão.
- A função deve lançar `ZeroDivisionError` se a expressão incluir uma divisão por zero.

Arquivos do projeto:
(vazio)