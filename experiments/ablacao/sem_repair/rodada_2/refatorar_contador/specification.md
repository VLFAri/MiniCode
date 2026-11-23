# Specification

## Objective
Refatorar o arquivo `contador.py` para utilizar uma classe `Contador` que encapsula a lógica de contagem. A refatoração deve manter as funcionalidades existentes do módulo, mas agora utilizando métodos da classe `Contador`. Além disso, deve-se garantir que diferentes instâncias da classe `Contador` sejam independentes entre si.

## Parameters / Requirements
- **Entrada:** O código deve aceitar parâmetros opcionais para incrementar, zerar e obter o valor atual do contador.
- **Tipo:** A classe `Contador` deve ter os seguintes métodos:
  - `incrementar(passo=1)`: Incrementa o valor do contador em `passo`.
  - `valor()`: Retorna o valor atual do contador.
  - `zerar()`: Zera o valor do contador.
- **Restrições:** 
  - A implementação deve manter as funções de módulo (`incrementar`, `valor`, `zerar`) funcionando, mas agora delegando a uma instância padrão da classe `Contador`.
  - Diferentes instâncias da classe `Contador` devem ser independentes entre si.
- **Regras de Negócio:** 
  - A função `incrementar` deve poder ser chamada sem argumentos, incrementando o contador em 1.
  - A função `valor` deve retornar o valor atual do contador.
  - A função `zerar` deve resetar o valor do contador para zero.

## Acceptance Criteria
- **Teste 1:** A função `incrementar()` deve incrementar o valor do contador em 1 quando chamada sem argumentos.
- **Teste 2:** A função `incrementar(passo)` deve incrementar o valor do contador em `passo` quando chamada com um argumento.
- **Teste 3:** A função `valor()` deve retornar o valor atual do contador.
- **Teste 4:** A função `zerar()` deve resetar o valor do contador para zero.
- **Teste 5:** Duas instâncias diferentes da classe `Contador` devem ser independentes entre si, ou seja, incrementar um contador não deve afetar o outro.
- **Teste 6:** As funções de módulo (`incrementar`, `valor`, `zerar`) devem funcionar corretamente, delegando a uma instância padrão da classe `Contador`.

Essa especificação fornece uma estrutura clara para a refatoração do arquivo `contador.py`, garantindo que todas as funcionalidades existentes sejam mantidas e que novas instâncias da classe `Contador` sejam independentes entre si.