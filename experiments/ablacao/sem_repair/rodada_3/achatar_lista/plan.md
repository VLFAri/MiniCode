Baseado na especificação fornecida, aqui está um plano numerado, passo a passo, do que deve ser programado para o projeto `achatar.py`, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Criação do Ambiente de Desenvolvimento**
   - Certifique-se de ter Python instalado no seu ambiente de desenvolvimento.
   - Crie um novo diretório para o projeto e navegue até ele.
   - Crie um arquivo chamado `achatar.py` dentro desse diretório.

2. **Implementação da Função `achatar(items)`**
   - Abra o arquivo `achatar.py` e adicione a função `achatar(items)` conforme descrito na especificação.
   - A função deve ser capaz de lidar com estruturas de entrada complexas, mantendo a ordem dos elementos e não dividindo strings.
   - Implemente a função utilizando recursão para lidar com estruturas de qualquer profundidade.

3. **Testes Unitários**
   - Adicione uma seção ao final do arquivo `achatar.py` para os testes unitários.
   - Use a biblioteca `unittest` do Python para criar casos de teste.
   - Implemente pelo menos três casos de teste, conforme especificado nos critérios de aceitação.

4. **Execução dos Testes**
   - Execute os testes unitários para garantir que a função `achatar(items)` funcione corretamente.
   - Verifique se todos os casos de teste passam sem erros.

5. **Documentação**
   - Adicione comentários ao código para documentar a função `achatar(items)`.
   - Certifique-se de que a documentação seja clara sobre como a função funciona e quais são suas expectativas de entrada e saída.

### Código Exemplo

Aqui está um exemplo básico de como a função `achatar(items)` poderia ser implementada e testada:

```python
def achatar(items):
    """
    Flattens a nested list or tuple structure into a single-level list.
    
    :param items: A nested structure containing lists, tuples, or strings.
    :return: A single-level list containing all elements from the input structure.
    """
    flat_list = []
    for item in items:
        if isinstance(item, (list, tuple)):
            flat_list.extend(achatar(item))
        else:
            flat_list.append(item)
    return flat_list

import unittest

class TestAchatar(unittest.TestCase):
    def test_achatar(self):
        self.assertEqual(achatar([1, [2, 3], 4]), [1, 2, 3, 4])
        self.assertEqual(achatar(([1, 2], [3, [4, 5]], 6)), [1, 2, 3, 4, 5, 6])
        self.assertEqual(achatar([[[1, 'two'], 3], ['four', 5]]), [1, 'two', 3, 'four', 5])

if __name__ == '__main__':
    unittest.main()
```

### Execução do Projeto

Para executar o projeto, você pode usar o seguinte comando no terminal:

```bash
python -m unittest achatar.py
```

Este comando irá rodar os testes unitários definidos no arquivo `achatar.py` e verificar se a função `achatar(items)` está funcionando corretamente de acordo com os critérios de aceitação fornecidos.

### Conclusão

Este plano cobre todas as etapas necessárias para implementar a função `achatar(items)` e garantir que ela funcione corretamente através de testes unitários. Certifique-se de revisar o código e os testes antes de considerar o projeto completo.