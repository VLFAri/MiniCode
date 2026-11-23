Baseado na especificação fornecida e nos requisitos do projeto, aqui está um plano passo a passo para implementar a função `normalizar_telefone` em Python:

### Plano de Implementação

1. **Criar o arquivo principal do projeto:**
   - Crie um novo arquivo Python chamado `phone_normalizer.py`.

2. **Definir a função `normalizar_telefone`:**
   - Na função `normalizar_telefone`, defina os seguintes passos:
     - Remova todos os caracteres não numéricos da entrada.
     - Verifique se a entrada começa com `+55` e remova-o se presente.
     - Normalize a entrada para garantir que ela contenha apenas dígitos.
     - Verifique se a entrada tem exatamente 10 ou 11 dígitos após a normalização.
     - Formate a saída no formato `+55DDDNUMBER`.
     - Se a entrada não estiver no formato correto, lance uma exceção `ValueError`.

3. **Implementar a lógica de validação:**
   - Certifique-se de que a função lance uma `ValueError` se a entrada não tiver exatamente 10 ou 11 dígitos após a remoção de caracteres não numéricos.

4. **Testar a função com casos de teste:**
   - Adicione casos de teste para verificar se a função funciona corretamente com diferentes formatos de entrada.
   - Use a biblioteca `unittest` para criar e executar os testes.

5. **Escrever os testes unitários:**
   - Crie um arquivo separado chamado `test_phone_normalizer.py`.
   - Escreva testes unitários para cada caso de uso mencionado na especificação.
   - Certifique-se de que os testes cobrem todas as possíveis entradas válidas e inválidas.

### Código de Exemplo

#### Arquivo `phone_normalizer.py`

```python
def normalizar_telefone(phone_number):
    # Remove all non-digit characters
    cleaned_number = ''.join(filter(str.isdigit, phone_number))
    
    # Check if the cleaned number starts with +55 and remove it
    if cleaned_number.startswith('+55'):
        cleaned_number = cleaned_number[3:]
    
    # Validate the length of the cleaned number
    if len(cleaned_number) not in [10, 11]:
        raise ValueError("Invalid phone number format")
    
    # Format the phone number in the required format
    formatted_number = f"+55{cleaned_number}"
    
    return formatted_number
```

#### Arquivo `test_phone_normalizer.py`

```python
import unittest
from phone_normalizer import normalizar_telefone

class TestPhoneNormalizer(unittest.TestCase):
    def test_valid_phone_numbers(self):
        self.assertEqual(normalizar_telefone('(67) 99999-1234'), '+5567999991234')
        self.assertEqual(normalizar_telefone('+55 (67) 99999-1234'), '+5567999991234')
        self.assertEqual(normalizar_telefone('67 99999 1234'), '+556799991234')
        self.assertEqual(normalizar_telefone('+5567999991234'), '+5567999991234')
        self.assertEqual(normalizar_telefone('67999991234'), '+5567999991234')

    def test_invalid_phone_numbers(self):
        with self.assertRaises(ValueError):
            normalizar_telefone('+556799999123')
        with self.assertRaises(ValueError):
            normalizar_telefone('6799999123')

if __name__ == '__main__':
    unittest.main()
```

### Execução dos Testes

Para executar os testes, você pode usar o seguinte comando no terminal:

```bash
python -m unittest test_phone_normalizer.py
```

Este comando irá rodar todos os testes definidos no arquivo `test_phone_normalizer.py` e verificar se a função `normalizar_telefone` está funcionando conforme esperado.

Este plano de implementação cobre todos os aspectos necessários para criar a função `normalizar_telefone` e garantir sua funcionalidade através de testes unitários.