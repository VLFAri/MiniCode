Baseado na especificação fornecida, aqui está um plano passo a passo para refatorar o arquivo `contador.py`:

### Plano de Refatoração

1. **Criação da Classe `Contador`**
   - Defina a classe `Contador` com os métodos `incrementar`, `valor` e `zerar`.
   - Implemente o método `__init__` para inicializar o valor do contador.

2. **Implementação dos Métodos da Classe `Contador`**
   - Implemente o método `incrementar` que aceita um parâmetro opcional `passo` (padrão = 1).
   - Implemente o método `valor` que retorna o valor atual do contador.
   - Implemente o método `zerar` que redefine o valor do contador para zero.

3. **Atualização das Funções de Módulo**
   - Crie uma instância padrão da classe `Contador` para ser usada pelas funções de módulo.
   - Atualize as funções `incrementar`, `valor` e `zerar` para delegar suas operações para a instância padrão da classe `Contador`.

4. **Testes Unitários**
   - Crie ou atualize os testes unitários para garantir que todos os métodos funcionem conforme esperado.
   - Teste a independência entre diferentes instâncias da classe `Contador`.

### Passo a Passo Detalhado

#### Passo 1: Criação da Classe `Contador`

```python
class Contador:
    def __init__(self):
        self.valor_atual = 0
    
    def incrementar(self, passo=1):
        self.valor_atual += passo
    
    def valor(self):
        return self.valor_atual
    
    def zerar(self):
        self.valor_atual = 0
```

#### Passo 2: Atualização das Funções de Módulo

```python
from contador import Contador

# Instanciando a classe Contador para uso nas funções de módulo
contador_padrao = Contador()

def incrementar(passo=1):
    contador_padrao.incrementar(passo)

def valor():
    return contador_padrao.valor()

def zerar():
    contador_padrao.zerar()
```

#### Passo 3: Testes Unitários

```python
import unittest
from contador import Contador, incrementar, valor, zerar

class TestContador(unittest.TestCase):
    
    def test_incrementar(self):
        c = Contador()
        incrementar(2)
        self.assertEqual(valor(), 2)
        
        c.incrementar(3)
        self.assertEqual(c.valor(), 3)
    
    def test_valor(self):
        c = Contador()
        c.incrementar(5)
        self.assertEqual(c.valor(), 5)
    
    def test_zerar(self):
        c = Contador()
        c.incrementar(10)
        c.zerar()
        self.assertEqual(c.valor(), 0)
    
    def test_independencia_instancias(self):
        c1 = Contador()
        c2 = Contador()
        
        c1.incrementar(5)
        c2.incrementar(7)
        
        self.assertEqual(c1.valor(), 5)
        self.assertEqual(c2.valor(), 7)
    
    def test_modulo_functions(self):
        zerar()
        incrementar(3)
        self.assertEqual(valor(), 3)
        zerar()
        self.assertEqual(valor(), 0)

if __name__ == '__main__':
    unittest.main()
```

### Explicação do Plano

- **Passo 1**: Define a classe `Contador` com os métodos necessários.
- **Passo 2**: Atualiza as funções de módulo para usar uma instância padrão da classe `Contador`.
- **Passo 3**: Cria testes unitários para verificar a funcionalidade e a independência entre diferentes instâncias da classe `Contador`.

Este plano garante que a refatoração seja feita de maneira organizada e que todas as funcionalidades existentes sejam mantidas, além de adicionar a capacidade de criar múltiplas instâncias independentes da classe `Contador`.