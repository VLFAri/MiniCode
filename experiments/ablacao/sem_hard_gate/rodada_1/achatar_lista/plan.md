Baseado na especificação fornecida, aqui está um plano passo a passo para criar o script `achatar.py` conforme solicitado:

### Plano de Desenvolvimento

1. **Criação do Arquivo `achatar.py`**
   - Crie um novo arquivo chamado `achatar.py`.

2. **Importação de Módulos Necessários**
   - Como não são necessários módulos externos para este script, esta etapa pode ser omitida.

3. **Definição da Função `achatar(items)`**
   - Defina a função `achatar(items)` no arquivo `achatar.py`.
   - A função deve aceitar uma única entrada `items` que pode ser uma estrutura de dados aninhada contendo listas, tuplas e strings.
   - A função deve retornar uma lista de nível único contendo todos os elementos da estrutura de entrada, preservando a ordem dos elementos.
   - Implemente a lógica para evitar a quebra de strings dentro da estrutura de entrada.

4. **Implementação da Lógica de Flattening**
   - Utilize recursão para percorrer a estrutura de dados aninhada.
   - Para cada elemento da estrutura, verifique se é uma lista ou tupla e, em caso afirmativo, chame recursivamente a função `achatar()` sobre esse elemento.
   - Se o elemento for uma string, adicione-o diretamente à lista resultante sem modificação.

5. **Testes Unitários**
   - Adicione testes unitários ao final do arquivo `achatar.py` para garantir que a função `achatar()` funcione corretamente.
   - Os testes devem cobrir diferentes cenários, incluindo estruturas vazias, estruturas com múltiplos níveis de aninhamento, e estruturas que contêm strings.

6. **Execução dos Testes**
   - Execute os testes unitários para verificar se a função `achatar()` atende aos critérios de aceitação.

### Código Exemplo

Aqui está um exemplo básico de como o código poderia ser implementado:

```python
def achatar(items):
    resultado = []
    for item in items:
        if isinstance(item, (list, tuple)):
            resultado.extend(achatar(item))
        else:
            resultado.append(item)
    return resultado

# Testes unitários
assert achatar([1, [2, 3], 4]) == [1, 2, 3, 4]
assert achatar((1, (2,), [3, [4]])) == [1, 2, 3, 4]
assert achatar(['a', ['b', 'c'], ('d', 'e')]) == ['a', 'b', 'c', 'd', 'e']
assert achatar([]) == []
assert achatar(('a',)) == ['a']
```

### Passos Finais

7. **Revisão e Refatoração**
   - Revisar o código para garantir que ele seja eficiente e fácil de entender.
   - Refatorar o código se necessário para melhorar a legibilidade e a performance.

8. **Documentação**
   - Adicionar documentação ao código para explicar a função `achatar()` e seus usos.

9. **Commit e Push**
   - Comitar as mudanças no controle de versão (como Git).
   - Empurrar as alterações para o repositório remoto.

Este plano deve guiar você através do processo de desenvolvimento do script `achatar.py`.