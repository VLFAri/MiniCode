Baseado na especificação e nos requisitos fornecidos, aqui está um plano passo a passo para implementar a função `dias_entre`:

### Plano de Implementação

1. **Criar o ambiente de desenvolvimento:**
   - Certifique-se de ter um ambiente Python configurado.
   - Crie um novo diretório para o projeto e inicie um novo arquivo Python, por exemplo, `data_calculator.py`.

2. **Definir a estrutura básica da função:**
   - No arquivo `data_calculator.py`, defina a função `dias_entre(d1, d2)` com os parâmetros `d1` e `d2`.
   - Inicialmente, a função pode apenas imprimir os parâmetros recebidos para verificar se a entrada é correta.

3. **Validar as entradas:**
   - Dentro da função `dias_entre`, adicione lógica para validar se ambas as strings estão no formato correto (`AAAA-MM-DD`).
   - Use expressões regulares ou métodos de string para verificar a validade das datas.

4. **Converter as strings em objetos datetime:**
   - Utilize a biblioteca `datetime` para converter as strings de data em objetos `datetime`.
   - Verifique novamente a validade das datas convertidas para garantir que não haja erros.

5. **Calcular a diferença entre as datas:**
   - Subtraia a primeira data da segunda para obter um objeto `timedelta`.
   - Extraia o número de dias do objeto `timedelta`.

6. **Tratar exceções:**
   - Adicione tratamento de exceções para lidar com datas inválidas, lançando uma exceção `ValueError` quando necessário.

7. **Retornar o resultado:**
   - Retorne o número de dias como um valor inteiro positivo.

8. **Implementar testes unitários:**
   - Crie um arquivo separado para testes, por exemplo, `test_data_calculator.py`.
   - Use a biblioteca `unittest` para escrever casos de teste que cobrem todos os cenários possíveis, incluindo entradas válidas e inválidas.

9. **Executar os testes:**
   - Execute os testes para garantir que a função `dias_entre` funcione conforme esperado em todas as condições.

### Código Exemplo

Aqui está um exemplo básico de como a função poderia ser implementada:

```python
from datetime import datetime

def dias_entre(d1, d2):
    try:
        # Convertendo as strings para objetos datetime
        date_format = "%Y-%m-%d"
        date1 = datetime.strptime(d1, date_format)
        date2 = datetime.strptime(d2, date_format)
        
        # Calculando a diferença entre as datas
        delta = abs(date2 - date1)
        
        # Retornando o número de dias
        return delta.days
    except ValueError:
        raise ValueError("Invalid date format")
```

### Testes Unitários

Aqui está um exemplo de como os testes podem ser escritos usando a biblioteca `unittest`:

```python
import unittest
from data_calculator import dias_entre

class TestDateCalculator(unittest.TestCase):
    def test_valid_dates(self):
        self.assertEqual(dias_entre('2020-01-01', '2020-01-05'), 4)
        self.assertEqual(dias_entre('2020-02-01', '2020-02-29'), 28)
        # Adicionar mais casos de teste válidos aqui...

    def test_invalid_dates(self):
        with self.assertRaises(ValueError):
            dias_entre('2020-01-01', '2020-01-00')
        with self.assertRaises(ValueError):
            dias_entre('2020-01-01', '2020-01-32')
        # Adicionar mais casos de teste inválidos aqui...

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `dias_entre` e garantir sua corretude através de testes rigorosos.