Baseado na especificação e nos arquivos fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado:

1. **Criação da Classe `Inventario`:**
   - Implementar o método `__init__` que inicializa o dicionário `items`.
   - Implementar o método `adicionar` que adiciona itens ao estoque, validando a quantidade e o preço.
   - Implementar o método `remover` que remove itens do estoque, validando a quantidade.
   - Implementar o método `quantidade` que retorna a soma das quantidades de todos os itens no estoque.
   - Implementar o método `quantidade_item_existente` que verifica se um item específico existe no estoque.

2. **Implementação dos Testes:**
   - Criar os casos de teste para cada método da classe `Inventario` em `test_inventario.py`.
   - Testar a adição de itens válidos e inválidos.
   - Testar a remoção de itens válidos e inválidos.
   - Testar a soma correta das quantidades de itens.
   - Testar a verificação correta da existência de itens.

Aqui está um exemplo detalhado de como esses passos podem ser implementados:

### Passo 1: Implementação da Classe `Inventario`

#### Arquivo `inventario.py`
```python
class Inventario:
    def __init__(self):
        self.items = {}

    def adicionar(self, item_name, quantity, price):
        """
        Adiciona um item ao estoque.
        :param item_name: Nome do item.
        :param quantity: Quantidade do item.
        :param price: Preço unitário do item.
        :raises ValueError: Se a quantidade ou preço for inválido.
        """
        if quantity <= 0 or price < 0:
            raise ValueError("Quantidade e preço devem ser positivos.")
        
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity
        
        return True

    def remover(self, item_name, quantity):
        """
        Remove um item do estoque.
        :param item_name: Nome do item.
        :param quantity: Quantidade do item a ser removida.
        :raises ValueError: Se a quantidade for inválida.
        """
        if quantity <= 0 or quantity > self.items.get(item_name, 0):
            raise ValueError("Quantidade deve ser positiva e menor ou igual à quantidade atual.")
        
        if self.items[item_name] >= quantity:
            self.items[item_name] -= quantity
        else:
            raise ValueError("Quantidade solicitada excede a quantidade disponível.")
        
        return True

    def quantidade(self):
        """
        Retorna a soma das quantidades de todos os itens no estoque.
        """
        return sum(self.items.values())

    def quantidade_item_existente(self, item_name):
        """
        Verifica se um item específico existe no estoque.
        :param item_name: Nome do item.
        :return: True se o item existe, False caso contrário.
        """
        return item_name in self.items
```

### Passo 2: Implementação dos Testes

#### Arquivo `tests/test_inventario.py`
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

Este plano cobre a implementação da classe `Inventario` e a criação de testes para garantir que os métodos funcionem conforme especificado.