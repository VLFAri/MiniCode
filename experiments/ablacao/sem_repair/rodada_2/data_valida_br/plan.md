Baseado na especificação fornecida, aqui está um plano numerado de como implementar o script Python `datas_br.py` conforme solicitado:

### Plano de Implementação

1. **Criação do Arquivo `datas_br.py`**
   - Crie um novo arquivo chamado `datas_br.py`.

2. **Importação de Módulos Necessários**
   - Importe os módulos necessários para manipulação de datas e validação de strings.

3. **Definição da Função `eh_data_valida(texto)`**
   - Defina uma função chamada `eh_data_valida(texto)` que recebe uma única string `texto` como parâmetro.
   - Dentro da função, use expressões regulares para verificar se a string segue o formato `dd/mm/yyyy`.
   - Separe a string em dia, mês e ano usando o método `split()`.

4. **Validação das Restrições de Data**
   - Verifique se o ano está entre 1900 e 2100.
   - Verifique se o mês está entre 1 e 12.
   - Verifique se o dia está entre 1 e 31.
   - Use uma lista com o número de dias em cada mês para validar o número de dias no mês correspondente.
   - Para fevereiro, verifique se o ano é bissexto antes de validar o número de dias.

5. **Função Auxiliar para Verificar Anos Bissextos**
   - Crie uma função auxiliar para determinar se um ano é bissexto, seguindo as regras especificadas.

6. **Retorno do Resultado**
   - Retorne `True` se todas as condições forem satisfeitas; caso contrário, retorne `False`.

7. **Criação de Testes Unitários**
   - Crie um conjunto de casos de teste para a função `eh_data_valida()`.
   - Inclua testes para datas válidas e inválidas conforme especificado nas restrições e critérios de aceitação.
   - Use a biblioteca `unittest` para escrever e executar os testes.

### Código Proposto

```python
import re
from datetime import datetime

def eh_data_valida(texto):
    # Verifica se a data está no formato correto
    if not re.match(r'\d{2}/\d{2}/\d{4}', texto):
        return False
    
    try:
        # Tenta converter a string para um objeto datetime
        data = datetime.strptime(texto, '%d/%m/%Y')
        
        # Verifica as restrições de ano, mês e dia
        if 1900 <= data.year <= 2100 and 1 <= data.month <= 12 and 1 <= data.day <= 31:
            return True
        else:
            return False
    except ValueError:
        # Caso a conversão falhe, a data não é válida
        return False

def is_leap_year(year):
    # Função auxiliar para verificar se o ano é bissexto
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# Testes unitários
import unittest

class TestDateValidation(unittest.TestCase):
    def test_valid_dates(self):
        self.assertTrue(eh_data_valida('05/03/2024'))
        self.assertTrue(eh_data_valida('29/02/2024'))
    
    def test_invalid_dates(self):
        self.assertFalse(eh_data_valida('32/01/2024'))
        self.assertFalse(eh_data_valida('00/00/2024'))
        self.assertFalse(eh_data_valida('01/13/2024'))
        self.assertFalse(eh_data_valida('01/00/2024'))
        self.assertFalse(eh_data_valida('01/01/1899'))
        self.assertFalse(eh_data_valida('01/01/2101'))
        self.assertFalse(eh_data_valida('29/02/2021'))
        self.assertFalse(eh_data_valida('29/02/2023'))

if __name__ == '__main__':
    unittest.main()
```

### Execução dos Testes

Para executar os testes unitários, você pode usar o seguinte comando no terminal:

```bash
python -m unittest datas_br.py
```

Este comando irá rodar todos os testes definidos na classe `TestDateValidation`. Certifique-se de que o arquivo `datas_br.py` esteja no mesmo diretório onde você está executando o comando.

Este plano cobre a criação da função principal, a implementação de testes unitários e a execução desses testes para garantir que a função funcione corretamente com diferentes entradas.