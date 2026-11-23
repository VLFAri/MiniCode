Baseado na especificação e nos arquivos do projeto fornecidos, segue um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Criar a função `aplicar_desconto`**:
   - Definir a função `aplicar_desconto(valor, percentual)` dentro do arquivo `preco.py`.
   - Implementar a lógica para verificar se o `percentual` está entre 0 e 100 e se o `valor` é negativo.
   - Se qualquer uma das condições acima for verdadeira, lançar um `ValueError`.
   - Calcular o desconto aplicando a porcentagem ao valor e retornar o resultado arredondado para duas casas decimais.

2. **Modificar as funções existentes (`preco_vip`, `preco_normal`, `preco_promocao`)**:
   - Atualizar cada função para usar a função `aplicar_desconto` em vez da lógica de cálculo de desconto existente.
   - Certificar-se de que os parâmetros de entrada para `aplicar_desconto` correspondam aos valores atuais usados nas funções.

3. **Implementar testes unitários**:
   - Adicionar testes para a função `aplicar_desconto` verificando diferentes cenários (por exemplo, entradas válidas e inválidas).
   - Adicionar testes para as funções `preco_vip`, `preco_normal`, e `preco_promocao` para garantir que elas ainda funcionam corretamente após a refatoração.

### Passos Detalhados

#### Passo 1: Criar a função `aplicar_desconto`

```python
def aplicar_desconto(valor, percentual):
    if not 0 <= percentual <= 100 or valor < 0:
        raise ValueError("Invalid input parameters")
    
    desconto = valor * (percentual / 100)
    return round(valor - desconto, 2)
```

#### Passo 2: Modificar as funções existentes

```python
def preco_vip(valor):
    return aplicar_desconto(valor, 20)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
```

#### Passo 3: Implementar testes unitários

Adicione os seguintes testes ao final do arquivo `preco.py` ou em um novo arquivo de teste separado:

```python
import unittest

class TestPreco(unittest.TestCase):

    def test_aplicar_desconto_valid(self):
        self.assertEqual(aplicar_desconto(100, 20), 80)
        self.assertEqual(aplicar_desconto(100, 5), 95)
        self.assertEqual(aplicar_desconto(100, 30), 70)

    def test_aplicar_desconto_invalid(self):
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 20)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, -1)

    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 80)

    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 95)

    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 70)

if __name__ == '__main__':
    unittest.main()
```

### Execução dos Testes

Para executar os testes, você pode rodar o script diretamente se estiver configurado corretamente. Certifique-se de que o ambiente Python esteja configurado para reconhecer e executar os testes.

Este plano cobre todos os aspectos mencionados na especificação, garantindo que a refatoração seja feita corretamente e que os testes confirmem a funcionalidade esperada.