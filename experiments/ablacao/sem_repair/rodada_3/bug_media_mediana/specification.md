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
- A função `media()` deve retornar a média correta da lista de entrada.
- A função `mediana()` deve retornar a mediana correta da lista de entrada.
- Ambas as funções devem lançar um `ValueError` se a lista de entrada estiver vazia.
- A lista de entrada não deve ser alterada após a execução das funções.
- Deve haver testes automatizados para verificar cada condição acima.