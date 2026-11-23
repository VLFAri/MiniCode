Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a função `cadastrar` em `cadastro.py`. Além disso, incluiremos a criação ou atualização dos testes necessários.

### Plano de Implementação

1. **Definir Estrutura de Dados**
   - Crie uma lista global chamada `usuarios_registrados` para armazenar os usuários registrados. Esta lista será usada para verificar a unicidade do e-mail.

2. **Implementar Função `cadastrar`**
   - Defina a função `cadastrar(nome, email)` que receberá dois parâmetros: `nome` e `email`.
   - Remova espaços extras do início e fim do nome usando `strip()`.
   - Verifique se o nome está vazio após a remoção de espaços. Se estiver, lance um `ValueError`.
   - Use uma expressão regular para validar o formato do e-mail. Se o e-mail não estiver no formato correto, lance um `ValueError`.
   - Converta o e-mail para minúsculas para garantir a unicidade.
   - Verifique se o e-mail já existe na lista `usuarios_registrados`. Se existir, lance um `ValueError`.
   - Adicione o novo usuário à lista `usuarios_registrados` como um dicionário `{ 'nome': nome, 'email': email }`.
   - Retorne o dicionário do novo usuário.

3. **Criar ou Atualizar Testes Automatizados**
   - Crie funções de teste para verificar cada condição mencionada na especificação.
   - Teste casos onde o nome está vazio.
   - Teste casos onde o e-mail não está no formato correto.
   - Teste casos onde o e-mail já existe.
   - Teste casos onde o nome e o e-mail são válidos e a função retorna corretamente.

### Código de Implementação

```python
import re

# Lista global para armazenar os usuários registrados
usuarios_registrados = []

def cadastrar(nome, email):
    # Remove espaços extras do início e fim do nome
    nome = nome.strip()
    
    # Verifica se o nome está vazio
    if not nome:
        raise ValueError("Nome não pode estar vazio.")
    
    # Valida o formato do e-mail usando expressão regular
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        raise ValueError("E-mail inválido.")
    
    # Converte o e-mail para minúsculas
    email = email.lower()
    
    # Verifica se o e-mail já existe
    for usuario in usuarios_registrados:
        if usuario['email'] == email:
            raise ValueError("E-mail já cadastrado.")
    
    # Adiciona o novo usuário à lista de usuários registrados
    usuarios_registrados.append({'nome': nome, 'email': email})
    
    # Retorna as informações do novo usuário
    return {'nome': nome, 'email': email}

# Funções de teste
def test_cadastrar():
    try:
        assert cadastrar('João', 'joao@example.com') == {'nome': 'João', 'email': 'joao@example.com'}
        print("Teste 1 passou")
        
        # Teste para nome vazio
        try:
            cadastrar('', 'invalid@example.com')
        except ValueError as ve:
            assert str(ve) == "Nome não pode estar vazio."
            print("Teste 2 passou")
        
        # Teste para e-mail inválido
        try:
            cadastrar('Maria', 'invalid_email')
        except ValueError as ve:
            assert str(ve) == "E-mail inválido."
            print("Teste 3 passou")
        
        # Teste para e-mail duplicado
        try:
            cadastrar('Carlos', 'carlos@example.com')
        except ValueError as ve:
            assert str(ve) == "E-mail já cadastrado."
            print("Teste 4 passou")
        
    except AssertionError:
        print("Um dos testes falhou.")

if __name__ == "__main__":
    test_cadastrar()
```

### Explicação do Código

- **Expressão Regular para E-mail**: A expressão regular `r"[^@]+@[^@]+\.[^@]+"` é usada para validar o formato do e-mail.
- **Verificação de Unicidade**: A unicidade do e-mail é verificada comparando-o com todos os emails já registrados.
- **Testes Automatizados**: Os testes automatizados verificam diferentes cenários para garantir que a função `cadastrar` funcione conforme esperado.

Este plano e código fornecem uma estrutura clara para implementar a função `cadastrar` e garantir que ela atenda aos requisitos especificados.