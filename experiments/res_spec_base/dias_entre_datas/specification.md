# Specification

## Objective
O objetivo deste projeto é criar uma função `dias_entre` no arquivo `datas.py`, que recebe duas datas no formato AAAA-MM-DD e retorna o número inteiro de dias entre elas, considerando sempre que a data de início seja anterior à data final.

## Parameters / Requirements
- A função `dias_entre` deve receber duas entradas:
  - `d1`: Uma string representando a primeira data no formato AAAA-MM-DD.
  - `d2`: Uma string representando a segunda data no formato AAAA-MM-DD.
  
- As datas devem ser validas para o cálculo dos dias entre elas. Caso alguma das datas seja inválida, a função deve lançar um `ValueError`.

- O resultado da função deve ser um número inteiro positivo ou zero, independente da ordem das datas fornecidas.

## Acceptance Criteria
- A função `dias_entre` deve funcionar corretamente para todas as combinações possíveis de datas válidas.
- Se as datas forem iguais, a função deve retornar 0.
- Se a data de início for posterior à data final, a função deve retornar um erro.
- A função deve ser robusta contra erros de entrada e formato inválido.

## Arquivos do projeto
(vazio)

Pedido do utilizador: Crie datas.py com a função dias_entre(d1, d2) que receba duas datas no formato AAAA-MM-DD e devolva o número inteiro de dias entre elas (sempre não negativo, independentemente da ordem). Datas inválidas lançam ValueError.