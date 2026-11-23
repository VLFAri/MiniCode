Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `avaliar_rpn` no arquivo `rpn.py`. Além disso, também incluirei a criação ou atualização dos testes necessários.

### Passo 1: Estrutura do Projeto
Criar a estrutura básica do projeto com os seguintes arquivos:
- `rpn.py`: Arquivo principal onde será implementada a função `avaliar_rpn`.
- `tests/test_rpn.py`: Arquivo de teste para validar a função `avaliar_rpn`.

### Passo 2: Implementação da Função `avaliar_rpn`
No arquivo `rpn.py`, implemente a função `avaliar_rpn` seguindo as etapas abaixo:

1. **Validação da Entrada**: Verifique se a string de entrada não é vazia e se contém apenas tokens válidos (números e operadores).
2. **Processamento da Expressão**: Use uma pilha para processar a expressão RPN. Para cada token, faça o seguinte:
   - Se for um número, adicione-o à pilha.
   - Se for um operador, remova dois elementos da pilha, aplique o operador e coloque o resultado de volta na pilha.
3. **Verificação de Erros**: Certifique-se de que a pilha tenha exatamente um elemento ao final da expressão. Se não, lance um `ValueError`. Verifique também se ocorreu uma tentativa de divisão por zero e lance um `ZeroDivisionError` nesse caso.

### Passo 3: Criação de Testes Automatizados
No arquivo `tests/test_rpn.py`, crie casos de teste para cobrir todos os cenários possíveis, incluindo entradas válidas e inválidas.

1. **Teste de Entrada Válida**: Crie testes para expressões RPN válidas que devem retornar resultados corretos.
2. **Teste de Entrada Inválida**: Crie testes para expressões RPN inválidas que devem lançar exceções (`ValueError` ou `ZeroDivisionError`) conforme especificado.
3. **Teste de Divisão por Zero**: Crie testes específicos para verificar se a função lança `ZeroDivisionError` quando a divisão por zero é tentada.

### Passo 4: Execução dos Testes
Executar os testes criados para garantir que a função `avaliar_rpn` funcione corretamente e lance as exceções apropriadas em situações inválidas.

### Código Exemplo

#### rpn.py
```python
def avaliar_rpn(expression):
    if not expression:
        raise ValueError("Expression cannot be empty")

    stack = []
    operators = {'+', '-', '*', '/'}
    
    # Split the expression into tokens
    tokens = expression.split()
    
    for token in tokens:
        if token in operators:
            try:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)
            except IndexError:
                raise ValueError("Invalid expression: missing operands")
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError(f"Invalid token '{token}'")
    
    if len(stack) != 1:
        raise ValueError("Invalid expression: too many operands")
    
    return stack[0]
```

#### tests/test_rpn.py
```python
import unittest
from rpn import avaliar_rpn

class TestRPN(unittest.TestCase):
    def test_valid_expression(self):
        self.assertEqual(avaliar_rpn("3 4 +"), 7)
        self.assertEqual(avaliar_rpn("5 1 2 + 4 * + 3 -"), 14)
    
    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            avaliar_rpn("")
        with self.assertRaises(ValueError):
            avaliar_rpn("3 4 + x")
        with self.assertRaises(ValueError):
            avaliar_rpn("3 4 + 5")
    
    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            avaliar_rpn("3 0 /")

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `avaliar_rpn` e garantir sua correta validação através de testes automatizados.