Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a função `cadastrar` e criar/actualizar os testes necessários:

### Plano de Implementação

1. **Verificar Estrutura do Projeto**
   - Certifique-se de que o arquivo `cadastro.py` existe e está vazio ou contém apenas a estrutura básica da função `cadastrar`.

2. **Definir Estrutura Básica da Função**
   - No arquivo `cadastro.py`, defina a função `cadastrar` com os parâmetros `nome` e `email`.
   - Crie um dicionário global chamado `USUARIOS` para armazenar os emails dos usuários em minúsculas.

3. **Validar Nome**
   - Verifique se o `nome` não é vazio após remover espaços das extremidades.
   - Se o nome estiver vazio, lance um `ValueError` com a mensagem "Nome inválido".

4. **Validar E-mail**
   - Verifique se o `email` está no formato correto (`algo@dominio.ext`) e não contém espaços.
   - Se o email não estiver no formato correto ou tiver espaços, lance um `ValueError` com a mensagem "E-mail inválido".

5. **Verificar Duplicidade do E-mail**
   - Converta o `email` para minúsculas e verifique se ele já existe no dicionário `USUARIOS`.
   - Se o email já existir, lance um `ValueError` com a mensagem "E-mail já cadastrado".

6. **Registrar Usuário**
   - Se todas as validações forem bem-sucedidas, adicione o email (em minúsculas) ao dicionário `USUARIOS`.
   - Retorne um dicionário contendo as informações do usuário, incluindo o email convertido para minúsculas.

7. **Testar a Função**
   - Implemente testes unitários para verificar cada caso de erro e sucesso.
   - Use a biblioteca `unittest` para criar os testes.

### Código Exemplo

Aqui está um exemplo básico de como a função `cadastrar` poderia ser implementada:

```python
def cadastrar(nome, email):
    USUARIOS = {}

    # Validar nome
    if not nome.strip():
        raise ValueError("Nome inválido")

    # Validar e-mail
    if not "@" in email or " " in email:
        raise ValueError("E-mail inválido")

    # Verificar duplicidade do e-mail
    email_lower = email.lower()
    if email_lower in USUARIOS:
        raise ValueError("E-mail já cadastrado")

    # Registrar usuário
    USUARIOS[email_lower] = {"nome": nome, "email": email_lower}
    return USUARIOS[email_lower]
```

### Testes Automatizados

Para garantir que a função `cadastrar` funcione conforme esperado, você deve criar testes automatizados. Aqui está um exemplo de como os testes podem ser implementados usando a biblioteca `unittest`:

```python
import unittest
from cadastro import cadastrar

class TestCadastro(unittest.TestCase):

    def setUp(self):
        self.USUARIOS = {}

    def test_cadastro_valido(self):
        user_info = cadastrar("João Silva", "joao.silva@example.com")
        self.assertEqual(user_info["nome"], "João Silva")
        self.assertEqual(user_info["email"], "joao.silva@example.com")

    def test_nome_invalido(self):
        with self.assertRaises(ValueError):
            cadastrar("", "valid.email@example.com")

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            cadastrar("Maria Silva", "invalid email@example.com")

    def test_email_ja_cadastrado(self):
        cadastrar("Carlos Silva", "carlos.silva@example.com")
        with self.assertRaises(ValueError):
            cadastrar("Carlos Silva", "CARLOS.SILVA@example.com")

if __name__ == '__main__':
    unittest.main()
```

Este plano e código de exemplo fornecem uma estrutura sólida para implementar a função `cadastrar` e garantir sua integridade através de testes automatizados.