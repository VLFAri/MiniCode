# Specification

## Objective
O objetivo deste projeto é criar uma função `eh_data_valida` em Python que verifica se um texto fornecido representa uma data válida no formato `dd/mm/yyyy`, considerando anos bissextos.

## Parameters / Requirements
- O parâmetro `texto` deve ser uma string que contém uma data no formato `dd/mm/yyyy`.

## Acceptance Criteria
A função deve retornar `True` se a data fornecida é válida, ou `False` caso contrário.

### Test Cases
1. `eh_data_valida("05/03/2024")` deve retornar `True`.
2. `eh_data_valida("31/02/2024")` deve retornar `False`.
3. `eh_data_valida("01/01/2023")` deve retornar `True`.
4. `eh_data_valida("15/06/2024")` deve retornar `True`.
5. `eh_data_valida("00/00/2024")` deve retornar `False`.
6. `eh_data_valida("13/04/2024")` deve retornar `False`.
7. `eh_data_valida("29/02/2020")` deve retornar `True`.
8. `eh_data_valida("29/02/2021")` deve retornar `False`.
9. `eh_data_valida("12/31/2024")` deve retornar `True`.
10. `eh_data_valida("01/01/2025")` deve retornar `True`.

### Arquivos do projeto
(vazio)

Pedido do utilizador: Crie datas_br.py com a função eh_data_valida(texto) que devolva True se o texto for uma data real no formato dd/mm/aaaa (com zeros à esquerda, ex.: 05/03/2024), considerando anos bissextos, e False caso contrário.