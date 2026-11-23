Baseado na especificação fornecida e considerando que os arquivos do projeto estão vazios, podemos criar um plano passo a passo para implementar a função `para_segundos`. Vamos incluir também a criação de testes para garantir que a função funcione corretamente.

### Plano de Implementação

1. **Criar o arquivo principal do projeto**:
   - Crie um arquivo chamado `converter_tempo.py`.

2. **Definir a função `para_segundos`**:
   - No arquivo `converter_tempo.py`, defina a função `para_segundos` que aceita uma string como entrada e retorna o número total de segundos correspondente.
   - A função deve lidar com diferentes formatos de entrada (por exemplo, `'1h30m15s'`, `'2h'`, `'90m'`, `'45s'`) e converter essas entradas em segundos.
   - A função deve levantar uma exceção `ValueError` se a entrada estiver vazia ou não seguir o formato esperado.

3. **Implementar a lógica da função**:
   - Dentro da função `para_segundos`, use expressões regulares para extrair as partes da string que representam horas, minutos e segundos.
   - Converta cada parte extraída para o número de segundos correspondente e some-os para obter o resultado final.
   - Se a string de entrada estiver vazia ou não seguir o formato esperado, levante uma exceção `ValueError`.

4. **Criar um arquivo de teste**:
   - Crie um arquivo chamado `test_converter_tempo.py` para escrever os casos de teste.

5. **Escrever os casos de teste**:
   - No arquivo `test_converter_tempo.py`, escreva os casos de teste usando a biblioteca `unittest`.
   - Teste diferentes formatos de entrada para garantir que a função `para_segundos` produza os resultados esperados.
   - Certifique-se de testar entradas válidas e inválidas para garantir que a função levante `ValueError` quando necessário.

### Código de Exemplo

Aqui está um exemplo de como você pode implementar a função `para_segundos` e seus testes:

#### Arquivo `converter_tempo.py`

```python
import re

def para_segundos(duration_str):
    # Regular expression to match the pattern
    pattern = r'(\d+)h(\d*)m(\d*)s'
    
    # Match the input string against the pattern
    match = re.match(pattern, duration_str)
    
    if not match:
        raise ValueError("Invalid input format")
    
    # Extract hours, minutes, and seconds from the matched groups
    hours = int(match.group(1) or 0)
    minutes = int(match.group(2) or 0)
    seconds = int(match.group(3) or 0)
    
    # Convert to total seconds
    return hours * 3600 + minutes * 60 + seconds
```

#### Arquivo `test_converter_tempo.py`

```python
import unittest
from converter_tempo import para_segundos

class TestConverterTempo(unittest.TestCase):

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            para_segundos('')
    
    def test_hours_only(self):
        self.assertEqual(para_segundos('1h'), 3600)
    
    def test_minutes_only(self):
        self.assertEqual(para_segundos('1m'), 60)
    
    def test_seconds_only(self):
        self.assertEqual(para_segundos('1s'), 1)
    
    def test_hours_and_minutes(self):
        self.assertEqual(para_segundos('2h30m'), 9000)
    
    def test_minutes_and_seconds(self):
        self.assertEqual(para_segundos('45m30s'), 2730)
    
    def test_all_units(self):
        self.assertEqual(para_segundos('1h2m3s'), 4323)
    
    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            para_segundos('invalid')

if __name__ == '__main__':
    unittest.main()
```

Este plano e os exemplos de código fornecem uma estrutura clara para implementar a função `para_segundos` e garantir sua precisão através de testes automatizados.