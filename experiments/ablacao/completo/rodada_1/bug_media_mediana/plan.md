Baseado na especificação e nos arquivos do projeto fornecidos, aqui está um plano passo a passo de como implementar as correções necessárias:

### Plano de Implementação

1. **Verificar o estado atual das funções**:
   - Abra o arquivo `estatistica.py` e examine as funções `media()` e `mediana()`.
   - Identifique quais partes dessas funções precisam ser corrigidas ou adicionadas.

2. **Implementar a verificação de lista vazia**:
   - Para ambas as funções (`media()` e `mediana()`), adicione uma verificação no início da função para verificar se a lista é vazia.
   - Se a lista estiver vazia, lance um `ValueError`.

3. **Corrigir a função `media()`**:
   - Certifique-se de que a função `media()` calcula corretamente a média dos números na lista.
   - Use a fórmula padrão para calcular a média: soma de todos os elementos dividido pelo número de elementos.
   - Garanta que a lista original não seja modificada durante a execução da função.

4. **Corrigir a função `mediana()`**:
   - Certifique-se de que a função `mediana()` calcula corretamente a mediana dos números na lista.
   - Implemente a lógica para ordenar a lista temporariamente sem modificar a lista original.
   - Se o tamanho da lista for ímpar, retorne o elemento central.
   - Se o tamanho da lista for par, retorne a média dos dois elementos centrais.

5. **Criar ou atualizar os testes**:
   - Crie ou atualize os casos de teste para as funções `media()` e `mediana()`.
   - Teste com listas vazias para garantir que um `ValueError` é lançado.
   - Teste com listas preenchidas para garantir que as médias e medianas são calculadas corretamente.
   - Verifique que a lista original não é modificada após a execução das funções.

6. **Executar os testes**:
   - Execute os testes automatizados para garantir que todas as condições de aceitação são atendidas.
   - Corrija quaisquer falhas encontradas nos testes.

7. **Documentar as mudanças**:
   - Documente quaisquer mudanças significativas feitas nas funções `media()` e `mediana()`.
   - Certifique-se de que a documentação reflete corretamente o comportamento atual das funções.

8. **Validação final**:
   - Revisite o código para garantir que ele atende aos requisitos especificados.
   - Certifique-se de que o código é limpo e fácil de entender.

Este plano deve guiar você através da implementação das correções necessárias para as funções `media()` e `mediana()` no módulo `estatistica.py`.