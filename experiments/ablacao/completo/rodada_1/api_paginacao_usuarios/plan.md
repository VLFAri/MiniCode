Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Implementação

1. **Analisar o Código Atual**
   - Verifique o arquivo `app.py` para entender a estrutura atual da aplicação e onde a nova funcionalidade de paginação deve ser inserida.

2. **Adicionar Função de Paginação**
   - Crie uma função dentro de `app.py` que será responsável por processar os parâmetros `page` e `page_size` e retornar os dados paginados.
   - Certifique-se de que a função lida corretamente com diferentes tipos de entrada (strings e inteiros) para `page` e `page_size`.

3. **Validar Parâmetros de Entrada**
   - Dentro da função de paginação, adicione lógica para validar os parâmetros `page` e `page_size`.
   - Implemente verificações para garantir que `page` seja maior que zero e `page_size` esteja entre 1 e 100.
   - Retorne um status HTTP 400 e um JSON de erro específico se qualquer um desses parâmetros for inválido.

4. **Processar Dados de Usuários**
   - Implemente a lógica para calcular o início e o fim dos dados de usuário com base em `page` e `page_size`.
   - Certifique-se de que a função retorne uma lista vazia de itens para páginas além do final do conjunto de dados.

5. **Montar Resposta JSON**
   - Formate a resposta JSON para incluir os campos necessários (`page`, `page_size`, `total`, `items`).

6. **Integrar Função à Rota GET /users**
   - Modifique a rota GET `/users` no arquivo `app.py` para chamar a função de paginação criada anteriormente.

7. **Testar a Implementação**
   - Crie testes unitários para validar a entrada, processamento de dados e montagem da resposta JSON.
   - Teste diferentes cenários, incluindo entradas inválidas, entradas válidas, e limites de `page_size`.

### Exemplo de Estrutura de Código

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    query = request.args.to_dict()
    return paginate(query)

def paginate(query):
    try:
        page = int(query.get('page', 1))
        page_size = min(int(query.get('page_size', 20)), 100)
        
        if page < 1 or page_size < 1:
            raise ValueError
        
        # Simulação de banco de dados
        users = [f"User {i}" for i in range(1, 101)]
        
        start = (page - 1) * page_size
        end = start + page_size
        items = users[start:end]
        
        response = {
            'page': page,
            'page_size': page_size,
            'total': len(users),
            'items': items
        }
        return jsonify(response), 200
    
    except ValueError:
        return jsonify({'error': 'Invalid page or page_size'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

### Exemplo de Testes Unitários

```python
import unittest
from app import app, paginate

class TestPagination(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_invalid_page(self):
        response = self.app.get('/users?page=0&page_size=20')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid page or page_size', str(response.data))

    def test_invalid_page_size(self):
        response = self.app.get('/users?page=1&page_size=150')
        self.assertEqual(response.status_code, 400)
        self.assertIn('Invalid page or page_size', str(response.data))

    def test_valid_pagination(self):
        response = self.app.get('/users?page=1&page_size=10')
        self.assertEqual(response.status_code, 200)
        data = response.json
        self.assertIn('page', data)
        self.assertIn('page_size', data)
        self.assertIn('total', data)
        self.assertIn('items', data)

if __name__ == '__main__':
    unittest.main()
```

Este plano e exemplo de código devem fornecer uma boa base para implementar a funcionalidade de paginação conforme especificado.