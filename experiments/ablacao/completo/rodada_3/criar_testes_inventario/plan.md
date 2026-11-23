Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, de como criar o arquivo de teste `tests/test_inventario.py` usando o pytest framework para testar a classe `Inventario` do arquivo `inventario.py`.

### Plano de Implementação

1. **Configuração do Ambiente**
   - Certifique-se de que o ambiente Python esteja configurado corretamente.
   - Instale o pytest se ainda não estiver instalado (`pip install pytest`).

2. **Criação da Estrutura de Testes**
   - Crie a estrutura de diretórios necessária para os testes:
     ```bash
     mkdir -p tests
     touch tests/test_inventario.py
     ```

3. **Importação das Dependências**
   - No arquivo `test_inventario.py`, importe a classe `Inventario` do módulo `inventario`.
   - Importe também o pytest para usar suas funcionalidades de teste.

4. **Definição das Funções de Teste**
   - Para cada método da classe `Inventario`, defina uma função de teste correspondente.
   - Use assert statements para verificar se os métodos funcionam conforme esperado.

5. **Implementação dos Testes**

   - **Teste de Adicionar Itens**
     - Crie um teste para adicionar itens ao inventário.
     - Verifique se a quantidade de itens foi adicionada corretamente.
   
   - **Teste de Remover Itens**
     - Crie um teste para remover itens do inventário.
     - Verifique se a quantidade de itens foi removida corretamente.
   
   - **Teste de Consultar Quantidade**
     - Crie um teste para consultar a quantidade de um item existente no inventário.
     - Verifique se a quantidade retornada é correta.
   
   - **Teste de Consultar Item Inexistente**
     - Crie um teste para tentar consultar a quantidade de um item que não existe no inventário.
     - Verifique se o comportamento é adequado (por exemplo, retorna None ou levanta uma exceção).
   
   - **Teste de Adicionar Itens com Quantidade Não Positiva**
     - Crie um teste para tentar adicionar itens com quantidade não positiva.
     - Verifique se o comportamento é adequado (por exemplo, falha silenciosamente ou levanta uma exceção).
   
   - **Teste de Remover Mais Itens do que Estão Disponíveis em Estoque**
     - Crie um teste para tentar remover mais itens do que estão disponíveis em estoque.
     - Verifique se o comportamento é adequado (por exemplo, falha silenciosamente ou levanta uma exceção).

6. **Execução dos Testes**
   - Execute os testes usando o comando `pytest`.
   - Verifique se todos os testes passam sem modificar o arquivo original `inventario.py`.

7. **Organização e Legibilidade dos Testes**
   - Certifique-se de que o código de teste é organizado e legível.
   - Use comentários e docstrings onde apropriado para explicar o propósito de cada teste.

### Exemplo de Código de Teste

Aqui está um exemplo básico de como o arquivo `tests/test_inventario.py` poderia ser implementado:

```python
import pytest
from inventario import Inventario

def setup_function():
    """Setup function to initialize the inventory before each test."""
    global inv
    inv = Inventario()

def test_add_item():
    """Test adding an item to the inventory."""
    inv.add_item("apple", 10)
    assert inv.get_quantity("apple") == 10

def test_remove_item():
    """Test removing an item from the inventory."""
    inv.add_item("banana", 20)
    inv.remove_item("banana", 10)
    assert inv.get_quantity("banana") == 10

def test_get_quantity_existing_item():
    """Test getting the quantity of an existing item."""
    inv.add_item("orange", 15)
    assert inv.get_quantity("orange") == 15

def test_get_quantity_nonexistent_item():
    """Test getting the quantity of a non-existent item."""
    assert inv.get_quantity("grape") is None  # Or raises an exception depending on implementation

def test_add_item_with_non_positive_quantity():
    """Test adding an item with a non-positive quantity."""
    with pytest.raises(ValueError):  # Adjust according to expected behavior
        inv.add_item("pear", -5)

def test_remove_more_items_than_available():
    """Test removing more items than are available in stock."""
    inv.add_item("cherry", 10)
    with pytest.raises(ValueError):  # Adjust according to expected behavior
        inv.remove_item("cherry", 15)
```

Este plano e exemplo de código devem fornecer uma boa base para criar um conjunto robusto de testes para a classe `Inventario`.