Baseado na especificação fornecida, aqui está um plano numerado de como implementar o script `intervalos.py` em Python:

### Plano de Implementação

1. **Criação do Arquivo de Script**
   - Crie um arquivo chamado `intervalos.py`.

2. **Importação de Módulos Necessários**
   - Importe os módulos necessários para o script. Para este caso, não são necessários módulos externos além da biblioteca padrão do Python.

3. **Definição da Função `mesclar_intervalos`**
   - Defina a função `mesclar_intervalos(lista)` que recebe uma lista de tuplas representando intervalos.
   - Dentro da função, inicialize uma lista vazia para armazenar os intervalos ordenados e mesclados.

4. **Ordenação dos Intervalos**
   - Ordene a lista de entrada com base no valor inicial de cada intervalo usando a função `sorted()`.

5. **Mesclagem dos Intervalos**
   - Percorra a lista ordenada de intervalos e use uma estrutura de controle (como um loop for) para iterar sobre os elementos.
   - Para cada intervalo, verifique se ele se sobrepõe ou toca o próximo intervalo na lista.
   - Se houver sobreposição ou contato, combine os dois intervalos em um único intervalo maior.
   - Continue adicionando intervalos à lista de saída até que todos os intervalos tenham sido processados.

6. **Retorno da Lista Final**
   - Retorne a lista final de intervalos mesclados e ordenados.

7. **Testes Unitários**
   - Crie um arquivo separado chamado `test_intervalos.py` para os testes unitários.
   - Escreva casos de teste para cobrir todas as condições mencionadas na especificação, incluindo:
     - Intervalos sobrepostos.
     - Intervalos adjacentes.
     - Intervalos não sobrepostos e não adjacentes.
     - Lista de entrada vazia.
   - Use a biblioteca `unittest` para escrever os casos de teste.

8. **Execução dos Testes**
   - Execute os testes unitários para garantir que a função `mesclar_intervalos(lista)` funcione corretamente em todas as condições.

### Exemplo de Código

Aqui está um exemplo básico de como o código poderia ser escrito:

```python
def mesclar_intervalos(lista):
    # Ordena os intervalos com base no primeiro número
    lista.sort(key=lambda x: x[0])
    
    # Inicializa a lista de intervalos mesclados
    merged = []
    
    for current in lista:
        # Verifica se a lista de intervalos mesclados está vazia ou se o último intervalo não se sobrepõe com o atual
        if not merged or merged[-1][1] < current[0]:
            merged.append(current)
        else:
            # Se há sobreposição, combina os intervalos
            last = merged.pop()
            merged.append((last[0], max(last[1], current[1])))
    
    return merged
```

### Exemplo de Testes

```python
import unittest
from intervalos import mesclar_intervalos

class TestIntervalos(unittest.TestCase):
    def test_overlapping_intervals(self):
        self.assertEqual(mesclar_intervalos([(1, 3), (2, 6), (8, 10), (15, 18)]), [(1, 6), (8, 10), (15, 18)])
    
    def test_adjacent_intervals(self):
        self.assertEqual(mesclar_intervalos([(1, 4), (4, 5)]), [(1, 5)])
    
    def test_non_overlapping_and_non_adjacent_intervals(self):
        self.assertEqual(mesclar_intervalos([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)]), [(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)])
    
    def test_empty_input_list(self):
        self.assertEqual(mesclar_intervalos([]), [])

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `mesclar_intervalos`, bem como orientações sobre como criar e executar testes unitários para garantir a qualidade do código.