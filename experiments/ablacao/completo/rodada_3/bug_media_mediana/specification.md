# Specification

## Objective
Corrigir as funções `media()` e `mediana()` no módulo `estatistica.py` para que elas retornem os valores corretos. Além disso, garantir que uma lista vazia lance um `ValueError` em ambas as funções e que a lista recebida não seja alterada.

## Parameters / Requirements
- **Entradas**: 
  - Uma lista de números (inteiros ou floats).
- **Tipos**:
  - A função `media()` deve aceitar uma lista de números e retornar um número (float).
  - A função `mediana()` deve aceitar uma lista de números e retornar um número (float).
- **Restrições**:
  - Se a lista de entrada for vazia, a função deve lançar um `ValueError`.
  - A lista de entrada não deve ser modificada durante a execução das funções.
- **Regras de Negócio**:
  - A função `media()` deve calcular a média aritmética dos números na lista.
  - A função `mediana()` deve calcular a mediana dos números na lista.

## Acceptance Criteria
- A função `media()` deve retornar a média correta da lista de entrada.
- A função `mediana()` deve retornar a mediana correta da lista de entrada.
- Ambas as funções devem lançar um `ValueError` se a lista de entrada estiver vazia.
- A lista de entrada não deve ser alterada após a execução das funções.
- Os testes automatizados devem passar sem erros para validar as correções.