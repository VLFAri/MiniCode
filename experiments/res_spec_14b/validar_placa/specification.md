# Specification

## Objective
Implementar uma função `validar_placa` no arquivo `placas.py` que valide placas brasileiras conforme os padrões antigos e Mercosul.

## Parameters / Requirements
- **Entrada**: Uma string `texto` que representa a placa a ser validada.
- **Saída**: Um valor booleano `True` se a placa for válida conforme os padrões definidos; caso contrário, retorna `False`.
- **Padrões de Placas**:
  - Padrão Antigo: Três letras seguidas de quatro números, podendo conter um hífen opcional entre as letras e os números (ex.: ABC-1234 ou ABC1234).
  - Padrão Mercosul: Três letras seguidas de um número, seguido de mais duas letras e dois números (ex.: ABC1D23).
- **Restrições**:
  - A função deve aceitar tanto letras maiúsculas quanto minúsculas.
  - Qualquer entrada que não seja uma string deve retornar `False`.

## Acceptance Criteria
- A função deve retornar `True` para placas que seguem os padrões antigos e Mercosul.
- A função deve retornar `False` para entradas que não são strings ou que não seguem os padrões de placas definidos.
- Deve ser possível testar a função com casos de teste automatizados para garantir a corretude da implementação.

Arquivos do projeto:
(vazio)