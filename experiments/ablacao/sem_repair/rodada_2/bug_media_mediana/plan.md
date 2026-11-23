Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar as correções necessárias nas funções `media()` e `mediana()` no arquivo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o Código Atual**
   - Abra o arquivo `estatistica.py` e revise as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas existentes, como manipulação da lista original ou falta de tratamento de listas vazias.

2. **Implementar Tratamento de Listas Vazias**
   - Modifique as funções `media()` e `mediana()` para que, se a lista de entrada estiver vazia, elas lancem um `ValueError`.
     ```python
     if not numbers:
         raise ValueError("Lista vazia")
     ```

3. **Garantir que a Lista Original Não Seja Alterada**
   - Certifique-se de que as funções não modifiquem a lista de entrada. Isso pode ser feito criando uma cópia da lista antes de processá-la.
     ```python
     numbers = numbers.copy()
     ```

4. **Corrigir a Lógica da Média**
   - Verifique se a função `media()` calcula corretamente a média aritmética dos números na lista.
     ```python
     def media(numbers):
         if not numbers:
             raise ValueError("Lista vazia")
         return sum(numbers) / len(numbers)
     ```

5. **Corrigir a Lógica da Mediana**
   - Verifique se a função `mediana()` calcula corretamente a mediana dos números na lista.
     ```python
     def mediana(numbers):
         if not numbers:
             raise ValueError("Lista vazia")
         numbers_sorted = sorted(numbers)
         n = len(numbers_sorted)
         if n % 2 == 0:
             return (numbers_sorted[n // 2 - 1] + numbers_sorted[n // 2]) / 2
         else:
             return numbers_sorted[n // 2]
     ```

6. **Criar ou Atualizar Testes Automatizados**
   - Crie ou atualize os testes automatizados para verificar se as funções estão funcionando corretamente.
   - Os testes devem cobrir casos de uso válidos, listas vazias e exceções.
     ```python
     import unittest
     from estatistica import media, mediana

     class TestEstatistica(unittest.TestCase):
         def test_media(self):
             self.assertEqual(media([1, 2, 3]), 2)
             self.assertAlmostEqual(media([1.0, 2.0, 3.0]), 2.0)
             with self.assertRaises(ValueError):
                 media([])

         def test_mediana(self):
             self.assertEqual(mediana([1, 2, 3]), 2)
             self.assertAlmostEqual(mediana([1.0, 2.0, 3.0]), 2.0)
             with self.assertRaises(ValueError):
                 mediana([])
             self.assertEqual(mediana([1, 2, 3, 4]), 2.5)
             self.assertAlmostEqual(mediana([1.0, 2.0, 3.0, 4.0]), 2.5)

     if __name__ == '__main__':
         unittest.main()
     ```

7. **Executar Testes**
   - Execute os testes automatizados para garantir que todas as condições de aceitação estão sendo satisfeitas.
   - Corrija quaisquer falhas encontradas nos testes.

8. **Documentação**
   - Certifique-se de que a documentação do código reflete as mudanças feitas.
   - Adicione comentários explicativos onde necessário para facilitar a manutenção futura.

Este plano fornece uma estrutura clara para corrigir as funções `media()` e `mediana()` e garantir que os testes automatizados estejam de acordo com as especificações fornecidas.