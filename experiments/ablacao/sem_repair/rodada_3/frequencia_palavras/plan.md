Baseado na especificação fornecida e considerando que o projeto está vazio, aqui está um plano passo a passo para implementar o módulo `palavras.py` conforme solicitado:

### Plano de Implementação

1. **Criar o arquivo `palavras.py`:**
   - Crie um novo arquivo Python chamado `palavras.py`.

2. **Definir a função `frequencia_palavras`:**
   - Dentro do arquivo `palavras.py`, defina uma função chamada `frequencia_palavras` que aceita um parâmetro `texto`.
   - A função deve retornar um dicionário contendo a contagem de cada palavra no texto de entrada.

3. **Processamento do texto:**
   - Converta todas as palavras para minúsculas para garantir que a contagem seja case-insensitive.
   - Remova todos os sinais de pontuação do texto antes de contar as palavras.

4. **Contagem das palavras:**
   - Use um dicionário para manter a contagem de cada palavra.
   - Para cada palavra processada, incremente a contagem correspondente no dicionário.

5. **Tratamento de entradas vazias:**
   - Se o texto de entrada estiver vazio, retorne um dicionário vazio.

6. **Testes unitários:**
   - Crie um conjunto de casos de teste para verificar se a função `frequencia_palavras` funciona corretamente.
   - Os casos de teste devem incluir entradas com diferentes formatos, como palavras mistas de maiúsculas e minúsculas, palavras com pontuação e entradas vazias.

7. **Implementar os testes:**
   - Adicione os casos de teste ao arquivo `palavras.py` ou em um arquivo separado de testes.
   - Certifique-se de que os testes cobrem todos os aspectos da função, incluindo a conversão de letras para minúsculas, ignorância de pontuação e tratamento de entradas vazias.

8. **Executar os testes:**
   - Execute os testes para garantir que a função funcione conforme esperado.

9. **Documentação:**
   - Adicione documentação ao código para explicar o propósito da função e como ela deve ser usada.

### Exemplo de Código

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

### Exemplo de Testes

Você pode adicionar testes usando a biblioteca `unittest` do Python:

```python
import unittest
from palavras import frequencia_palavras

class TestFrequenciaPalavras(unittest.TestCase):
    def test_vazio(self):
        self.assertEqual(frequencia_palavras(""), {})
    
    def test_sem_pontuacao(self):
        self.assertEqual(frequencia_palavras("Olá mundo"), {"olá": 1, "mundo": 1})
    
    def test_com_pontuacao(self):
        self.assertEqual(frequencia_palavras("Olá, Mundo!"), {"olá": 1, "mundo": 1})
    
    def test_maiusculas_minusculas(self):
        self.assertEqual(frequencia_palavras("Olá olá Olá"), {"olá": 3})

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `frequencia_palavras` e garantir que ela funcione corretamente através de testes adequados.