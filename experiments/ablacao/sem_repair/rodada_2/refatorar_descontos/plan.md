### Plano de Refatoração do Arquivo `preco.py`

#### Passo 1: Criar a Função `aplicar_desconto`
1. Defina a função `aplicar_desconto(valor, percentual)` no arquivo `preco.py`.
2. Verifique se o valor é negativo ou se o percentual está fora da faixa válida (0-100).
3. Se os valores estiverem inválidos, lance uma exceção `ValueError`.
4. Caso contrário, calcule o preço com desconto aplicando o percentual ao valor original.
5. Arredonde o preço final para duas casas decimais antes de retorná-lo.

#### Passo 2: Modificar as Funções Existentes
1. Atualize a função `preco_vip(valor)` para usar `aplicar_desconto(valor, 20)`.
2. Atualize a função `preco_normal(valor)` para usar `aplicar_desconto(valor, 5)`.
3. Atualize a função `preco_promocao(valor)` para usar `aplicar_desconto(valor, 30)`.

#### Passo 3: Implementar Testes Unitários
1. Crie ou atualize os testes unitários para verificar o comportamento da função `aplicar_desconto`.
2. Certifique-se de incluir casos de teste que verificam:
   - Valores válidos que retornam preços corretos.
   - Valores inválidos que levantam `ValueError`.
3. Teste também as funções `preco_vip`, `preco_normal`, e `preco_promocao` para garantir que elas ainda funcionam corretamente após a refatoração.

### Código Proposto

```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or percentual < 0 or percentual > 100:
        raise ValueError("Valores inválidos")
    desconto = valor * (percentual / 100)
    preco_final = valor - desconto
    return round(preco_final, 2)

def preco_vip(valor):
    return aplicar_desconto(valor, 20)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
```

### Testes Unitários

```python
import unittest

class TestPreco(unittest.TestCase):

    def test_aplicar_desconto(self):
        self.assertAlmostEqual(aplicar_desconto(100, 20), 79.99, places=2)
        self.assertAlmostEqual(aplicar_desconto(100, 5), 95.00, places=2)
        self.assertAlmostEqual(aplicar_desconto(100, 30), 69.99, places=2)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 20)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(100, -1)
        
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

### Passo 4: Executar os Testes
1. Execute os testes unitários para garantir que todas as funções estão funcionando conforme esperado.
2. Corrija quaisquer erros encontrados durante a execução dos testes.

### Passo 5: Revisar e Comitar as Alterações
1. Revisar o código refatorado para garantir que ele atende aos requisitos e especificações.
2. Comitar as alterações no controle de versão (git, por exemplo).

Este plano garante que o código seja limpo, manutenível e funcione conforme as especificações fornecidas.