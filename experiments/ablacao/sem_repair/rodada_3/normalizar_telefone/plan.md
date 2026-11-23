Baseado na especificação fornecida e considerando que os arquivos do projeto estão vazios, podemos criar um plano passo a passo para implementar a função `normalizar_telefone` em Python. Além disso, incluiremos a criação de testes unitários para garantir a qualidade da implementação.

### Plano de Implementação

1. **Criar o arquivo principal do projeto:**
   - Crie um arquivo Python chamado `normalize_phone.py` onde a função `normalizar_telefone` será definida.

2. **Definir a função `normalizar_telefone`:**
   - Na função `normalizar_telefone`, primeiro remova espaços, parênteses e hífens do número de telefone.
   - Verifique se o número começa com `+55` e remova esse prefixo se presente.
   - Valide se o número de telefone resultante tem exatamente 10 ou 11 dígitos.
   - Se o número tiver 10 dígitos, ele é um número fixo e deve ser formatado como `+55DDDXXXXXX`.
   - Se o número tiver 11 dígitos, ele é um número móvel e deve ser formatado como `+55DDD9XXXXXXXX`.
   - Se o número não atender aos critérios acima, lance uma exceção `ValueError`.

3. **Implementar a função `normalizar_telefone`:**
   - Use expressões regulares para remover caracteres indesejados e validar o formato do número.
   - Utilize condicionais para verificar o comprimento do número e aplicar a formatação correta.

4. **Criar o arquivo de teste:**
   - Crie um arquivo Python chamado `test_normalize_phone.py` para escrever os casos de teste.

5. **Escrever os casos de teste:**
   - Escreva testes para números válidos e inválidos.
   - Certifique-se de incluir testes para números com diferentes formatos de entrada (com espaços, parênteses, etc.).
   - Inclua testes para números que devem gerar uma exceção `ValueError`.

6. **Executar os testes:**
   - Execute os testes para garantir que a função `normalizar_telefone` funcione conforme esperado.
   - Corrija quaisquer problemas encontrados durante a execução dos testes.

### Código Exemplo

#### Arquivo `normalize_phone.py`

```python
import re

def normalizar_telefone(phone_number):
    # Remove spaces, parentheses, and hyphens
    phone_number = re.sub(r'[\s\(\)-]', '', phone_number)
    
    # Remove +55 prefix if present
    if phone_number.startswith('+55'):
        phone_number = phone_number[3:]
    
    # Validate the length and structure of the phone number
    if len(phone_number) == 10:
        # Fixed line number
        return f'+55{phone_number[:2]}{phone_number[2:]}'
    elif len(phone_number) == 11 and phone_number[2] == '9':
        # Mobile number
        return f'+55{phone_number[:2]}{phone_number[2:]}'
    else:
        raise ValueError("Invalid phone number")
```

#### Arquivo `test_normalize_phone.py`

```python
import unittest
from normalize_phone import normalizar_telefone

class TestNormalizePhone(unittest.TestCase):

    def test_valid_fixed_line(self):
        self.assertEqual(normalizar_telefone('1234567890'), '+551234567890')
    
    def test_valid_mobile(self):
        self.assertEqual(normalizar_telefone('12987654321'), '+5512987654321')
    
    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            normalizar_telefone('123456789')
    
    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            normalizar_telefone('1234567890123')

if __name__ == '__main__':
    unittest.main()
```

Este plano e os exemplos de código fornecem uma estrutura clara para implementar a função `normalizar_telefone` e garantir sua correção através de testes unitários.