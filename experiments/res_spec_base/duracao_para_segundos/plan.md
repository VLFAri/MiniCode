Baseado na especificação fornecida e nas necessidades do projeto, aqui está um plano passo a passo para implementar a função `para_segundos` no arquivo `duracao.py`. O plano também inclui a criação ou atualização dos testes.

### Plano de Implementação

1. **Criar o arquivo `duracao.py`:**
   - Crie um novo arquivo chamado `duracao.py` no diretório do projeto.

2. **Implementar a função `para_segundos`:**
   - Na função `para_segundos`, defina a lógica para converter uma string de duração em segundos.
   - Use expressões regulares para extrair as partes da string que contêm horas, minutos e segundos.
   - Converta as partes extraídas em valores numéricos e calcule o total em segundos.
   - Trate casos onde a string de entrada esteja vazia ou não siga o formato esperado, lançando um `ValueError` nessas situações.

3. **Testar a função `para_segundos`:**
   - Crie um arquivo de teste chamado `test_duracao.py`.
   - Escreva casos de teste para verificar se a função `para_segundos` funciona corretamente com diferentes entradas.
   - Teste entradas válidas, entradas inválidas, entradas vazias, entradas com múltiplas unidades e entradas com números negativos.
   - Certifique-se de que os testes cobrem todos os requisitos e critérios de aceitação.

### Código de Exemplo

#### `duracao.py`
```python
import re

def para_segundos(texto):
    if not texto:
        raise ValueError("Entrada vazia ou inválida")
    
    # Expressão regular para encontrar horas, minutos e segundos
    match = re.match(r'^(\d+)h(\d+)m(\d+)s$', texto)
    
    if not match:
        raise ValueError("Formato de entrada inválido")
    
    # Extrair horas, minutos e segundos
    horas, minutos, segundos = match.groups()
    
    # Converter strings para inteiros
    horas = int(horas)
    minutos = int(minutos)
    segundos = int(segundos)
    
    # Calcular o total em segundos
    return horas * 3600 + minutos * 60 + segundos
```

#### `test_duracao.py`
```python
import unittest
from duracao import para_segundos

class TestDuracao(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(para_segundos('2h30m'), 9000)
        self.assertEqual(para_segundos('1h30m15s'), 5415)
        self.assertEqual(para_segundos('1h'), 3600)
        self.assertEqual(para_segundos('30m'), 1800)
        self.assertEqual(para_segundos('15s'), 15)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            para_segundos('')
        with self.assertRaises(ValueError):
            para_segundos('2h30')
        with self.assertRaises(ValueError):
            para_segundos('2h 30m')
        with self.assertRaises(ValueError):
            para_segundos('abc')

    def test_negative_input(self):
        self.assertEqual(para_segundos('-1h30m'), -5400)
        self.assertEqual(para_segundos('-30m'), -1800)
        self.assertEqual(para_segundos('-15s'), -15)

if __name__ == '__main__':
    unittest.main()
```

### Execução dos Testes
Para executar os testes, você pode usar o comando `pytest` se estiver usando o framework `pytest` ou `unittest` se estiver usando o framework padrão do Python.

```bash
python -m unittest test_duracao.py
```

ou

```bash
pytest
```

Este plano fornece uma estrutura clara para implementar a função `para_segundos` e garantir que ela funcione conforme especificado.