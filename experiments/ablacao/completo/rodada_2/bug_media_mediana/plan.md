Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar as correções necessárias nas funções `media()` e `mediana()` no arquivo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o estado atual das funções:**
   - Abra o arquivo `estatistica.py` e examine as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas atuais com essas funções, como a falta de tratamento de listas vazias ou a modificação da lista de entrada.

2. **Implementar tratamento de listas vazias:**
   - Adicione uma verificação no início de cada função para verificar se a lista de entrada está vazia.
   - Se a lista estiver vazia, lance um `ValueError`.

3. **Garantir que a lista de entrada não seja modificada:**
   - Certifique-se de que as funções trabalham com cópias da lista de entrada, não com a lista original.
   - Isso pode ser feito usando a função `copy()` do Python ou criando uma nova lista com os mesmos elementos.

4. **Corrigir a lógica para calcular a média:**
   - Verifique se a função `media()` soma corretamente todos os elementos da lista e divide pelo número total de elementos.
   - Certifique-se de que a função trata corretamente os casos onde a lista contém apenas um elemento.

5. **Corrigir a lógica para calcular a mediana:**
   - Verifique se a função `mediana()` ordena corretamente a lista de entrada antes de calcular a mediana.
   - Para listas de tamanho ímpar, a mediana é o valor central.
   - Para listas de tamanho par, a mediana é a média dos dois valores centrais.

6. **Adicionar testes automatizados:**
   - Crie ou atualize os testes automatizados para verificar se as funções `media()` e `mediana()` estão funcionando corretamente.
   - Testes devem cobrir vários cenários, incluindo listas vazias, listas com um único elemento, listas com números pares e ímpares de elementos.

### Exemplo de Código

Aqui está um exemplo de como as funções podem ser implementadas:

```python
def media(lista):
    if not lista:
        raise ValueError("Lista vazia")
    
    # Criar uma cópia da lista para evitar modificar a lista original
    lista_copia = lista.copy()
    
    return sum(lista_copia) / len(lista_copia)

def mediana(lista):
    if not lista:
        raise ValueError("Lista vazia")
    
    # Ordenar a lista sem modificar a lista original
    lista_ordenada = sorted(lista)
    
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[(n // 2) - 1] + lista_ordenada[n // 2]) / 2
```

### Exemplo de Testes Automatizados

Você pode usar a biblioteca `unittest` do Python para criar testes automatizados:

```python
import unittest
from estatistica import media, mediana

class TestEstatistica(unittest.TestCase):
    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            media([])

    def test_mediana_lista_vazia(self):
        with self.assertRaises(ValueError):
            mediana([])

    def test_media_lista_um_elemento(self):
        self.assertEqual(media([10]), 10)

    def test_mediana_lista_um_elemento(self):
        self.assertEqual(mediana([10]), 10)

    def test_media_lista_dois_elementos(self):
        self.assertEqual(media([1, 2]), 1.5)

    def test_mediana_lista_dois_elementos(self):
        self.assertEqual(mediana([1, 2]), 1.5)

    def test_media_lista_tres_elementos(self):
        self.assertEqual(media([1, 2, 3]), 2)

    def test_mediana_lista_tres_elementos(self):
        self.assertEqual(mediana([1, 2, 3]), 2)

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar as correções necessárias e garantir que os testes automatizados cobrem todas as condições especificadas.