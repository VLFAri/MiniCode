### Plano de Desenvolvimento

1. **Análise do Código Atual**
   - Analisar o arquivo `preco.py` para entender a lógica existente em `preco_vip`, `preco_normal`, e `preco_promocao`.
   - Identificar a duplicação de código relacionada ao cálculo de desconto.

2. **Criação da Função `aplicar_desconto`**
   - Definir a função `aplicar_desconto(valor, percentual)` que calcula o valor com desconto.
   - Implementar a verificação de entrada para garantir que `valor` não seja negativo e `percentual` esteja entre 0 e 100.
   - Tratar entradas inválidas lançando uma exceção `ValueError`.
   - Arredondar o resultado para duas casas decimais.

3. **Refatoração das Funções Existentes**
   - Substituir a lógica de cálculo de desconto nas funções `preco_vip`, `preco_normal`, e `preco_promocao` pela chamada à função `aplicar_desconto`.
   - Manter o comportamento atual das funções sem alterações significativas.

4. **Testes Unitários**
   - Criar ou atualizar os testes unitários para verificar o funcionamento correto da função `aplicar_desconto`.
   - Incluir casos de teste para entradas válidas e inválidas.
   - Verificar se as funções `preco_vip`, `preco_normal`, e `preco_promocao` ainda funcionam corretamente após a refatoração.

5. **Execução e Verificação dos Testes**
   - Executar todos os testes unitários para garantir que todas as condições de aceitação são atendidas.
   - Corrigir quaisquer problemas identificados durante a execução dos testes.

6. **Documentação e Revisão**
   - Documentar as mudanças feitas no código e os novos testes criados.
   - Revisar o código refatorado para garantir que ele está de acordo com as melhores práticas de codificação.

### Implementação Detalhada

#### Passo 1: Análise do Código Atual
- Abra o arquivo `preco.py` e identifique onde a lógica de cálculo de desconto é repetida.

#### Passo 2: Criação da Função `aplicar_desconto`
```python
def aplicar_desconto(valor, percentual):
    if valor < 0:
        raise ValueError("O valor não pode ser negativo.")
    if not (0 <= percentual <= 100):
        raise ValueError("O percentual de desconto deve estar entre 0 e 100.")
    
    desconto = valor * (percentual / 100)
    preco_com_desconto = valor - desconto
    
    return round(preco_com_desconto, 2)
```

#### Passo 3: Refatoração das Funções Existentes
- Modificar as funções `preco_vip`, `preco_normal`, e `preco_promocao` para usar a função `aplicar_desconto`.

```python
def preco_vip(valor):
    return aplicar_desconto(valor, 10)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 20)
```

#### Passo 4: Testes Unitários
- Adicionar ou modificar os testes unitários para incluir verificações da nova função `aplicar_desconto`.

```python
import unittest
from preco import aplicar_desconto, preco_vip, preco_normal, preco_promocao

class TestPreco(unittest.TestCase):
    def test_aplicar_desconto(self):
        self.assertEqual(aplicar_desconto(100, 10), 90.0)
        self.assertEqual(aplicar_desconto(200, 20), 160.0)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 10)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)
        
        with self.assertRaises(ValueError):
            aplicar_desconto(100, -10)
    
    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 90.0)
    
    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 95.0)
    
    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 80.0)

if __name__ == '__main__':
    unittest.main()
```

#### Passo 5: Execução e Verificação dos Testes
- Executar os testes unitários para garantir que todas as funções estão funcionando corretamente.

#### Passo 6: Documentação e Revisão
- Documentar as mudanças feitas no código e os novos testes criados.
- Revisar o código refatorado para garantir que ele está de acordo com as melhores práticas de codificação.

Este plano fornece uma estrutura clara para refatorar o código e garantir que ele funcione corretamente após as alterações.