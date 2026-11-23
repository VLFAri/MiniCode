# Specification

## Objective
Implementar uma função `cadastrar` que valida o nome e o e-mail fornecidos e registra o usuário corretamente.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
  
- **Saída**: A função retorna um dicionário contendo as informações do usuário registrado, com o e-mail convertido para minúsculas.

- **Restrições**:
  - O nome não pode estar vazio após a remoção de espaços nas extremidades.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail não pode ser duplicado, ignorando diferenças entre maiúsculas e minúsculas.
  - Se qualquer uma dessas condições não for satisfeita, a função deve lançar um `ValueError`.

- **Regras de Negócio**:
  - O e-mail deve ser armazenado em minúsculas.
  - A função deve ser implementada no arquivo `cadastro.py`.
  
## Acceptance Criteria
- A função deve aceitar entradas válidas e retornar um dicionário com as informações do usuário.
- A função deve lançar `ValueError` se:
  - O nome estiver vazio após a remoção de espaços nas extremidades.
  - O e-mail não estiver no formato correto ou tiver espaços.
  - O e-mail já existir no sistema, ignorando diferenças entre maiúsculas e minúsculas.
- Deve haver testes automatizados que verifiquem todos os casos acima.
- O e-mail deve ser armazenado em minúsculas em um dicionário chamado `USUARIOS`.