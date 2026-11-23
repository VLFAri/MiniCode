### Plano de Refatoração do Código em `preco.py`

#### Passo 1: Criar a Função `aplicar_desconto`
1. Defina a função `aplicar_desconto(valor, percentual)` no arquivo `preco.py`.
2. Verifique se o valor é negativo ou se o percentual está fora do intervalo de 0 a 100. Se qualquer uma dessas condições for verdadeira, lance um `ValueError`.
3. Calcule o desconto aplicando a porcentagem ao valor original.
4. Arredonde o resultado para duas casas decimais antes de retorná-lo.

```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or not 0 <= percentual <= 100:
        raise ValueError("Invalid input: valor must be non-negative and percentual must be between 0 and 100")
    
    desconto = valor * (percentual / 100)
    preco_final = valor - desconto
    return round(preco_final, 2)
```

#### Passo 2: Atualizar as Funções Existentes
1. Modifique as funções `preco_vip`, `preco_normal`, e `preco_promocao` para usar a função `aplicar_desconto`.
2. Certifique-se de que cada função passe os parâmetros corretos para `aplicar_desconto`.

```python
def preco_vip(valor):
    return aplicar_desconto(valor, 20)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
```

#### Passo 3: Criação ou Atualização dos Testes
1. Adicione testes unitários para a função `aplicar_desconto` usando a biblioteca `unittest`.
2. Certifique-se de que os testes verifiquem tanto o comportamento esperado quanto as exceções `ValueError`.

```python
import unittest

class TestPreco(unittest.TestCase):
    def test_aplicar_desconto(self):
        self.assertAlmostEqual(aplicar_desconto(100, 20), 80.00, places=2)
        self.assertAlmostEqual(aplicar_desconto(100, 5), 95.00, places=2)
        self.assertAlmostEqual(aplicar_desconto(100, 30), 70.00, places=2)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 20)
            
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)
            
    def test_preco_vip(self):
        self.assertAlmostEqual(preco_vip(100), 80.00, places=2)
        
    def test_preco_normal(self):
        self.assertAlmostEqual(preco_normal(100), 95.00, places=2)
        
    def test_preco_promocao(self):
        self.assertAlmostEqual(preco_promocao(100), 70.00, places=2)

if __name__ == '__main__':
    unittest.main()
```

### Resumo do Plano
1. Implemente a função `aplicar_desconto` com verificações de entrada válidas e cálculo de desconto.
2. Atualize as funções existentes (`preco_vip`, `preco_normal`, `preco_promocao`) para utilizar a função `aplicar_desconto`.
3. Crie testes unitários para garantir que a refatoração não altera o comportamento das funções originais e que a função `aplicar_desconto` funciona conforme esperado.

Este plano garante que o código seja refatorado de forma eficiente, mantendo a funcionalidade original e adicionando testes para garantir a qualidade do código.