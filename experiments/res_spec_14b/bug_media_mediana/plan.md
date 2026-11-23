Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar as correções necessárias nas funções `media()` e `mediana()` no arquivo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o estado atual das funções**:
   - Abra o arquivo `estatistica.py` e examine as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas atuais com essas funções, como a falta de tratamento de listas vazias ou a modificação da lista de entrada.

2. **Implementar tratamento de listas vazias**:
   - Adicione uma verificação inicial em ambas as funções para verificar se a lista de entrada está vazia.
   - Se a lista estiver vazia, lance um `ValueError` com a mensagem "A lista de entrada não pode estar vazia".

3. **Garantir que a lista de entrada não seja modificada**:
   - Certifique-se de que as funções trabalham com cópias locais da lista de entrada, em vez de modificar a lista original.
   - Para fazer isso, você pode usar a função `copy()` do Python para criar uma cópia da lista antes de realizar qualquer operação.

4. **Corrigir a função `media()`**:
   - Verifique se a função `media()` calcula corretamente a média da lista de entrada.
   - Se necessário, ajuste a lógica da função para garantir que ela retorna a média correta.

5. **Corrigir a função `mediana()`**:
   - Verifique se a função `mediana()` calcula corretamente a mediana da lista de entrada.
   - Se necessário, ajuste a lógica da função para garantir que ela retorna a mediana correta.
   - Considere usar a função `sorted()` para ordenar a lista antes de calcular a mediana.

6. **Criar ou atualizar os testes**:
   - Crie ou atualize os testes automatizados para verificar se as funções `media()` e `mediana()` estão funcionando corretamente.
   - Testes devem cobrir vários cenários, incluindo listas vazias, listas com números inteiros e floats, e listas de tamanho ímpar e par.
   - Use a biblioteca `unittest` do Python para escrever os testes.

7. **Executar os testes**:
   - Execute os testes automatizados para garantir que todas as condições de aceitação são satisfeitas.
   - Corrija quaisquer falhas nos testes e ajuste as funções conforme necessário.

8. **Documentar as mudanças**:
   - Documente quaisquer mudanças significativas feitas nas funções `media()` e `mediana()`.
   - Certifique-se de que a documentação reflete corretamente a funcionalidade atual das funções.

### Exemplo de Código

Aqui está um exemplo de como as funções podem ser implementadas:

```python
def media(lista):
    if not lista:
        raise ValueError("A lista de entrada não pode estar vazia")
    return sum(lista) / len(lista)

def mediana(lista):
    if not lista:
        raise ValueError("A lista de entrada não pode estar vazia")
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 0:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        return lista_ordenada[n // 2]
```

### Exemplo de Testes

Aqui está um exemplo de como os testes podem ser escritos usando a biblioteca `unittest`:

```python
import unittest
from estatistica import media, mediana

class TestEstatistica(unittest.TestCase):
    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(media([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)
        with self.assertRaises(ValueError):
            media([])

    def test_mediana(self):
        self.assertEqual(mediana([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(mediana([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)
        self.assertEqual(mediana([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(mediana([1.0, 2.0, 3.0, 4.0]), 2.5)
        with self.assertRaises(ValueError):
            mediana([])

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para corrigir as funções `media()` e `mediana()` e garantir que os testes automatizados cobrem todos os casos de uso especificados.