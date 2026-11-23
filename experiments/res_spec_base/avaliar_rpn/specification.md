# Specification

## Objective
O objetivo deste projeto é criar uma função `avaliar_rpn` no arquivo `rpn.py`, capaz de avaliar expressões em notação polonesa reversa (RPN). A função deve receber uma string contendo as operações e operandos separados por espaços e retornar o resultado da avaliação.

## Parameters / Requirements
- **Entradas**: Uma única string `expressao` contendo as operações e operandos separados por espaços.
- **Tipos**:
  - Operações: `+`, `-`, `*`, `/`.
  - Operandos: Números inteiros e floats.
- **Restrições e Regras de Negociação**:
  - A expressão deve ser válida, isto é, não pode conter tokens desconhecidos, operações inválidas, ou operações que resultem em resultados inválidos.
  - Não há necessidade de tratamento de exceções para divisão por zero, pois a função já lança ZeroDivisionError quando necessário.
- **Critérios Claros e Verificáveis por Testes Automatizados**:
  - A função deve retornar o resultado correto para todas as expressões válidas fornecidas.
  - A função deve lançar ValueError para expressões inválidas.
  - A função deve lançar ZeroDivisionError para expressões onde a divisão por zero ocorre.

## Acceptance Criteria
1. A função `avaliar_rpn` deve aceitar uma string `expressao` como entrada.
2. A função deve retornar o resultado da avaliação da expressão em RPN.
3. A função deve lançar ValueError se a expressão for inválida.
4. A função deve lançar ZeroDivisionError se a expressão contiver uma divisão por zero.

## Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie rpn.py com a função avaliar_rpn(expressao) que avalie uma expressão em notação polonesa reversa, com tokens separados por espaço, números e os operadores + - * /. Expressão inválida (vazia, token desconhecido, operandos faltando ou sobrando) lança ValueError; divisão por zero lança ZeroDivisionError.