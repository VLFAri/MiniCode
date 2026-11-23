Baseado na especificação fornecida, aqui está um plano numerado de como implementar o módulo `palavras.py` conforme solicitado:

### Plano de Implementação

1. **Criação do Módulo `palavras.py`:**
   - Crie um novo arquivo Python chamado `palavras.py`.

2. **Importação de Bibliotecas Necessárias:**
   - No início do arquivo `palavras.py`, importe as bibliotecas necessárias para manipulação de texto e tratamento de pontuação.

3. **Definição da Função `frequencia_palavras`:**
   - Defina uma função chamada `frequencia_palavras` que aceita um parâmetro `texto`.
   - Dentro da função, converta todas as letras do texto para minúsculas usando métodos adequados.
   - Remova todos os caracteres de pontuação do texto utilizando expressões regulares ou métodos de string.
   - Substitua múltiplos espaços por um único espaço para garantir que palavras não sejam contadas erroneamente devido a espaços extras.
   - Separe o texto em palavras usando o método `split()`.

4. **Contagem das Palavras:**
   - Use um dicionário para contar a frequência de cada palavra.
   - Para cada palavra no texto separado, incremente o valor correspondente no dicionário.

5. **Retorno do Resultado:**
   - Retorne o dicionário com a contagem de palavras.

6. **Testes Unitários:**
   - Crie um novo arquivo Python chamado `test_palavras.py`.
   - Importe a função `frequencia_palavras` do módulo `palavras`.
   - Escreva casos de teste para cobrir todos os cenários mencionados na seção de critérios de aceitação.
     - Um texto com várias palavras e pontuação.
     - Um texto vazio.
     - Um texto com apenas espaços em branco e/ou pontuação.
     - Um texto com palavras repetidas e pontuação.
   - Utilize a biblioteca `unittest` para definir e executar os testes.

7. **Execução dos Testes:**
   - Execute os testes unitários para verificar se a função `frequencia_palavras` atende aos requisitos e critérios de aceitação.

### Código Exemplo

Aqui está um exemplo básico de como o código poderia ser estruturado:

#### `palavras.py`
```python
import re

def frequencia_palavras(texto):
    # Convertendo tudo para minúsculas
    texto = texto.lower()
    
    # Removendo pontuação
    texto = re.sub(r'[^\w\s]', '', texto)
    
    # Substituindo múltiplos espaços por um único espaço
    texto = re.sub(r'\s+', ' ', texto).strip()
    
    # Separando o texto em palavras
    palavras = texto.split(' ')
    
    # Contagem de palavras
    contador = {}
    for palavra in palavras:
        if palavra:
            contador[palavra] = contador.get(palavra, 0) + 1
    
    return contador
```

#### `test_palavras.py`
```python
import unittest
from palavras import frequencia_palavras

class TestFrequenciaPalavras(unittest.TestCase):
    def test_texto_com_palavras_e_pontuacao(self):
        resultado = frequencia_palavras("Olá, mundo! Olá, universo!")
        self.assertEqual(resultado, {'olá': 2, 'mundo': 1, 'universo': 1})
    
    def test_texto_vazio(self):
        resultado = frequencia_palavras("")
        self.assertEqual(resultado, {})
    
    def test_texto_com_espacos_e_pontuacao(self):
        resultado = frequencia_palavras(" , ; :")
        self.assertEqual(resultado, {})
    
    def test_texto_com_palavras_repetidas_e_pontuacao(self):
        resultado = frequencia_palavras("Python, Python, Python!")
        self.assertEqual(resultado, {'python': 3})

if __name__ == '__main__':
    unittest.main()
```

Este plano e os exemplos de código fornecem uma estrutura clara para implementar a função `frequencia_palavras` e seus testes associados.