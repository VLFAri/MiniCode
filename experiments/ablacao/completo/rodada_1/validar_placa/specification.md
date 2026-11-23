# Specification

## Objective
Implementar uma função `validar_placa` no arquivo `placas.py` que valide placas brasileiras de veículos conforme os padrões antigos e Mercosul.

## Parameters / Requirements
- **Entrada:** Uma string `texto` que representa a placa a ser validada.
- **Saída:** Um valor booleano `True` se a placa for válida conforme os padrões definidos; caso contrário, retorna `False`.
- **Padrão Antigo:** Deve seguir o formato de três letras seguidas de quatro números, podendo ou não conter um hífen entre as letras e os números (exemplos válidos: "ABC-1234", "ABC1234").
- **Padrão Mercosul:** Deve seguir o formato de três letras seguidas de um número, uma letra e dois números (exemplo válido: "ABC1D23").
- **Caso Especial:** A função deve aceitar tanto letras maiúsculas quanto minúsculas.
- **Outros Casos:** Qualquer entrada que não seja uma string ou que não siga os formatos acima deve retornar `False`.

## Acceptance Criteria
- A função deve retornar `True` para todas as entradas que correspondem aos padrões antigos e Mercosul de placas brasileiras.
- A função deve retornar `False` para entradas que não são strings ou que não seguem os formatos especificados.
- A função deve ser capaz de lidar com letras maiúsculas e minúsculas corretamente.
- Testes automatizados devem verificar que a função atende a todos os requisitos acima.

Arquivos do projeto:
(vazio)