# Specification

## Objective
Implementar uma função `cadastrar` que valida o nome e o e-mail fornecidos e registra o usuário se as validações forem bem-sucedidas.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
- **Saída**: A função retorna um dicionário contendo os dados do usuário registrado.
- **Restrições**:
  - O nome não pode ser vazio após a remoção de espaços nas extremidades.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser único, ignorando diferenças entre maiúsculas e minúsculas.
  - O e-mail deve ser armazenado em minúsculas.
  - Se qualquer uma das condições acima não for satisfeita, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve aceitar entradas válidas e retornar um dicionário com os dados do usuário.
- A função deve lançar `ValueError` se o nome estiver vazio após a remoção de espaços.
- A função deve lançar `ValueError` se o e-mail não estiver no formato correto ou se já existir um usuário com esse e-mail (ignorando diferenças entre maiúsculas e minúsculas).
- A função deve armazenar o e-mail em minúsculas.
- Deve haver testes automatizados para verificar todos os cenários mencionados acima.