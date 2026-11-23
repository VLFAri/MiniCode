Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a funcionalidade de paginação na rota GET `/users` do aplicativo Flask em `app.py`.

### Plano de Implementação

1. **Verificar a existência da função para listar usuários**: Certifique-se de que existe uma função que lista todos os usuários sem paginação. Se não existir, você precisará criar essa função primeiro.

2. **Adicionar parâmetros de query string**: Modificar a função que lista os usuários para aceitar os parâmetros de query string `page` e `page_size`. Esses parâmetros devem ter valores padrão (`page = 1`, `page_size = 20`).

3. **Validar os parâmetros de entrada**:
   - Verificar se `page` é um inteiro válido e maior ou igual a 1.
   - Verificar se `page_size` é um inteiro válido entre 1 e 100.
   - Retornar os códigos de erro correspondentes se as validações falharem.

4. **Calcular o total de usuários**: Antes de processar a paginação, calcular o total de usuários disponíveis.

5. **Calcular o índice inicial e final**: Com base no valor de `page` e `page_size`, calcular o índice inicial e final dos usuários que serão retornados.

6. **Retornar os dados da página solicitada**: Se a página solicitada estiver dentro do intervalo válido, retornar os dados da página solicitada.

7. **Tratar páginas inválidas**: Se a página solicitada for maior que a última página possível, retornar uma resposta vazia com informações sobre a página solicitada e o total de usuários.

8. **Criar ou atualizar os testes**:
   - Adicionar casos de teste para verificar todas as condições de erro mencionadas na especificação.
   - Adicionar casos de teste para verificar o comportamento normal da função quando os parâmetros estão dentro dos limites válidos.

### Código Exemplo

Aqui está um exemplo básico de como a função poderia ser implementada:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados de usuários
users = ["User {}".format(i) for i in range(1, 101)]

@app.route('/users', methods=['GET'])
def get_users():
    page = int(request.args.get('page', 1))
    page_size = int(request.args.get('page_size', 20))

    # Validações
    if not isinstance(page, int) or page < 1:
        return jsonify({"erro": "Page must be an integer greater than or equal to 1"}), 400
    
    if not isinstance(page_size, int) or page_size < 1 or page_size > 100:
        return jsonify({"erro": "Page size must be an integer between 1 and 100"}), 400
    
    # Calcular total de usuários
    total_users = len(users)
    
    # Calcular índices inicial e final
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    # Verificar se a página solicitada está dentro do intervalo válido
    if end_index > total_users:
        return jsonify({
            "page": page,
            "page_size": page_size,
            "total": total_users,
            "items": []
        })
    
    # Retornar os dados da página solicitada
    items = users[start_index:end_index]
    return jsonify({
        "page": page,
        "page_size": page_size,
        "total": total_users,
        "items": items
    })

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes

Para criar ou atualizar os testes, você pode usar uma biblioteca como `pytest` ou `unittest` do Python. Aqui está um exemplo de como os testes podem ser escritos usando `unittest`:

```python
import unittest
from app import app, get_users

class TestUsers(unittest.TestCase):
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
        self.assertIn("erro", response.json)

    def test_invalid_pagesize(self):
        response = self.client.get('/users?page=1&page_size=101')
        self.assertEqual(response.status_code, 400)
        self.assertIn("erro", response.json)

if __name__ == '__main__':
    unittest.main()
```

Este plano e código de exemplo fornecem uma estrutura básica para implementar a funcionalidade de paginação conforme especificado.