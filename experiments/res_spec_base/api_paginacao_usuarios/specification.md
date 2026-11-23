# Specification

## Objective
Adicionar paginação à rota GET /users no aplicativo Flask.

## Parameters / Requirements
- **query**: Um dicionário contendo as seguintes chaves:
  - `page`: O número da página a ser retornada. Valor padrão é 1.
  - `page_size`: O tamanho da página. Valor padrão é 20, mas não pode ser maior que 100.

- **Resposta**:
  - Status Code: 200
  - Conteúdo JSON:
    ```json
    {
      "page": <número da página>,
      "page_size": <tamanho da página>,
      "total": <total de usuários>,
      "items": [<lista de itens na página>]
    }
    ```
  - Validação de erros:
    - Status Code: 400
    - Conteúdo JSON:
      ```json
      {
        "erro": "<mensagem de erro>"
      }
      ```

## Acceptance Criteria
- A rota GET /users deve retornar uma lista de usuários paginados conforme solicitado.
- Se a página ou o tamanho da página for inválido, a resposta deve ter status code 400 e mensagem de erro adequada.
- A resposta deve conter os campos `page`, `page_size`, `total`, e `items` conforme definido no exemplo.

Arquivos do projeto:
- app.py

Pedido do utilizador: No mini roteador app.py, adicione paginação à rota GET /users: ela deve ler page (padrão 1) e page_size (padrão 20, máximo 100) do dicionário query (os valores podem vir como texto, ex.: "2", ou como int). A resposta deve ser 200 com {"page": ..., "page_size": ..., "total": <total de usuários>, "items": [...]}. Valores inválidos (não inteiros, menores que 1, ou page_size acima de 100) devem devolver 400 com {"erro": "..."}. Páginas além do fim devolvem items vazio.