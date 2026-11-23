Baseado na especificação fornecida e nos arquivos do projeto, segue um plano passo a passo para criar os casos de teste usando o pytest framework:

### Plano de Criação de Casos de Teste

1. **Instalação do Pytest**
   - Certifique-se de que o pytest esteja instalado no ambiente de desenvolvimento. Se não estiver, instale-o usando pip:
     ```bash
     pip install pytest
     ```

2. **Criação da Estrutura de Diretórios**
   - Verifique se há uma estrutura de diretórios adequada para os testes. Deve haver um diretório chamado `tests` onde os arquivos de teste serão colocados.
     ```bash
     mkdir -p tests
     ```

3. **Criação do Arquivo de Testes**
   - Crie o arquivo `test_calculadora.py` dentro do diretório `tests`:
     ```bash
     touch tests/test_calculadora.py
     ```

4. **Importação das Funções da Calculadora**
   - No arquivo `test_calculadora.py`, importe as funções `somar`, `subtrair`, e `dividir` do módulo `calculadora.py`.
     ```python
     from calculadora import somar, subtrair, dividir
     ```

5. **Definição dos Casos de Teste**
   - Defina os casos de teste para cada função. Use a sintaxe do pytest para definir os testes.

6. **Teste da Função `somar`**
   - Adicione testes para a função `somar` que cubram diferentes cenários, como números inteiros e floats.
     ```python
     def test_somar():
         assert somar(1, 2) == 3
         assert somar(-1, 1) == 0
         assert somar(1.5, 2.5) == 4.0
     ```

7. **Teste da Função `subtrair`**
   - Adicione testes para a função `subtrair` que cubram diferentes cenários, incluindo números negativos.
     ```python
     def test_subtrair():
         assert subtrair(5, 3) == 2
         assert subtrair(10, 10) == 0
         assert subtrair(3.5, 1.5) == 2.0
     ```

8. **Teste da Função `dividir`**
   - Adicione testes para a função `dividir` que cubram diferentes cenários, incluindo divisão por zero.
     ```python
     def test_dividir():
         assert dividir(10, 2) == 5
         assert dividir(9.0, 3.0) == 3.0
         # Teste para divisão por zero
         with pytest.raises(ZeroDivisionError):
             dividir(1, 0)
     ```

9. **Verificação da Instalação do Pytest**
   - Certifique-se de que o pytest está instalado corretamente e que você pode executar os testes sem erros.
     ```bash
     pytest
     ```

10. **Execução dos Testes**
    - Execute todos os testes para garantir que eles passem e que todas as funções estão funcionando conforme esperado.
      ```bash
      pytest tests/test_calculadora.py
      ```

### Código Completo do Arquivo `test_calculadora.py`
```python
import pytest
from calculadora import somar, subtrair, dividir

def test_somar():
    assert somar(1, 2) == 3
    assert somar(-1, 1) == 0
    assert somar(1.5, 2.5) == 4.0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(10, 10) == 0
    assert subtrair(3.5, 1.5) == 2.0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(9.0, 3.0) == 3.0
    # Teste para divisão por zero
    with pytest.raises(ZeroDivisionError):
        dividir(1, 0)
```

Este plano cobre a criação de casos de teste para as funções `somar`, `subtrair`, e `dividir` em `calculadora.py`, incluindo a verificação de divisão por zero sem modificar o código original.