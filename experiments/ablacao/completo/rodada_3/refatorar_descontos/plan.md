Baseado na especificação e nos arquivos do projeto fornecidos, segue um plano numerado, passo a passo, do que deve ser programado:

### Plano de Desenvolvimento

1. **Criar a função `aplicar_desconto`:**
   - Definir a função `aplicar_desconto(valor, percentual)` que recebe dois parâmetros: `valor` (um número de ponto flutuante) e `percentual` (um número inteiro).
   - Dentro da função, verificar se o `percentual` está fora do intervalo de 0 a 100 ou se o `valor` é negativo. Se qualquer uma dessas condições for verdadeira, a função deve levantar uma exceção `ValueError`.
   - Calcular o desconto aplicando o percentual ao valor e subtraindo-o do valor original.
   - Arredondar o resultado para duas casas decimais antes de retorná-lo.

2. **Modificar as funções existentes (`preco_vip`, `preco_normal`, `preco_promocao`):**
   - Para cada função, substituir a lógica de cálculo de desconto pela chamada à função `aplicar_desconto`.
   - Passar os parâmetros apropriados para a função `aplicar_desconto`:
     - `preco_vip`: usar `aplicar_desconto(valor, 20)`
     - `preco_normal`: usar `aplicar_desconto(valor, 5)`
     - `preco_promocao`: usar `aplicar_desconto(valor, 30)`

3. **Implementar testes unitários:**
   - Criar um módulo de teste separado (por exemplo, `test_preco.py`) para conter todos os casos de teste.
   - Escrever casos de teste para a função `aplicar_desconto`:
     - Testar com valores válidos para `valor` e `percentual`.
     - Testar com valores inválidos para `valor` e `percentual` (por exemplo, `valor` negativo ou `percentual` fora do intervalo).
   - Escrever casos de teste para as funções modificadas (`preco_vip`, `preco_normal`, `preco_promocao`):
     - Verificar se as funções usam corretamente a função `aplicar_desconto`.
     - Verificar se os resultados são arredondados para duas casas decimais.

4. **Executar os testes e ajustar conforme necessário:**
   - Executar todos os testes criados no módulo de teste.
   - Corrigir quaisquer erros encontrados durante a execução dos testes.
   - Certificar-se de que todas as funções funcionam conforme esperado e que os testes cobrem todas as possíveis entradas válidas e inválidas.

### Exemplo de Código

Aqui está um exemplo de como o código poderia ser implementado:

```python
def aplicar_desconto(valor, percentual):
    if not (0 <= percentual <= 100) or valor < 0:
        raise ValueError("Invalid input parameters")
    
    desconto = valor * percentual / 100
    preco_final = round(valor - desconto, 2)
    return preco_final

def preco_vip(valor):
    return aplicar_desconto(valor, 20)

def preco_normal(valor):
    return aplicar_desconto(valor, 5)

def preco_promocao(valor):
    return aplicar_desconto(valor, 30)
```

### Exemplo de Testes

E aqui está um exemplo de como os testes poderiam ser implementados:

```python
import unittest
from preco import aplicar_desconto, preco_vip, preco_normal, preco_promocao

class TestPreco(unittest.TestCase):
    def test_aplicar_desconto_valid(self):
        self.assertEqual(aplicar_desconto(100, 20), 80.00)
        self.assertEqual(aplicar_desconto(100, 5), 95.00)
        self.assertEqual(aplicar_desconto(100, 30), 70.00)

    def test_aplicar_desconto_invalid(self):
        with self.assertRaises(ValueError):
            aplicar_desconto(-100, 20)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, 101)
        with self.assertRaises(ValueError):
            aplicar_desconto(100, -1)

    def test_preco_vip(self):
        self.assertEqual(preco_vip(100), 80.00)

    def test_preco_normal(self):
        self.assertEqual(preco_normal(100), 95.00)

    def test_preco_promocao(self):
        self.assertEqual(preco_promocao(100), 70.00)

if __name__ == '__main__':
    unittest.main()
```

Este plano inclui a criação ou atualização dos testes para garantir que o código funcione corretamente em todas as situações.