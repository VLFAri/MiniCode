### Plano de Desenvolvimento

Baseado na especificação fornecida e nos arquivos do projeto, segue um plano passo a passo para corrigir as funções `eh_palindromo` e `contar_vogais` no arquivo `texto.py`. O plano inclui a criação ou atualização dos testes.

#### Passos:

1. **Análise das Funções Atuais:**
   - Abra o arquivo `texto.py` e analise as funções `eh_palindromo` e `contar_vogais`.
   - Identifique quais partes dessas funções precisam ser modificadas para atender aos requisitos especificados.

2. **Correção da Função `eh_palindromo`:**
   - Implemente uma função auxiliar para normalizar a entrada (converter para minúsculas, remover espaços e pontuação).
   - Use essa função auxiliar para preparar a string antes de verificar se é um palíndromo.
   - Compare a string normalizada com sua versão invertida para determinar se é um palíndromo.

3. **Correção da Função `contar_vogais`:**
   - Crie uma lista de todas as vogais, incluindo as maiúsculas e acentuadas.
   - Implemente uma função que itere sobre cada caractere da string de entrada e conte quantas delas são vogais.

4. **Criação ou Atualização dos Testes:**
   - Adicione novos casos de teste para as funções corrigidas.
   - Certifique-se de que os casos de teste cobrem todas as condições especificadas (case-insensitive, espaços e pontuação ignorados para `eh_palindromo`; contagem de vogais maiúsculas e acentuadas para `contar_vogais`).

5. **Execução dos Testes:**
   - Execute os testes para garantir que as funções corrigidas funcionem conforme esperado.
   - Corrija quaisquer problemas encontrados durante a execução dos testes.

6. **Documentação:**
   - Adicione comentários ao código explicando as mudanças feitas e como as funções agora funcionam.
   - Certifique-se de que a documentação seja clara e fácil de entender.

### Detalhes do Plano

#### 1. Análise das Funções Atuais
- Examine o código existente em `texto.py`.
- Identifique quais partes do código precisam ser alteradas para atender aos requisitos.

#### 2. Correção da Função `eh_palindromo`
```python
import re

def eh_palindromo(s):
    # Normaliza a string: remove espaços, pontuação e converte para minúsculas
    s = re.sub(r'[^a-zA-Z]', '', s).lower()
    
    # Verifica se a string é igual à sua inversa
    return s == s[::-1]
```

#### 3. Correção da Função `contar_vogais`
```python
def contar_vogais(s):
    # Lista de vogais, incluindo maiúsculas e acentuadas
    vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'â', 'ê', 'ô', 'ã', 'õ']
    
    # Conta o número de vogais na string
    return sum(1 for char in s if char.lower() in vogais)
```

#### 4. Criação ou Atualização dos Testes
```python
import unittest
from texto import eh_palindromo, contar_vogais

class TestTexto(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("Anotaram a data da maratona"))
        self.assertFalse(eh_palindromo("Hello World"))

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Olá Mundo!"), 3)
        self.assertEqual(contar_vogais("AEIOU"), 5)

if __name__ == '__main__':
    unittest.main()
```

#### 5. Execução dos Testes
- Execute os testes usando o módulo `unittest` para garantir que as funções estão funcionando corretamente.
- Faça ajustes conforme necessário.

#### 6. Documentação
- Adicione comentários ao código explicando as mudanças feitas.
- Certifique-se de que a documentação seja clara e fácil de entender.

Este plano deve guiar você através da correção das funções e garantir que elas atendam aos requisitos especificados.