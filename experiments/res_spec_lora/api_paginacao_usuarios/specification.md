# Specification

## Objective
Adicionar uma funcionalidade de paginação à rota GET `/users` no aplicativo Flask `app.py`. Esta funcionalidade permitirá listar usuários paginados, onde cada página contém um número limitado de itens.

## Parameters / Requirements
- **Entrada:** Uma requisição HTTP GET para a rota `/users`.
- **Parâmetros da Query String:** 
  - `page`: Um inteiro representando a página atual (padrão é 1).
  - `page_size`: Um inteiro representando o tamanho da página (padrão é 20, máximo é 100).
- **Restrições:**
  - Se `page` não for um inteiro válido, retornar 400 com `"erro": "Page must be an integer greater than or equal to 1"`.
  - Se `page_size` não for um inteiro válido, retornar 400 com `"erro": "Page size must be an integer between 1 and 100"`.
  - Se `page` for menor que 1, retornar 400 com `"erro": "Page must be greater than or equal to 1"`.
  - Se `page_size` estiver fora dos limites definidos (1 a 100), retornar 400 com `"erro": "Page size must be between 1 and 100"`.
  - Se `page` for maior que a última página possível, retornar 200 com `{ "page": <page>, "page_size": <page_size>, "total": <total de usuários>, "items": [] }`.
  - Caso contrário, retornar 200 com os dados da página solicitada.

## Acceptance Criteria
- `GET /users?page=1&page_size=20` retorna `{ "page": 1, "page_size": 20, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=2&page_size=30` retorna `{ "page": 2, "page_size": 30, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=1&page_size=50` retorna `{ "page": 1, "page_size": 50, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=1&page_size=-1` retorna `{ "erro": "Page size must be an integer between 1 and 100" }`
- `GET /users?page=0&page_size=20` retorna `{ "erro": "Page must be greater than or equal to 1" }`
- `GET /users?page=1&pagesize=101` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=0` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=100` retorna `{ "page": 1, "page_size": 100, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=1&pagesize=101` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=99` retorna `{ "page": 1, "page_size": 99, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=1&pagesize=1` retorna `{ "page": 1, "page_size": 1, "total": <total de usuários>, "items": [<lista de usuários>] }`
- `GET /users?page=1&pagesize=21` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1000` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1001` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1002` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1003` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1004` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1005` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1006` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1007` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1008` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1009` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1010` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1011` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1012` retorna `{ "erro": "Page size must be between 1 and 100" }`
- `GET /users?page=1&pagesize=1013` retorna `{ "erro": "Page size must