Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar as correções necessárias nas funções `media()` e `mediana()` no módulo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o Código Atual**
   - Abra o arquivo `estatistica.py` e examine as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas atuais, como manipulação da lista original, falta de tratamento de listas vazias, etc.

2. **Tratamento de Listas Vazias**
   - Adicione uma verificação inicial em ambas as funções para verificar se a lista está vazia.
   - Se a lista estiver vazia, lance um `ValueError`.

3. **Cálculo da Média**
   - Na função `media()`, certifique-se de que a lista original não é modificada.
   - Calcule a soma dos elementos da lista e divida pelo número de elementos para obter a média.
   - Retorne o valor da média calculada.

4. **Cálculo da Mediana**
   - Na função `mediana()`, certifique-se de que a lista original não é modificada.
   - Ordenar a lista temporariamente sem modificar a lista original.
   - Calcular a mediana com base no tamanho da lista ordenada.
     - Se o tamanho da lista for ímpar, a mediana será o elemento central.
     - Se o tamanho da lista for par, a mediana será a média dos dois elementos centrais.

5. **Testes Automatizados**
   - Crie ou atualize os testes automatizados para verificar o comportamento das funções.
   - Teste casos onde a lista está vazia, contém números inteiros, contém números float, e contém uma mistura de ambos.
   - Verifique se a lista original não é modificada após a execução das funções.

### Exemplo de Código Modificado

```python
def media(lista):
    if not lista:
        raise ValueError("Lista vazia")
    return sum(lista) / len(lista)

def mediana(lista):
    if not lista:
        raise ValueError("Lista vazia")
    
    # Ordena a lista temporariamente sem modificar a lista original
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[(n // 2) - 1] + lista_ordenada[n // 2]) / 2
```

### Exemplo de Testes Automatizados

```python
import unittest
from estatistica import media, mediana

class TestEstatistica(unittest.TestCase):
    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(media([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)
        with self.assertRaises(ValueError):
            media([])

    def test_mediana(self):
        self.assertEqual(mediana([1, 2, 3, 4, 5]), 3)
        self.assertAlmostEqual(mediana([1.0, 2.0, 3.0, 4.0, 5.0]), 3.0)
        self.assertAlmostEqual(mediana([1.0, 2.0, 3.0, 4.0, 5.0, 6.0]), 3.5)
        with self.assertRaises(ValueError):
            mediana([])

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para corrigir as funções `media()` e `mediana()` e garantir que os testes automatizados cobrem todos os cenários relevantes.