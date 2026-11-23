# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py`. A implementação deve permitir a leitura dos parâmetros `page` e `page_size` do dicionário `query`, processar os dados de acordo com esses parâmetros e retornar uma resposta formatada.

## Parameters / Requirements
- **Entrada**: Um dicionário `query` contendo os seguintes campos:
  - `page`: O número da página solicitada (padrão 1).
  - `page_size`: O tamanho da página (padrão 20, máximo 100).
  
- **Restrições**:
  - Os valores de `page` e `page_size` podem ser fornecidos como strings ou inteiros.
  - Se `page` não for fornecido, o valor padrão será 1.
  - Se `page_size` não for fornecido, o valor padrão será 20.
  - `page_size` não pode exceder 100.
  
- **Regras de Negócio**:
  - Valores inválidos para `page` ou `page_size` (não inteiros, menores que 1, ou `page_size` acima de 100) devem resultar em um código de status HTTP 400 e uma mensagem de erro no corpo da resposta.

## Acceptance Criteria
- **Teste 1**: Quando a rota GET /users é chamada sem parâmetros, a resposta deve conter `page: 1`, `page_size: 20`, `total` igual ao número total de usuários e `items` com até 20 usuários.
- **Teste 2**: Quando a rota GET /users é chamada com `page: 2` e `page_size: 30`, a resposta deve conter `page: 2`, `page_size: 30`, `total` igual ao número total de usuários e `items` com até 30 usuários.
- **Teste 3**: Quando a rota GET /users é chamada com `page: 1` e `page_size: 50`, a resposta deve conter `page: 1`, `page_size: 50`, `total` igual ao número total de usuários e `items` com até 50 usuários.
- **Teste 4**: Quando a rota GET /users é chamada com `page: 1` e `page_size: 150`, a resposta deve ter status HTTP 400 e uma mensagem de erro indicando que `page_size` é inválido.
- **Teste 5**: Quando a rota GET /users é chamada com `page: 0` e `page_size: 20`, a resposta deve ter status HTTP 400 e uma mensagem de erro indicando que `page` é inválido.
- **Teste 6**: Quando a rota GET /users é chamada com `page: 1` e `page_size: 100`, a resposta deve conter `page: 1`, `page_size: 100`, `total` igual ao número total de usuários e `items` com até 100 usuários.
- **Teste 7**: Quando a rota GET /users é chamada com `page: 2` e `page_size: 20`, mas há menos de 40 usuários, a resposta deve conter `page: 2`, `page_size: 20`, `total` igual ao número total de usuários e `items` com todos os usuários disponíveis.
- **Teste 8**: Quando a rota GET /users é chamada com `page: 3` e `page_size: 20`, mas há apenas duas páginas de usuários, a resposta deve conter `page: 3`, `page_size: 20`, `total` igual ao número total de usuários e `items` vazio.