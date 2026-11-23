# Specification

## Objective
Corrigir as funções `media()` e `mediana()` no módulo `estatistica.py` para que elas retornem os valores corretos. Além disso, garantir que uma lista vazia lance um `ValueError` em ambas as funções e que a lista recebida não seja alterada.

## Parameters / Requirements
- **Entrada:** Uma lista de números (inteiros ou floats).
- **Tipo:** A função aceita uma lista de números.
- **Restrições:** 
  - Se a lista estiver vazia, a função deve lançar um `ValueError`.
  - A lista de entrada não deve ser modificada pela função.
- **Regras de Negócio:**
  - A função `media()` deve calcular a média dos números na lista.
  - A função `mediana()` deve calcular a mediana dos números na lista.

## Acceptance Criteria
- A função `media()` deve retornar a média correta da lista de entrada.
- A função `mediana()` deve retornar a mediana correta da lista de entrada.
- Se a lista de entrada estiver vazia, ambas as funções (`media()` e `mediana()`) devem lançar um `ValueError`.
- A lista de entrada não deve ser alterada após a execução das funções.
- Os testes automatizados devem verificar se as funções funcionam conforme especificado acima.