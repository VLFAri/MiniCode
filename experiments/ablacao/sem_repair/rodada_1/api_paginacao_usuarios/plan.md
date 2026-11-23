Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a paginação na rota GET `/users`:

### Plano de Implementação

1. **Analisar o Código Atual**
   - Verifique o código existente em `app.py` para entender a estrutura atual da aplicação e onde a nova funcionalidade será inserida.

2. **Adicionar Lógica de Paginação**
   - No método responsável pela rota GET `/users`, adicione lógica para processar os parâmetros `page` e `page_size`.
     - Converta os parâmetros `page` e `page_size` de string para inteiros, se necessário.
     - Verifique se `page` é um número inteiro positivo ou nulo (padrão).
     - Verifique se `page_size` é um número inteiro positivo entre 1 e 100 (inclusive), ou nulo (padrão).
     - Em caso de valores inválidos, retorne um status HTTP 400 e uma mensagem de erro.

3. **Calcular Dados de Paginação**
   - Calcule o índice inicial da lista de usuários com base no valor de `page` e `page_size`.
   - Calcule o índice final da lista de usuários.
   - Extraia a sublista de usuários correspondente à página solicitada.

4. **Montar Resposta**
   - Crie um dicionário que contenha os campos necessários para a resposta:
     - `"page"`: O número da página solicitado.
     - `"page_size"`: O tamanho da página solicitado.
     - `"total"`: O total de usuários disponíveis.
     - `"items"`: Uma lista de usuários na página solicitada.
   - Se os parâmetros de entrada forem válidos, retorne um status HTTP 200 e o dicionário de resposta.
   - Se os parâmetros de entrada forem inválidos, retorne um status HTTP 400 e um dicionário de resposta contendo uma mensagem de erro.

5. **Testar a Implementação**
   - Crie ou atualize os testes automatizados para verificar a implementação da paginação.
     - Teste diferentes combinações de `page` e `page_size` válidas e inválidas.
     - Verifique se as páginas além do final da lista retornam uma lista vazia de itens (`"items"`).
     - Certifique-se de que a resposta contém os campos corretos e os status HTTP estão conforme esperado.

6. **Documentar a Implementação**
   - Adicione comentários ao código para documentar a implementação da paginação.
   - Atualize a documentação da API para incluir a descrição da nova rota GET `/users` e seus parâmetros.

### Exemplo de Código

Aqui está um exemplo básico de como essa implementação pode ser feita em Python:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de uma lista de usuários
users = ["User 1", "User 2", "User 3", "User 4", "User 5", "User 6"]

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    page_size = min(int(request.args.get('page_size', 20)), 100)
    
    if not isinstance(page, int) or page < 1:
        return jsonify({"error": "Invalid page number"}), 400
    
    if not isinstance(page_size, int) or page_size < 1 or page_size > 100:
        return jsonify({"error": "Invalid page size"}), 400
    
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    items = users[start_index:end_index]
    
    response = {
        "page": page,
        "page_size": page_size,
        "total": len(users),
        "items": items
    }
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes Automatizados

Para criar ou atualizar os testes automatizados, você pode usar uma biblioteca como `pytest`. Aqui está um exemplo de como os testes podem ser escritos:

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
    response = client.get('/users?page=abc')
    assert response.status_code == 400
    assert 'error' in response.json

def test_invalid_page_size(client):
    response = client.get('/users?page_size=-1')
    assert response.status_code == 400
    assert 'error' in response.json

def test_empty_items(client):
    response = client.get('/users?page=100&page_size=1')
    assert response.status_code == 200
    assert response.json['items'] == []
```

Este plano fornece uma estrutura clara para implementar a paginação na rota GET `/users` e garantir que os testes cobrem todas as possíveis entradas e saídas.