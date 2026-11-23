# Specification

## Objective
O objetivo deste projeto é criar uma função `achatar` no arquivo `achatar.py`, que recebe uma lista ou tupla aninhada em qualquer profundidade e retorna uma nova lista contendo todos os elementos da estrutura original, mantendo a ordem.

## Parameters / Requirements
- **Entradas**: A função `achatar` deve receber como entrada uma variável `itens` que pode ser uma lista ou uma tupla.
- **Tipos**: Os itens podem ser de qualquer tipo, incluindo números, strings, listas, tuplas, dicionários, etc.
- **Restrições**: Não há restrições específicas para os itens.
- **Regras de negócio**: Os itens não devem ser achatados (strings continuam sendo um único elemento).

## Acceptance Criteria
A função `achatar` deve retornar uma lista simples contendo todos os elementos da estrutura original, mantendo a ordem. Strings não devem ser achatadas.

### Test Cases
1. **Lista Aninhada de Inteiros**:
   - Entrada: `[1, [2, 3], 4]`
   - Saída: `[1, 2, 3, 4]`

2. **Lista Aninhada de Strings**:
   - Entrada: `["a", ["b", "c"], "d"]`
   - Saída: `["a", "b", "c", "d"]`

3. **Lista Aninhada de Dicionários**:
   - Entrada: `[{1: 2}, {3: 4}, {5: 6}]`
   - Saída: `[1, 2, 3, 4, 5, 6]`

4. **Lista Aninhada de Listas e Tuplas**:
   - Entrada: `[1, [2, [3, 4]], (5, 6)]`
   - Saída: `[1, 2, 3, 4, 5, 6]`

5. **Lista Aninhada de Múltiplas Níveis**:
   - Entrada: `[1, [2, [3, [4, [5]]]], 6]`
   - Saída: `[1, 2, 3, 4, 5, 6]`

### Arquivos do Projeto
(vazio)

Pedido do Utilizador: Crie achatar.py com a função achatar(itens) que receba listas e tuplas aninhadas em qualquer profundidade e devolva uma lista simples com todos os elementos, na ordem. Strings não devem ser achatadas.