# Specification

## Objective
Implementar uma função `validar_placa` no arquivo `placas.py` que valide placas brasileiras conforme os padrões antigos e Mercosul.

## Parameters / Requirements
- **Entrada**: Uma string `texto`.
- **Saída**: Um valor booleano `True` se a placa for válida conforme os padrões definidos; caso contrário, retorna `False`.
- **Padrões de Placas**:
  - Padrão Antigo: Três letras seguidas de quatro números, podendo conter um hífen opcional entre as letras e os números (ex.: ABC-1234 ou ABC1234).
  - Padrão Mercosul: Três letras seguidas de um número, seguido de mais duas letras e dois números (ex.: ABC1D23).
- **Restrições**:
  - A função deve aceitar tanto letras maiúsculas quanto minúsculas.
  - Se a entrada não for uma string, a função deve retornar `False`.

## Acceptance Criteria
- A função deve retornar `True` para placas que seguem os padrões antigos e Mercosul.
- A função deve retornar `False` para entradas que não são strings ou que não seguem os padrões de placas definidos.
- A função deve ser capaz de lidar com entradas em letras maiúsculas e minúsculas.
- Testes automatizados devem verificar corretamente a validade das placas conforme os critérios acima.

Arquivos do projeto:
(vazio)