Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `cadastrar` conforme solicitado:

### Plano de Implementação

1. **Verificar a existência de um dicionário para armazenamento de registros**:
   - Verifique se há um dicionário global chamado `registros` no arquivo `cadastro.py`. Este dicionário será usado para armazenar os e-mails registrados.
   - Se o dicionário não existir, crie-o.

2. **Implementar a função `cadastrar`**:
   - Defina a função `def cadastrar(nome: str, email: str) -> dict:`.
   - Dentro da função, remova espaços extras do início e fim do nome usando `nome.strip()`.
   - Verifique se o nome é vazio após a remoção de espaços. Se for, lance um `ValueError` com a mensagem "Nome não pode ser vazio".
   - Use uma expressão regular para verificar se o e-mail está no formato correto (`algo@dominio.ext`). Se não estiver, lance um `ValueError` com a mensagem "E-mail inválido".
   - Converta o e-mail para minúsculas usando `email.lower()`.
   - Verifique se o e-mail já existe no dicionário `registros`. Se existir, lance um `ValueError` com a mensagem "E-mail já registrado".
   - Adicione o e-mail ao dicionário `registros` como chave e o nome como valor.
   - Retorne o dicionário `registros` atualizado.

3. **Criar ou atualizar os testes**:
   - Crie um novo arquivo chamado `test_cadastro.py` para os testes unitários.
   - Importe a função `cadastrar` do módulo `cadastro`.
   - Escreva casos de teste para cobrir todos os cenários possíveis, incluindo:
     - Nome vazio.
     - E-mail inválido.
     - E-mail já registrado.
     - Registro bem-sucedido.
   - Use a biblioteca `unittest` para escrever os testes.

4. **Executar os testes**:
   - Execute os testes criados em `test_cadastro.py` para garantir que a função `cadastrar` funcione conforme esperado.

### Exemplo de Código

Aqui está um exemplo de como o código poderia ser implementado:

```python
import re

# Supondo que esteja no topo do arquivo cadastro.py
registros = {}

def cadastrar(nome: str, email: str) -> dict:
    nome = nome.strip()
    
    if not nome:
        raise ValueError("Nome não pode ser vazio")
    
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("E-mail inválido")
    
    email = email.lower()
    
    if email in registros:
        raise ValueError("E-mail já registrado")
    
    registros[email] = nome
    return registros
```

### Exemplo de Testes

Aqui está um exemplo de como os testes podem ser escritos:

```python
import unittest
from cadastro import cadastrar

class TestCadastro(unittest.TestCase):
    def setUp(self):
        global registros
        registros = {}

    def test_nome_vazio(self):
        with self.assertRaises(ValueError):
            cadastrar("", "teste@test.com")

    def test_email_invalido(self):
        with self.assertRaises(ValueError):
            cadastrar("João", "invalid-email")

    def test_email_ja_registrado(self):
        cadastrar("Maria", "maria@example.com")
        with self.assertRaises(ValueError):
            cadastrar("Carlos", "Maria@example.com")

    def test_registro_bem_sucedido(self):
        resultado = cadastrar("Ana", "ana@example.com")
        self.assertIn("ana@example.com", resultado)
        self.assertEqual(resultado["ana@example.com"], "Ana")

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem ajudá-lo a implementar a função `cadastrar` conforme especificado e a criar testes adequados para garantir a qualidade do código.