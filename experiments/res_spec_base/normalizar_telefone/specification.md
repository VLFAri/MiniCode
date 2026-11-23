# Specification

## Objective
O objetivo deste projeto é criar uma função `normalizar_telefone` em Python que recebe um telefone brasileiro como entrada e retorna ele no formato internacional.

## Parameters / Requirements
- A função `normalizar_telefone` deve receber um argumento chamado `texto`, que é uma string representando o telefone brasileiro.
- O telefone brasileiro deve ser formatado da seguinte maneira:
  - Remover todos os espaços, parênteses e hífens.
  - Se o telefone começar com +55, remover esse prefixo antes de validar.
  - O restante do telefone deve ter 10 dígitos (DDD + número fixo de 8 dígitos) ou 11 dígitos (DDD + celular de 9 dígitos começando com 9).
  - Caso o telefone não atenda aos requisitos, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- A função `normalizar_telefone` deve retornar o telefone no formato internacional conforme especificado.
- A função deve lidar corretamente com diferentes formatos de telefones brasileiros.
- A função deve lançar uma exceção `ValueError` quando o telefone não atende aos requisitos.

## Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie telefone.py com a função normalizar_telefone(texto) que receba um telefone brasileiro e devolva no formato internacional +55DDDNUMERO. Remova espaços, parênteses e hífens; se começar com +55, remova esse prefixo antes de validar. O restante deve ter 10 dígitos (DDD + número fixo de 8 dígitos) ou 11 dígitos (DDD + celular de 9 dígitos começando com 9); caso contrário lance ValueError. Exemplo: '(67) 99999-1234' vira '+5567999991234'.