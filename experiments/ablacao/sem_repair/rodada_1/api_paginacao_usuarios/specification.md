# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py` para retornar uma lista paginada de usuários.

## Parameters / Requirements
- **Entrada**: Os parâmetros de entrada são passados via dicionário `query`, contendo os seguintes campos:
  - `page`: Número da página solicitada (padrão: 1).
  - `page_size`: Tamanho da página (padrão: 20, máximo: 100).

- **Restrições**:
  - `page` deve ser um número inteiro positivo ou nulo (padrão).
  - `page_size` deve ser um número inteiro positivo entre 1 e 100 (inclusive), ou nulo (padrão).

- **Regras de Negócio**:
  - Se `page` ou `page_size` forem fornecidos como texto, eles devem ser convertidos para números inteiros.
  - Valores inválidos para `page` ou `page_size` (não inteiros, menores que 1, ou `page_size` acima de 100) devem resultar em um status HTTP 400 e uma mensagem de erro no corpo da resposta.

## Acceptance Criteria
- A resposta deve conter os seguintes campos:
  - `"page"`: O número da página solicitado.
  - `"page_size"`: O tamanho da página solicitado.
  - `"total"`: O total de usuários disponíveis.
  - `"items"`: Uma lista de usuários na página solicitada.

- Caso os parâmetros de entrada sejam válidos, a resposta deve ter o status HTTP 200 e conter os campos mencionados acima.

- Caso os parâmetros de entrada sejam inválidos, a resposta deve ter o status HTTP 400 e conter um campo `"erro"` com uma mensagem de erro específica.

- Testes automatizados devem verificar que as páginas além do final da lista retornam uma lista vazia de itens (`"items"`).