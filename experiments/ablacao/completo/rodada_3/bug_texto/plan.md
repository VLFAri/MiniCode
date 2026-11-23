Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano numerado, passo a passo, do que deve ser programado, incluindo a criação ou atualização dos testes:

### Plano de Desenvolvimento

1. **Preparação do Ambiente**
   - Certifique-se de que o ambiente Python está configurado corretamente.
   - Crie um novo arquivo chamado `texto.py`.

2. **Implementação da Função `eh_palindromo`**
   - No arquivo `texto.py`, defina a função `eh_palindromo(texto)` que recebe uma string como entrada.
   - Dentro da função, converta toda a string para letras minúsculas para ignorar a diferença entre maiúsculas e minúsculas.
   - Remova todos os espaços e pontuação da string usando expressões regulares ou métodos de string.
   - Verifique se a string resultante é igual à sua versão invertida para determinar se é um palíndromo.

3. **Implementação da Função `contar_vogais`**
   - Defina a função `contar_vogais(texto)` que também recebe uma string como entrada.
   - Utilize uma lista de todas as vogais em português (considerando letras maiúsculas e acentos).
   - Conte quantas dessas vogais estão presentes na string de entrada.

4. **Testes Unitários**
   - Crie um novo arquivo chamado `test_texto.py`.
   - Importe as funções `eh_palindromo` e `contar_vogais` do módulo `texto`.
   - Implemente testes unitários para cada função utilizando a biblioteca `unittest` ou `pytest`.
   - Para `eh_palindromo`, teste com pelo menos cinco diferentes entradas, incluindo casos de palíndromos conhecidos e não-palíndromos.
   - Para `contar_vogais`, teste com pelo menos cinco diferentes entradas, incluindo strings com vogais maiúsculas e acentuadas.

5. **Execução dos Testes**
   - Execute os testes criados para garantir que ambas as funções funcionem conforme esperado.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

6. **Documentação**
   - Adicione comentários ao código em `texto.py` explicando o propósito de cada função e como elas são utilizadas.
   - Documente os testes em `test_texto.py` para clareza e futuras referências.

### Exemplo de Código

#### `texto.py`
```python
import re

def eh_palindromo(texto):
    # Convertendo para minúsculas e removendo espaços e pontuação
    texto = re.sub(r'[^a-záéíóúâêîôãõ]', '', texto.lower())
    # Verificando se a string é igual à sua inversa
    return texto == texto[::-1]

def contar_vogais(texto):
    # Lista de vogais em português
    vogais = 'aeiouáéíóúâêîôãõAEIOUÁÉÍÓÚÂÊÎÔÃÕ'
    # Contagem das vogais na string
    return sum(1 for char in texto if char in vogais)
```

#### `test_texto.py`
```python
import unittest
from texto import eh_palindromo, contar_vogais

class TestTexto(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("Anotaram a data da maratona"))
        self.assertTrue(eh_palindromo("Socorram-me subi no onibus em Marrocos"))
        self.assertFalse(eh_palindromo("Este não é um palíndromo"))
        self.assertFalse(eh_palindromo("Python"))
        self.assertTrue(eh_palindromo("A man a plan a canal Panama"))

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Olá Mundo!"), 3)
        self.assertEqual(contar_vogais("Árvore"), 4)
        self.assertEqual(contar_vogais("Teste com Acentuação"), 8)
        self.assertEqual(contar_vogais("Vogais Maiusculas"), 7)
        self.assertEqual(contar_vogais("Sem Vogais"), 0)

if __name__ == '__main__':
    unittest.main()
```

### Executando os Testes
Para executar os testes, você pode usar o seguinte comando no terminal:
```bash
python -m unittest test_texto.py
```

Este plano cobre a implementação das duas funções necessárias, bem como a criação de testes adequados para garantir a qualidade do código.