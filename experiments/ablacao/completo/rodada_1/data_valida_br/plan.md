Baseado na especificação fornecida, aqui está um plano numerado de como implementar o script `datas_br.py` em Python:

### Plano de Implementação

1. **Criação do Arquivo `datas_br.py`**
   - Crie um novo arquivo chamado `datas_br.py`.

2. **Importação de Módulos Necessários**
   - Importe os módulos necessários para manipulação de datas e testes unitários.
     ```python
     import re
     from datetime import datetime
     ```

3. **Definição da Função `eh_data_valida(texto)`**
   - Defina a função `eh_data_valida(texto)` que recebe uma única string `texto` e retorna `True` se a data for válida no formato `dd/mm/yyyy`, considerando anos bissextos, e `False` caso contrário.
     ```python
     def eh_data_valida(texto):
         # Lógica da função aqui
         pass
     ```

4. **Validação do Formato da Data**
   - Use uma expressão regular para validar o formato da data.
     ```python
     pattern = r'^([0-2]\d|3[01])/(0\d|1[012])/\d{4}$'
     match = re.match(pattern, texto)
     if not match:
         return False
     ```

5. **Separação das Partes da Data**
   - Separe a string em dia, mês e ano.
     ```python
     dia, mes, ano = map(int, texto.split('/'))
     ```

6. **Verificação das Restrições de Valores**
   - Verifique se o dia está entre 1 e 31, o mês entre 1 e 12, e o ano dentro de um intervalo razoável (por exemplo, 1900 a 2100).
     ```python
     if not (1 <= dia <= 31) or not (1 <= mes <= 12) or not (1900 <= ano <= 2100):
         return False
     ```

7. **Verificação de Ano Bissexto**
   - Verifique se o ano é bissexto para fevereiro ter 29 dias.
     ```python
     def is_leap_year(year):
         return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
     ```

8. **Verificação do Número de Dias por Mês**
   - Verifique se o número de dias é válido para cada mês, incluindo meses com 31 dias e fevereiro em anos bissextos.
     ```python
     if mes in [4, 6, 9, 11] and dia > 30:
         return False
     elif mes == 2 and dia > 29:
         return False
     elif mes == 2 and dia == 29 and not is_leap_year(ano):
         return False
     ```

9. **Teste de Data Efetiva**
   - Use a biblioteca `datetime` para verificar se a data é efetivamente válida.
     ```python
     try:
         datetime.strptime(texto, '%d/%m/%Y')
     except ValueError:
         return False
     else:
         return True
     ```

10. **Documentação da Função**
    - Adicione comentários explicativos à função para documentar a lógica utilizada.

11. **Criação de Testes Unitários**
    - Crie um arquivo de teste `test_datas_br.py` para escrever casos de teste.
      ```python
      import unittest
      from datas_br import eh_data_valida
      
      class TestDateValidation(unittest.TestCase):
          def test_valid_dates(self):
              self.assertTrue(eh_data_valida('01/01/2023'))
              self.assertTrue(eh_data_valida('29/02/2020'))
              
              # Adicionar mais casos de teste válidos aqui
              
          def test_invalid_dates(self):
              self.assertFalse(eh_data_valida('32/01/2023'))
              self.assertFalse(eh_data_valida('01/13/2023'))
              
              # Adicionar mais casos de teste inválidos aqui
              
      if __name__ == '__main__':
          unittest.main()
      ```

12. **Execução dos Testes**
    - Execute os testes unitários para garantir que a função `eh_data_valida(texto)` funcione corretamente em todas as condições possíveis.

Este plano fornece uma estrutura clara para implementar a função desejada e garantir sua correção através de testes abrangentes.