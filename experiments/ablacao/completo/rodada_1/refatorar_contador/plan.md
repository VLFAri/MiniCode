### Plano Numerado para Refatoração do Projeto

#### Passo 1: Criar a Classe `Contador`
- Defina a classe `Contador` com os métodos `incrementar`, `valor`, e `zerar`.
- O método `incrementar` deve aceitar um parâmetro opcional `passo` com valor padrão `1`.
- O método `valor` deve retornar o valor atual do contador.
- O método `zerar` deve reiniciar o contador ao seu estado inicial.

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

#### Passo 2: Atualizar as Funções Modulares
- Crie uma instância única da classe `Contador` para uso pelas funções modulares.
- As funções `incrementar`, `valor`, e `zerar` devem delegar suas operações para a instância da classe `Contador`.

```python
_contador_instance = Contador()

def incrementar(passo=1):
    _contador_instance.incrementar(passo)

def valor():
    return _contador_instance.valor()

def zerar():
    _contador_instance.zerar()
```

#### Passo 3: Implementar Testes Automatizados
- Crie ou atualize os testes automatizados para garantir que todas as funcionalidades funcionam corretamente.
- Os testes devem verificar a independência entre diferentes instâncias da classe `Contador`.

```python
import unittest
from contador import Contador, incrementar, valor, zerar

class TestContador(unittest.TestCase):
    def setUp(self):
        self.contador1 = Contador()
        self.contador2 = Contador()
    
    def test_incrementar(self):
        self.contador1.incrementar(5)
        self.assertEqual(self.contador1.valor(), 5)
    
    def test_valor(self):
        self.contador1.incrementar(10)
        self.assertEqual(self.contador1.valor(), 10)
    
    def test_zerar(self):
        self.contador1.incrementar(20)
        self.contador1.zerar()
        self.assertEqual(self.contador1.valor(), 0)
    
    def test_independent_instances(self):
        self.contador1.incrementar(10)
        self.contador2.incrementar(20)
        self.assertNotEqual(self.contador1.valor(), self.contador2.valor())
    
    def test_module_functions(self):
        incrementar(5)
        self.assertEqual(valor(), 5)
        zerar()
        self.assertEqual(valor(), 0)

if __name__ == '__main__':
    unittest.main()
```

### Explicação do Plano

1. **Criar a Classe `Contador`:** A classe `Contador` é definida com três métodos principais: `incrementar`, `valor`, e `zerar`. Essa abordagem encapsula a lógica de gerenciamento do contador em uma única classe.

2. **Atualizar as Funções Modulares:** As funções modulares são atualizadas para usar uma instância única da classe `Contador`. Isso permite que as funções continuem a funcionar como antes, mas agora delegam suas operações para a instância da classe.

3. **Implementar Testes Automatizados:** Testes automatizados são criados ou atualizados para garantir que todas as funcionalidades funcionem corretamente. Especificamente, os testes verificam a independência entre diferentes instâncias da classe `Contador`, além de validar as operações das funções modulares.

Este plano garante que o código seja refatorado de forma eficiente e que todas as funcionalidades sejam testadas adequadamente.