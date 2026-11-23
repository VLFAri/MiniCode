# Specification

## Objective
Implementar uma função `cadastrar` que valida o nome e o e-mail fornecidos e registra o usuário se as validações forem bem-sucedidas.

## Parameters / Requirements
- **Entrada:** A função `cadastrar` recebe dois parâmetros:
  - `nome`: uma string representando o nome do usuário.
  - `email`: uma string representando o e-mail do usuário.
  
- **Saída:** A função retorna um dicionário contendo os dados do usuário registrado, caso todas as validações sejam aprovadas.
  
- **Validações:**
  - O nome não pode estar vazio após a remoção de espaços nas extremidades.
  - O e-mail deve estar no formato `algo@dominio.ext`, sem espaços.
  - O e-mail não pode ser duplicado, ignorando diferenças entre maiúsculas e minúsculas.
  - O e-mail deve ser armazenado em minúsculas na variável global `USUARIOS`.
  
- **Exceções:**
  - Se qualquer uma das validações falhar, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- A função `cadastrar` deve aceitar entradas válidas e retornar um dicionário com os dados do usuário.
- A função deve lançar `ValueError` se o nome estiver vazio ou se o e-mail estiver no formato incorreto.
- A função deve lançar `ValueError` se o e-mail já existir em `USUARIOS`, ignorando diferenças entre maiúsculas e minúsculas.
- Os e-mails devem ser armazenados em minúsculas na variável global `USUARIOS`.
- Testes automatizados devem verificar todos os cenários acima para garantir que a função funcione conforme especificado.