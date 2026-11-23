Baseado na especificação fornecida e nos arquivos do projeto, aqui está um plano passo a passo para implementar a paginação na rota GET `/users` do aplicativo Flask:

### Plano de Implementação

1. **Atualizar `app.py` para incluir paginação:**
   - Adicione lógica para processar os parâmetros `page` e `page_size` na rota GET `/users`.
   - Certifique-se de que os valores padrão sejam aplicados corretamente (`page`=1 e `page_size`=20).
   - Verifique se `page_size` não ultrapassa 100.
   - Implemente a lógica para validar os valores de entrada (`page` e `page_size`) e garantir que eles sejam números inteiros válidos.
   - Crie uma função para calcular o total de usuários e extrair os itens correspondentes à página solicitada.
   - Formate a resposta JSON conforme especificado.

2. **Implementar validações de entrada:**
   - Verifique se `page` é um número inteiro positivo.
   - Verifique se `page_size` é um número inteiro entre 1 e 100.
   - Em caso de falha em qualquer uma das validações, retorne um status HTTP 400 com uma mensagem de erro apropriada.

3. **Retornar dados formatados:**
   - Construa a resposta JSON com os campos `page`, `page_size`, `total`, e `items`.
   - Certifique-se de que a resposta seja retornada com status HTTP 200.

4. **Testes:**
   - Crie ou atualize os testes unitários para verificar a funcionalidade da paginação.
   - Teste diferentes cenários, incluindo entradas válidas e inválidas.
   - Verifique se a resposta JSON é formatada corretamente em todos os casos.

### Código Exemplo

Aqui está um exemplo básico de como você poderia implementar essa funcionalidade em `app.py`:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados
users = ["User {}".format(i) for i in range(1, 101)]

@app.route('/users', methods=['GET'])
def get_users():
    # Parâmetros padrão
    page = request.args.get('page', default=1, type=int)
    page_size = request.args.get('page_size', default=20, type=int)

    # Validações
    if page < 1 or page_size < 1 or page_size > 100:
        return jsonify({"error": "Invalid page or page_size"}), 400

    # Calcular total de usuários
    total_users = len(users)

    # Calcular início e fim da página
    start = (page - 1) * page_size
    end = start + page_size

    # Extrair itens da página
    items = users[start:end]

    # Resposta formatada
    response = {
        "page": page,
        "page_size": page_size,
        "total": total_users,
        "items": items
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes

Para criar ou atualizar os testes, você pode usar a biblioteca `pytest`. Aqui está um exemplo de como você poderia escrever alguns testes:

```python
import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    data = response.json
    assert 'page' in data
    assert 'page_size' in data
    assert 'total' in data
    assert 'items' in data

def test_invalid_page(client):
    response = client.get('/users?page=-1')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid page or page_size'

def test_invalid_page_size(client):
    response = client.get('/users?page_size=150')
    assert response.status_code == 400
    assert response.json['error'] == 'Invalid page or page_size'
```

Este plano e código de exemplo fornecem uma estrutura sólida para implementar a paginação na sua aplicação Flask, além de sugerir como você pode testar adequadamente essa funcionalidade.