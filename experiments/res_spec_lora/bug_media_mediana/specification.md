# Specification

## Objective
Corrigir os métodos `media()` e `mediana()` no módulo `estatistica.py` para que eles funcione corretamente.

## Parameters / Requirements
- **Entrada:** Uma lista de números inteiros (`int`) ou floats (`float`).
- **Restrições:** A função deve lançar uma exceção `ValueError` se a lista estiver vazia.
- **Retorno:** Se a lista contém pelo menos um elemento, a função retorna o valor médio (média) e a mediana da lista, respectivamente.
- **Método `media()`**: Calcula a média dos elementos na lista.
- **Método `mediana()`**: Calcula a mediana dos elementos na lista. Se a lista tiver tamanho ímpar, a mediana é o elemento central. Se a lista tiver tamanho par, a mediana é a média dos dois elementos centrais.

## Acceptance Criteria
- `estatistica.media([1, 2, 3])` retorna `2`
- `estatistica.mediana([1, 2, 3])` retorna `2`
- `estatistica.media([])` lança `ValueError("Lista vazia")`
- `estatistica.mediana([])` lança `ValueError("Lista vazia")`
- `estatistica.media([10])` retorna `10`
- `estatistica.mediana([10, 20])` retorna `15`
- `estatistica.media([10, 20, 30])` retorna `20`
- `estatistica.mediana([10, 20, 30, 40])` retorna `25`
- `estatistica.mediana([10, 20, 30, 40, 50])` retorna `30`
- `estatistica.media([10, 20, 30, 40, 50, 60])` retorna `35`
- `estatistica.mediana([10, 20, 30, 40, 50, 60, 70])` retorna `40`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80])` retorna `45`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90])` retorna `50`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])` retorna `55`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110])` retorna `60`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120])` retorna `65`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130])` retorna `70`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140])` retorna `75`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150])` retorna `80`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160])` retorna `85`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170])` retorna `90`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180])` retorna `95`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190])` retorna `100`
- `estatistica.media([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 14