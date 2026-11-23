Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo de como implementar as correções necessárias nas funções `media()` e `mediana()` no módulo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o Código Atual**
   - Abra o arquivo `estatistica.py` e verifique as implementações atuais das funções `media()` e `mediana()`.
   - Identifique quais partes do código precisam ser corrigidas para atender aos requisitos especificados.

2. **Implementar a Verificação de Lista Vazia**
   - Adicione uma verificação no início de ambas as funções (`media()` e `mediana()`) para verificar se a lista de entrada está vazia.
   - Se a lista estiver vazia, lance um `ValueError`.

3. **Corrigir a Cálculo da Média**
   - Certifique-se de que a função `media()` calcula a média corretamente.
   - A média é calculada somando todos os elementos da lista e dividindo pelo número de elementos.
   - Garanta que a lista original não seja modificada durante o cálculo.

4. **Corrigir a Cálculo da Mediana**
   - Certifique-se de que a função `mediana()` calcula a mediana corretamente.
   - A mediana é o valor do meio quando os números são ordenados. Se houver um número par de elementos, a mediana é a média dos dois números centrais.
   - Garanta que a lista original não seja modificada durante o cálculo.

5. **Criar Testes Automatizados**
   - Crie ou atualize os testes automatizados para garantir que as funções funcionem conforme esperado.
   - Os testes devem cobrir diferentes cenários, incluindo listas vazias, listas com um único elemento, listas com números pares e ímpares de elementos.
   - Use uma estrutura de teste como `unittest` ou `pytest` para escrever os testes.

6. **Executar os Testes**
   - Execute os testes automatizados para verificar se todas as funções estão funcionando corretamente.
   - Corrija quaisquer falhas encontradas nos testes.

7. **Documentar as Alterações**
   - Documente as alterações feitas no código e nos testes.
   - Certifique-se de que a documentação reflete as mudanças feitas e como usar as funções corretamente.

### Exemplo de Código Modificado

Aqui está um exemplo de como as funções podem ser modificadas:

```python
def media(lista):
    if not lista:
        raise ValueError("Lista vazia")
    return sum(lista) / len(lista)

def mediana(lista):
    if not lista:
        raise ValueError("Lista vazia")
    
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    if n % 2 == 1:
        return lista_ordenada[n // 2]
    else:
        return (lista_ordenada[(n // 2) - 1] + lista_ordenada[n // 2]) / 2
```

### Exemplo de Testes

Aqui está um exemplo de como os testes podem ser escritos usando `unittest`:

```python
import unittest
from estatistica import media, mediana

class TestEstatistica(unittest.TestCase):
    def test_media_lista_vazia(self):
        with self.assertRaises(ValueError):
            media([])

    def test_media_lista_um_elemento(self):
        self.assertEqual(media([10]), 10)

    def test_media_lista_dois_elementos(self):
        self.assertAlmostEqual(media([10, 20]), 15)

    def test_mediana_lista_vazia(self):
        with self.assertRaises(ValueError):
            mediana([])

    def test_mediana_lista_um_elemento(self):
        self.assertEqual(mediana([10]), 10)

    def test_mediana_lista_dois_elementos(self):
        self.assertEqual(mediana([10, 20]), 15)

    def test_mediana_lista_tres_elementos(self):
        self.assertEqual(mediana([10, 20, 30]), 20)

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar as correções necessárias e garantir que os testes cobrem adequadamente as funcionalidades.