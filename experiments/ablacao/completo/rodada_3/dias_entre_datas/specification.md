# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato AAAA-MM-DD e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada:** Duas strings `d1` e `d2`, ambas no formato "AAAA-MM-DD".
- **Saída:** Um número inteiro representando a diferença absoluta em dias entre as duas datas.
- **Restrições:**
  - As entradas devem ser válidas conforme o formato especificado.
  - A função deve retornar um valor não negativo, independentemente da ordem das datas fornecidas.
  - Se qualquer uma das datas for inválida, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve aceitar duas strings no formato "AAAA-MM-DD" como entrada.
- Deve calcular corretamente a diferença absoluta em dias entre as duas datas.
- A função deve funcionar corretamente para todas as datas válidas dentro do intervalo suportado pelo módulo datetime.
- Se qualquer uma das datas fornecidas não estiver no formato correto ou for inválida, a função deve lançar um `ValueError`.
- Testes automatizados devem verificar que a função retorna valores corretos para diferentes casos de uso, incluindo datas extremas e datas inválidas.

Arquivos do projeto:
(vazio)