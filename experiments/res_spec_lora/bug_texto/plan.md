Baseado na especificação fornecida, aqui está um plano passo a passo para implementar as funções `eh_palindromo` e `contar_vogais` no arquivo `texto.py`, incluindo a criação ou atualização dos testes:

### Passo 1: Preparação do Ambiente
- Certifique-se de que o ambiente Python está configurado corretamente.
- Crie um diretório para o projeto se ainda não existir.
- Crie o arquivo `texto.py` dentro desse diretório.

### Passo 2: Implementação da Função `eh_palindromo`
1. Abra o arquivo `texto.py`.
2. Adicione a função `eh_palindromo(texto)` com os seguintes passos internos:
   - Remova todos os caracteres que não são letras usando expressões regulares ou métodos de string.
   - Converta todas as letras para minúsculas.
   - Compare a string original (limpa) com sua versão invertida.
3. Teste a função com exemplos fornecidos na especificação para garantir que ela funcione corretamente.

### Passo 3: Implementação da Função `contar_vogais`
1. No mesmo arquivo `texto.py`, adicione a função `contar_vogais(texto)` com os seguintes passos internos:
   - Converta todas as letras para minúsculas para facilitar a contagem.
   - Use um loop para percorrer cada caractere da string.
   - Verifique se cada caractere é uma vogal e incremente um contador se for.
2. Teste a função com exemplos fornecidos na especificação para garantir que ela funcione corretamente.

### Passo 4: Criação ou Atualização dos Testes
1. Crie um novo arquivo chamado `test_texto.py` no mesmo diretório.
2. Importe as funções `eh_palindromo` e `contar_vogais` do módulo `texto`.
3. Use o framework de teste `unittest` para criar casos de teste para ambas as funções.
4. Para cada caso de teste, use os exemplos fornecidos na especificação para verificar se as funções retornam os valores esperados.

### Passo 5: Execução dos Testes
1. Execute os testes criados em `test_texto.py` para garantir que todas as funções funcionem conforme especificado.
2. Corrija quaisquer erros encontrados durante a execução dos testes.

### Código Exemplo

#### Arquivo `texto.py`
```python
import re

def eh_palindromo(texto):
    # Remove non-alphabetic characters and converts to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z]', '', texto).lower()
    # Checks if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

def contar_vogais(texto):
    # Converts all letters to lowercase for uniformity
    texto = texto.lower()
    # Counts the number of vowels in the text
    return sum(1 for char in texto if char in 'aeiouáéíóúâêîôûàèìòù')

```

#### Arquivo `test_texto.py`
```python
import unittest
from texto import eh_palindromo, contar_vogais

class TestTexto(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("Anotaram a data da maratona"))
        self.assertFalse(eh_palindromo("Ola mundo!"))

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Anotaram a data da maratona"), 10)
        self.assertEqual(contar_vogais("Python é incrível!"), 9)
        self.assertEqual(contar_vogais(""), 0)

if __name__ == '__main__':
    unittest.main()
```

Este plano fornece uma estrutura clara para implementar as funções necessárias e garantir que elas funcionem corretamente através de testes automatizados.