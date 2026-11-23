### Plano de Desenvolvimento

1. **Análise das Funções Atuais**
   - Abra o arquivo `texto.py`.
   - Analise as funções `eh_palindromo` e `contar_vogais` para entender como elas estão implementadas atualmente.

2. **Implementação da Função `eh_palindromo`**
   - Crie uma nova função `eh_palindromo` que ignora a case, espaços e pontuação.
   - Use métodos de string Python para normalizar a entrada (converter tudo para minúsculas, remover espaços e pontuação).
   - Implemente a lógica para verificar se a string é um palíndromo após a normalização.

3. **Implementação da Função `contar_vogais`**
   - Crie uma nova função `contar_vogais` que conta todas as vogais, incluindo as com acentos.
   - Utilize expressões regulares para contar todas as ocorrências de vogais na string.
   - Certifique-se de incluir todas as vogais listadas nas restrições.

4. **Testes Unitários**
   - Crie ou atualize os testes unitários para ambas as funções.
   - Para `eh_palindromo`, teste com casos que incluem letras maiúsculas/minúsculas, espaços e pontuação.
   - Para `contar_vogais`, teste com strings que contêm vogais normais e com acentos.

5. **Execução dos Testes**
   - Execute os testes unitários para garantir que ambas as funções funcionam conforme esperado.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

6. **Documentação**
   - Adicione comentários ao código para documentar as mudanças feitas.
   - Certifique-se de que a documentação reflete corretamente as funcionalidades das funções.

7. **Revisão Final**
   - Revisite o código para garantir que ele está de acordo com as especificações.
   - Faça ajustes finais se necessário.

### Detalhes do Código

#### Função `eh_palindromo`

```python
import re

def eh_palindromo(texto):
    # Remove espaços e pontuação e converte para minúsculas
    texto = re.sub(r'[^a-zA-Z]', '', texto).lower()
    
    # Verifica se a string é um palíndromo
    return texto == texto[::-1]
```

#### Função `contar_vogais`

```python
def contar_vogais(texto):
    # Define a regex para encontrar todas as vogais
    vogais = r'[aeiouAEIOUáéíóúâêîôû]'
    return len(re.findall(vogais, texto))
```

### Testes Unitários

#### Teste para `eh_palindromo`

```python
def test_eh_palindromo():
    assert eh_palindromo("Anotaram a data da maratona") == True
    assert eh_palindromo("Was it a car or a cat I saw?") == True
    assert eh_palindromo("No lemon, no melon") == True
    assert eh_palindromo("Hello World!") == False
```

#### Teste para `contar_vogais`

```python
def test_contar_vogais():
    assert contar_vogais("Árvore") == 3
    assert contar_vogais("Abacaxi") == 4
    assert contar_vogais("Saudável") == 5
    assert contar_vogais("Café") == 2
```

### Execução dos Testes

```python
if __name__ == "__main__":
    test_eh_palindromo()
    test_contar_vogais()
    print("Todos os testes passaram!")
```

Este plano detalha os passos necessários para implementar as funções corretamente e garantir que elas atendam aos requisitos especificados.