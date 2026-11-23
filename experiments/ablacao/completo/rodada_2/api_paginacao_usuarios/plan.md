Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a paginação na rota GET `/users` do arquivo `app.py`. Além disso, incluiremos a criação ou atualização dos testes conforme necessário.

### Plano de Implementação

1. **Analisar o Código Atual**
   - Verifique se há uma função existente para lidar com a rota GET `/users`.
   - Identifique onde as informações dos usuários são obtidas e como elas são retornadas.

2. **Adicionar Lógica de Paginação**
   - Adicione lógica para processar os parâmetros `page` e `page_size` do dicionário `query`.
   - Certifique-se de que `page` tenha um valor padrão de 1 e `page_size` tenha um valor padrão de 20.
   - Implemente validações para garantir que `page_size` não exceda 100 e que ambos os parâmetros sejam números inteiros positivos.

3. **Formatar a Resposta**
   - Formate a resposta para incluir `page`, `page_size`, `total` (número total de usuários) e `items` (usuários na página atual).

4. **Tratamento de Erros**
   - Implemente tratamento de erros para casos onde `page` ou `page_size` são inválidos, retornando um código de status HTTP 400 e uma mensagem de erro apropriada.

5. **Testes Unitários**
   - Crie ou atualize os testes unitários para cobrir todos os cenários listados nos critérios de aceitação.

### Passos Detalhados

#### Passo 1: Análise do Código Atual
- Examine a função atual que lida com a rota GET `/users`.
- Identifique onde os dados dos usuários são obtidos e como eles são formatados para retorno.

#### Passo 2: Adicionar Lógica de Paginação
```python
def get_users(query):
    # Definindo valores padrão
    page = query.get('page', 1)
    page_size = query.get('page_size', 20)

    # Validando os parâmetros
    try:
        page = int(page)
        page_size = min(int(page_size), 100)  # Limitando page_size a 100
    except ValueError:
        return {"error": "Invalid page or page_size"}, 400
    
    if page < 1 or page_size < 1:
        return {"error": "Invalid page or page_size"}, 400

    # Simulando obtenção de dados de usuário (substitua isso pelo seu método real)
    users = get_all_users()  # Esta função deve retornar todos os usuários
    total_users = len(users)
    
    # Calculando os índices de início e fim para a página corrente
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    
    # Obtendo os usuários para a página corrente
    items = users[start_index:end_index]
    
    # Formatando a resposta
    response = {
        'page': page,
        'page_size': page_size,
        'total': total_users,
        'items': items
    }
    
    return response
```

#### Passo 3: Testes Unitários
- Crie funções de teste para cada caso de uso descrito nos critérios de aceitação.
- Use bibliotecas como `unittest` ou `pytest` para escrever e executar os testes.

Exemplo de teste usando `unittest`:

```python
import unittest
from app import get_users

class TestGetUsers(unittest.TestCase):
    def test_default_pagination(self):
        query = {}
        response = get_users(query)
        self.assertEqual(response['page'], 1)
        self.assertEqual(response['page_size'], 20)
        # Adicione mais verificações conforme necessário

    def test_custom_pagination(self):
        query = {'page': 2, 'page_size': 30}
        response = get_users(query)
        self.assertEqual(response['page'], 2)
        self.assertEqual(response['page_size'], 30)
        # Adicione mais verificações conforme necessário

    def test_invalid_page_size(self):
        query = {'page': 1, 'page_size': 150}
        response = get_users(query)
        self.assertEqual(response[1], 400)
        self.assertIn("Invalid page or page_size", response[0]['error'])

    # Adicione mais testes conforme necessário

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a funcionalidade de paginação na rota GET `/users` e garantir que ela funcione conforme especificado através de testes adequados.