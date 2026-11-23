### Plano de Refatoração do Projeto `preco.py`

#### Passo 1: Criar a Função `aplicar_desconto`
1. **Definir a função `aplicar_desconto`**: Crie uma função que aceite dois parâmetros, `valor` e `percentual`.
2. **Validar os Parâmetros**: Verifique se `valor` é negativo ou se `percentual` está fora da faixa de 0 a 100. Se qualquer uma dessas condições for verdadeira, lance um `ValueError`.
3. **Calcular o Desconto**: Subtraia o desconto do valor original e arredonde o resultado para duas casas decimais.
4. **Retornar o Valor Descontado**: Retorne o valor calculado.

```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or not 0 <= percentual <= 100:
        raise ValueError("Invalid input: valor must be non-negative and percentual must be between 0 and 100")
    desconto = valor * (percentual / 100)
    valor_final = round(valor - desconto, 2)
    return valor_final
```

#### Passo 2: Refatorar as Funções Existentes
5. **Refatorar `preco_vip`**: Use a função `aplicar_desconto` com os argumentos apropriados para calcular o preço VIP.
6. **Refatorar `preco_normal`**: Use a função `aplicar_desconto` com os argumentos apropriados para calcular o preço normal.
7. **Refatorar `preco_promocao`**: Use a função `aplicar_desconto` com os argumentos apropriados para calcular o preço promocional.

```python
def preco_vip(valor):
    return aplicar_desconto(valor, 10)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 20)
```

#### Passo 3: Implementar Testes Unitários
8. **Criar Testes para `aplicar_desconto`**:
   - Teste com valores válidos.
   - Teste com valores inválidos (negativos e fora do intervalo).

```python
import unittest

class TestPreco(unittest.TestCase):
    def test_aplicar_desconto_valid(self):
        self.assertEqual(aplicar_desconto(100, 10), 90.00)
        self.assertEqual(aplicar_desconto(200, 20), 160.00)
    
    def test_aplicar_desconto_invalid(self):
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 10)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 110)
```

9. **Criar Testes para as Funções Refatoradas**:
   - Verificar se as funções retornam os mesmos resultados que antes da refatoração.

```python
    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 90.00)
    
    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 95.00)
    
    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 80.00)
```

#### Passo 4: Executar os Testes
10. **Executar os Testes**: Certifique-se de que todos os testes passem sem erros.

```bash
python -m unittest
```

### Conclusão
Este plano detalha os passos necessários para refatorar o arquivo `preco.py`, incluindo a criação de uma nova função `aplicar_desconto` e a implementação de testes unitários para garantir a integridade das mudanças.