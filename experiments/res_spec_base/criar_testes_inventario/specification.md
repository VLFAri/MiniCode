# Specification

## Objective
O objetivo deste projeto é implementar uma classe `Inventario` que gerencie os itens disponíveis em um estoque. A classe deve permitir adicionar, remover e consultar quantidades de itens existentes no estoque.

## Parameters / Requirements
- **Itens**: O estoque deve armazenar itens com informações como nome, quantidade e preço.
- **Adicionar Item**: O método `adicionar` deve permitir adicionar itens ao estoque com validações de quantidade e preços.
- **Remover Item**: O método `remover` deve permitir remover itens do estoque com validações de quantidade e existência.
- **Quantidade de Itens**: O método `quantidade` deve retornar a quantidade total de itens no estoque.
- **Quantidade de Item Existente**: O método `quantidade_item_existente` deve verificar se um item específico existe no estoque.
- **Adição com Quantidade Não Positiva**: O método `adicionar` deve validar se a quantidade a ser adicionada é positiva.
- **Remoção Maior Que Estoque**: O método `remover` deve validar se a quantidade a ser removida é menor ou igual à quantidade atual no estoque.

## Acceptance Criteria
1. O método `adicionar` deve lançar uma exceção `ValueError` se a quantidade for negativa.
2. O método `remover` deve lançar uma exceção `ValueError` se a quantidade for negativa ou maior que a quantidade atual no estoque.
3. O método `quantidade` deve retornar a soma das quantidades de todos os itens no estoque.
4. O método `quantidade_item_existente` deve retornar `True` se o item existe no estoque, e `False` caso contrário.
5. Os testes `test_inventario.py` devem garantir que as funções `adicionar`, `remover`, `quantidade`, `quantidade_item_existente` funcionem conforme esperado.

## Arquivos do projeto:
- `inventario.py`
- `tests/test_inventario.py`

### inventario.py
```python
class Inventario:
    def __init__(self):
        self.items = {}

    def adicionar(self, item_name, quantity, price):
        if quantity <= 0 or price < 0:
            raise ValueError("Quantidade e preço devem ser positivos.")
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        return True

    def remover(self, item_name, quantity):
        if quantity <= 0 or quantity > self.items.get(item_name, 0):
            raise ValueError("Quantidade deve ser positiva e menor ou igual à quantidade atual.")
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
        else:
            raise ValueError("Quantidade solicitada excede a quantidade disponível.")
        return True

    def quantidade(self):
        return sum(self.items.values())

    def quantidade_item_existente(self, item_name):
        return item_name in self.items
```

### tests/test_inventario.py
```python
import pytest
from inventario import Inventario

def test_adicionar():
    inv = Inventario()
    assert inv.adicionar('Lápis', 10, 0.5) == True
    assert inv.quantidade() == 10
    with pytest.raises(ValueError):
        inv.adicionar('Lápis', -5, 0.5)
    with pytest.raises(ValueError):
        inv.adicionar('Caneta', 0, 0.5)

def test_remover():
    inv = Inventario()
    inv.adicionar('Lápis', 10, 0.5)
    assert inv.remover('Lápis', 5) == True
    assert inv.quantidade() == 5
    with pytest.raises(ValueError):
        inv.remover('Lápis', -5)
    with pytest.raises(ValueError):
        inv.remover('Lápis', 15)
    with pytest.raises(ValueError):
        inv.remover('Caneta', 0)

def test_quantidade():
    inv = Inventario()
    assert inv.quantidade() == 0
    inv.adicionar('Lápis', 10, 0.5)
    assert inv.quantidade() == 10
    inv.remover('Lápis', 5)
    assert inv.quantidade() == 5

def test_quantidade_item_existente():
    inv = Inventario()
    assert inv.quantidade_item_existente('Lápis') == False
    inv.adicionar('Lápis', 10, 0.5)
    assert inv.quantidade_item_existente('Lápis') == True
```

Este projeto implementa uma classe `Inventario` que gerencia itens em um estoque, com validações e testes para garantir a integridade dos dados.