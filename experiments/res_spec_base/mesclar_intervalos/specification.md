# Specification

## Objective
O objetivo deste projeto é criar uma função `mesclar_intervalos` no arquivo `intervalos.py`, que recebe uma lista de tuplas representando intervalos e retorna essa lista ordenada com os intervalos sobrepostos ou que se tocam mesclados.

## Parameters / Requirements
- A entrada deve ser uma lista de tuplas `(inicio, fim)` onde `inicio` e `fim` são números inteiros.
- Os intervalos podem estar desordenados na entrada.
- O resultado deve ser uma lista de tuplas ordenada com os intervalos sobrepostos ou que se tocam mesclados.

## Acceptance Criteria
- A função deve retornar uma lista de tuplas ordenada.
- Se dois intervalos se tocam ou se sobrepõem, eles devem ser combinados em um único intervalo.
- Os intervalos devem permanecer independentes dos outros.

## Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie intervalos.py com a função mesclar_intervalos(lista) que receba uma lista de tuplas (inicio, fim), possivelmente desordenada, e devolva a lista de tuplas ordenada com os intervalos sobrepostos ou que se tocam mesclados. Exemplo: [(1, 3), (2, 6), (8, 10)] vira [(1, 6), (8, 10)].