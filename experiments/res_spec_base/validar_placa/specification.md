# Specification

## Objective
O objetivo deste projeto é criar uma função `validar_placa` no arquivo `placas.py`, que verifica se um texto fornecido corresponde a uma placa brasileira válida, seguindo os padrões antigos e Mercosul.

## Parameters / Requirements
- O parâmetro `texto` deve ser uma string.
- A função deve retornar `True` se o texto for uma placa válida, conforme os padrões antigos e Mercosul, e `False` caso contrário.

## Acceptance Criteria
- A função deve aceitar apenas strings como entrada.
- Se a entrada não for uma string, a função deve retornar `False`.
- As palavras reservadas (`ABCD`, `1234`, etc.) devem ser consideradas inválidas.
- Os caracteres especiais (`!@#$%^&*()_+-=[]{}|;:,.<>?/`) devem ser ignorados.
- Os espaços entre as letras e números devem ser permitidos.
- Os dígitos podem ser repetidos, mas não podem estar adjacentes.
- Os padrões antigos (ABC-1234 ou ABC1234) devem ser aceitos.
- Os padrões Mercosul (ABC1D23) devem ser aceitos.
- A função deve ser case-insensitive.

## Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie placas.py com a função validar_placa(texto) que devolva True para placas brasileiras válidas: padrão antigo (três letras e quatro dígitos, com hífen opcional: ABC-1234 ou ABC1234) e padrão Mercosul (ABC1D23). Aceite maiúsculas e minúsculas. Qualquer outra coisa, inclusive valores que não sejam texto, devolve False.