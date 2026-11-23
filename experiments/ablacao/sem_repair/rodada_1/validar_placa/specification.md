# Specification

## Objective
Implementar uma função `validar_placa` no arquivo `placas.py` que valide placas brasileiras de acordo com dois padrões: o padrão antigo (três letras seguidas de quatro números, podendo ter um hífen opcional entre as letras e os números) e o padrão Mercosul (três letras, um número, mais duas letras e dois números).

## Parameters / Requirements
- **Entrada:** Uma string representando a placa a ser validada.
- **Saída:** Um valor booleano (`True` ou `False`) indicando se a placa é válida conforme os padrões especificados.
- **Restrições:**
  - A função deve aceitar tanto letras maiúsculas quanto minúsculas.
  - Deve retornar `False` para entradas que não são strings ou que não se encaixam nos padrões especificados.

## Acceptance Criteria
- A função deve retornar `True` para placas que seguem o padrão antigo (ABC-1234 ou ABC1234).
- A função deve retornar `True` para placas que seguem o padrão Mercosul (ABC1D23).
- A função deve retornar `False` para qualquer entrada que não seja uma string ou que não se encaixe nos padrões especificados.
- A função deve ser capaz de lidar com entradas vazias ou inválidas retornando `False`.

Arquivos do projeto:
(vazio)