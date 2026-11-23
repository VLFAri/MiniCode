Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a paginação na rota GET `/users` do arquivo `app.py`. O plano inclui a criação ou atualização dos testes necessários.

### Plano de Implementação

1. **Validação dos Parâmetros de Entrada**
   - Adicione validações para os parâmetros `page` e `page_size` no início da função que lida com a rota GET `/users`.
   - Certifique-se de que ambos os parâmetros sejam convertidos para inteiros.
   - Verifique se `page` é maior que zero e se `page_size` está entre 1 e 100.

2. **Cálculo do Índice de Início e Fim**
   - Calcule o índice inicial (`start_index`) usando `(page - 1) * page_size`.
   - Calcule o índice final (`end_index`) usando `start_index + page_size`.

3. **Obtenção da Lista de Usuários**
   - Obtenha a lista completa de usuários.
   - Use os índices calculados para obter a sublista de usuários correspondente à página solicitada.

4. **Verificação da Página Solicitada**
   - Verifique se a página solicitada está dentro dos limites da lista de usuários.
   - Se a página solicitada estiver além do número total de páginas, retorne uma lista vazia para `items`.

5. **Montagem da Resposta**
   - Montar a resposta em formato JSON contendo os campos `page`, `page_size`, `total`, e `items`.
   - Se houver erros de validação, monte a resposta com o campo `erro` contendo a mensagem de erro e retorne um status HTTP 400 Bad Request.

6. **Testes Unitários**
   - Crie ou atualize os testes unitários para cobrir todas as condições possíveis, incluindo entradas inválidas, páginas fora dos limites, etc.
   - Teste a função com diferentes valores de `page` e `page_size` para garantir que ela funcione corretamente em todos os casos.

### Exemplo de Código

Aqui está um exemplo básico de como a função poderia ser implementada:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados
users = ["User1", "User2", "User3", "User4", "User5", "User6"]

@app.route('/users', methods=['GET'])
def get_users():
    try:
        page = int(request.args.get('page', 1))
        page_size = min(int(request.args.get('page_size', 20)), 100)
        
        if page < 1 or page_size < 1 or page_size > 100:
            return jsonify({"erro": "Valores inválidos para 'page' ou 'page_size'"}), 400
        
        start_index = (page - 1) * page_size
        end_index = start_index + page_size
        total_users = len(users)
        
        items = users[start_index:end_index] if start_index < total_users else []
        
        return jsonify({
            "page": page,
            "page_size": page_size,
            "total": total_users,
            "items": items
        })
    
    except ValueError:
        return jsonify({"erro": "Valores inválidos para 'page' ou 'page_size'"}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes

Para criar ou atualizar os testes, você pode usar uma biblioteca como `pytest` ou `unittest` do Python. Aqui estão alguns exemplos de testes que você pode adicionar:

```python
import unittest
from app import app, get_users

class TestUsersAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_valid_page_and_pagesize(self):
        response = self.client.get('/users?page=1&page_size=20')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn("page", data)
        self.assertIn("page_size", data)
        self.assertIn("total", data)
        self.assertIn("items", data)

    def test_invalid_page(self):
        response = self.client.get('/users?page=0&page_size=20')
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertIn("erro", data)

    def test_invalid_pagesize(self):
        response = self.client.get('/users?page=1&page_size=101')
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertIn("erro", data)

    def test_out_of_bounds_page(self):
        response = self.client.get('/users?page=100&page_size=20')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertEqual(data["items"], [])

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem fornecer uma boa base para implementar a paginação na sua aplicação Flask.