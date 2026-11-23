# Specification

## Objective
Implementar uma função `cadastrar` que valida o nome e o e-mail fornecidos e registra o usuário corretamente.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
- **Restrições**:
  - O nome não pode estar vazio após a remoção de espaços das pontas.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser único, ignorando diferenças entre maiúsculas e minúsculas.
  - O e-mail deve ser armazenado em minúsculas.
- **Saída**: A função retorna o registro do usuário criado, que é um dicionário contendo as chaves `'nome'` e `'email'`.

## Acceptance Criteria
- Se o nome estiver vazio após a remoção de espaços das pontas, a função deve lançar um `ValueError`.
- Se o e-mail não estiver no formato correto ou se já existir um usuário com esse e-mail (ignorando diferenças entre maiúsculas e minúsculas), a função deve lançar um `ValueError`.
- O e-mail deve ser armazenado em minúsculas.
- A função deve retornar um dicionário contendo as chaves `'nome'` e `'email'` para um usuário registrado corretamente.

Para verificar esses critérios, os seguintes testes automatizados podem ser usados:

```python
def test_cadastrar():
    # Testa caso de sucesso
    assert cadastrar('João', 'joao@example.com') == {'nome': 'João', 'email': 'joao@example.com'}
    
    # Testa caso de nome vazio
    try:
        cadastrar('', 'joao@example.com')
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for empty name")
        
    # Testa caso de e-mail inválido
    try:
        cadastrar('Maria', 'invalid_email')
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for invalid email format")
        
    # Testa caso de e-mail duplicado
    cadastrar('João', 'joao@example.com')
    try:
        cadastrar('Maria', 'Joao@example.com')
    except ValueError:
        pass
    else:
        raise AssertionError("Expected ValueError for duplicate email")
```

Esses testes cobrem todos os casos de uso mencionados na especificação acima.