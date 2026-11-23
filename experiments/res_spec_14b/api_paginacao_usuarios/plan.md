Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo para implementar a paginação na rota GET `/users`:

### Plano de Implementação

1. **Validação dos Parâmetros de Entrada**
   - Adicionar validações para os parâmetros `page` e `page_size` no início da função que lida com a rota GET `/users`.
   - Certificar-se de que ambos os parâmetros sejam convertidos para inteiros, caso sejam fornecidos como strings.
   - Verificar se `page` é um número inteiro positivo.
   - Verificar se `page_size` é um número inteiro positivo e não excede 100.
   - Retornar um status HTTP 400 Bad Request com uma mensagem de erro específica se qualquer um dos parâmetros estiver fora dos limites permitidos.

2. **Definição das Variáveis de Páginação**
   - Definir variáveis padrão para `page` e `page_size` dentro da função.
   - Usar essas variáveis padrão se nenhum valor for fornecido para `page` e `page_size`.

3. **Cálculo do Índice Inicial e Final**
   - Calcular o índice inicial (`start_index`) usando a fórmula `start_index = (page - 1) * page_size`.
   - Calcular o índice final (`end_index`) usando a fórmula `end_index = start_index + page_size`.

4. **Obtenção dos Dados de Usuários**
   - Obter a lista completa de usuários.
   - Filtrar a lista de usuários para incluir apenas aqueles que estão dentro do intervalo definido por `start_index` e `end_index`.

5. **Montagem da Resposta**
   - Montar a resposta em formato JSON contendo os campos necessários: `"page"`, `"page_size"`, `"total"` e `"items"`.
   - `"total"` deve representar o total de usuários disponíveis.
   - `"items"` deve conter a lista filtrada de usuários.

6. **Retorno da Resposta**
   - Retornar a resposta montada em formato JSON.

### Criação ou Atualização dos Testes

7. **Teste de Validação de Parâmetros**
   - Escrever testes unitários para validar que a função retorna um status HTTP 400 Bad Request quando `page` ou `page_size` são inválidos.
   - Testar entradas inválidas como strings não numéricas, números negativos, e `page_size` maior que 100.

8. **Teste de Funcionalidade**
   - Escrever testes para verificar se a função retorna os dados corretos quando `page` e `page_size` são válidos.
   - Testar diferentes combinações de `page` e `page_size` para garantir que a paginação funcione corretamente.
   - Testar se o campo `"total"` reflete corretamente o número total de usuários disponíveis.

9. **Teste de Limites**
   - Escrever testes para verificar o comportamento da função quando `page_size` é igual ao limite superior (100).
   - Testar se a função funciona corretamente quando `page` é 1 e `page_size` é 100.

10. **Teste de Casos Especiais**
    - Escrever testes para verificar se a função retorna os dados corretos quando nenhum valor é fornecido para `page` e `page_size`.
    - Testar se a função retorna os dados corretos quando `page` é 1 e `page_size` é o padrão (20).

Este plano fornece uma estrutura clara para implementar a paginação na rota GET `/users` e também define os testes necessários para garantir que a implementação atenda aos requisitos especificados.