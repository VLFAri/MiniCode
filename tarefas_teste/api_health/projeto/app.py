"""Mini roteador HTTP em memória (sem frameworks): cada rota recebe o dicionário `query` e devolve (status, corpo)."""
ROTAS = {}


def rota(metodo, caminho):
    def decorador(funcao):
        ROTAS[(metodo, caminho)] = funcao
        return funcao
    return decorador


def handle(metodo, caminho, query=None):
    funcao = ROTAS.get((metodo, caminho))
    if funcao is None:
        return 404, {"erro": "não encontrado"}
    return funcao(query or {})


@rota("GET", "/")
def raiz(query):
    return 200, {"mensagem": "bem-vindo"}
