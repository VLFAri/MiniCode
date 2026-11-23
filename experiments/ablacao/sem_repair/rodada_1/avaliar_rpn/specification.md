# Specification

## Objective
Implementar uma função `avaliar_rpn` no arquivo `rpn.py` que avalie uma expressão em notação polonesa reversa (RPN).

## Parameters / Requirements
- **Entrada:** Uma string representando a expressão RPN, onde os tokens são separados por espaços.
- **Tokens válidos:** Números inteiros ou decimais e os operadores matemáticos básicos `+`, `-`, `*`, `/`.
- **Restrições:** A expressão deve ser válida, ou seja, não pode estar vazia, conter tokens desconhecidos, ou ter um número incorreto de operandos para os operadores presentes.
- **Regras de negócio:** 
  - Se a expressão for inválida, a função deve lançar um `ValueError`.
  - Se ocorrer uma divisão por zero, a função deve lançar um `ZeroDivisionError`.

## Acceptance Criteria
- A função `avaliar_rpn` deve aceitar uma string de entrada e retornar o resultado da avaliação da expressão RPN.
- A função deve lançar `ValueError` se a expressão estiver vazia, conter tokens desconhecidos, ou ter um número incorreto de operandos para os operadores presentes.
- A função deve lançar `ZeroDivisionError` se ocorrer uma tentativa de divisão por zero.

Arquivos do projeto:
(vazio)