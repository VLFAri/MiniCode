# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato AAAA-MM-DD e retorna o número inteiro de dias entre essas duas datas.

## Parameters / Requirements
- **Entrada**: Duas strings `d1` e `d2`, ambas no formato "AAAA-MM-DD".
- **Saída**: Um número inteiro representando a diferença em dias entre as duas datas.
- **Restrições**:
  - As datas devem ser válidas (por exemplo, não pode haver um mês com mais de 31 dias).
  - A função deve lidar corretamente com anos bissextos.
  - Se qualquer uma das datas fornecidas for inválida, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve retornar um valor não negativo, independentemente da ordem das datas fornecidas.
- Testes automatizados devem verificar que a função funciona corretamente para datas válidas e lança `ValueError` para datas inválidas.
- A implementação deve incluir documentação clara e exemplos de uso.

Arquivos do projeto:
(vazio)