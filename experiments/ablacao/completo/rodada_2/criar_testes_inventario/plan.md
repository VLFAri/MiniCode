Baseado na especificação e nos arquivos do projeto fornecidos, segue um plano numerado, passo a passo, do que deve ser programado para criar os testes de unidade usando o pytest para a classe `Inventario` definida em `inventario.py`.

### Plano de Implementação

1. **Preparação do Ambiente**
   - Certifique-se de que o ambiente Python está configurado corretamente.
   - Instale o pytest se ainda não estiver instalado (`pip install pytest`).

2. **Criação da Estrutura de Testes**
   - Crie a estrutura de diretórios necessária para os testes, se ainda não existir.
     ```bash
     mkdir -p tests
     touch tests/test_inventario.py
     ```

3. **Importação das Dependências**
   - No arquivo `tests/test_inventario.py`, importe a classe `Inventario` do módulo `inventario.py`.
     ```python
     from inventario import Inventario
     ```

4. **Definição das Funções de Teste**
   - Defina funções de teste para cada método da classe `Inventario`.
   
5. **Teste de Adicionar Item**
   - Crie um teste para verificar se o método `add_item` adiciona corretamente um item ao inventário.
     ```python
     def test_add_item():
         inv = Inventario()
         inv.add_item('apple', 10)
         assert inv.get_quantity('apple') == 10
     ```
   
6. **Teste de Remover Item**
   - Crie um teste para verificar se o método `remove_item` remove corretamente um item do inventário.
     ```python
     def test_remove_item():
         inv = Inventario()
         inv.add_item('banana', 20)
         inv.remove_item('banana', 10)
         assert inv.get_quantity('banana') == 10
     ```

7. **Teste de Quantidade de Item Existente**
   - Crie um teste para verificar se o método `get_quantity` retorna a quantidade correta de um item existente.
     ```python
     def test_get_quantity_existing_item():
         inv = Inventario()
         inv.add_item('orange', 30)
         assert inv.get_quantity('orange') == 30
     ```

8. **Teste de Quantidade de Item Não Existe**
   - Crie um teste para verificar se tentar obter a quantidade de um item que não existe levanta uma exceção apropriada.
     ```python
     def test_get_quantity_nonexistent_item():
         inv = Inventario()
         try:
             inv.get_quantity('grape')
         except KeyError as e:
             assert str(e) == "'Item grape does not exist'"
         else:
             assert False, "KeyError was not raised"
     ```

9. **Teste de Adicionar Item com Quantidade Não Positiva**
   - Crie um teste para verificar se tentar adicionar um item com uma quantidade não positiva levanta uma exceção apropriada.
     ```python
     def test_add_item_with_non_positive_quantity():
         inv = Inventario()
         try:
             inv.add_item('lemon', -5)
         except ValueError as e:
             assert str(e) == "'Quantity must be positive'"
         else:
             assert False, "ValueError was not raised"
     ```

10. **Teste de Remover Mais Itens do que Estão Disponíveis em Estoque**
    - Crie um teste para verificar se tentar remover mais itens do que estão disponíveis em estoque levanta uma exceção apropriada.
      ```python
      def test_remove_more_items_than_available():
          inv = Inventario()
          inv.add_item('pear', 15)
          try:
              inv.remove_item('pear', 20)
          except ValueError as e:
              assert str(e) == "'Cannot remove more items than available'"
          else:
              assert False, "ValueError was not raised"
      ```

11. **Execução dos Testes**
    - Execute todos os testes criados usando o comando pytest.
      ```bash
      pytest tests/test_inventario.py
      ```

12. **Verificação dos Resultados**
    - Verifique se todos os testes passaram sem erros ou falhas.
    - Certifique-se de que a classe `Inventario` no arquivo `inventario.py` permaneceu inalterada.

Este plano cobre todas as funcionalidades mencionadas na especificação e garante que a implementação da classe `Inventario` esteja funcionando conforme esperado.