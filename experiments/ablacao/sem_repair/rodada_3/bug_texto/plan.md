### Plano de Desenvolvimento

1. **Analisar o Código Atual**:
   - Abra o arquivo `texto.py` para analisar as funções `eh_palindromo` e `contar_vogais`.
   - Identifique quais partes do código precisam ser corrigidas ou adicionadas.

2. **Corrigir a Função `eh_palindromo`**:
   - Implemente uma função auxiliar para remover espaços e pontuação do texto.
   - Converta todo o texto para minúsculas para garantir a insensibilidade ao caso.
   - Verifique se o texto limpo é igual ao seu reverso para determinar se é um palíndromo.

3. **Corrigir a Função `contar_vogais`**:
   - Crie uma lista de todas as vogais, incluindo as maiúsculas e acentuadas.
   - Percorra cada caractere do texto e verifique se ele está na lista de vogais.
   - Conte e retorne o número de vogais encontradas.

4. **Implementar Testes Unitários**:
   - Adicione os testes fornecidos (`test_eh_palindromo` e `test_contar_vogais`) ao arquivo `texto.py`.
   - Certifique-se de que os testes estão sendo executados corretamente.

5. **Executar Testes e Corrigir Bugs**:
   - Execute os testes unitários para verificar se as funções funcionam conforme esperado.
   - Corrija quaisquer bugs identificados durante a execução dos testes.

6. **Documentar as Alterações**:
   - Adicione comentários ao código explicando as mudanças feitas.
   - Documente as funções `eh_palindromo` e `contar_vogais` para clareza.

7. **Revisar e Confirmar**:
   - Revisar o código para garantir que ele atenda aos requisitos e critérios de aceitação.
   - Confirmar que ambos os testes passam sem erros.

### Implementação Detalhada

#### 1. Análise do Código Atual
- Examine o código existente em `texto.py` para entender como as funções estão implementadas atualmente.

#### 2. Correção da Função `eh_palindromo`
```python
import re

def eh_palindromo(texto):
    # Remove espaços e pontuação e converte para minúsculas
    cleaned_text = re.sub(r'[^a-zA-Z]', '', texto).lower()
    # Verifica se o texto limpo é igual ao seu reverso
    return cleaned_text == cleaned_text[::-1]
```

#### 3. Correção da Função `contar_vogais`
```python
def contar_vogais(texto):
    # Lista de todas as vogais, incluindo maiúsculas e acentuadas
    vogais = "aeiouAEIOUáéíóúâêôãõ"
    # Conta o número de vogais no texto
    return sum(1 for char in texto if char in vogais)
```

#### 4. Implementação de Testes Unitários
```python
def test_eh_palindromo():
    assert eh_palindromo("Anotaram a data da maratona") == True
    assert eh_palindromo("Was it a car or a cat I saw?") == True
    assert eh_palindromo("No lemon, no melon") == True
    assert eh_palindromo("Hello World!") == False

def test_contar_vogais():
    assert contar_vogais("aeiouAEIOUáéíóúâêôãõ") == 20
    assert contar_vogais("Python Programming") == 4
```

#### 5. Executar Testes e Corrigir Bugs
- Execute os testes unitários para verificar a funcionalidade das funções.
- Corrija quaisquer problemas identificados.

#### 6. Documentar as Alterações
- Adicione comentários explicativos ao código.
- Documente as funções para clareza.

#### 7. Revisão e Confirmação
- Revisar o código para garantir que ele atende aos requisitos.
- Confirmar que todos os testes passam sem erros.

Este plano fornece uma estrutura clara para a correção e teste das funções `eh_palindromo` e `contar_vogais`.