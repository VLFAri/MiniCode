### Plano de Refatoração do Projeto `preco.py`

#### Passo 1: Criar a Função `aplicar_desconto`
1. Defina a função `aplicar_desconto(valor, percentual)` no arquivo `preco.py`.
2. Verifique se o parâmetro `valor` é negativo ou se o parâmetro `percentual` está fora da faixa de 0 a 100. Se qualquer uma dessas condições for verdadeira, lance um `ValueError`.
3. Calcule o desconto aplicando o percentual ao valor.
4. Arredonde o resultado para duas casas decimais antes de retorná-lo.

```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or percentual < 0 or percentual > 100:
        raise ValueError("Valor inválido")
    desconto = valor * (percentual / 100)
    return round(valor - desconto, 2)
```

#### Passo 2: Modificar as Funções Existentes
1. Atualize a função `preco_vip` para usar `aplicar_desconto` com um desconto de 20%.
2. Atualize a função `preco_normal` para usar `aplicar_desconto` com um desconto de 5%.
3. Atualize a função `preco_promocao` para usar `aplicar_desconto` com um desconto de 30%.

```python
def preco_vip(valor):
    return aplicar_desconto(valor, 20)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
```

#### Passo 3: Implementar Testes Unitários
1. Crie um módulo de teste chamado `test_preco.py`.
2. Importe as funções necessárias do arquivo `preco.py`.
3. Escreva casos de teste para verificar se a função `aplicar_desconto` funciona corretamente com valores válidos e inválidos.
4. Escreva casos de teste para verificar se as funções `preco_vip`, `preco_normal`, e `preco_promocao` estão usando corretamente a função `aplicar_desconto`.

```python
import unittest
from preco import aplicar_desconto, preco_vip, preco_normal, preco_promocao

class TestPreco(unittest.TestCase):

    def test_aplicar_desconto_valid(self):
        self.assertEqual(aplicar_desconto(100, 20), 80)
        self.assertEqual(aplicar_desconto(150, 5), 142.5)
        self.assertEqual(aplicar_desconto(200, 30), 140)

    def test_aplicar_desconto_invalid(self):
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 20)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, -1)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)

    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 80)

    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 95)

    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 70)

if __name__ == '__main__':
    unittest.main()
```

#### Passo 4: Executar os Testes
1. Execute os testes unitários para garantir que todas as funções funcionem conforme esperado.
2. Certifique-se de que todos os casos de teste passam sem erros.

```bash
python -m unittest test_preco.py
```

Este plano detalha os passos necessários para refatorar o código existente em `preco.py`, criando uma função genérica para calcular descontos e garantindo que todas as funções de preço sejam testadas adequadamente.