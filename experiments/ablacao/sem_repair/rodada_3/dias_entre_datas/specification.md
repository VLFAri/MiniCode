# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato `AAAA-MM-DD` e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada**: Duas strings `d1` e `d2`, ambas no formato `AAAA-MM-DD`.
- **Saída**: Um número inteiro representando a diferença em dias entre as duas datas.
- **Restrições**:
  - As datas devem ser válidas (por exemplo, 2023-02-30 não é uma data válida).
  - A função deve lidar corretamente com datas que estão na mesma dia, mês ou ano.
  - Se qualquer uma das datas fornecidas for inválida, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve retornar um valor numérico inteiro não negativo.
- A função deve funcionar corretamente para datas válidas.
- A função deve lançar um `ValueError` se qualquer uma das datas fornecidas for inválida.
- Testes automatizados devem verificar todas as condições acima.

Arquivos do projeto:
(vazio)