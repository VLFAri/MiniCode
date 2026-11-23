# Specification

## Objective
O objetivo deste projeto é criar uma calculadora simples que permita realizar operações básicas como soma, subtração e divisão. A divisão por zero deve ser tratada como uma exceção.

## Parameters / Requirements
- O programa deve ter as seguintes funções:
  - `somar(a, b)`: Recebe dois números e retorna a soma desses números.
  - `subtrair(a, b)`: Recebe dois números e retorna a diferença entre eles.
  - `dividir(a, b)`: Recebe dois números e retorna a divisão de a por b. Se b for zero, deve lançar uma exceção ZeroDivisionError.

- As funções devem retornar valores float ou int conforme necessário.

- Os parâmetros das funções devem ser obrigatórios e devem ser do tipo float ou int.

- A função `dividir` deve verificar se o segundo parâmetro é zero antes de tentar dividir.

## Acceptance Criteria
1. A função `somar(a, b)` deve retornar a soma correta dos dois números.
2. A função `subtrair(a, b)` deve retornar a diferença correta dos dois números.
3. A função `dividir(a, b)` deve retornar a divisão correta dos dois números quando b não é zero.
4. A função `dividir(a, b)` deve lançar uma exceção ZeroDivisionError quando b é zero.
5. Todas as funções devem funcionar corretamente com os dados fornecidos.

## Arquivos do projeto
- **calculadora.py**: Contém as implementações das funções da calculadora.
- **tests/test_calculadora.py**: Contém os testes para as funções da calculadora.

### Calculadora.py
```python
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero")
    return a / b
```

### tests/test_calculadora.py
```python
import pytest

def test_somar():
    assert somar(2, 3) == 5
    assert somar(-1, 1) == 0
    assert somar(0, 0) == 0

def test_subtrair():
    assert subtrair(5, 3) == 2
    assert subtrair(-2, -2) == 0
    assert subtrair(0, 0) == 0

def test_dividir():
    assert dividir(10, 2) == 5
    assert dividir(7, 3) == 2.3333333333333335
    with pytest.raises(ZeroDivisionError):
        dividir(10, 0)
```
Este projeto segue o padrão de Spec-Driven Development, onde a especificação é escrita em forma de documentação e testes são criados para garantir que a implementação atenda aos requisitos.