# Specification

## Objective
O objetivo deste projeto é implementar uma funcionalidade para adicionar usuários ao sistema, com validações específicas para os campos nome e e-mail.

## Parameters / Requirements
- **nome**: String que representa o nome do usuário. Não pode ser vazio após remoção de espaços nas extremidades.
- **email**: String que representa o e-mail do usuário. Deve seguir o formato `algo@dominio.ext` e não conter espaços. O e-mail deve ser convertido para minúsculas antes de ser armazenado no sistema.

## Acceptance Criteria
1. A função `cadastrar(nome, email)` deve validar se o nome é vazio após remoção de espaços nas extremidades.
2. A função `cadastrar(nome, email)` deve validar se o e-mail está no formato correto (`algo@dominio.ext`).
3. A função `cadastrar(nome, email)` deve verificar se o e-mail já existe na base de dados (ignorando maiúsculas).
4. A função `cadastrar(nome, email)` deve retornar o registro criado quando o e-mail for válido e não existente.

## Arquivos do projeto
- **cadastro.py**

### Pedido do utilizador
Adicione validação à função cadastrar(nome, email) de cadastro.py: o nome não pode ser vazio (após remover espaços das pontas) e o e-mail deve ter formato válido (algo@dominio.ext, sem espaços), senão lance ValueError. E-mail repetido (ignorando maiúsculas) também lança ValueError. O e-mail deve ser guardado em minúsculas em USUARIOS e a função devolve o registro criado.