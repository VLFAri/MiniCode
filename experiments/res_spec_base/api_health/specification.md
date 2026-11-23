# Specification

## Objective
Adicionar uma nova rota GET /health no aplicativo Python `app.py` para retornar um status 200 com um corpo JSON contendo `"status": "ok"`.

## Parameters / Requirements
- A rota `/health` deve ser adicionada ao aplicativo Python `app.py`.
- O corpo da resposta deve ser um objeto JSON com a chave `"status"` e valor `"ok"`.
- A rota `/health` deve retornar o código HTTP 200.
- As rotas existentes devem continuar funcionando corretamente.
- Caminhos desconhecidos devem retornar o código HTTP 404.

## Acceptance Criteria
- Teste automático para verificar se a rota `/health` retorna o status 200 e o corpo correto.
- Teste automático para verificar se as rotas existentes funcionam corretamente.
- Teste automático para verificar se os caminhos desconhecidos retornam o código HTTP 404.

Arquivos do projeto:
- app.py

### app.py
```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

@app.route('/', defaults={'path': ''})
def index(path):
    return f'Hello, World! {path}'

if __name__ == '__main__':
    app.run(debug=True)
```

### Testes Automatizados
1. **Teste 1**: Verificar se a rota `/health` retorna o status 200 e o corpo `{ "status": "ok" }`.
   - Criação de uma nova instância do Flask.
   - Adição da rota `/health` à aplicação.
   - Execução de uma requisição GET a `/health` e verificação dos resultados.

2. **Teste 2**: Verificar se as rotas existentes funcionam corretamente.
   - Criação de uma nova instância do Flask.
   - Adição das rotas existentes à aplicação.
   - Execução de várias requisições para diferentes rotas e verificação dos resultados.

3. **Teste 3**: Verificar se os caminhos desconhecidos retornam o código HTTP 404.
   - Criação de uma nova instância do Flask.
   - Adição das rotas existentes à aplicação.
   - Execução de uma requisição a um caminho desconhecido e verificação do código HTTP retornado.