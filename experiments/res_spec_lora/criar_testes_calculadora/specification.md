# Specification

## Objective
Criar uma função que realize operações matemáticas básicas como soma, subtração e divisão.

## Parameters / Requirements
- **Funções:** `somar(a, b)`, `subtrair(a, b)`, `dividir(a, b)`
- **Entrada:** Duas entradas numéricas (`int` ou `float`) representando os números a serem operados.
- **Saída:** Um número (`int` ou `float`) representando o resultado da operação.
- **Restrições:** 
  - A função `dividir(a, b)` deve levantar uma exceção `ZeroDivisionError` se o segundo argumento for zero.
  - As funções `somar`, `subtrair` e `dividir` devem retornar valores inteiros quando ambos os operandos são inteiros.

## Acceptance Criteria
- `somar(10, 5)` retorna `15`
- `subtrair(10, 5)` retorna `5`
- `dividir(10, 2)` retorna `5`
- `dividir(10, 0)` levanta `ZeroDivisionError`
- `somar('a', 'b')` levanta `TypeError`
- `subtrair('a', 'b')` levanta `TypeError`
- `dividir('a', 'b')` levanta `TypeError`
- `somar(10, 'b')` levanta `TypeError`
- `subtrair(10, 'b')` levanta `TypeError`
- `dividir(10, 'b')` levanta `TypeError`
- `somar(10, None)` levanta `TypeError`
- `subtrair(10, None)` levanta `TypeError`
- `dividir(10, None)` levanta `TypeError`
- `somar(None, 10)` levanta `TypeError`
- `subtrair(None, 10)` levanta `TypeError`
- `dividir(None, 10)` levanta `TypeError`
- `somar(10, float('inf'))` levanta `TypeError`
- `subtrair(10, float('inf'))` levanta `TypeError`
- `dividir(10, float('inf'))` levanta `TypeError`
- `somar(float('inf'), 10)` levanta `TypeError`
- `subtrair(float('inf'), 10)` levanta `TypeError`
- `dividir(float('inf'), 10)` levanta `TypeError`
- `somar(float('-inf'), 10)` levanta `TypeError`
- `subtrair(float('-inf'), 10)` levanta `TypeError`
- `dividir(float('-inf'), 10)` levanta `TypeError`
- `somar(float('nan'), 10)` levanta `TypeError`
- `subtrair(float('nan'), 10)` levanta `TypeError`
- `dividir(float('nan'), 10)` levanta `TypeError`
- `somar(int('10'), float('inf'))` levanta `TypeError`
- `subtrair(int('10'), float('inf'))` levanta `TypeError`
- `dividir(int('10'), float('inf'))` levanta `TypeError`
- `somar(float('inf'), int('10'))` levanta `TypeError`
- `subtrair(float('inf'), int('10'))` levanta `TypeError`
- `dividir(float('inf'), int('10'))` levanta `TypeError`
- `somar(float('-inf'), int('10'))` levanta `TypeError`
- `subtrair(float('-inf'), int('10'))` levanta `TypeError`
- `dividir(float('-inf'), int('10'))` levanta `TypeError`
- `somar(int('10'), float('nan'))` levanta `TypeError`
- `subtrair(int('10'), float('nan'))` levanta `TypeError`
- `dividir(int('10'), float('nan'))` levanta `TypeError`
- `somar(float('nan'), int('10'))` levanta `TypeError`
- `subtrair(float('nan'), int('10'))` levanta `TypeError`
- `dividir(float('nan'), int('10'))` levanta `TypeError`
- `somar(int('10'), None)` levanta `TypeError`
- `subtrair(int('10'), None)` levanta `TypeError`
- `dividir(int('10'), None)` levanta `TypeError`
- `somar(None, int('10'))` levanta `TypeError`
- `subtrair(None, int('10'))` levanta `TypeError`
- `dividir(None, int('10'))` levanta `TypeError`
- `somar(int('10'), float('inf'))` levanta `TypeError`
- `subtrair(int('10'), float('inf'))` levanta `TypeError`
- `dividir(int('10'), float('inf'))` levanta `TypeError`
- `somar(float('inf'), int('10'))` levanta `TypeError`
- `subtrair(float('inf'), int('10'))` levanta `TypeError`
- `dividir(float('inf'), int('10'))` levanta `TypeError`
- `somar(float('-inf'), int('10'))` levanta `TypeError`
- `subtrair(float('-inf'), int('10'))` levanta `TypeError`
- `dividir(float('-inf'), int('10'))` levanta `TypeError`
- `somar(int('10'), float('nan'))` levanta `TypeError`
- `subtrair(int('10'), float('nan'))` levanta `TypeError`
- `dividir(int('10'), float('nan'))` levanta `TypeError`
- `somar(float('nan'), int('10'))` levanta `TypeError`
- `subtrair(float('nan'), int('10'))` levanta `TypeError`
- `dividir(float('nan'), int('10'))` levanta `TypeError`
- `somar(int('10'), None)` levanta `TypeError`
- `subtrair(int('10'), None)` levanta `TypeError