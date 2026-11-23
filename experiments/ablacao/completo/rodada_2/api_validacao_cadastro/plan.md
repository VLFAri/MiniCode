Baseado na especificação fornecida, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Implementação

1. **Verificar a existência de um dicionário para armazenamento de emails:**
   - Verifique se há um dicionário global chamado `emails_registrados` no arquivo `cadastro.py`. Este dicionário será usado para armazenar os emails registrados.
   - Se o dicionário não existir, crie-o.

2. **Implementar a função `validar_email`:**
   - Crie uma função auxiliar chamada `validar_email(email)` que verifica se o email está no formato correto (`algo@dominio.ext`) e retorna `True` se estiver no formato correto, caso contrário, retorna `False`.

3. **Implementar a função `cadastrar`:**
   - Atualize a função `cadastrar(nome, email)` para incluir as seguintes verificações:
     - Verifique se o nome é uma string não vazia após a remoção de espaços das pontas.
     - Use a função `validar_email` para verificar se o email está no formato correto.
     - Converta o email para minúsculas antes de verificar se ele já existe no dicionário `emails_registrados`.
     - Se o email já existir no dicionário, lance um `ValueError`.
     - Se todas as verificações forem bem-sucedidas, adicione o email ao dicionário `emails_registrados` e retorne o registro criado.

4. **Criar ou atualizar os testes:**
   - Adicione testes unitários para a função `cadastrar` usando uma biblioteca como `unittest` ou `pytest`.
   - Teste casos onde o nome é vazio ou contém apenas espaços.
   - Teste casos onde o email não está no formato correto.
   - Teste casos onde o email já está registrado.
   - Teste casos onde o cadastro é bem-sucedido.

### Exemplo de Código

Aqui está um exemplo de como o código poderia ser implementado:

```python
# cadastro.py

emails_registrados = {}

def validar_email(email):
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def cadastrar(nome, email):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    
    email = email.lower()
    if not validar_email(email):
        raise ValueError("E-mail inválido.")
    
    if email in emails_registrados:
        raise ValueError("E-mail já registrado.")
    
    emails_registrados[email] = {'nome': nome, 'email': email}
    return emails_registrados[email]

# Testes
import unittest

class TestCadastro(unittest.TestCase):
    def test_cadastro_bem_sucedido(self):
        resultado = cadastrar('João', 'joao@example.com')
        self.assertEqual(resultado['nome'], 'João')
        self.assertEqual(resultado['email'], 'joao@example.com')

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            cadastrar('', 'joao@example.com')

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            cadastrar('João', 'invalid-email')

    def test_email_ja_registrado(self):
        cadastrar('João', 'joao@example.com')
        with self.assertRaises(ValueError):
            cadastrar('Maria', 'Joao@example.com')

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem ajudá-lo a implementar a funcionalidade desejada conforme especificado.