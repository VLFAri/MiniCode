Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Criar o arquivo `matriz.py`:**
   - Crie um novo arquivo chamado `matriz.py` no diretório do projeto.

2. **Implementar a função `transposta`:**
   - Dentro do arquivo `matriz.py`, implemente a função `transposta` que aceita uma matriz (lista de listas) como parâmetro.
   - A função deve verificar se todas as sublistas têm o mesmo tamanho. Se não tiverem, a função deve lançar uma exceção `ValueError`.
   - Caso contrário, a função deve calcular a matriz transposta e retorná-la.

3. **Testar a função `transposta`:**
   - Crie um novo arquivo chamado `test_matriz.py` no diretório do projeto.
   - Implemente os seguintes casos de teste dentro do arquivo `test_matriz.py`:
     - Teste para uma matriz válida (exemplo: `[[1, 2], [3, 4]]`).
     - Teste para uma matriz vazia (deve retornar `[]`).
     - Teste para uma matriz inválida (sublistas de tamanhos diferentes) - este teste deve falhar e lançar uma exceção `ValueError`.

4. **Executar os testes:**
   - Use um framework de teste como `pytest` para executar os testes criados em `test_matriz.py`.
   - Certifique-se de que todos os testes passem e que a função `transposta` funcione conforme especificado.

### Código de Exemplo

#### matriz.py
```python
def transposta(matriz):
    if not matriz:
        return []
    
    # Verifica se todas as sublistas têm o mesmo tamanho
    if len(set(map(len, matriz))) != 1:
        raise ValueError("Sublistas devem ter o mesmo tamanho")
    
    # Calcula a matriz transposta
    return [list(row) for row in zip(*matriz)]
```

#### test_matriz.py
```python
import pytest
from matriz import transposta

def test_transposta_valid():
    assert transposta([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]

def test_transposta_empty():
    assert transposta([]) == []

def test_transposta_invalid():
    with pytest.raises(ValueError):
        transposta([[1, 2], [3, 4, 5]])
```

### Execução dos Testes
Para executar os testes, você pode usar o comando `pytest` no terminal:

```bash
pytest test_matriz.py
```

Este comando irá rodar todos os testes definidos no arquivo `test_matriz.py` e garantir que a função `transposta` funcione corretamente de acordo com os requisitos especificados.

Este plano cobre a implementação da função `transposta`, a criação de testes unitários e a execução desses testes para garantir a qualidade do código.