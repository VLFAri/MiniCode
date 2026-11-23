Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a paginação na rota GET `/users`:

### Plano de Implementação

1. **Validação dos Parâmetros de Entrada**
   - Adicione validações para os parâmetros `page` e `page_size` no início da função que lida com a rota GET `/users`.
   - Certifique-se de que ambos os parâmetros sejam convertidos para inteiros, se forem fornecidos como strings.
   - Verifique se `page` é maior que zero e `page_size` está entre 1 e 100.
   - Se qualquer um dos parâmetros estiver fora dessas condições, retorne um status HTTP 400 Bad Request com uma mensagem de erro em formato JSON.

2. **Recuperação da Lista de Usuários**
   - Implemente a lógica para recuperar a lista completa de usuários. Isso pode envolver consultas ao banco de dados ou acesso a uma lista pré-definida de usuários.
   - Certifique-se de que a lista de usuários seja tratada como uma lista Python.

3. **Paginação da Lista de Usuários**
   - Use os valores de `page` e `page_size` para calcular o índice inicial (`start`) e o tamanho da sublista (`end`) que será retornada.
   - Garanta que a sublista não exceda o tamanho total da lista de usuários.

4. **Montagem da Resposta**
   - Crie um dicionário JSON que inclui os campos `page`, `page_size`, `total` (tamanho da lista de usuários) e `items` (sublista de usuários).
   - Se a página solicitada estiver além do final da lista de usuários, certifique-se de que `items` seja uma lista vazia.

5. **Retorno da Resposta**
   - Retorne a resposta em formato JSON junto com o status HTTP 200 OK.

6. **Testes Automatizados**
   - Crie ou atualize os testes automatizados para cobrir todos os casos mencionados na especificação.
   - Testes devem incluir entradas válidas e inválidas para `page` e `page_size`.
   - Testes devem verificar que a resposta contém os campos corretos e que os status HTTP são corretos.

### Exemplo de Código

Aqui está um exemplo básico de como a função poderia ser implementada:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de uma lista de usuários
users = ["User1", "User2", "User3", "User4", "User5", "User6"]

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    page_size = min(int(request.args.get('page_size', 20)), 100)
    
    if page < 1 or page_size < 1 or page_size > 100:
        return jsonify({"error": "Invalid page or page_size"}), 400
    
    start = (page - 1) * page_size
    end = start + page_size
    items = users[start:end]
    
    response = {
        'page': page,
        'page_size': page_size,
        'total': len(users),
        'items': items
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes Automatizados

Para criar ou atualizar os testes automatizados, você pode usar uma biblioteca como `pytest`. Aqui estão alguns exemplos de testes que você pode adicionar:

```python
import pytest
from app import app, get_users

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users_valid(client):
    response = client.get('/users?page=1&page_size=2')
    assert response.status_code == 200
    data = response.json
    assert data['page'] == 1
    assert data['page_size'] == 2
    assert data['total'] == 6
    assert len(data['items']) == 2

def test_get_users_invalid_page(client):
    response = client.get('/users?page=0&page_size=2')
    assert response.status_code == 400
    data = response.json
    assert 'error' in data

def test_get_users_invalid_page_size(client):
    response = client.get('/users?page=1&page_size=101')
    assert response.status_code == 400
    data = response.json
    assert 'error' in data

def test_get_users_out_of_range(client):
    response = client.get('/users?page=3&page_size=2')
    assert response.status_code == 200
    data = response.json
    assert len(data['items']) == 0
```

Este plano e exemplo de código fornecem uma estrutura sólida para implementar a funcionalidade de paginação desejada, bem como garantir que os testes cobrem adequadamente todas as condições possíveis.