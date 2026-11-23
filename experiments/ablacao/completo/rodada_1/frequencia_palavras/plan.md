Baseado na especificação fornecida e considerando que o projeto está vazio, podemos criar um plano passo a passo para implementar a função `frequencia_palavras(texto)` no módulo `palavras.py`. Além disso, incluiremos a criação de testes automatizados para garantir a qualidade da implementação.

### Plano de Implementação

1. **Criar o arquivo `palavras.py`:**
   - Crie um novo arquivo chamado `palavras.py` no diretório do projeto.

2. **Implementar a função `frequencia_palavras(texto)` em `palavras.py`:**
   - Defina a função `frequencia_palavras(texto)` dentro do arquivo `palavras.py`.
   - A função deve receber uma única string como parâmetro (`texto`).
   - Use expressões regulares para remover pontuação do texto.
   - Converta todas as palavras para minúsculas.
   - Utilize um dicionário para contar a frequência de cada palavra.
   - Retorne o dicionário com as contagens de palavras.

3. **Testar a função com casos de teste:**
   - Crie um conjunto de casos de teste para verificar se a função funciona corretamente.
   - Teste com textos vazios, textos normais, textos com pontuação e caracteres especiais.

4. **Escrever testes automatizados usando pytest:**
   - Instale o pytest se ainda não estiver instalado (`pip install pytest`).
   - Crie um arquivo `test_palavras.py` para os testes automatizados.
   - Escreva funções de teste para cobrir todos os casos de uso da função `frequencia_palavras`.

5. **Executar os testes automatizados:**
   - Execute os testes usando o comando `pytest` para garantir que a função funcione conforme esperado.

### Código de Exemplo

Aqui está um exemplo básico de como o código poderia ser implementado:

```python
import re
from collections import Counter

def frequencia_palavras(texto):
    # Remove pontuação e converte tudo para minúsculas
    palavras = re.findall(r'\b\w+\b', texto.lower())
    
    # Conta a frequência de cada palavra
    contador = Counter(palavras)
    
    return dict(contador)
```

### Arquivo de Testes Automatizados

E aqui está um exemplo de como os testes automatizados podem ser escritos:

```python
import pytest
from palavras import frequencia_palavras

def test_frequencia_palavras_vazio():
    assert frequencia_palavras("") == {}

def test_frequencia_palavras_normal():
    resultado = frequencia_palavras("Olá Mundo")
    assert resultado == {"olá": 1, "mundo": 1}

def test_frequencia_palavras_com_pontuacao():
    resultado = frequencia_palavras("Olá, Mundo!")
    assert resultado == {"olá": 1, "mundo": 1}

def test_frequencia_palavras_com_caracteres_especiais():
    resultado = frequencia_palavras("Olá! Mundo?")
    assert resultado == {"olá": 1, "mundo": 1}
```

### Executando os Testes

Para executar os testes, você pode usar o seguinte comando no terminal:

```bash
pytest
```

Este comando irá rodar todos os testes definidos no arquivo `test_palavras.py` e fornecerá relatórios sobre quais testes passaram ou falharam.

### Conclusão

Este plano fornece uma estrutura clara para implementar a função `frequencia_palavras(texto)` e garantir sua qualidade através de testes automatizados.