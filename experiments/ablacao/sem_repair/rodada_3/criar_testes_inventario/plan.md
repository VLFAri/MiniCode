### Plano de Desenvolvimento de Testes para o Projeto `inventario.py`

1. **Instalação das Dependências**
   - Certifique-se de que o ambiente Python tenha a biblioteca `pytest` instalada. Se não estiver instalada, execute o comando `pip install pytest`.

2. **Criação da Estrutura de Testes**
   - Crie uma estrutura de diretórios para os testes se ainda não existir. A estrutura deve ser similar a esta:
     ```
     project/
     ├── inventario.py
     └── tests/
         └── __init__.py
     ```

3. **Criação do Arquivo de Testes**
   - Crie o arquivo `test_inventario.py` dentro da pasta `tests/`.
   - Importe a classe `Inventario` do módulo `inventario.py` no arquivo de teste.

4. **Definição de Funções Auxiliares (se necessário)**
   - Defina funções auxiliares que podem ser usadas em vários testes, como a criação de instâncias de `Inventario` com diferentes estados iniciais.

5. **Implementação dos Testes**
   - Implemente cada caso de teste conforme especificado abaixo:

#### Adicionar Itens ao Inventário
   - Escreva um teste para adicionar um item ao inventário e verificar se a quantidade foi incrementada corretamente.
   ```python
   def test_add_item():
       inv = Inventario()
       inv.add_item('apple', 10)
       assert inv.check_quantity('apple') == 10
   ```

#### Remover Itens do Inventário
   - Escreva um teste para remover um item do inventário e verificar se a quantidade foi decrementada corretamente.
   ```python
   def test_remove_item():
       inv = Inventario()
       inv.add_item('banana', 20)
       inv.remove_item('banana', 10)
       assert inv.check_quantity('banana') == 10
   ```

#### Verificar Quantidade de Itens Existentes
   - Escreva um teste para verificar a quantidade de um item que já existe no inventário.
   ```python
   def test_check_quantity_existing_item():
       inv = Inventario()
       inv.add_item('orange', 15)
       assert inv.check_quantity('orange') == 15
   ```

#### Lidar com Itens Não Existentes
   - Escreva um teste para lidar com tentativas de acessar itens que não existem no inventário.
   ```python
   def test_check_quantity_nonexistent_item():
       inv = Inventario()
       assert inv.check_quantity('grape') == 0
   ```

#### Adicionar Itens com Quantidade Não Positiva
   - Escreva um teste para falhar quando tenta adicionar um item com uma quantidade não positiva.
   ```python
   def test_add_item_with_non_positive_quantity():
       inv = Inventario()
       with pytest.raises(ValueError):
           inv.add_item('pear', -5)
   ```

#### Remover Mais Itens do que Estão em Estoque
   - Escreva um teste para falhar quando tenta remover mais itens do que estão disponíveis no inventário.
   ```python
   def test_remove_more_items_than_available():
       inv = Inventario()
       inv.add_item('cherry', 10)
       with pytest.raises(ValueError):
           inv.remove_item('cherry', 15)
   ```

6. **Execução dos Testes**
   - Execute todos os testes usando o comando `pytest` no terminal.
   - Certifique-se de que todos os testes passam sem erros.

7. **Documentação dos Testes**
   - Adicione comentários claros e concisos aos testes para explicar o propósito de cada teste e quais cenários estão sendo verificados.

8. **Revisão e Refatoração**
   - Revisar os testes para garantir que eles são eficientes e cobrem todas as funcionalidades relevantes da classe `Inventario`.
   - Refatore o código dos testes se necessário para melhorar a legibilidade e a manutenção.

Este plano fornece uma estrutura clara para criar e executar testes para a classe `Inventario`, garantindo que todas as funcionalidades importantes sejam adequadamente verificadas.