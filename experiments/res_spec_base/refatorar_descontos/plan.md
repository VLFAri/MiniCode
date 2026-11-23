Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para reestruturar o arquivo `preco.py` e incluir a criação ou atualização dos testes:

### Plano de Implementação

1. **Reestruturação da Função `aplicar_desconto`**
   - Mantenha a verificação de entradas válidas (`valor` positivo e `percentual` entre 0 e 100).
   - Ajuste a função para calcular o valor final após o desconto, em vez de apenas o desconto.
   - Certifique-se de que o resultado é arredondado para duas casas decimais.

2. **Criação de Funções Específicas para Descontos**
   - Crie funções específicas para cada tipo de desconto (`preco_vip`, `preco_normal`, `preco_promocao`).
   - Use a função `aplicar_desconto` internamente para calcular os preços finais.

3. **Testes Automatizados**
   - Atualize os testes existentes para refletir as mudanças feitas na função `aplicar_desconto`.
   - Adicione novos testes para as funções específicas de desconto.

### Código Reestruturado

```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or not 0 <= percentual <= 100:
        raise ValueError("Valor deve ser positivo e percentual deve estar entre 0 e 100")
    
    valor_final = valor * ((100 - percentual) / 100)
    return round(valor_final, 2)

def preco_vip(value):
    return aplicar_desconto(value, 20)

def preco_normal(value):
    return aplicar_desconto(value, 5)

def preco_promocao(value):
    return aplicar_desconto(value, 30)
```

### Testes Automatizados

```python
import unittest

class TestPrecoFunctions(unittest.TestCase):
    def test_aplicar_desconto(self):
        self.assertAlmostEqual(aplicar_desconto(100, 20), 80.00, places=2)
        self.assertAlmostEqual(aplicar_desconto(50, 10), 45.00, places=2)
        with self.assertRaises(ValueError):
            aplicar_desconto(-10, 10)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 0)
        self.assertAlmostEqual(aplicar_desconto(100, 100), 0.00, places=2)

    def test_preco_vip(self):
        self.assertAlmostEqual(preco_vip(100), 80.00, places=2)
        self.assertAlmostEqual(preco_vip(50), 45.00, places=2)

    def test_preco_normal(self):
        self.assertAlmostEqual(preco_normal(100), 95.00, places=2)

    def test_preco_promocao(self):
        self.assertAlmostEqual(preco_promocao(100), 70.00, places=2)

if __name__ == '__main__':
    unittest.main()
```

### Passo a Passo

1. **Atualizar a função `aplicar_desconto`**
   - Modificar a função para calcular o valor final após o desconto.
   - Manter a verificação de entradas válidas.

2. **Criar funções específicas para descontos**
   - Definir funções `preco_vip`, `preco_normal`, e `preco_promocao` que utilizam `aplicar_desconto`.

3. **Atualizar os testes automatizados**
   - Ajustar os testes existentes para refletir as mudanças na função `aplicar_desconto`.
   - Adicionar novos testes para as funções específicas de desconto.

Este plano garante que o código seja limpo, eficiente e fácil de manter, além de garantir que todas as funções funcionem corretamente através de testes automatizados.