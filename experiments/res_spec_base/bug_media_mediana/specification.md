# Specification

## Objective
O objetivo deste projeto é corrigir os erros na implementação das funções `media()` e `mediana()` no arquivo `estatistica.py`. A função `media()` deve retornar a média dos elementos da lista, e a função `mediana()` deve retornar a mediana dos elementos da lista. Ambas as funções devem lançar um `ValueError` se a lista for vazia.

## Parameters / Requirements
- **Entradas**: 
  - Uma lista de números (float ou int) como entrada para as funções `media()` e `mediana()`.
  
- **Tipos**:
  - Os elementos da lista podem ser float ou int.
  
- **Restrições e Regras de Negócio**:
  - Não é permitido alterar a lista original passada para as funções `media()` e `mediana()`.
  
- **Avaliação**:
  - As funções devem retornar o valor correto para cada caso de teste.
  - Se a lista for vazia, ambas as funções devem lançar um `ValueError`.

## Acceptance Criteria
1. **Teste 1**: Verificar se a função `media()` retorna a média correta para uma lista com números positivos.
2. **Teste 2**: Verificar se a função `media()` retorna a média correta para uma lista com números negativos.
3. **Teste 3**: Verificar se a função `media()` retorna a média correta para uma lista com números positivos e negativos.
4. **Teste 4**: Verificar se a função `media()` lança um `ValueError` quando a lista está vazia.
5. **Teste 5**: Verificar se a função `mediana()` retorna a mediana correta para uma lista com números positivos.
6. **Teste 6**: Verificar se a função `mediana()` retorna a mediana correta para uma lista com números negativos.
7. **Teste 7**: Verificar se a função `mediana()` retorna a mediana correta para uma lista com números positivos e negativos.
8. **Teste 8**: Verificar se a função `mediana()` lança um `ValueError` quando a lista está vazia.

## Arquivos do projeto
- estatistica.py

### Pedido do Utilizador
O módulo `estatistica.py` tem bugs: `media()` e `mediana()` devolvem valores errados. Corrija as duas funções. Lista vazia deve lançar ValueError em ambas, e a lista recebida não pode ser alterada.