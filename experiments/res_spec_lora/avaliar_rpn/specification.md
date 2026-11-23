# Specification

## Objective
Implementar uma função que avalie uma expressão matemática escrita na Notação Polonesa Reversa (RPN). A função deve receber uma string contendo os tokens da expressão separados por espaços e retornar o resultado da avaliação.

## Parameters / Requirements
- **Entrada:** Uma única string contendo os tokens da expressão RPN, separados por espaços.
- **Saída:** O resultado da avaliação da expressão RPN como um número float.
- **Restrições:**
  - Se a expressão estiver vazia, lançar `ValueError`.
  - Se algum dos tokens não for um número válido ou um operador válido (+, -, *, /), lançar `ValueError`.
  - Se houver uma divisão por zero, lançar `ZeroDivisionError`.
  - Se houver sobra algum operando após a avaliação, lançar `ValueError`.

## Acceptance Criteria
- `avaliar_rpn("10 20 +")` retorna `30.0`
- `avaliar_rpn("5 6 * 7 +")` retorna `49.0`
- `avaliar_rpn("10 20 /")` lança `ZeroDivisionError`
- `avaliar_rpn("10 20 + 30 *")` lança `ValueError`
- `avaliar_rpn("")` lança `ValueError`
- `avaliar_rpn("10 abc +")` lança `ValueError`
- `avaliar_rpn("10 20 30 + *")` lança `ValueError`
- `avaliar_rpn("10 20 30 / +")` lança `ZeroDivisionError`
- `avaliar_rpn("10 20 30 * +")` retorna `80.0`
- `avaliar_rpn("10 20 30 / -")` retorna `-10.0`
- `avaliar_rpn("10 20 30 * /")` lança `ZeroDivisionError`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 30 + * /")` retorna `80.0`
- `avaliar_rpn("10 20 3