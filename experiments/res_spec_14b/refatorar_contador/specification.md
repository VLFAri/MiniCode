# Specification

## Objective
Refatorar o arquivo `contador.py` para utilizar uma classe `Contador` que encapsula a lógica de contagem. A refatoração deve manter as funcionalidades existentes do módulo, mas agora utilizando métodos de uma instância da classe `Contador`. Além disso, deve permitir a criação de múltiplas instâncias independentes da classe `Contador`.

## Parameters / Requirements
- **Entrada:** O código deve aceitar parâmetros opcionais para o passo de incremento.
- **Tipo:** Todos os métodos devem retornar valores do tipo inteiro.
- **Restrições:** As instâncias da classe `Contador` devem ser independentes entre si.
- **Regras de Negócio:** 
  - A função `incrementar(passo=1)` deve incrementar o valor interno do objeto `Contador`.
  - A função `valor()` deve retornar o valor atual do objeto `Contador`.
  - A função `zerar()` deve resetar o valor do objeto `Contador` para zero.

## Acceptance Criteria
- Deve ser possível criar múltiplas instâncias da classe `Contador`, cada uma independente das outras.
- As funções de módulo `incrementar(passo=1)`, `valor()`, e `zerar()` devem funcionar corretamente, delegando a uma instância padrão do módulo.
- Os métodos da classe `Contador` devem passar nos seguintes testes automatizados:
  - Incrementar o valor de uma instância da classe `Contador` usando o método `incrementar(passo=1)`.
  - Verificar se o valor retornado pelo método `valor()` é correto após a chamada ao método `incrementar(passo=1)`.
  - Resetar o valor de uma instância da classe `Contador` para zero usando o método `zerar()`.
  - Verificar se o valor retornado pelo método `valor()` é zero após a chamada ao método `zerar()`.
  - Verificar se duas instâncias diferentes da classe `Contador` podem ter valores diferentes independentemente uma da outra.