# Specification

## Objective
Implementar uma função `dias_entre` que recebe duas strings representando datas no formato `AAAA-MM-DD` e retorna o número inteiro de dias entre as duas datas.

## Parameters / Requirements
- **Entrada**: Dois parâmetros de entrada, ambos strings (`str`), representando datas no formato `YYYY-MM-DD`.
- **Restrições**:
  - As entradas devem ser válidas conforme o formato `YYYY-MM-DD`. Se uma das entradas estiver fora desse formato, deve ser lançado um `ValueError`.
  - A função deve retornar um valor numérico inteiro não negativo, representando a diferença em dias entre as duas datas.
- **Regras de Negócio**:
  - A função deve calcular corretamente a diferença entre duas datas válidas.
  - A ordem das datas na chamada da função não afeta o resultado final, ou seja, `dias_entre('2023-01-01', '2023-01-05')` deve dar o mesmo resultado que `dias_entre('2023-01-05', '2023-01-01')`.

## Acceptance Criteria
- A função deve aceitar duas strings no formato `YYYY-MM-DD` como argumentos.
- A função deve retornar um número inteiro não negativo que representa a diferença em dias entre as duas datas.
- A função deve lançar um `ValueError` se qualquer uma das datas fornecidas não estiver no formato correto.
- Deve haver testes automatizados para verificar que a função funciona corretamente com datas válidas e lança exceções quando necessário.

Arquivos do projeto:
(vazio)