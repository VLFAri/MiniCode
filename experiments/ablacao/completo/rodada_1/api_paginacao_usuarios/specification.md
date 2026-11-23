# Specification

## Objective
Implementar paginação na rota GET /users do arquivo `app.py`. A implementação deve permitir a leitura dos parâmetros `page` e `page_size` do dicionário `query`, processar os dados de acordo com esses parâmetros e retornar uma resposta formatada.

## Parameters / Requirements
- **Entrada**: Um dicionário `query` contendo os seguintes campos:
  - `page`: O número da página solicitada (padrão 1).
  - `page_size`: O tamanho da página (padrão 20, máximo 100).
  
- **Restrições**:
  - Os valores de `page` e `page_size` podem ser fornecidos como strings ou inteiros.
  - Se `page` não for fornecido, ele deve ter o valor padrão 1.
  - Se `page_size` não for fornecido, ele deve ter o valor padrão 20.
  - `page_size` não pode exceder 100.
  
- **Regras de Negócio**:
  - Se `page` ou `page_size` forem inválidos (não inteiros, menores que 1, ou `page_size` acima de 100), a rota deve retornar um status HTTP 400 e um corpo JSON contendo `"erro": "..."`.
  - Para páginas válidas, a rota deve retornar um status HTTP 200 e um corpo JSON contendo os seguintes campos:
    - `page`: O número da página atual.
    - `page_size`: O tamanho da página.
    - `total`: O total de usuários disponíveis.
    - `items`: Uma lista de usuários na página solicitada.

## Acceptance Criteria
- **Validação de entrada**: Testes que verifiquem se a função retorna HTTP 400 e um erro específico quando `page` ou `page_size` são inválidos.
- **Processamento de dados**: Testes que verifiquem se a função retorna HTTP 200 e um JSON válido com os campos corretos para páginas válidas.
- **Limites de `page_size`**: Testes que verifiquem se a função limita `page_size` a 100.
- **Páginas vazias**: Testes que verifiquem se a função retorna uma lista vazia de itens para páginas além do final do conjunto de dados.
- **Padrões de entrada**: Testes que verifiquem se a função aceita entradas de `page` e `page_size` como strings ou inteiros e processa corretamente ambos os tipos.