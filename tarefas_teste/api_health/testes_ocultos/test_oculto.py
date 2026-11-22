import app

def test_health():
    assert app.handle("GET", "/health") == (200, {"status": "ok"})

def test_rota_existente_continua():
    status, corpo = app.handle("GET", "/")
    assert status == 200 and "mensagem" in corpo

def test_desconhecida_404():
    assert app.handle("GET", "/nada")[0] == 404

def test_metodo_errado_nao_e_200():
    assert app.handle("POST", "/health")[0] in (404, 405)
