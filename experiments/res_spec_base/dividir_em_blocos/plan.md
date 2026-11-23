Baseado na especificação fornecida, aqui está um plano passo a passo para implementar a função `dividir` conforme solicitado:

### Plano de Implementação

1. **Criar o arquivo `blocos.py`:**
   - Crie um novo arquivo chamado `blocos.py` no diretório do projeto.

2. **Implementar a função `dividir`:**
   - Dentro do arquivo `blocos.py`, defina a função `dividir` que aceita dois parâmetros: `lista` e `n`.
   - Verifique se `n` é maior que zero. Se não for, lance um `ValueError`.
   - Use um loop para iterar sobre a lista e criar sub-listas de tamanho `n`.
   - Adicione cada sub-lista a uma nova lista chamada `resultados`.
   - Retorne a lista `resultados` após a iteração.

3. **Adicionar documentação à função:**
   - Adicione docstrings à função `dividir` para descrever os parâmetros, o comportamento da função e os possíveis retornos.

4. **Escrever casos de teste:**
   - Crie um novo arquivo chamado `test_blocos.py` para armazenar os casos de teste.
   - Escreva testes unitários para verificar se a função `dividir` funciona corretamente para diferentes entradas.
   - Teste casos onde a lista é vazia ou tem apenas um elemento.
   - Teste casos onde `n` é menor ou igual a zero para garantir que um `ValueError` é lançado.
   - Teste casos onde a lista tem mais elementos do que `n` para garantir que os blocos são criados corretamente.

5. **Executar os testes:**
   - Execute os testes usando uma ferramenta de teste como `pytest`.
   - Certifique-se de que todos os casos de teste passam antes de considerar a implementação completa.

### Código Exemplo

Aqui está um exemplo básico de como o código poderia ser implementado:

```python
# blocos.py

def dividir(lista, n):
    """
    Divide uma lista em blocos de tamanho n.

    Args:
        lista (list): A lista a ser dividida.
        n (int): Tamanho dos blocos.

    Returns:
        list: Lista de blocos de tamanho n.

    Raises:
        ValueError: Se n for menor ou igual a zero.
    """
    if n <= 0:
        raise ValueError("n deve ser maior que zero")

    resultados = []
    for i in range(0, len(lista), n):
        resultados.append(lista[i:i + n])
    
    return resultados
```

E aqui estão alguns exemplos de testes que você pode adicionar ao `test_blocos.py`:

```python
# test_blocos.py

import pytest
from blocos import dividir

def test_dividir_lista_vazia():
    assert dividir([], 2) == []

def test_dividir_lista_um_elemento():
    assert dividir([1], 2) == [[1]]

def test_dividir_lista_tamanho_n():
    assert dividir([1, 2, 3, 4, 5, 6], 2) == [[1, 2], [3, 4], [5, 6]]

def test_dividir_lista_tamanho_maior_que_n():
    assert dividir([1, 2, 3, 4, 5, 6, 7], 3) == [[1, 2, 3], [4, 5, 6], [7]]

def test_dividir_lista_n_menor_ou_igual_zero():
    with pytest.raises(ValueError):
        dividir([1, 2, 3], 0)
    with pytest.raises(ValueError):
        dividir([1, 2, 3], -1)
```

Este plano e os exemplos de código fornecem uma estrutura clara para implementar a função `dividir` e garantir sua funcionalidade através de testes rigorosos.