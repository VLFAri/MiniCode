# Specification

## Objective
O objetivo deste projeto é corrigir um bug no código `carrinho.py` que ocorre quando várias chamadas independentes de adicionar(item) são feitas ao mesmo carrinho.

## Parameters / Requirements
1. **Entradas**:
   - `item`: O item a ser adicionado ao carrinho.

2. **Tipos**:
   - `item` deve ser uma instância de uma classe ou tipo válido para representar um item.

3. **Restrições**:
   - Não há restrições específicas para o tipo de `item`.

4. **Regras de Negócios**:
   - Quando um item é adicionado ao carrinho, o método `adicionar(item)` deve retornar o próprio objeto `item`.
   - Se nenhum carrinho for fornecido, o método `adicionar(item)` deve criar um novo carrinho e adicionar o item nele.

## Acceptance Criteria
1. **Critérios Claro e Verificáveis por Testes Automatizados**:
   - A função `adicionar(item)` deve retornar o próprio objeto `item` quando chamada com um item específico.
   - Se nenhum carrinho for fornecido, a função `adicionar(item)` deve criar um novo carrinho e adicionar o item nele.

## Arquivos do projeto
carrinho.py

```python
class Carrinho:
    def __init__(self):
        self.items = []

    def adicionar(self, item):
        if self.items is None:
            self.items = []
        self.items.append(item)
        return item
```

### Testes Automatizados
Para garantir que a correção funcione conforme esperado, você pode usar os seguintes testes:

```python
def test_adicionar_item():
    carrinho = Carrinho()
    item = "Item 1"
    result = carrinho.adicionar(item)
    assert result == item, f"Expected {item}, but got {result}"
    assert isinstance(result, str), f"Expected string, but got {type(result)}"

def test_adicionar_novo_carrinho():
    carrinho = Carrinho()
    item = "Item 2"
    result = carrinho.adicionar(item)
    assert result == item, f"Expected {item}, but got {result}"
    assert isinstance(result, str), f"Expected string, but got {type(result)}"
    assert carrinho.items == [item], f"Expected items to be [{item}], but got {carrinho.items}"

if __name__ == "__main__":
    test_adicionar_item()
    test_adicionar_novo_carrinho()
```

Esses testes garantem que a função `adicionar(item)` funcione como esperado, criando um novo carrinho se nenhum for fornecido e retornando o próprio objeto `item`.