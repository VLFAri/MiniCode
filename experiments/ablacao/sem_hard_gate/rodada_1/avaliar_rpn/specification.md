# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada**: Uma string representando a expressão RPN, onde os tokens são separados por espaços. Os tokens podem ser números inteiros ou decimais, ou um dos seguintes operadores: `+`, `-`, `*`, `/`.
- **Saída**: O resultado da avaliação da expressão RPN como um número (inteiro ou decimal).
- **Restrições**:
  - A função deve lançar um `ValueError` se a expressão for vazia, conter tokens desconhecidos, ou se houver operandos faltando ou sobrando.
  - A função deve lançar um `ZeroDivisionError` se a divisão por zero for tentada.

## Acceptance Criteria
- A função deve aceitar uma string válida de expressão RPN e retornar o valor correto da avaliação.
- A função deve lançar `ValueError` para entradas inválidas conforme descrito acima.
- A função deve lançar `ZeroDivisionError` quando uma divisão por zero é tentada.
- Deve haver testes automatizados que verifiquem todos os casos mencionados nos critérios de aceitação.

Arquivos do projeto:
(vazio)