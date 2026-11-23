# Specification

## Objective
Corrigir as funções `media()` e `mediana()` no módulo `estatistica.py` para que elas retornem os valores corretos. Adicionalmente, implementar a lógica para que uma lista vazia lance um `ValueError` em ambas as funções e garantir que a lista recebida não seja alterada.

## Parameters / Requirements
- **Entrada:** Uma lista de números (inteiros ou floats).
- **Tipo:** A função aceita uma lista de números.
- **Restrições:** 
  - Se a lista estiver vazia, a função deve lançar um `ValueError`.
  - A lista original não deve ser modificada.
- **Regras de Negócio:**
  - A função `media()` deve calcular a média dos números na lista.
  - A função `mediana()` deve calcular a mediana dos números na lista.

## Acceptance Criteria
- A função `media()` deve retornar o valor correto da média dos números na lista.
- A função `mediana()` deve retornar o valor correto da mediana dos números na lista.
- Se a lista estiver vazia, ambas as funções (`media()` e `mediana()`) devem lançar um `ValueError`.
- A lista original não deve ser alterada após a execução das funções.
- Os testes automatizados devem passar sem erros, validando que as funções estão funcionando corretamente.