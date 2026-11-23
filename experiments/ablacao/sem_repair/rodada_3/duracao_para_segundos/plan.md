Baseado na especificação fornecida, aqui está um plano numerado de como implementar a função `para_segundos` em Python, incluindo a criação ou atualização dos testes:

### Plano de Implementação

1. **Criar o arquivo principal do projeto:**
   - Crie um arquivo Python chamado `converter_tempo.py` onde a função `para_segundos` será definida.

2. **Definir a função `para_segundos`:**
   - Na função `para_segundos`, defina os parâmetros necessários para lidar com a entrada de string.
   - Implemente a lógica para converter a string de duração em segundos.
   - Certifique-se de que a função levanta uma exceção `ValueError` quando a entrada é vazia ou inválida.

3. **Implementar a lógica de conversão:**
   - Use expressões regulares para extrair os valores de horas, minutos e segundos da string de entrada.
   - Converta esses valores em segundos e some-os para obter o resultado final.

4. **Testar a função com casos de teste válidos:**
   - Crie um conjunto de entradas válidas para testar a função.
   - Verifique se a função retorna o valor correto em segundos para cada entrada.

5. **Testar a função com entradas inválidas:**
   - Crie um conjunto de entradas inválidas para testar a função.
   - Verifique se a função levanta uma exceção `ValueError` corretamente para cada entrada inválida.

6. **Incluir testes automatizados:**
   - Crie um arquivo de teste chamado `test_converter_tempo.py`.
   - Defina funções de teste para validar a funcionalidade da função `para_segundos`.
   - Use a biblioteca `unittest` para escrever os casos de teste.

7. **Executar os testes:**
   - Execute os testes automatizados para garantir que a função `para_segundos` funcione conforme esperado.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

8. **Documentar a função:**
   - Adicione comentários ao código para documentar a função `para_segundos`.
   - Certifique-se de que a documentação inclui informações sobre os parâmetros de entrada, saída esperada e possíveis exceções.

9. **Revisar e refatorar o código:**
   - Revisar o código para garantir que ele seja limpo e fácil de entender.
   - Refatore o código se necessário para melhorar a legibilidade e a eficiência.

### Exemplo de Código

Aqui está um exemplo básico de como a função `para_segundos` poderia ser implementada:

```python
import re

def para_segundos(duration_str):
    if not duration_str:
        raise ValueError("Input string cannot be empty")

    # Regular expression to match the pattern
    pattern = r'(\d+h)?(\d+m)?(\d+s)?'
    match = re.match(pattern, duration_str)

    if not match:
        raise ValueError("Invalid format")

    hours = int(match.group(1)[:-1]) if match.group(1) else 0
    minutes = int(match.group(2)[:-1]) if match.group(2) else 0
    seconds = int(match.group(3)[:-1]) if match.group(3) else 0

    # Convert to seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds
```

### Exemplo de Arquivo de Testes

Aqui está um exemplo de como o arquivo de testes `test_converter_tempo.py` pode ser estruturado usando a biblioteca `unittest`:

```python
import unittest
from converter_tempo import para_segundos

class TestConverterTempo(unittest.TestCase):

    def test_valid_inputs(self):
        self.assertEqual(para_segundos('1h'), 3600)
        self.assertEqual(para_segundos('1m'), 60)
        self.assertEqual(para_segundos('1s'), 1)
        self.assertEqual(para_segundos('1h30m'), 5400)
        self.assertEqual(para_segundos('30m15s'), 1815)
        self.assertEqual(para_segundos('1h2m3s'), 4323)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            para_segundos('')
        with self.assertRaises(ValueError):
            para_segundos('abc')
        with self.assertRaises(ValueError):
            para_segundos('1h2m3')

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `para_segundos` e garantir sua correta funcionalidade através de testes automatizados.