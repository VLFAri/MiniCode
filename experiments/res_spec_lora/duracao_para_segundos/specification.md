# Specification

## Objective
Implementar uma função `segundos` que receba uma string no formato `'HHHhMMMmSSSs'`, onde cada parte pode ser opcional e pode conter zeros à esquerda, retornando o valor correspondente em segundos.

## Parameters / Requirements
- A função deve aceitar uma única string como parâmetro.
- Se a string não for válida (por exemplo, contém letras ou caracteres especiais), a função deve lançar uma exceção `ValueError`.
- As unidades são obrigatórias e devem estar presentes na sequência H, M, S.
- Os valores podem ter até 2 dígitos após a unidade correspondente (por exemplo, '1h' representa 60 segundos).
- Se a string estiver vazia ou não corresponder ao formato esperado, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- `segundos('1h30m15s')` retorna `4515`
- `segundos('2h')` retorna `7200`
- `segundos('90m')` retorna `5400`
- `segundos('45s')` retorna `45`
- `segundos('1h30m')` retorna `5400`
- `segundos('1h30')` lança `ValueError`
- `segundos('1h30m15')` lança `ValueError`
- `segundos('1h30m15s')` lança `ValueError`
- `segundos('1h30m15s ')` lança `ValueError`
- `segundos('1h30m15s0')` lança `ValueError`
- `segundos('1h30m15s00')` lança `ValueError`
- `segundos('1h30m15s000')` lança `ValueError`
- `segundos('1h30m15s0000')` lança `ValueError`
- `segundos('1h30m15s00000')` lança `ValueError`
- `segundos('1h30m15s000000')` lança `ValueError`
- `segundos('1h30m15s0000000')` lança `ValueError`
- `segundos('1h30m15s00000000')` lança `ValueError`
- `segundos('1h30m15s000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s000000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s00000000000000000000000000000')` lança `ValueError`
- `segundos('1h30m15s0000000000