# Specification

## Objective
O objetivo deste projeto é criar uma função `segundos` no arquivo `duracao.py` que recebe uma string representando uma duração e retorna o valor correspondente em segundos.

## Parameters / Requirements
A função `segundos` deve aceitar uma string com a seguinte sintaxe:
- Uma quantidade de horas (h)
- Uma quantidade de minutos (m)
- Uma quantidade de segundos (s)
- A ordem das unidades deve ser h, m e s
- Não há espaços entre as unidades

Se a entrada for vazia ou não estiver na forma solicitada, a função deve lançar um `ValueError`.

## Acceptance Criteria
Os seguintes critérios devem ser atendidos para considerar a implementação concluída e válida:

1. A função `segundos` deve retornar o valor correto em segundos para diferentes entradas.
2. Se a entrada for vazia ou não estiver na forma solicitada, a função deve lançar um `ValueError`.
3. A função deve ser capaz de lidar com entradas com múltiplas unidades (por exemplo, '2h30m').
4. A função deve ser capaz de lidar com entradas com números negativos (por exemplo, '-1h30m').

## Arquivos do projeto
(vazio)

Pedido do utilizador: Crie duracao.py com a função para_segundos(texto) que converta uma duração como '1h30m15s' em segundos. Aceite qualquer combinação de horas (h), minutos (m) e segundos (s), nessa ordem e sem espaços (ex.: '2h', '90m', '45s'). Texto vazio ou em formato inválido lança ValueError.