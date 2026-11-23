Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar as correções necessárias nas funções `media()` e `mediana()` no módulo `estatistica.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Verificar o Código Atual**
   - Abra o arquivo `estatistica.py` e revise as funções `media()` e `mediana()`.
   - Identifique quaisquer problemas existentes, como manipulação da lista de entrada ou falta de tratamento de listas vazias.

2. **Implementar Tratamento de Listas Vazias**
   - Adicione uma verificação no início de cada função para verificar se a lista de entrada está vazia.
   - Se a lista estiver vazia, lance um `ValueError`.

3. **Garantir que a Lista de Entrada Não Seja Modificada**
   - Certifique-se de que nenhuma operação dentro das funções modifica a lista original.
   - Use cópias da lista de entrada quando necessário para evitar alterações na lista original.

4. **Corrigir a Função `media()`**
   - Implemente a lógica para calcular a média aritmética corretamente.
   - Certifique-se de que a soma é calculada corretamente e dividida pelo número de elementos.

5. **Corrigir a Função `mediana()`**
   - Implemente a lógica para calcular a mediana corretamente.
   - Considere o caso onde a lista tem um número par de elementos e a mediana é a média entre os dois elementos centrais.

6. **Criar ou Atualizar Testes Automatizados**
   - Crie ou atualize os casos de teste para cobrir todas as condições mencionadas na especificação.
   - Inclua testes para listas vazias, listas com um único elemento, listas com números pares e ímpares de elementos.
   - Verifique se as funções lançam `ValueError` corretamente para listas vazias.
   - Verifique se a lista de entrada não é modificada após a execução das funções.

7. **Executar Testes**
   - Execute todos os testes automatizados para garantir que todas as funções funcionem conforme esperado.
   - Corrija quaisquer falhas encontradas nos testes.

8. **Documentação e Revisão**
   - Revise o código para garantir que ele atenda aos requisitos e critérios de aceitação.
   - Documente as funções e os testes para facilitar a manutenção futura.

### Exemplo de Código Corrigido

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
    if n % 2 == 0:
        return (lista_ordenada[n // 2 - 1] + lista_ordenada[n // 2]) / 2
    else:
        return lista_ordenada[n // 2]
```

### Exemplo de Testes

```python
import unittest
from estatistica import media, mediana

class TestEstatistica(unittest.TestCase):
    def test_media(self):
        self.assertEqual(media([1, 2, 3, 4]), 2.5)
        self.assertAlmostEqual(media([1.5, 2.5, 3.5]), 2.5)
        with self.assertRaises(ValueError):
            media([])

    def test_mediana(self):
        self.assertEqual(mediana([1, 2, 3, 4]), 2.5)
        self.assertEqual(mediana([1, 2, 3, 4, 5]), 3)
        with self.assertRaises(ValueError):
            mediana([])

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem ajudar a garantir que as funções `media()` e `mediana()` funcionem corretamente e que os testes automatizados validem as correções.