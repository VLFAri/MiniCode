Baseado nas especificações e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para corrigir as funções `eh_palindromo` e `contar_vogais` no arquivo `texto.py`.

### Plano de Implementação

1. **Importar Módulos Necessários**
   - Certifique-se de que o módulo `re` esteja importado para usar expressões regulares, que serão úteis para manipular strings.

2. **Corrigir a Função `eh_palindromo`**
   - **Limpar a String**: Remova todos os caracteres que não são letras usando expressões regulares.
   - **Converter para Minúsculas**: Converta toda a string para minúsculas para ignorar a diferenciação entre maiúsculas e minúsculas.
   - **Verificar Palíndromo**: Compare a string original limpa com sua versão invertida para verificar se é palíndromo.

3. **Corrigir a Função `contar_vogais`**
   - **Definir Vogais**: Crie uma lista ou conjunto de todas as vogais, incluindo as maiúsculas e acentuadas.
   - **Contagem de Vogais**: Use um loop para contar quantas vogais existem na string.

4. **Implementar Testes Unitários**
   - **Teste `eh_palindromo`**: Crie casos de teste para verificar se a função retorna `True` para palíndromos e `False` para strings que não são palíndromos.
   - **Teste `contar_vogais`**: Crie casos de teste para verificar se a função conta corretamente as vogais em diferentes strings.

5. **Executar Testes**
   - Execute os testes unitários para garantir que ambas as funções atendam aos critérios de aceitação.

### Código Proposto

```python
import re

def eh_palindromo(texto):
    # Remove tudo que não seja letra
    texto_limp = re.sub(r'[^a-zA-Z]', '', texto)
    # Converte para minúsculas
    texto_limp = texto_limp.lower()
    # Verifica se é palíndromo
    return texto_limp == texto_limp[::-1]

def contar_vogais(texto):
    # Define todas as vogais, incluindo maiúsculas e acentuadas
    vogais = 'aeiouáéíóúâêôãõAEIOUÁÉÍÓÚÂÊÔÃÕ'
    # Conta as vogais
    return sum(1 for char in texto if char in vogais)

# Exemplos de uso
print(eh_palindromo("Anotaram a data da maratona"))  # Deve imprimir True
print(contar_vogais("Anotaram a data da maratona"))  # Deve imprimir 7
```

### Testes Unitários

Para criar testes unitários, você pode usar o módulo `unittest` do Python:

```python
import unittest

class TestTexto(unittest.TestCase):
    def test_eh_palindromo(self):
        self.assertTrue(eh_palindromo("Anotaram a data da maratona"))
        self.assertFalse(eh_palindromo("Python"))

    def test_contar_vogais(self):
        self.assertEqual(contar_vogais("Anotaram a data da maratona"), 7)
        self.assertEqual(contar_vogais("Testando"), 3)

if __name__ == '__main__':
    unittest.main()
```

Este plano e código devem resolver os problemas mencionados e garantir que as funções `eh_palindromo` e `contar_vogais` funcionem conforme especificado.