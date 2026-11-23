# Specification

## Objective
Corrigir as funções `media()` e `mediana()` no arquivo `estatistica.py` para que elas retornem os valores corretos. Adicionalmente, implementar a lógica para que uma lista vazia lance um `ValueError` em ambas as funções e garantir que a lista recebida não seja alterada.

## Parameters / Requirements
- **Entradas**: 
  - Uma lista de números (inteiros ou floats).
- **Tipos**:
  - A função `media()` deve aceitar uma lista de números (inteiros ou floats).
  - A função `mediana()` deve aceitar uma lista de números (inteiros ou floats).
- **Restrições**:
  - Se a lista for vazia, a função deve lançar um `ValueError`.
  - A lista original não deve ser modificada durante a execução das funções.
- **Regras de Negócio**:
  - A função `media()` deve calcular a média aritmética dos números na lista.
  - A função `mediana()` deve calcular a mediana dos números na lista.

## Acceptance Criteria
- As funções `media()` e `mediana()` devem funcionar corretamente com listas válidas.
- Se a lista for vazia, ambas as funções devem lançar um `ValueError`.
- A lista original não deve ser alterada após a execução das funções.
- Testes automatizados devem verificar que as funções retornam os valores corretos e que as exceções são lançadas conforme especificado.