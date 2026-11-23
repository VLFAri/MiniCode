Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `dividir`:

### Plano de Implementação

1. **Criar o arquivo principal do projeto**:
   - Crie um arquivo Python chamado `chunker.py`. Este será o arquivo principal onde a função `dividir` será implementada.

2. **Definir a função `dividir`**:
   - Na função `dividir`, verifique se o segundo argumento `n` é maior que zero. Caso contrário, lance uma exceção `ValueError` com a mensagem "n must be positive".
   - Verifique também se `n` é menor ou igual ao comprimento da lista. Caso contrário, lance uma exceção `ValueError` com a mensagem "n must be less than or equal to the length of the list".

3. **Dividir a lista em blocos**:
   - Use um loop para iterar sobre a lista e criar blocos de tamanho `n`.
   - Utilize a função `list()` para converter as partes da lista em sublistas.

4. **Retornar a lista de blocos**:
   - Retorne a lista de blocos resultante.

5. **Adicionar testes unitários**:
   - Crie um arquivo chamado `test_chunker.py` para os testes unitários.
   - Importe a função `dividir` do módulo `chunker`.
   - Escreva casos de teste para cada condição mencionada nos critérios de aceitação.
   - Use a biblioteca `unittest` para escrever os testes.

### Código de Exemplo

#### Arquivo `chunker.py`

```python
def dividir(lista, n):
    if n <= 0:
        raise ValueError("n must be positive")
    if n > len(lista):
        raise ValueError("n must be less than or equal to the length of the list")

    return [lista[i:i+n] for i in range(0, len(lista), n)]
```

#### Arquivo `test_chunker.py`

```python
import unittest
from chunker import dividir

class TestChunker(unittest.TestCase):

    def test_divide_evenly(self):
        self.assertEqual(dividir([1, 2, 3, 4], 2), [[1, 2], [3, 4]])

    def test_divide_single_elements(self):
        self.assertEqual(dividir(['a', 'b', 'c'], 1), [['a'], ['b'], ['c']])

    def test_empty_list(self):
        self.assertEqual(dividir([], 3), [])

    def test_single_element_list(self):
        self.assertEqual(dividir([10], 5), [[10]])

    def test_invalid_n_value(self):
        with self.assertRaises(ValueError) as context:
            dividir([1, 2, 3, 4, 5], 0)
        self.assertTrue('n must be positive' in str(context.exception))

    def test_invalid_n_greater_than_length(self):
        with self.assertRaises(ValueError) as context:
            dividir([1, 2, 3, 4, 5], 6)
        self.assertTrue('n must be less than or equal to the length of the list' in str(context.exception))

if __name__ == '__main__':
    unittest.main()
```

### Execução dos Testes

Para executar os testes, você pode usar o seguinte comando no terminal:

```bash
python -m unittest test_chunker.py
```

Este comando irá rodar todos os testes definidos no arquivo `test_chunker.py`.

### Conclusão

Este plano cobre a implementação da função `dividir` e a criação de testes unitários para garantir que a função funcione conforme esperado em todas as condições possíveis.