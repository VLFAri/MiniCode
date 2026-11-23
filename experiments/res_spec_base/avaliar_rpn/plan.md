Baseado na especificação e nas instruções fornecidas, aqui está um plano passo a passo para implementar a função `avaliar_rpn` no arquivo `rpn.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Criar o arquivo `rpn.py`**
   - Crie um novo arquivo chamado `rpn.py`.

2. **Implementar a função `avaliar_rpn`**
   - Dentro do arquivo `rpn.py`, defina a função `avaliar_rpn(expressao)` que recebe uma string `expressao` como parâmetro.
   - Implemente a lógica para avaliar a expressão em notação polonesa reversa (RPN).
   - Use uma pilha para armazenar operandos e realizar operações conforme encontradas na expressão.
   - Para cada token na expressão:
     - Se for um número, adicione-o à pilha.
     - Se for um operador, remova dois operandos da pilha, realize a operação correspondente e empilhe o resultado.
   - Certifique-se de que a função lance `ValueError` para expressões inválidas e `ZeroDivisionError` para divisões por zero.

3. **Validar a entrada**
   - Antes de processar a expressão, valide a entrada para garantir que ela seja uma string não vazia.
   - Verifique se todos os tokens são válidos (números ou operadores conhecidos).

4. **Testar condições de erro**
   - Adicione casos de teste que incluem expressões inválidas e divisões por zero para garantir que os erros sejam lançados corretamente.

5. **Criar um arquivo de teste**
   - Crie um novo arquivo chamado `test_rpn.py` para os testes automatizados.
   - Importe a função `avaliar_rpn` do módulo `rpn`.
   - Escreva casos de teste para validar a funcionalidade da função, incluindo entradas válidas, inválidas, e divisões por zero.

6. **Executar os testes**
   - Execute os testes usando um framework de testes como `unittest` ou `pytest` para verificar se a função `avaliar_rpn` atende aos critérios especificados.

### Exemplo de Código

#### `rpn.py`
```python
def avaliar_rpn(expressao):
    if not expressao:
        raise ValueError("Expressão vazia")

    pilha = []
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    try:
        for token in expressao.split():
            if token in operadores:
                try:
                    y = pilha.pop()
                    x = pilha.pop()
                    resultado = operadores[token](x, y)
                    pilha.append(resultado)
                except IndexError:
                    raise ValueError("Operadores faltam operandos")
            else:
                pilha.append(float(token))
    except ZeroDivisionError:
        raise ZeroDivisionError("Divisão por zero")

    return pilha[0]
```

#### `test_rpn.py`
```python
import unittest
from rpn import avaliar_rpn

class TestRPN(unittest.TestCase):
    def test_valid_expression(self):
        self.assertEqual(avaliar_rpn('3 4 +'), 7)
        self.assertEqual(avaliar_rpn('3 4 *'), 12)
        self.assertEqual(avaliar_rpn('3 4 /'), 0.75)
        self.assertEqual(avaliar_rpn('3 4 -'), -1)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            avaliar_rpn('3 4 + a')
        with self.assertRaises(ValueError):
            avaliar_rpn('3 4 + -')

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            avaliar_rpn('3 0 /')

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código fornecem uma estrutura clara para implementar a função `avaliar_rpn` e seus testes associados.