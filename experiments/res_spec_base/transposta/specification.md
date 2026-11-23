# Specification

## Objective
O objetivo deste projeto é criar uma função `transposta` no arquivo `matriz.py` que recebe uma matriz como entrada e retorna sua transposta. A transposta de uma matriz é obtida intercambiando suas linhas e colunas.

## Parameters / Requirements
1. **Entrada**:
   - Uma matriz `m` deve ser passada como uma lista de listas.
   - As sublistas podem ter tamanhos diferentes, mas todas devem ter o mesmo número de elementos.

2. **Restrições e Regras de Negócio**:
   - Se a matriz for vazia, a função deve retornar uma lista vazia.
   - Se as linhas da matriz não tiverem o mesmo tamanho, a função deve lançar um `ValueError`.

3. **Critérios Claros e Verificáveis por Testes Automatizados**:
   - O código deve funcionar corretamente para matrizes vazias.
   - O código deve funcionar corretamente para matrizes com linhas de tamanhos diferentes.
   - O código deve retornar a transposta correta para matrizes com linhas de tamanhos iguais.

## Acceptance Criteria
1. **Caso 1**: Matriz vazia
   - Entrada: []
   - Saída: []

2. **Caso 2**: Matriz com linhas de tamanhos diferentes
   - Entrada: [[1, 2], [3, 4]]
   - Saída: [[1, 3], [2, 4]]

3. **Caso 3**: Matriz com linhas de tamanhos iguais
   - Entrada: [[1, 2, 3], [4, 5, 6]]
   - Saída: [[1, 4], [2, 5], [3, 6]]

## Arquivos do projeto:
(vazio)

Pedido do utilizador: Crie matriz.py com a função transposta(m) que receba uma matriz como lista de listas e devolva a transposta (nova matriz). Lista vazia devolve []. Se as linhas tiverem tamanhos diferentes, lance ValueError.