Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a paginação na rota GET `/users`:

### Plano de Implementação

1. **Validação dos Parâmetros de Entrada**
   - Adicione validações para os parâmetros `page` e `page_size` no início da função que lida com a rota GET `/users`.
   - Certifique-se de que ambos os parâmetros sejam convertidos para inteiros.
   - Verifique se `page` é maior que zero e se `page_size` está entre 1 e 100.
   - Se qualquer um dos parâmetros não estiver dentro dessas restrições, retorne um status HTTP 400 Bad Request com uma mensagem de erro em formato JSON.

2. **Recuperação da Lista de Usuários**
   - Implemente a lógica para recuperar a lista completa de usuários. Isso pode envolver consultas ao banco de dados ou acesso a uma lista pré-existente de usuários.
   - Certifique-se de que a lista de usuários seja ordenada consistentemente para evitar inconsistências entre as páginas.

3. **Cálculo das Informações de Página**
   - Calcule o índice inicial da lista de usuários com base no valor de `page` e `page_size`.
   - Determine o número total de itens na lista de usuários.
   - Calcule o número total de páginas necessárias para exibir todos os usuários com base no tamanho da página.

4. **Formatação da Resposta**
   - Formate a resposta como um dicionário JSON contendo os campos `page`, `page_size`, `total`, e `items`.
   - O campo `items` deve conter a sublista de usuários correspondente à página solicitada.

5. **Tratamento de Páginas Inválidas**
   - Se a página solicitada for além do número total de páginas, retorne uma lista vazia para `items`.

6. **Testes Unitários**
   - Crie ou atualize os testes unitários para cobrir todas as condições possíveis, incluindo entradas válidas e inválidas.
   - Teste a funcionalidade com diferentes valores de `page` e `page_size`.
   - Certifique-se de que os testes verifiquem corretamente a formatação da resposta JSON e os status HTTP retornados.

### Exemplo de Código

Aqui está um exemplo básico de como a função poderia ser implementada:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de uma lista de usuários
users = ["User1", "User2", "User3", ...]  # Suponha que esta lista seja populada de alguma forma

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    page_size = min(int(request.args.get('page_size', 20)), 100)

    if page < 1 or page_size < 1 or page_size > 100:
        return jsonify({"error": "Invalid page or page_size"}), 400

    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    items = users[start_index:end_index]

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

### Testes Unitários

Certifique-se de criar ou atualizar os testes unitários para verificar a funcionalidade da rota GET `/users`. Aqui está um exemplo de como os testes podem ser estruturados:

```python
import unittest
from app import app, get_users

class TestUsersRoute(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_valid_page_and_pagesize(self):
        response = self.app.get('/users?page=1&page_size=20')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('page', data)
        self.assertIn('page_size', data)
        self.assertIn('total', data)
        self.assertIn('items', data)

    def test_invalid_page(self):
        response = self.app.get('/users?page=0&page_size=20')
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertIn('error', data)

    def test_invalid_pagesize(self):
        response = self.app.get('/users?page=1&page_size=150')
        self.assertEqual(response.status_code, 400)
        data = response.json
        self.assertIn('error', data)

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem fornecer uma boa base para implementar a funcionalidade de paginação desejada na sua aplicação Flask.