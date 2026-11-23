Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `normalizar_telefone` em Python:

### Plano de Implementação

1. **Criar o arquivo `telefone.py`:**
   - Crie um novo arquivo Python chamado `telefone.py` onde a função `normalizar_telefone` será definida.

2. **Definir a função `normalizar_telefone`:**
   - Na função `normalizar_telefone`, defina o parâmetro `texto` que representa o telefone brasileiro.
   - Remova todos os caracteres não numéricos (espaços, parênteses, hífens) do texto de entrada usando expressões regulares ou métodos de string.
   - Verifique se o texto começa com "+55" e remova este prefixo se presente.
   - Valide se o texto resultante tem exatamente 10 ou 11 dígitos após a remoção de caracteres não numéricos.
     - Se o texto tiver 10 dígitos, adicione "+55" no início e retorne o resultado.
     - Se o texto tiver 11 dígitos, adicione "+55" no início e retorne o resultado.
     - Se o texto não tiver 10 ou 11 dígitos, lance uma exceção `ValueError`.
   
3. **Implementar testes unitários:**
   - No mesmo arquivo `telefone.py`, ou em um arquivo separado `test_telefone.py`, implemente testes unitários para a função `normalizar_telefone`.
   - Use a biblioteca `unittest` para criar casos de teste que cobrem diferentes formatos de entrada e as condições de erro.
   - Teste entradas válidas e inválidas para garantir que a função funcione corretamente e lance exceções `ValueError` quando necessário.

### Código de Exemplo

Aqui está um exemplo básico de como a função `normalizar_telefone` poderia ser implementada:

```python
import re

def normalizar_telefone(texto):
    # Remove espaços, parênteses e hífens
    texto = re.sub(r'[ -()]+', '', texto)
    
    # Remove prefixo +55 se presente
    if texto.startswith('+55'):
        texto = texto[3:]
    
    # Validação do tamanho do texto
    if len(texto) not in [10, 11]:
        raise ValueError("Telefone inválido")
    
    # Adiciona o prefixo +55
    return f"+55{texto}"
```

E aqui estão alguns exemplos de testes unitários que você pode usar:

```python
import unittest
from telefone import normalizar_telefone

class TestTelefone(unittest.TestCase):
    def test_valid_phone(self):
        self.assertEqual(normalizar_telefone('(67) 99999-1234'), '+5567999991234')
        self.assertEqual(normalizar_telefone('67999991234'), '+5567999991234')
    
    def test_invalid_phone(self):
        with self.assertRaises(ValueError):
            normalizar_telefone('679999912')
        with self.assertRaises(ValueError):
            normalizar_telefone('679999912345')

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `normalizar_telefone` e garantir sua correta validação e formatação.