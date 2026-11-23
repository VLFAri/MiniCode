# Specification

## Objective
Corrigir as funções `media()` e `mediana()` no módulo `estatistica.py` para que elas retornem os valores corretos. Além disso, garantir que uma lista vazia lance um `ValueError` em ambas as funções e que a lista recebida não seja alterada.

## Parameters / Requirements
- **Entrada**: Uma lista de números (inteiros ou floats).
- **Saída**:
  - Para `media()`: Um float representando a média dos números na lista.
  - Para `mediana()`: Um float representando a mediana dos números na lista.
- **Restrições**:
  - Se a lista estiver vazia, a função deve lançar um `ValueError`.
  - A lista original não deve ser modificada durante a execução das funções.

## Acceptance Criteria
- A função `media()` deve calcular corretamente a média da lista de entrada.
- A função `mediana()` deve calcular corretamente a mediana da lista de entrada.
- Ambas as funções devem lançar um `ValueError` se a lista de entrada estiver vazia.
- A lista de entrada não deve ser alterada após a execução das funções.
- Os testes automatizados devem passar sem erros.