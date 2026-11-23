# Specification

## Objective
Implementar uma função que valide se um texto representa uma data válida no formato DD/MM/YYYY, considerando anos bissextos.

## Parameters / Requirements
- A função `eh_data_valida` deve receber uma string como parâmetro.
- A string deve seguir o formato DD/MM/YYYY, onde DD é um número inteiro entre 01 e 31, MM é um número inteiro entre 01 e 12, e YYYY é um número inteiro válido para anos bissextos.
- Um ano é bissexto se ele é divisível por 4 mas não por 100, exceto quando é divisível por 400.
- Se a entrada não corresponder ao formato esperado ou não for uma data válida, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- `eh_data_valida("05/03/2024")` retorna `True`
- `eh_data_valida("31/02/2020")` retorna `False`
- `eh_data_valida("01/01/2000")` retorna `True`
- `eh_data_valida("01/01/2001")` lança `ValueError`
- `eh_data_valida("01/01/20000")` lança `ValueError`
- `eh_data_valida("01/01/abc")` lança `ValueError`
- `eh_data_valida("01/01/")` lança `ValueError`
- `eh_data_valida("")` lança `ValueError`
- `eh_data_valida("13/02/2020")` lança `ValueError`
- `eh_data_valida("00/00/0000")` lança `ValueError`
- `eh_data_valida("00/00/0001")` lança `ValueError`
- `eh_data_valida("00/00/0002")` lança `ValueError`
- `eh_data_valida("00/00/0003")` lança `ValueError`
- `eh_data_valida("00/00/0004")` lança `ValueError`
- `eh_data_valida("00/00/0005")` lança `ValueError`
- `eh_data_valida("00/00/0006")` lança `ValueError`
- `eh_data_valida("00/00/0007")` lança `ValueError`
- `eh_data_valida("00/00/0008")` lança `ValueError`
- `eh_data_valida("00/00/0009")` lança `ValueError`
- `eh_data_valida("00/00/0010")` lança `ValueError`
- `eh_data_valida("00/00/0011")` lança `ValueError`
- `eh_data_valida("00/00/0012")` lança `ValueError`
- `eh_data_valida("00/00/0013")` lança `ValueError`
- `eh_data_valida("00/00/0014")` lança `ValueError`
- `eh_data_valida("00/00/0015")` lança `ValueError`
- `eh_data_valida("00/00/0016")` lança `ValueError`
- `eh_data_valida("00/00/0017")` lança `ValueError`
- `eh_data_valida("00/00/0018")` lança `ValueError`
- `eh_data_valida("00/00/0019")` lança `ValueError`
- `eh_data_valida("00/00/0020")` lança `ValueError`
- `eh_data_valida("00/00/0021")` lança `ValueError`
- `eh_data_valida("00/00/0022")` lança `ValueError`
- `eh_data_valida("00/00/0023")` lança `ValueError`
- `eh_data_valida("00/00/0024")` lança `ValueError`
- `eh_data_valida("00/00/0025")` lança `ValueError`
- `eh_data_valida("00/00/0026")` lança `ValueError`
- `eh_data_valida("00/00/0027")` lança `ValueError`
- `eh_data_valida("00/00/0028")` lança `ValueError`
- `eh_data_valida("00/00/0029")` lança `ValueError`
- `eh_data_valida("00/00/0030")` lança `ValueError`
- `eh_data_valida("00/00/0031")` lança `ValueError`
- `eh_data_valida("00/00/0032")` lança `ValueError`
- `eh_data_valida("00/00/0033")` lança `ValueError`
- `eh_data_valida("00/00/0034")` lança `ValueError`
- `eh_data_valida("00/00/0035")` lança `ValueError`
- `eh_data_valida("00/00/0036")` lança `ValueError`
- `eh_data_valida("00/00/0037")` lança `ValueError`
- `eh_data_valida("00/00/0038")` lança `ValueError`
- `eh_data_valida("00/00/0039")` lança `ValueError`
- `eh_data_valida("00/00/0040")` lança `ValueError`
- `eh_data_valida("00/00/0041")` lança `ValueError`
- `eh_data_valida("00/00