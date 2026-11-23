# Specification

## Objective
Implementar uma validação na função `cadastrar(nome, email)` no arquivo `cadastro.py` para garantir que o nome não seja vazio e que o e-mail tenha um formato válido. Além disso, a função deve lançar um `ValueError` se o e-mail já estiver registrado (ignorando diferenças de maiúsculas e minúsculas). O e-mail deve ser armazenado em minúsculas e a função deve retornar o registro criado.

## Parameters / Requirements
- **Entrada:** A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
- **Restrições:**
  - O nome não pode ser vazio após remover espaços das pontas.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail deve ser único (ignorando diferenças entre maiúsculas e minúsculas).
  - O e-mail deve ser armazenado em minúsculas.
- **Saída:** A função retorna o registro do usuário criado ou lança um `ValueError` se as condições acima não forem satisfeitas.

## Acceptance Criteria
1. Se o nome for vazio após remover espaços das pontas, a função deve lançar um `ValueError`.
2. Se o e-mail não estiver no formato `algo@dominio.ext`, a função deve lançar um `ValueError`.
3. Se o e-mail já estiver registrado (ignorando diferenças entre maiúsculas e minúsculas), a função deve lançar um `ValueError`.
4. O e-mail deve ser armazenado em minúsculas.
5. A função deve retornar o registro do usuário criado se todas as condições forem satisfeitas.