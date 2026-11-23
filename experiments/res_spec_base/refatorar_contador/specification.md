# Specification

## Objective
O objetivo deste projeto é refatorar o arquivo `contador.py` para criar uma classe chamada `Contador`. Esta classe deve implementar três métodos principais: `incrementar`, `valor`, e `zerar`. Além disso, a classe deve manter as funções de módulo `incrementar`, `valor`, e `zerar` funcionando corretamente, delegando a uma instância padrão do módulo.

## Parameters / Requirements
### Input/Output
- O método `incrementar` aceita um parâmetro opcional chamado `passo`, que indica quantos passos o contador deve aumentar. Se não for fornecido, o contador deve aumentar em 1.
- O método `valor` retorna o valor atual do contador.
- O método `zerar` redefine o valor do contador para zero.

### Constraints and Rules of Business
- O valor do contador deve ser sempre um número inteiro positivo ou zero.
- A função `incrementar` deve ser thread-safe, garantindo que várias threads possam incrementar o contador simultaneamente sem interferência.

### Acceptance Criteria
- Os testes unitários devem verificar se o método `incrementar` funciona corretamente com diferentes valores de `passo`.
- Os testes unitários devem verificar se o método `valor` retorna o valor correto.
- Os testes unitários devem verificar se o método `zerar` redefine o valor do contador para zero.
- Os testes unitários devem verificar se a função `incrementar` é thread-safe.

## Arquivos do projeto
- **contador.py**: Este arquivo contém a implementação da classe `Contador`.

### Pedido do Utilizador
Refatore contador.py (que usa uma variável global): crie a classe Contador com os métodos incrementar(passo=1), valor() e zerar(), e mantenha as funções de módulo incrementar(passo=1), valor() e zerar() funcionando, delegando a uma instância padrão do módulo. Instâncias diferentes de Contador devem ser independentes.

---

**Observações:**  
- Certifique-se de que todas as funções de módulo (`incrementar`, `valor`, e `zerar`) estão funcionando corretamente antes de iniciar o processo de refatoração.
- Use a linguagem Python para implementar a classe `Contador` e seus métodos.
- Garanta que a classe seja thread-safe para suportar múltiplas threads.
- Implemente os testes unitários para validar a funcionalidade do código.