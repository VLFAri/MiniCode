import json
import urllib.error

import pytest
from src.modelo import cliente_llm
from src.modelo.cliente_llm import LLMClient, URL_LOCAL_PADRAO, URL_PADRAO, escolher_modelo_qwen, listar_modelos

VARS = ("MINICODE_BACKEND", "MINICODE_BASE_URL", "MINICODE_MODEL", "MINICODE_API_KEY", "TOKEN")


class OpenAIFalso:
    ultimo = None

    def __init__(self, **kw):
        self.kw = kw
        OpenAIFalso.ultimo = self


@pytest.fixture
def ambiente(monkeypatch):
    for v in VARS:
        monkeypatch.delenv(v, raising=False)
    monkeypatch.setattr(cliente_llm, "load_dotenv", lambda: None)     # um .env real não pode interferir
    monkeypatch.setattr(cliente_llm, "OpenAI", OpenAIFalso)
    return monkeypatch


def test_escolhe_o_maior_qwen_instalado():
    instalados = ["llama3:8b", "qwen2.5-coder:1.5b-instruct", "qwen2.5-coder:7b", "qwen2.5:14b-instruct-q4_K_M", "qwen2.5:0.5b"]
    assert escolher_modelo_qwen(instalados) == "qwen2.5:14b-instruct-q4_K_M"
    assert escolher_modelo_qwen(["qwen2.5-coder:latest"]) == "qwen2.5-coder:latest"
    assert escolher_modelo_qwen(["llama3:8b", "mistral"]) is None and escolher_modelo_qwen([]) is None


def test_listar_modelos_le_a_resposta_openai_e_tolera_servidor_fora(monkeypatch):
    class Resp:
        def __enter__(self): return self
        def __exit__(self, *a): return False
        def read(self): return json.dumps({"data": [{"id": "qwen2.5-coder:7b"}, {"id": "llama3"}]}).encode()

    urls = []
    monkeypatch.setattr("urllib.request.urlopen", lambda req, timeout=None: (urls.append(req.full_url), Resp())[1])
    assert listar_modelos("http://x:11434/v1/") == ["qwen2.5-coder:7b", "llama3"]
    assert urls == ["http://x:11434/v1/models"]

    def fora(*a, **k):
        raise urllib.error.URLError("recusado")
    monkeypatch.setattr("urllib.request.urlopen", fora)
    assert listar_modelos("http://x/v1") == []


def test_backend_local_detecta_qwen_sem_chave_e_com_timeout_longo(ambiente):
    ambiente.setenv("MINICODE_BACKEND", "local")
    ambiente.setattr(cliente_llm, "listar_modelos", lambda base, timeout=5.0: ["llama3", "qwen2.5-coder:7b"])
    llm = LLMClient()
    kw = OpenAIFalso.ultimo.kw
    assert llm.backend == "local" and llm.model == "qwen2.5-coder:7b"
    assert kw["base_url"] == URL_LOCAL_PADRAO and kw["api_key"] == "local" and kw["timeout"] == 600.0
    m = llm.metricas()
    assert m["llm_backend"] == "local" and m["llm_model"] == "qwen2.5-coder:7b" and m["llm_calls"] == 0


def test_modelo_e_url_podem_ser_forcados(ambiente):
    ambiente.setenv("MINICODE_BACKEND", "local")
    ambiente.setenv("MINICODE_MODEL", "qwen2.5-coder:1.5b-instruct")
    ambiente.setenv("MINICODE_BASE_URL", "http://localhost:1234/v1")
    ambiente.setattr(cliente_llm, "listar_modelos", lambda *a, **k: pytest.fail("não deveria listar"))
    llm = LLMClient(timeout=30)
    assert llm.model == "qwen2.5-coder:1.5b-instruct"
    assert OpenAIFalso.ultimo.kw["base_url"] == "http://localhost:1234/v1" and OpenAIFalso.ultimo.kw["timeout"] == 30


def test_local_sem_qwen_explica_como_resolver(ambiente):
    ambiente.setenv("MINICODE_BACKEND", "local")
    ambiente.setattr(cliente_llm, "listar_modelos", lambda *a, **k: ["llama3"])
    with pytest.raises(ValueError, match="ollama pull"):
        LLMClient()


def test_remoto_continua_exigindo_chave_e_usa_o_endpoint_da_disciplina(ambiente):
    with pytest.raises(ValueError, match="MINICODE_BACKEND=local"):
        LLMClient()
    ambiente.setenv("MINICODE_API_KEY", "segredo")
    llm = LLMClient()
    assert llm.backend == "remoto" and OpenAIFalso.ultimo.kw["base_url"] == URL_PADRAO
    assert OpenAIFalso.ultimo.kw["timeout"] == 120.0 and "14B" in llm.model


def test_backend_desconhecido_falha_em_vez_de_cair_em_outro(ambiente):
    ambiente.setenv("MINICODE_BACKEND", "nuvem")
    with pytest.raises(ValueError, match="inválido"):
        LLMClient()
