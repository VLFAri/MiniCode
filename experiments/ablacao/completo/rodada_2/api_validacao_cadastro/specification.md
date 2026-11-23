# Specification

## Objective
Implementar uma validação na função `cadastrar(nome, email)` no arquivo `cadastro.py` para garantir que o nome não seja vazio e que o e-mail tenha um formato válido. Além disso, a função deve lançar um `ValueError` se o e-mail já estiver registrado (ignorando diferenças de maiúsculas e minúsculas). O e-mail deve ser armazenado em minúsculas e a função deve retornar o registro criado.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
- **Restrições**:
  - O nome não pode ser vazio após a remoção de espaços das pontas.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser único (ignorando diferenças entre maiúsculas e minúsculas).
  - O e-mail deve ser armazenado em minúsculas.
- **Regras de Negócio**:
  - Se o nome for vazio ou o e-mail não estiver no formato correto, a função deve lançar um `ValueError`.
  - Se o e-mail já estiver registrado (ignorando diferenças entre maiúsculas e minúsculas), a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função `cadastrar` deve validar corretamente o nome e o e-mail.
- A função deve lançar um `ValueError` se o nome for vazio ou o e-mail não estiver no formato correto.
- A função deve lançar um `ValueError` se o e-mail já estiver registrado (ignorando diferenças entre maiúsculas e minúsculas).
- A função deve armazenar o e-mail em minúsculas.
- A função deve retornar o registro criado com sucesso.