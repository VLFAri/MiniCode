# Specification

## Objective
Implementar uma função que calcule o número de dias entre duas datas fornecidas pelo usuário.

## Parameters / Requirements
- A função `dias_entre` deve receber dois parâmetros: `d1` e `d2`, ambos strings no formato `AAAA-MM-DD`.
- Se as datas forem inválidas (por exemplo, `'30-02-2020'`), a função deve levantar uma exceção `ValueError`.
- A função deve retornar um valor inteiro representando o número de dias entre as duas datas, sempre positivo.

## Acceptance Criteria
- `dias_entre('2020-01-01', '2020-01-05')` retorna `4`
- `dias_entre('2020-02-01', '2020-02-29')` retorna `28`
- `dias_entre('2020-04-01', '2020-04-30')` retorna `30`
- `dias_entre('2020-06-01', '2020-06-30')` retorna `30`
- `dias_entre('2020-07-01', '2020-07-31')` retorna `31`
- `dias_entre('2020-08-01', '2020-08-31')` retorna `31`
- `dias_entre('2020-10-01', '2020-10-31')` retorna `31`
- `dias_entre('2020-12-01', '2020-12-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-01-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-01-32')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-02-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-02-32')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-03-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-03-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-04-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-04-31')` retorna `30`
- `dias_entre('2020-01-01', '2020-05-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-05-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-06-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-06-30')` retorna `30`
- `dias_entre('2020-01-01', '2020-07-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-07-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-08-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-08-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-09-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-09-30')` retorna `30`
- `dias_entre('2020-01-01', '2020-10-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-10-31')` retorna `31`
- `dias_entre('2020-01-01', '2020-11-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-11-30')` retorna `30`
- `dias_entre('2020-01-01', '2020-12-00')` lança `ValueError`
- `dias_entre('2020-01-01', '2020-12-31')` retorna `31`
- `dias_entre('2020-02-01', '2020-02-29')` retorna `28`
- `dias_entre('2020-02-01', '2020-02-28')` lança `ValueError`
- `dias_entre('2020-02-01', '2020-02-27')` lança `ValueError`
- `dias_entre('