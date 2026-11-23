Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Criação do Ambiente de Desenvolvimento**
   - Crie um novo diretório para o projeto.
   - Configure o ambiente virtual (venv) para o projeto.
   - Instale as dependências necessárias, se houver.

2. **Definição da Estrutura do Projeto**
   - Crie os seguintes subdiretórios dentro do diretório principal do projeto:
     - `src`: Para colocar o código fonte da função `dias_entre`.
     - `tests`: Para colocar os testes unitários da função `dias_entre`.

3. **Implementação da Função `dias_entre`**
   - No diretório `src`, crie um arquivo chamado `data_utils.py`.
   - Implemente a função `dias_entre` conforme especificado na seção "Objective" da especificação.
   - Use o módulo `datetime` do Python para manipulação de datas.
   - Certifique-se de que a função lida corretamente com datas inválidas, lançando um `ValueError` quando necessário.
   - A função deve garantir que a diferença em dias seja sempre não negativa, independentemente da ordem das datas fornecidas.

4. **Testes Unitários**
   - No diretório `tests`, crie um arquivo chamado `test_data_utils.py`.
   - Importe a função `dias_entre` do módulo `data_utils`.
   - Escreva casos de teste para validar a implementação da função `dias_entre`.
   - Inclua testes para datas válidas e inválidas.
   - Use a biblioteca `unittest` do Python para escrever os testes.

5. **Execução dos Testes**
   - Execute os testes unitários para garantir que a função `dias_entre` funcione corretamente.
   - Verifique que todos os casos de teste passam sem erros.

6. **Documentação**
   - Adicione documentação ao código da função `dias_entre` para explicar seu propósito, parâmetros e retorno.
   - Documente os testes realizados e os resultados obtidos.

7. **Revisão e Refatoração**
   - Revisar o código da função `dias_entre` e os testes para garantir que estão de acordo com as melhores práticas de codificação.
   - Refatore o código se necessário para melhorar a legibilidade e a eficiência.

8. **Commit e Push**
   - Faça commit das alterações no controle de versão (git).
   - Faça push das alterações para o repositório remoto.

### Arquivos do Projeto

Aqui está como os arquivos do projeto podem ser organizados após a implementação:

```
projeto/
│
├── src/
│   └── data_utils.py
│
└── tests/
    └── test_data_utils.py
```

### Exemplo de Código

#### `data_utils.py`

```python
from datetime import datetime

def dias_entre(d1: str, d2: str) -> int:
    try:
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(d1, date_format)
        date2 = datetime.strptime(d2, date_format)
    except ValueError:
        raise ValueError("Invalid date format")
    
    delta = abs((date2 - date1).days)
    return delta
```

#### `test_data_utils.py`

```python
import unittest
from src.data_utils import dias_entre

class TestDataUtils(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(dias_entre('2023-01-01', '2023-01-02'), 1)
        self.assertEqual(dias_entre('2023-01-01', '2023-01-01'), 0)
    
    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            dias_entre('2023-01-01', '2023-02-30')
        
        with self.assertRaises(ValueError):
            dias_entre('2023-01-01', 'invalid-date')

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `dias_entre` e garantir sua qualidade através de testes rigorosos.