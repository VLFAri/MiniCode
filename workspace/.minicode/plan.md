Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Implementação

1. **Preparação do Ambiente**
   - Certifique-se de que o ambiente de desenvolvimento esteja configurado corretamente para Python.
   - Crie os arquivos necessários (`quick_sort.py` e `tests/test_quick_sort.py`).

2. **Implementação da Função QuickSort**
   - No arquivo `quick_sort.py`, implemente a função `quick_sort`.
   - A função `quick_sort` deve aceitar uma lista de inteiros como entrada e retornar a lista ordenada em ordem crescente.
   - Implemente a lógica do algoritmo QuickSort dentro da função `quick_sort`.
   - Adicione comentários explicando a função e a implementação do algoritmo.

3. **Testes Unitários**
   - No arquivo `tests/test_quick_sort.py`, implemente os testes unitários para a função `quick_sort`.
   - Crie três casos de teste diferentes, cada um usando uma das três listas pré-definidas no arquivo `quick_sort.py`.
   - Certifique-se de que os testes cobrem diferentes cenários, incluindo listas vazias e listas com valores duplicados.

4. **Documentação**
   - Adicione documentação ao código em `quick_sort.py`, explicando a função `quick_sort` e como ela funciona.
   - Certifique-se de que a documentação é clara e fácil de entender.

5. **Execução dos Testes**
   - Execute os testes unitários em `tests/test_quick_sort.py` para garantir que a função `quick_sort` funcione corretamente.
   - Verifique se todos os testes passam sem erros ou falhas.

6. **Revisão e Refatoração**
   - Revisite o código em `quick_sort.py` e os testes em `tests/test_quick_sort.py`.
   - Faça quaisquer ajustes necessários para melhorar a eficiência do código e garantir que ele atenda aos critérios de aceitação.

### Exemplo de Código

#### quick_sort.py
```python
def quick_sort(arr):
    """
    Sorts an array of integers in ascending order using the QuickSort algorithm.

    :param arr: List[int] -- the list of integers to be sorted
    :return: List[int] -- the sorted list of integers
    """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)

# Predefined lists
list1 = [3, 6, 8, 10, 1, 2, 1]
list2 = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6, 4, 1]
list3 = [4, 5, 1, 2, 8, 7, 6, 3]

# Sorting the lists
sorted_list1 = quick_sort(list1)
sorted_list2 = quick_sort(list2)
sorted_list3 = quick_sort(list3)
```

#### tests/test_quick_sort.py
```python
import unittest
from quick_sort import quick_sort, list1, list2, list3

class TestQuickSort(unittest.TestCase):
    def test_quick_sort(self):
        self.assertEqual(quick_sort(list1), [1, 1, 2, 3, 6, 8, 10])
        self.assertEqual(quick_sort(list2), [1, 2, 3, 4, 5, 6, 7, 9, 10, 11, 12, 14])
        self.assertEqual(quick_sort(list3), [1, 2, 3, 4, 5, 6, 7, 8])

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função QuickSort e seus testes associados, garantindo que todas as especificações sejam atendidas.