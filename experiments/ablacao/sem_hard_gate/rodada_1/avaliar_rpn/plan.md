Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `avaliar_rpn` no arquivo `rpn.py`. Além disso, incluiremos a criação ou atualização dos testes necessários.

### Passo 1: Criar o Arquivo `rpn.py`
Crie um novo arquivo chamado `rpn.py` no diretório do projeto.

### Passo 2: Implementar a Função `avaliar_rpn`
Dentro do arquivo `rpn.py`, implemente a função `avaliar_rpn` com as seguintes características:

```python
def avaliar_rpn(expression):
    # Implementação da função aqui
```

#### Estrutura Básica da Função
1. **Validação da Expressão**: Verifique se a expressão não está vazia.
2. **Tokenização**: Separe a expressão em tokens usando espaços como delimitador.
3. **Processamento da Expressão**: Use uma pilha para processar os tokens. Para cada token:
   - Se for um número, adicione-o à pilha.
   - Se for um operador, remova dois elementos da pilha, aplique o operador e coloque o resultado de volta na pilha.
4. **Verificação Final**: Certifique-se de que a pilha contenha apenas um elemento após processar toda a expressão.
5. **Retorno do Resultado**: Retorne o único elemento restante na pilha.

#### Exceções
- **ValueError**: Lançar `ValueError` se a expressão estiver vazia, contiver tokens desconhecidos, ou se houver operandos faltando ou sobrando.
- **ZeroDivisionError**: Lançar `ZeroDivisionError` se a divisão por zero for tentada.

### Passo 3: Implementar Testes Automatizados
Crie um novo arquivo chamado `test_rpn.py` para os testes automatizados.

#### Estrutura do Arquivo de Testes
```python
import unittest
from rpn import avaliar_rpn

class TestRPN(unittest.TestCase):

    def test_valid_expression(self):
        self.assertEqual(avaliar_rpn("3 4 +"), 7)
        self.assertEqual(avaliar_rpn("3 4 *"), 12)
        self.assertEqual(avaliar_rpn("3 4 -"), -1)
        self.assertEqual(avaliar_rpn("3 4 /"), 0.75)
        self.assertEqual(avaliar_rpn("3 4 5 + *"), 39)
        self.assertEqual(avaliar_rpn("3 4 5 * +"), 23)
        self.assertEqual(avaliar_rpn("3 4 5 + * 2 /"), 19.5)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            avaliar_rpn("")
            avaliar_rpn("3 4 + 5")
            avaliar_rpn("3 4 + 5 +")
            avaliar_rpn("3 4 + 5 + 6")
            avaliar_rpn("3 4 + 5 + 6 +")
            avaliar_rpn("3 4 + 5 + 6 + 7")
            avaliar_rpn("3 4 + 5 + 6 + 7 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 +")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19 + 20 + 21")
            avaliar_rpn("3 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12 + 13 + 14 + 15 + 16 + 17 + 18 + 19