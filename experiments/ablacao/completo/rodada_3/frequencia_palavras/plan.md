Baseado na especificação fornecida e considerando que o projeto está vazio, aqui está um plano passo a passo para implementar o módulo `palavras.py` conforme solicitado:

### Plano de Implementação

1. **Criar o arquivo `palavras.py`:**
   - Crie um novo arquivo Python chamado `palavras.py`.

2. **Definir a função `frequencia_palavras`:**
   - Dentro do arquivo `palavras.py`, defina uma função chamada `frequencia_palavras` que aceita um parâmetro `texto`.
   - Esta função deve retornar um dicionário contendo a contagem de cada palavra no texto de entrada.

3. **Processamento do texto:**
   - Converta todas as palavras para minúsculas.
   - Remova todos os sinais de pontuação do texto.

4. **Contagem das palavras:**
   - Use um dicionário para contar a frequência de cada palavra.
   - Para cada palavra processada, incremente o valor correspondente no dicionário.

5. **Tratamento de entradas vazias:**
   - Se o texto de entrada for uma string vazia, retorne um dicionário vazio.

6. **Testes unitários:**
   - Crie um conjunto de casos de teste para verificar se a função `frequencia_palavras` está funcionando corretamente.
   - Os casos de teste devem incluir:
     - Uma frase com várias palavras e pontuação.
     - Uma string vazia.
     - Uma string contendo apenas pontuação.
     - Uma string com palavras repetidas em diferentes casos e pontuação.

7. **Implementação dos testes:**
   - Adicione testes unitários ao arquivo `palavras.py` usando uma biblioteca de testes como `unittest` ou `pytest`.
   - Certifique-se de que os testes cobrem todos os cenários mencionados nos critérios de aceitação.

8. **Executar os testes:**
   - Execute os testes para garantir que a função `frequencia_palavras` esteja funcionando conforme esperado.

### Código Exemplo

Aqui está um exemplo básico de como o código poderia ser implementado:

```python
import string

def frequencia_palavras(texto):
    # Remove pontuação e converte tudo para minúsculas
    translator = str.maketrans('', '', string.punctuation)
    texto_processado = texto.translate(translator).lower()
    
    # Divide o texto em palavras
    palavras = texto_processado.split()
    
    # Conta a frequência de cada palavra
    frequencias = {}
    for palavra in palavras:
        if palavra in frequencias:
            frequencias[palavra] += 1
        else:
            frequencias[palavra] = 1
    
    return frequencias
```

### Testes Unitários

Aqui está um exemplo de como os testes podem ser implementados usando `unittest`:

```python
import unittest
from palavras import frequencia_palavras

class TestFrequenciaPalavras(unittest.TestCase):
    def test_frequencia_palavras(self):
        self.assertEqual(frequencia_palavras(""), {})
        self.assertEqual(frequencia_palavras("Olá, Mundo!"), {"olá": 1, "mundo": 1})
        self.assertEqual(frequencia_palavras("Olá olá Olá"), {"olá": 3})
        self.assertEqual(frequencia_palavras("!!!"), {})

if __name__ == '__main__':
    unittest.main()
```

Este plano e o exemplo de código fornecem uma estrutura clara para implementar a função `frequencia_palavras` e garantir sua funcionalidade através de testes adequados.