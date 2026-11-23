Baseado na especificação fornecida e nos arquivos do projeto, segue um plano numerado, passo a passo, do que deve ser programado em `app.py`. Além disso, incluiremos a criação ou atualização dos testes necessários.

### Plano de Implementação

1. **Validação dos Parâmetros de Entrada**
   - Implemente a validação dos parâmetros `page` e `page_size` recebidos na rota GET `/users`.
   - Certifique-se de que `page` seja convertido para um número inteiro maior ou igual a 1.
   - Verifique se `page_size` é convertido para um número inteiro entre 20 e 100 (inclusive).
   - Em caso de falha na validação, retorne um status HTTP 400 Bad Request com uma mensagem de erro.

2. **Recuperação da Lista de Usuários**
   - Implemente a lógica para recuperar a lista completa de usuários.
   - Esta lista pode ser simulada ou recuperada de um banco de dados, dependendo da implementação atual.

3. **Paginação**
   - Implemente a lógica para dividir a lista de usuários em páginas com base no valor de `page_size`.
   - Certifique-se de que a página solicitada (`page`) esteja dentro dos limites da lista de usuários.

4. **Montagem da Resposta**
   - Montar a resposta JSON contendo as informações da página atual: `page`, `page_size`, `total` (total de usuários) e `items` (itens da página atual).
   - Se a página solicitada estiver além do final da lista de usuários, a resposta deve conter `items` como uma lista vazia.

5. **Testes Unitários**
   - Crie ou atualize os testes unitários para garantir que a rota GET `/users` funcione conforme especificado.
   - Teste diferentes cenários, incluindo entradas válidas e inválidas para `page` e `page_size`.

### Código Exemplo

Aqui está um exemplo básico de como o código poderia ser estruturado:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação da lista de usuários
users = ["User1", "User2", "User3", "User4", "User5", "User6"]

@app.route('/users', methods=['GET'])
def get_users():
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', default=20, type=int)

    if page < 1 or page_size < 20 or page_size > 100:
        return jsonify({"error": "Invalid page or page_size"}), 400

    total_users = len(users)
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    items = users[start_index:end_index]

    response = {
        "page": page,
        "page_size": page_size,
        "total": total_users,
        "items": items
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes Unitários

Para criar ou atualizar os testes unitários, você pode usar a biblioteca `pytest` junto com `flask-testing`. Aqui está um exemplo de como os testes podem ser estruturados:

```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users_invalid_page(client):
    response = client.get('/users?page=-1')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid page or page_size'

def test_get_users_invalid_page_size(client):
    response = client.get('/users?page_size=150')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid page or page_size'

def test_get_users_valid(client):
    response = client.get('/users?page=1&page_size=20')
    assert response.status_code == 200
    assert response.json['page'] == 1
    assert response.json['page_size'] == 20
    assert response.json['total'] == 6
    assert len(response.json['items']) == 20
```

Este plano e o exemplo de código fornecem uma estrutura sólida para implementar a paginação na rota GET `/users` conforme especificado.