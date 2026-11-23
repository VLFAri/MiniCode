# Specification

## Objective
Implementar uma função `cadastrar` que valida o nome e o e-mail fornecidos e registra o usuário corretamente.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
  
- **Saída**: A função retorna um dicionário contendo as informações do usuário registrado.
  
- **Restrições**:
  - O nome não pode ser vazio após a remoção de espaços das pontas.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser único (ignorando diferenças entre maiúsculas e minúsculas).
  - O e-mail deve ser armazenado em minúsculas.
  
- **Regras de Negócio**:
  - Se o nome estiver vazio ou o e-mail não estiver no formato correto, a função deve lançar um `ValueError`.
  - Se o e-mail já existir (ignorando diferenças entre maiúsculas e minúsculas), a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função deve validar corretamente o nome e o e-mail.
- A função deve lançar `ValueError` se o nome estiver vazio ou o e-mail não estiver no formato correto.
- A função deve lançar `ValueError` se o e-mail já existir (ignorando diferenças entre maiúsculas e minúsculas).
- A função deve retornar um dicionário com as informações do usuário registrado.
- O e-mail deve ser armazenado em minúsculas.
- Testes automatizados devem verificar todas as condições acima.