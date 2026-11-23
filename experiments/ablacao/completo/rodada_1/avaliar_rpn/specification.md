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
- A função deve aceitar uma string válida de RPN e retornar o valor correto da expressão.
- A função deve lançar `ValueError` para entradas inválidas.
- A função deve lançar `ZeroDivisionError` para divisões por zero.
- Deve haver testes automatizados que verifiquem todos os casos acima.

Arquivos do projeto:
(vazio)