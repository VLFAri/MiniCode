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
   - Se o texto de entrada for uma string vazia, retorne um dicionário vazio.

6. **Testes unitários:**
   - Crie um conjunto de casos de teste para verificar se a função `frequencia_palavras` está funcionando corretamente.
   - Teste cenários como texto vazio, texto com palavras repetidas, texto com pontuação, etc.
   - Certifique-se de que a função ignora a pontuação e converte todas as palavras para minúsculas.

7. **Implementação dos testes:**
   - Adicione testes unitários ao arquivo `palavras.py` ou em um arquivo separado de teste.
   - Utilize uma biblioteca de testes como `unittest` ou `pytest` para escrever e executar os testes.

8. **Executar os testes:**
   - Execute os testes para garantir que a função `frequencia_palavras` atenda aos requisitos e critérios de aceitação.

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

Aqui está um exemplo de como os testes podem ser escritos usando `unittest`:

```python
import unittest
from palavras import frequencia_palavras

class TestFrequenciaPalavras(unittest.TestCase):
    def test_vazio(self):
        self.assertEqual(frequencia_palavras(""), {})
    
    def test_sem_pontuacao(self):
        self.assertEqual(frequencia_palavras("Olá Mundo"), {"olá": 1, "mundo": 1})
    
    def test_com_pontuacao(self):
        self.assertEqual(frequencia_palavras("Olá, Mundo!"), {"olá": 1, "mundo": 1})
    
    def test_repeticao(self):
        self.assertEqual(frequencia_palavras("Olá Olá Mundo"), {"olá": 2, "mundo": 1})

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar a função `frequencia_palavras` e garantir sua correta funcionalidade através de testes adequados.