# Specification

## Objective
Implementar uma validação na função `cadastrar(nome, email)` no arquivo `cadastro.py` para garantir que o nome não seja vazio e que o e-mail tenha um formato válido. Além disso, a função deve lançar um `ValueError` se o e-mail já estiver registrado (ignorando diferenças de maiúsculas/minúsculas). O e-mail deve ser armazenado em minúsculas e a função deve retornar o registro criado.

## Parameters / Requirements
- **Entrada**: A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
- **Restrições**:
  - O nome não pode ser vazio após remoção de espaços das pontas.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser armazenado em minúsculas.
  - Não deve haver duplicidade de e-mails (ignorando diferenças de maiúsculas/minúsculas).
- **Regras de Negócio**:
  - Se o nome for vazio ou o e-mail não estiver no formato correto, a função deve lançar um `ValueError`.
  - Se o e-mail já estiver registrado, a função deve lançar um `ValueError`.

## Acceptance Criteria
- A função `cadastrar` deve validar corretamente o nome e o e-mail.
- A função deve lançar `ValueError` se o nome for vazio ou o e-mail não estiver no formato correto.
- A função deve lançar `ValueError` se o e-mail já estiver registrado.
- A função deve retornar o registro criado se todas as validações forem bem-sucedidas.
- O e-mail deve ser armazenado em minúsculas.
- Testes automatizados devem verificar todos os cenários mencionados acima.