# Specification

## Objective
A função `paginar` deve retornar uma lista contendo apenas os itens da página solicitada, considerando que as páginas são 1-indexadas.

## Parameters / Requirements
- `itens`: Uma lista de itens que serão paginados.
- `pagina`: Um número inteiro que representa a página desejada (1-indexada).
- `tamanho`: Um número inteiro que representa o número de itens por página.

### Restrictions and Rules of Business
- Se `pagina` ou `tamanho` for menor que 1, deve lançar uma exceção `ValueError`.
- Se a página solicitada estiver fora do intervalo válido (0 <= página < total de páginas), deve retornar uma lista vazia.

### Acceptance Criteria
- A função `paginar` deve funcionar corretamente para todas as combinações possíveis de `pagina` e `tamanho`.
- A função deve lançar uma exceção `ValueError` se `pagina` ou `tamanho` for menor que 1.
- A função deve retornar uma lista vazia se a página solicitada estiver fora do intervalo válido.

## Arquivos do projeto
- **paginacao.py**

```python
def paginar(itens, pagina, tamanho):
    if pagina < 1 or tamanho < 1:
        raise ValueError("Pagina e tamanho devem ser maiores que zero.")
    
    total_paginas = len(itens) // tamanho + (len(itens) % tamanho != 0)
    
    if pagina > total_paginas:
        return []
    
    inicio = (pagina - 1) * tamanho
    fim = min(inicio + tamanho, len(itens))
    
    return itens[inicio:fim]
```

Este código implementa a função `paginar` conforme descrito no enunciado. Ele verifica se `pagina` e `tamanho` são válidos, calcula o total de páginas necessárias, verifica se a página solicitada está dentro do intervalo válido, e retorna a lista correspondente à página solicitada.