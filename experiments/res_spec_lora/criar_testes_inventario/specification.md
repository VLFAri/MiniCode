# Specification

## Objective
Criar uma classe `Inventario` que permita manipular itens no estoque, incluindo adicionar, remover itens, consultar a quantidade atual de um item específico e lidar com situações onde a quantidade não seja válida.

## Parameters / Requirements
- **Classe:** `Inventario`
- **Métodos:**
  - `adicionar(item: str, quantidade: int) -> None`: Adiciona uma quantidade de itens ao estoque.
  - `remover(item: str, quantidade: int) -> None`: Remove uma quantidade de itens do estoque.
  - `quantidade(item: str) -> int`: Retorna a quantidade atual de um item no estoque.
  - `quantidade_de_item_inexistente(item: str) -> bool`: Verifica se um item não existe no estoque.
  - `adicao_com_quantidade_negativa(item: str, quantidade: int) -> None`: Lança uma exceção `ValueError` caso a quantidade de adição seja negativa.
  - `remocao_maior_que_estoque(item: str, quantidade: int) -> None`: Lança uma exceção `ValueError` caso a quantidade de remoção seja maior que a quantidade disponível no estoque.
- **Restrições:**
  - A função `quantidade_de_item_inexistente` deve retornar `True` quando o item não está presente no estoque.
  - As funções `adicao_com_quantidade_negativa` e `remocao_maior_que_estoque` devem lançar `ValueError`.
  - Os valores de entrada devem ser strings ou números inteiros.

## Acceptance Criteria
- `Inventario().quantidade('banana')` retorna `0`
- `Inventario().adicionar('maçã', 10)` adiciona 10 maçãs ao estoque
- `Inventario().quantidade('maçã')` retorna `10`
- `Inventario().remover('maçã', 5)` remove 5 maçãs do estoque
- `Inventario().quantidade('maçã')` retorna `5`
- `Inventario().quantidade_de_item_inexistente('laranja')` retorna `True`
- `Inventario().adicionar('banana', -2)` lança `ValueError`
- `Inventario().remover('banana', 15)` lança `ValueError`
- `Inventario().adicionar('manga', 'abc')` lança `TypeError`
- `Inventario().remover('manga', 'def')` lança `TypeError`