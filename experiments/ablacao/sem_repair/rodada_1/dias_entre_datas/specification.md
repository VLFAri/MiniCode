# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato `AAAA-MM-DD` e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada:** Duas strings `d1` e `d2`, ambas no formato `AAAA-MM-DD`.
- **Saída:** Um número inteiro representando a diferença em dias entre as duas datas.
- **Restrições:**
  - As datas devem ser válidas; caso contrário, deve ser lançado um `ValueError`.
  - A função deve retornar um valor não negativo, independentemente da ordem das datas fornecidas.
  
## Acceptance Criteria
- A função deve aceitar duas strings no formato `AAAA-MM-DD` como entrada.
- Deve retornar um número inteiro que representa a diferença em dias entre as duas datas.
- Se qualquer uma das datas fornecidas for inválida, a função deve lançar um `ValueError`.
- A função deve funcionar corretamente para datas válidas, retornando sempre um valor não negativo.
- Testes automatizados devem verificar todas as condições acima.

Arquivos do projeto:
(vazio)