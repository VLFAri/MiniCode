Baseado na especificação fornecida, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Passo 1: Estrutura do Projeto
Criar a estrutura básica do projeto, incluindo o arquivo `matriz.py` onde a função `transposta(m)` será implementada.

### Passo 2: Implementação da Função `transposta(m)`
Implementar a função `transposta(m)` no arquivo `matriz.py`. A função deve realizar os seguintes passos:

1. Verificar se a matriz de entrada é vazia. Se for, retornar uma lista vazia `[]`.
2. Verificar se todas as linhas da matriz têm o mesmo tamanho. Se não tiverem, lançar um `ValueError`.
3. Transpor a matriz, criando uma nova matriz onde cada linha é formada pelos elementos correspondentes das colunas da matriz original.

### Passo 3: Testes Unitários
Criar um arquivo `test_matriz.py` para escrever e executar os testes unitários da função `transposta(m)`. Os testes devem cobrir todos os casos mencionados na especificação, incluindo:

1. Matriz vazia.
2. Matriz válida (todas as linhas têm o mesmo tamanho).
3. Matriz inválida (linhas de diferentes tamanhos).

### Passo 4: Execução dos Testes
Executar os testes unitários para garantir que a função `transposta(m)` funcione conforme esperado em todos os casos.

Aqui está um exemplo de como esses passos podem ser implementados:

#### Passo 1: Estrutura do Projeto
```plaintext
matriz/
    __init__.py
    matriz.py
    test_matriz.py
```

#### Passo 2: Implementação da Função `transposta(m)`
No arquivo `matriz.py`, adicione a função `transposta(m)`:

```python
def transposta(m):
    if not m:  # Verifica se a matriz é vazia
        return []
    
    row_lengths = [len(row) for row in m]  # Obtém o comprimento de cada linha
    
    if len(set(row_lengths)) != 1:  # Verifica se todas as linhas têm o mesmo tamanho
        raise ValueError("Linhas de diferentes tamanhos")
    
    # Transpõe a matriz
    transposed_matrix = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    
    return transposed_matrix
```

#### Passo 3: Testes Unitários
No arquivo `test_matriz.py`, adicione os testes unitários:

```python
import unittest
from matriz import transposta

class TestTransposta(unittest.TestCase):

    def test_transposta_vazia(self):
        self.assertEqual(transposta([]), [])

    def test_transposta_valida(self):
        self.assertEqual(transposta([[1, 2], [3, 4]]), [[1, 3], [2, 4]])

    def test_transposta_invalida(self):
        with self.assertRaises(ValueError):
            transposta([[1, 2], [3, 4, 5]])

if __name__ == '__main__':
    unittest.main()
```

#### Passo 4: Execução dos Testes
Execute os testes unitários para verificar a implementação:

```bash
python -m unittest test_matriz.py
```

Este plano cobre todos os aspectos necessários para implementar a função `transposta(m)` e garantir sua correta funcionalidade através de testes unitários.