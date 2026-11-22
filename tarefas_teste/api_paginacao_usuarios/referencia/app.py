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


USUARIOS = [{"id": i, "nome": f"usuario{i}"} for i in range(1, 51)]


def _inteiro(valor, nome, padrao, maximo=None):
    if valor is None:
        return padrao
    try:
        numero = int(valor)
    except (TypeError, ValueError):
        raise ValueError(f"{nome} deve ser um inteiro")
    if numero < 1 or (maximo is not None and numero > maximo):
        raise ValueError(f"{nome} fora do intervalo permitido")
    return numero


@rota("GET", "/users")
def listar_usuarios(query):
    try:
        page = _inteiro(query.get("page"), "page", 1)
        page_size = _inteiro(query.get("page_size"), "page_size", 20, maximo=100)
    except ValueError as erro:
        return 400, {"erro": str(erro)}
    inicio = (page - 1) * page_size
    return 200, {"page": page, "page_size": page_size, "total": len(USUARIOS),
                 "items": USUARIOS[inicio:inicio + page_size]}
