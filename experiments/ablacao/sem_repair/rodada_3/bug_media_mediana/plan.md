Baseado na especificação e nos arquivos do projeto fornecidos, segue um plano numerado, passo a passo, do que deve ser programado:

1. **Verificar o estado atual das funções:**
   - Abra o arquivo `estatistica.py` e examine as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas existentes nas funções, como falta de tratamento de listas vazias ou modificações indesejadas na lista de entrada.

2. **Implementar o tratamento de listas vazias:**
   - Modifique as funções `media()` e `mediana()` para incluir uma verificação inicial que lance um `ValueError` se a lista de entrada estiver vazia.
   - Exemplo de código para esta verificação:
     ```python
     if not entrada:
         raise ValueError("A lista de entrada não pode estar vazia.")
     ```

3. **Garantir que a lista de entrada não seja modificada:**
   - Certifique-se de que as funções `media()` e `mediana()` não alteram a lista de entrada.
   - Isso pode ser feito criando uma cópia da lista antes de realizar qualquer operação.
   - Exemplo de código para criar uma cópia da lista:
     ```python
     entrada = entrada.copy()
     ```

4. **Implementar a lógica para calcular a média:**
   - Implemente a lógica para calcular a média aritmética dos números na lista.
   - Certifique-se de que a soma é calculada corretamente e dividida pelo número total de elementos.
   - Exemplo de código para calcular a média:
     ```python
     def media(entrada):
         if not entrada:
             raise ValueError("A lista de entrada não pode estar vazia.")
         entrada = entrada.copy()
         return sum(entrada) / len(entrada)
     ```

5. **Implementar a lógica para calcular a mediana:**
   - Implemente a lógica para calcular a mediana dos números na lista.
   - Certifique-se de ordenar a lista corretamente e encontrar o valor central.
   - Exemplo de código para calcular a mediana:
     ```python
     def mediana(entrada):
         if not entrada:
             raise ValueError("A lista de entrada não pode estar vazia.")
         entrada = sorted(entrada.copy())
         n = len(entrada)
         if n % 2 == 0:
             return (entrada[n // 2 - 1] + entrada[n // 2]) / 2
         else:
             return entrada[n // 2]
     ```

6. **Criar ou atualizar os testes automatizados:**
   - Crie ou atualize os testes automatizados para verificar se as funções `media()` e `mediana()` estão funcionando corretamente.
   - Os testes devem cobrir todas as condições especificadas, incluindo entradas válidas e inválidas.
   - Exemplo de teste usando `unittest`:
     ```python
     import unittest
     
     class TestEstatistica(unittest.TestCase):
         def test_media(self):
             self.assertEqual(media([1, 2, 3]), 2)
             self.assertAlmostEqual(media([1.5, 2.5, 3.5]), 2.5)
             with self.assertRaises(ValueError):
                 media([])
     
         def test_mediana(self):
             self.assertEqual(mediana([1, 2, 3]), 2)
             self.assertAlmostEqual(mediana([1.5, 2.5, 3.5]), 2.5)
             self.assertAlmostEqual(mediana([1, 2, 3, 4]), 2.5)
             with self.assertRaises(ValueError):
                 mediana([])
     
     if __name__ == '__main__':
         unittest.main()
     ```

7. **Executar os testes:**
   - Execute os testes automatizados para garantir que todas as condições são atendidas.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

8. **Documentar as mudanças:**
   - Documente as mudanças feitas nas funções `media()` e `mediana()` e os testes adicionados.
   - Certifique-se de que a documentação está clara e fácil de entender.

Este plano deve guiar você através da correção e implementação das funções necessárias, além de garantir que todos os requisitos sejam satisfeitos.