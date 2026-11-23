# Specification

## Objective
Eliminar a duplicação no arquivo `preco.py` para criar funções específicas para diferentes tipos de descontos.

## Parameters / Requirements
- **Entradas**:
  - `valor`: Valor do produto (número).
  - `percentual`: Percentual de desconto (número).

- **Restrições e Regras de Negócio**:
  - O valor deve ser um número positivo.
  - O percentual deve estar entre 0 e 100.
  - Se o valor for negativo ou o percentual não estiver entre 0 e 100, deve lançar uma exceção `ValueError`.
  - O resultado deve ser arredondado para duas casas decimais.

## Acceptance Criteria
- A função `aplicar_desconto` deve retornar o valor com o desconto aplicado, arredondado para duas casas decimais.
- As funções `preco_vip`, `preco_normal`, e `preco_promocao` devem usar a função `aplicar_desconto` sem alterar seu comportamento atual.

## Arquivos do projeto
- `preco.py`

### Código do arquivo `preco.py`
```python
def aplicar_desconto(valor, percentual):
    if valor < 0 or not 0 <= percentual <= 100:
        raise ValueError("Valor deve ser positivo e percentual deve estar entre 0 e 100")
    
    desconto = valor * (percentual / 100)
    return round(desconto, 2)

def preco_vip(value):
    return aplicar_desconto(value, 20)

def preco_normal(value):
    return aplicar_desconto(value, 5)

def preco_promocao(value):
    return aplicar_desconto(value, 30)
```

### Testes Automatizados
Para garantir que as funções funcionam conforme esperado, você pode escrever os seguintes testes usando uma biblioteca como `unittest`:

```python
import unittest

class TestPrecoFunctions(unittest.TestCase):
    def test_aplicar_desconto(self):
        self.assertEqual(aplicar_desconto(100, 20), 80.00)
        self.assertEqual(aplicar_desconto(50, 10), 45.00)
        self.assertEqual(aplicar_desconto(-10, 10), ValueError)
        self.assertEqual(aplicar_desconto(100, 101), ValueError)
        self.assertEqual(aplicar_desconto(100, 0), ValueError)
        self.assertEqual(aplicar_desconto(100, 100), 100.00)

    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 80.00)
        self.assertEqual(preco_vip(50), 45.00)

    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 50.00)

    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 70.00)

if __name__ == '__main__':
    unittest.main()
```

Esses testes garantirão que as funções `aplicar_desconto`, `preco_vip`, `preco_normal`, e `preco_promocao` funcionem corretamente e que o código seja consistente.