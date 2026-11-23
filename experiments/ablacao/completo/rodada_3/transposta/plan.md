Baseado na especificação fornecida e considerando que o projeto está vazio, aqui está um plano passo a passo de como implementar a função `transposta(m)` conforme solicitado:

### Plano de Implementação

1. **Criar o arquivo `matriz.py`:**
   - Crie um novo arquivo chamado `matriz.py` no diretório do projeto.

2. **Definir a função `transposta(m)`:**
   - Dentro do arquivo `matriz.py`, defina a função `transposta(m)` que receberá uma matriz `m` como parâmetro.
   
3. **Verificar se a matriz é vazia:**
   - No início da função, verifique se a matriz `m` é vazia (`len(m) == 0`). Se for, retorne uma lista vazia `[]`.
   
4. **Verificar consistência nas dimensões das linhas:**
   - Verifique se todas as linhas da matriz têm o mesmo tamanho. Se não, lance um `ValueError` com a mensagem "Linhas de tamanho inconsistente".
   
5. **Calcular a matriz transposta:**
   - Se a matriz não estiver vazia e as linhas forem consistentes, calcule a matriz transposta. Isso pode ser feito usando compreensão de lista em Python, onde cada nova linha será formada pelos elementos correspondentes de cada linha da matriz original.
   
6. **Retornar a matriz transposta:**
   - Após calcular a matriz transposta, retorne-a.

7. **Incluir testes unitários:**
   - Adicione testes unitários para verificar se a função `transposta(m)` funciona corretamente. Use a biblioteca `unittest` para isso.
   - Teste casos de entrada válidos, entrada inválida (linhas de tamanho diferente), e entrada vazia.
   - Certifique-se de que os testes cobrem todos os requisitos e critérios de aceitação.

### Código de Exemplo

Aqui está um exemplo de como o código poderia ser escrito:

```python
def transposta(m):
    if len(m) == 0:
        return []
    
    # Verifica se todas as linhas têm o mesmo tamanho
    if not all(len(row) == len(m[0]) for row in m):
        raise ValueError("Linhas de tamanho inconsistente")
    
    # Calcula a matriz transposta
    transposed = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
    
    return transposed
```

### Testes Unitários

Adicione os seguintes testes ao seu projeto:

```python
import unittest
from matriz import transposta

class TestTransposta(unittest.TestCase):
    def test_transposta(self):
        self.assertEqual(transposta([[1, 2], [3, 4]]), [[1, 3], [2, 4]])
        self.assertEqual(transposta([]), [])
        
        with self.assertRaises(ValueError):
            transposta([[1, 2], [3, 4, 5]])

if __name__ == '__main__':
    unittest.main()
```

Este plano e o exemplo de código fornecem uma estrutura clara para implementar a função `transposta(m)` e garantir que ela funcione corretamente através de testes unitários.