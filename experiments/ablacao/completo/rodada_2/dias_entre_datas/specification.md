# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato `AAAA-MM-DD` e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada**: Duas strings `d1` e `d2`, ambas no formato `AAAA-MM-DD`.
- **Saída**: Um número inteiro representando a diferença em dias entre as duas datas.
- **Restrições**:
  - As datas devem ser válidas; caso contrário, deve ser lançado um `ValueError`.
  - A função deve retornar um valor não negativo, independentemente da ordem das datas fornecidas.
  
## Acceptance Criteria
- A função deve aceitar duas strings no formato `AAAA-MM-DD`.
- Deve calcular corretamente a diferença em dias entre as duas datas.
- Se uma ou ambas as datas forem inválidas, deve ser lançado um `ValueError`.
- A função deve funcionar para todas as datas válidas dentro do intervalo suportado pelo módulo datetime do Python.
- Testes automatizados devem verificar que a função retorna valores corretos para datas válidas e levanta `ValueError` para datas inválidas.

Arquivos do projeto:
(vazio)