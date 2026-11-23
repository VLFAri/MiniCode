Baseado na especificação e nos requisitos fornecidos, aqui está um plano numerado de como implementar a função `para_segundos` em Python:

### Plano de Implementação

1. **Criar o arquivo principal do projeto:**
   - Crie um novo arquivo Python chamado `duration_converter.py`.
   
2. **Definir a função `para_segundos`:**
   - Na função `para_segundos`, defina os parâmetros necessários para receber a string de duração.
   - Implemente a lógica para verificar se a string de entrada é vazia ou inválida.
     - Se a string estiver vazia, levante uma exceção `ValueError`.
     - Se a string não seguir o formato esperado (ex.: '1h30m15s'), também levante uma exceção `ValueError`.
   - Implemente a lógica para converter a string de duração em segundos.
     - Use expressões regulares para extrair os valores de horas, minutos e segundos da string de entrada.
     - Converta os valores extraídos em segundos e some-os para obter o resultado final.

3. **Implementar testes unitários:**
   - Crie um novo arquivo Python chamado `test_duration_converter.py`.
   - Importe a função `para_segundos` do arquivo `duration_converter.py`.
   - Escreva casos de teste para validar a função.
     - Inclua testes para entradas válidas (por exemplo, '1h30m15s').
     - Inclua testes para entradas vazias e inválidas que devem levantar `ValueError`.
     - Certifique-se de que a função retorna o valor correto em segundos para cada caso de teste válido.

4. **Executar os testes:**
   - Execute os testes unitários para garantir que a função `para_segundos` funcione conforme o esperado.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

### Exemplo de Código

Aqui estão exemplos de como os arquivos poderiam ser estruturados:

#### `duration_converter.py`

```python
import re

def para_segundos(duration_str):
    if not duration_str:
        raise ValueError("Input string is empty or invalid.")
    
    # Regular expression to match the pattern
    match = re.match(r'^(\d+h)?(\d+m)?(\d+s)?$', duration_str)
    
    if not match:
        raise ValueError("Input string is empty or invalid.")
    
    hours = int(match.group(1)[:-1]) if match.group(1) else 0
    minutes = int(match.group(2)[:-1]) if match.group(2) else 0
    seconds = int(match.group(3)[:-1]) if match.group(3) else 0
    
    total_seconds = (hours * 3600) + (minutes * 60) + seconds
    return total_seconds
```

#### `test_duration_converter.py`

```python
import unittest
from duration_converter import para_segundos

class TestDurationConverter(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(para_segundos('1h30m15s'), 5415)
        self.assertEqual(para_segundos('2h'), 7200)
        self.assertEqual(para_segundos('30m'), 1800)
        self.assertEqual(para_segundos('15s'), 15)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            para_segundos('')
        with self.assertRaises(ValueError):
            para_segundos('abc')
        with self.assertRaises(ValueError):
            para_segundos('1h2m3s4')

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `para_segundos` e garantir sua corretude através de testes unitários.