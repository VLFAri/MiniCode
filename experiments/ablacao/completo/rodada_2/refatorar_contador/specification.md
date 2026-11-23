# Specification

## Objective
Refatorar o arquivo `contador.py` para utilizar uma classe chamada `Contador`. A classe deve conter os métodos `incrementar(passo=1)`, `valor()` e `zerar()`. Além disso, as funções de módulo `incrementar(passo=1)`, `valor()` e `zerar()` devem continuar funcionando, mas agora delegando suas operações para uma instância padrão da classe `Contador`. Instâncias diferentes da classe `Contador` devem ser independentes entre si.

## Parameters / Requirements
- **Entradas**: 
  - O método `incrementar(passo)` recebe um parâmetro opcional `passo` que é um número inteiro.
- **Tipos**:
  - A classe `Contador` deve ter um atributo interno que armazena o valor atual do contador.
  - As funções de módulo devem usar uma instância padrão da classe `Contador`.
- **Restrições**:
  - A instância padrão da classe `Contador` deve ser única no módulo.
  - Cada instância da classe `Contador` deve manter seu próprio estado independente das outras instâncias.
- **Regras de Negócio**:
  - O método `incrementar(passo)` deve aumentar o valor do contador em `passo`.
  - O método `valor()` deve retornar o valor atual do contador.
  - O método `zerar()` deve resetar o valor do contador para zero.

## Acceptance Criteria
- **Teste de Incremento**:
  - Dado uma instância da classe `Contador`, quando o método `incrementar(passo)` for chamado com um valor específico, então o valor retornado pelo método `valor()` deve corresponder ao valor inicial mais o passo fornecido.
- **Teste de Valor**:
  - Dado uma instância da classe `Contador`, quando o método `valor()` for chamado, então ele deve retornar o valor atual do contador.
- **Teste de Zeramento**:
  - Dado uma instância da classe `Contador`, quando o método `zerar()` for chamado, então o valor retornado pelo método `valor()` deve ser zero.
- **Teste de Independência de Instâncias**:
  - Dado duas instâncias diferentes da classe `Contador`, quando cada uma chama seus respectivos métodos `incrementar(passo)`, `valor()` e `zerar()`, então cada instância deve manter seu próprio estado independente da outra.
- **Teste de Funções de Módulo**:
  - Dado a função `incrementar(passo)` do módulo, quando ela for chamada, então ela deve incrementar o valor da instância padrão da classe `Contador`.
  - Dado a função `valor()` do módulo, quando ela for chamada, então ela deve retornar o valor atual da instância padrão da classe `Contador`.
  - Dado a função `zerar()` do módulo, quando ela for chamada, então ela deve resetar o valor da instância padrão da classe `Contador` para zero.