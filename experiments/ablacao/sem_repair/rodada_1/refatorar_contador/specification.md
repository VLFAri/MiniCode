# Specification

## Objective
Refatorar o arquivo `contador.py` para utilizar uma classe `Contador` que encapsula a lógica de contagem. A classe deve incluir os métodos `incrementar(passo=1)`, `valor()` e `zerar()`. Além disso, as funções de módulo `incrementar(passo=1)`, `valor()` e `zerar()` devem continuar funcionando, mas agora delegando a uma instância padrão da classe `Contador`.

## Parameters / Requirements
- **Entrada:** O código deve aceitar parâmetros opcionais para ajustar o passo de incremento.
- **Tipo:** As entradas devem ser números inteiros ou float.
- **Restrições:** 
  - A função `incrementar(passo)` deve aumentar o valor interno do contador em `passo`.
  - A função `valor()` deve retornar o valor atual do contador.
  - A função `zerar()` deve resetar o valor do contador para zero.
  - As funções de módulo devem usar uma instância padrão da classe `Contador`.
  - Instâncias diferentes de `Contador` devem ser independentes entre si.

## Acceptance Criteria
- A classe `Contador` deve ter os métodos `incrementar(passo=1)`, `valor()` e `zerar()`.
- As funções de módulo `incrementar(passo=1)`, `valor()` e `zerar()` devem funcionar corretamente, usando uma instância padrão da classe `Contador`.
- Instâncias diferentes de `Contador` devem manter valores independentes entre si.
- Testes automatizados devem verificar que:
  - A função `incrementar(passo)` aumenta corretamente o valor do contador.
  - A função `valor()` retorna o valor atual do contador.
  - A função `zerar()` reseta corretamente o valor do contador para zero.
  - As funções de módulo usam corretamente uma instância padrão da classe `Contador`.
  - Instâncias diferentes de `Contador` são independentes entre si.