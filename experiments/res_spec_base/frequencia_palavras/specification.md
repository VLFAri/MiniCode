# Specification

## Objective
O objetivo deste módulo é criar uma função `frequencia_palavras` que recebe um texto como entrada e retorna um dicionário contendo a contagem de cada palavra no texto, convertida para minúsculas e ignorando a pontuação.

## Parameters / Requirements
- O parâmetro `texto` deve ser uma string.
- A função deve retornar um dicionário onde as chaves são as palavras (em minúsculas) e os valores são as contagens de cada palavra no texto.
- Se o texto for vazio, a função deve retornar um dicionário vazio.

## Acceptance Criteria
1. A função deve funcionar corretamente para textos vazios.
2. A função deve contar todas as palavras presentes no texto, independentemente de sua posição.
3. A função deve ignorar a pontuação e considerar apenas letras e números.
4. A função deve retornar um dicionário com palavras em minúsculas.
5. A função deve retornar um dicionário vazio se o texto for vazio.

Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie o módulo palavras.py com a função frequencia_palavras(texto) que devolva um dicionário com a contagem de cada palavra do texto, em minúsculas e ignorando a pontuação. Texto vazio devolve um dicionário vazio.