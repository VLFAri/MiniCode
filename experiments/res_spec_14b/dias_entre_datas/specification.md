# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato AAAA-MM-DD e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada:** Duas strings `d1` e `d2`, ambas no formato "AAAA-MM-DD".
- **Saída:** Um número inteiro representando a diferença em dias entre as duas datas.
- **Restrições:**
  - As datas devem ser válidas (por exemplo, não pode haver um mês com mais de 31 dias).
  - A função deve ignorar a ordem das datas fornecidas e sempre retornar um valor não negativo.
  - Se qualquer uma das datas for inválida, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve aceitar duas strings no formato "AAAA-MM-DD" como entrada.
- Deve calcular corretamente a diferença em dias entre as duas datas fornecidas.
- A função deve funcionar corretamente para datas válidas e lançar `ValueError` para datas inválidas.
- Testes automatizados devem verificar que a função retorna valores corretos para diferentes casos de uso, incluindo datas válidas e inválidas.

Arquivos do projeto:
(vazio)