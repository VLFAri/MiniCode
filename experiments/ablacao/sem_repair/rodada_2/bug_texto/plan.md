### Plano de Desenvolvimento

Baseado na especificação fornecida, o plano para implementar as funções corretamente em `texto.py` é o seguinte:

1. **Preparação do Ambiente de Desenvolvimento:**
   - Certifique-se de ter um ambiente Python configurado.
   - Crie um diretório para o projeto se ainda não existir.
   - Adicione os arquivos necessários ao diretório do projeto.

2. **Implementação da Função `eh_palindromo`:**
   - Abra o arquivo `texto.py`.
   - Implemente a função `eh_palindromo` que ignora maiúsculas/minúsculas, espaços e pontuação.
   - Use métodos de string como `lower()`, `replace()` para remover espaços e pontuação.
   - Compare a string original (limpa) com sua versão invertida para verificar se é um palíndromo.

3. **Implementação da Função `contar_vogais`:**
   - Na mesma janela do arquivo `texto.py`, implemente a função `contar_vogais`.
   - Utilize expressões regulares (`re.findall`) para encontrar todas as vogais, incluindo acentuadas e maiúsculas.
   - Retorne o número total de vogais encontradas.

4. **Criação ou Atualização dos Testes:**
   - No mesmo arquivo `texto.py` ou em um novo arquivo de teste (por exemplo, `test_texto.py`), adicione os casos de teste fornecidos na especificação.
   - Certifique-se de que cada função passe por todos os casos de teste fornecidos.

5. **Execução dos Testes:**
   - Execute os testes para garantir que ambas as funções funcionem conforme esperado.
   - Corrija quaisquer erros encontrados durante a execução dos testes.

6. **Documentação e Revisão:**
   - Adicione comentários ao código para explicar a lógica de cada função.
   - Faça uma revisão final do código para garantir que ele atenda aos requisitos e critérios de aceitação.

### Exemplo de Código

Aqui está um exemplo de como as funções podem ser implementadas:

```python
import re

def eh_palindromo(texto):
    # Remove spaces and punctuation, and converts to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z]', '', texto).lower()
    # Check if the cleaned text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

def contar_vogais(texto):
    # Define a regex pattern for vowels including accented ones
    pattern = r'[aeiouAEIOUáéíóúâêôãõ]'
    # Find all matches of the pattern in the text
    matches = re.findall(pattern, texto)
    # Return the count of matches
    return len(matches)

# Example tests
assert eh_palindromo("Anotaram a data da maratona") == True
assert eh_palindromo("Was it a car or a cat I saw?") == True
assert eh_palindromo("No lemon, no melon") == True

assert contar_vogais("aeiouAEIOUáéíóúâêôãõ") == 20
assert contar_vogais("") == 0
assert contar_vogais("Testando a função") == 6
```

### Passos Finais

7. **Revisar e Comentar o Código:**
   - Adicione comentários ao código para explicar a lógica de cada função.
   - Certifique-se de que o código é fácil de entender e manter.

8. **Commit e Push:**
   - Salve as alterações no arquivo `texto.py`.
   - Commit as mudanças no controle de versão (se estiver usando).
   - Se necessário, push as alterações para o repositório remoto.

Este plano garante que as funções `eh_palindromo` e `contar_vogais` sejam implementadas corretamente e que passem pelos casos de teste fornecidos.