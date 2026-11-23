### Plano Numerado de Desenvolvimento do Projeto

1. **Preparação do Ambiente de Desenvolvimento**
   - Certifique-se de que o ambiente Python está configurado corretamente.
   - Instale o pytest se ainda não estiver instalado (`pip install pytest`).

2. **Criação da Estrutura de Testes**
   - Crie a estrutura de diretórios para os testes se ainda não existir.
     ```bash
     mkdir -p tests
     ```

3. **Criação do Arquivo de Testes**
   - Crie o arquivo `test_inventario.py` dentro da pasta `tests`.
     ```bash
     touch tests/test_inventario.py
     ```

4. **Importação das Dependências**
   - No arquivo `test_inventario.py`, importe a classe `Inventario` do módulo `inventario.py`.
     ```python
     from inventario import Inventario
     ```

5. **Definição das Funções de Teste**
   - Defina funções de teste para cada método da classe `Inventario`.

6. **Teste de Adicionar Itens**
   - Crie uma função de teste para verificar se itens podem ser adicionados corretamente.
     ```python
     def test_add_item():
         inv = Inventario()
         inv.add_item('apple', 10)
         assert inv.get_quantity('apple') == 10
     ```

7. **Teste de Remover Itens**
   - Crie uma função de teste para verificar se itens podem ser removidos corretamente.
     ```python
     def test_remove_item():
         inv = Inventario()
         inv.add_item('banana', 20)
         inv.remove_item('banana', 10)
         assert inv.get_quantity('banana') == 10
     ```

8. **Teste de Verificar Quantidades**
   - Crie uma função de teste para verificar se a quantidade de um item pode ser consultada corretamente.
     ```python
     def test_get_quantity():
         inv = Inventario()
         inv.add_item('orange', 15)
         assert inv.get_quantity('orange') == 15
     ```

9. **Teste de Tentar Consultar Quantidade de Item Inexistente**
   - Crie uma função de teste para verificar como o sistema lida com tentativas de consultar a quantidade de um item que não existe.
     ```python
     def test_get_nonexistent_item():
         inv = Inventario()
         assert inv.get_quantity('nonexistent') == 0
     ```

10. **Teste de Adicionar Itens com Quantidade Não Positiva**
    - Crie uma função de teste para verificar como o sistema lida com tentativas de adicionar itens com quantidade não positiva.
      ```python
      def test_add_negative_quantity():
          inv = Inventario()
          try:
              inv.add_item('lemon', -5)
          except ValueError as e:
              assert str(e) == "Quantity must be positive"
      ```

11. **Teste de Remover Mais Itens do que Estão Disponíveis**
    - Crie uma função de teste para verificar como o sistema lida com tentativas de remover mais itens do que estão disponíveis em estoque.
      ```python
      def test_remove_more_than_available():
          inv = Inventario()
          inv.add_item('grape', 10)
          try:
              inv.remove_item('grape', 15)
          except ValueError as e:
              assert str(e) == "Cannot remove more items than available"
      ```

12. **Execução dos Testes**
    - Execute todos os testes usando o comando pytest.
      ```bash
      pytest tests/
      ```

13. **Verificação dos Resultados dos Testes**
    - Verifique se todos os testes passam sem erros.
    - Se algum teste falhar, revise o código do `inventario.py` para garantir que ele atenda aos requisitos especificados.

### Considerações Finais
- Certifique-se de que todas as funções de teste são bem documentadas e claramente nomeadas para facilitar a manutenção futura.
- Ajuste as mensagens de erro conforme necessário para garantir que eles sejam úteis e informativos.
- Mantenha o código do `inventario.py` intacto durante todo o processo de teste para garantir que os testes estejam verificando o comportamento esperado do código original.