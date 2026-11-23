Baseado nas especificações fornecidas, aqui está um plano passo a passo para implementar a função `mesclar_intervalos` conforme solicitado:

### Passo 1: Criar o arquivo `intervalos.py`
Crie um novo arquivo chamado `intervalos.py` no diretório do seu projeto.

### Passo 2: Implementar a função `mesclar_intervalos`
Implemente a função `mesclar_intervalos` dentro do arquivo `intervalos.py`. Esta função deve receber uma lista de tuplas `(inicio, fim)` e retornar uma lista de tuplas ordenadas com os intervalos mesclados corretamente.

#### Estrutura da função:
1. **Ordenar a lista de entrada**: Antes de começar a mesclar os intervalos, certifique-se de que a lista esteja ordenada com base no início de cada intervalo.
2. **Mesclar os intervalos**: Percorra a lista ordenada e combine os intervalos que se sobrepõem ou se tocam.
3. **Retornar a lista final**: Após a iteração completa, retorne a lista de intervalos mesclados.

### Passo 3: Escrever testes unitários
Escreva testes unitários para garantir que a função `mesclar_intervalos` funcione corretamente em diferentes cenários.

#### Testes a serem considerados:
- Teste com uma lista vazia.
- Teste com uma lista contendo apenas um intervalo.
- Teste com uma lista contendo múltiplos intervalos que não se sobrepõem.
- Teste com uma lista contendo intervalos que se sobrepõem.
- Teste com uma lista contendo intervalos que se tocam mas não se sobrepõem.

### Passo 4: Executar os testes
Execute os testes unitários para verificar se a função `mesclar_intervalos` está funcionando conforme esperado.

Aqui está um exemplo básico de como a função e os testes podem ser implementados:

```python
def mesclar_intervalos(intervalos):
    # Ordena os intervalos com base no início de cada intervalo
    intervalos.sort(key=lambda x: x[0])
    
    # Lista para armazenar os intervalos mesclados
    mesclados = []
    
    for intervalo in intervalos:
        # Se a lista de mesclados estiver vazia ou o último intervalo não se sobrepõe com o atual
        if not mesclados or mesclados[-1][1] < intervalo[0]:
            mesclados.append(intervalo)
        else:
            # Se o último intervalo se sobrepõe com o atual, mescla-os
            mesclados[-1] = (mesclados[-1][0], max(mesclados[-1][1], intervalo[1]))
    
    return mesclados

# Testes
import unittest

class TestMesclarIntervalos(unittest.TestCase):
    def test_vazio(self):
        self.assertEqual(mesclar_intervalos([]), [])
    
    def test_um_intervalo(self):
        self.assertEqual(mesclar_intervalos([(1, 3)]), [(1, 3)])
    
    def test_sem_sobreporencia(self):
        self.assertEqual(mesclar_intervalos([(1, 3), (5, 7)]), [(1, 3), (5, 7)])
    
    def test_com_sobreporencia(self):
        self.assertEqual(mesclar_intervalos([(1, 4), (3, 5)]), [(1, 5)])
    
    def test_com_tocamento(self):
        self.assertEqual(mesclar_intervalos([(1, 2), (2, 6), (8, 10)]), [(1, 6), (8, 10)])

if __name__ == "__main__":
    unittest.main()
```

Este código inclui a implementação da função `mesclar_intervalos` e um conjunto de testes unitários para validar sua funcionalidade. Certifique-se de executar os testes após a implementação da função para garantir que tudo esteja funcionando conforme o esperado.