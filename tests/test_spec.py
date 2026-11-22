import json

import pytest
from src.spec.avaliacao import (analisar_spec, avaliar_com_tentativas, avaliar_primeira_tentativa,
                                resumir_analises)
from src.spec.dataset import (CONTEXTOS, SYSTEM_TEACHER, carregar_tarefas, contexto_para, dividir_por_tarefa,
                              expandir_sementes, filtrar_sementes, gerar_dados_brutos, ler_cache, montar_itens,
                              tratar_e_dividir)
from src.spec.gerador import GeradorSpec, PROMPT_SPEC, validar_spec
from src.spec.qualidade import itens_criterios, validar_spec_estrita
from src.spec.treino import tokenizar_exemplo

SPEC_BOA = """# Specification

## Objective
Implementar `soma(a: int, b: int) -> int` em `soma.py`, que devolve a soma de dois inteiros e rejeita tipos inválidos.

## Parameters / Requirements
- `a`, `b`: inteiros (`int`); valores negativos e zero são permitidos.
- Se algum argumento não for `int` (incluindo `bool`), lançar `TypeError`.
- O módulo deve usar somente a biblioteca padrão do Python e ser testável com pytest.

## Acceptance Criteria
- `soma(2, 3)` retorna `5`.
- `soma(-1, 1)` retorna `0`.
- `soma(0, 0)` retorna `0`.
- `soma("a", 1)` lança `TypeError`.
"""


def com(spec, antigo, novo):
    assert antigo in spec
    return spec.replace(antigo, novo)


# ---------------------------------------------------------------- validação estrita
def test_spec_boa_passa_nos_dois_validadores():
    assert validar_spec(SPEC_BOA) == [] and validar_spec_estrita(SPEC_BOA) == []
    assert len(itens_criterios(SPEC_BOA)) == 4


@pytest.mark.parametrize("ruim, trecho", [
    ("Claro! Aqui está:\n\n" + SPEC_BOA, "não começa"),
    (SPEC_BOA.split("## Acceptance")[0], "Acceptance"),
    (com(SPEC_BOA, "- `soma(-1, 1)` retorna `0`.\n- `soma(0, 0)` retorna `0`.\n- `soma(\"a\", 1)` lança `TypeError`.", ""), "critérios"),
    (com(SPEC_BOA, "`", ""), "exemplos concretos"),
    (SPEC_BOA + "\n```python\ndef soma(a, b):\n    return a + b\n```\n", "implementação"),
    (SPEC_BOA + "\nUse FastAPI para expor a função.\n", "fora do escopo"),
    ("# Specification\n## Objective\nx\n## Parameters\ny\n## Acceptance Criteria\n- `a`\n- `b`\n- `c`\n", "curta"),
])
def test_validacao_estrita_rejeita(ruim, trecho):
    assert any(trecho in p for p in validar_spec_estrita(ruim)), validar_spec_estrita(ruim)


def test_formato_antigo_do_dataset_e_rejeitado():
    """O formato que o dataset anterior ensinaria ao modelo: o agente o recusa."""
    antigo = "# Especificação Técnica Formal\n\n## 1. Introdução\nTexto.\n\n### 7. Exemplos\n- `f(1)` retorna `1`\n"
    assert len(validar_spec(antigo)) == 5 and validar_spec_estrita(antigo)


def test_assinatura_sem_corpo_e_permitida():
    spec = SPEC_BOA + "\n```python\ndef soma(a: int, b: int) -> int: ...\n```\n"
    assert validar_spec_estrita(spec) == []


# ---------------------------------------------------------------- sementes e contexto
def test_filtrar_sementes_exclui_enunciado_fora_de_escopo_e_quase_duplicadas():
    tarefas = [
        "Crie uma função que calcule o fatorial de um número inteiro.",
        "Adicione paginação ao endpoint GET /users aceitando page e page_size.",
        "Adicione uma rota /health que retorne o JSON status ok.",
        "Adicione autenticação JWT em um endpoint protegido FastAPI.",
        "Corrija o erro de NullPointerException no serviço de usuários.",
        "Implemente o algoritmo de busca binária iterativa em uma lista ordenada.",
        "Implemente o algoritmo de busca binária iterativa em uma lista ordenada de inteiros.",
        "Crie uma classe de Pilha (Stack) com métodos push, pop, peek e verificação de vazia.",
    ]
    validas, excl = filtrar_sementes(tarefas)
    assert validas == [tarefas[5], tarefas[7]]
    assert len(excl["reservada_do_enunciado"]) == 3 and len(excl["fora_do_escopo_stdlib"]) == 2
    assert excl["quase_duplicada"] == [tarefas[6]]


def test_contexto_e_deterministico_e_no_formato_do_list_files():
    assert contexto_para("t", 0, 42) == contexto_para("t", 0, 42)
    assert {contexto_para(f"t{i}", 0, 42) for i in range(60)} <= set(CONTEXTOS)
    assert "(vazio)" in CONTEXTOS and contexto_para("t", 0, 1) != contexto_para("t", 1, 1)
    itens = montar_itens(["a", "b"], 2, 42)
    assert len(itens) == 4 and len({i for i in itens}) == 4


def test_carregar_tarefas_ignora_comentarios_e_linhas_vazias(tmp_path):
    f = tmp_path / "t.txt"
    f.write_text("# comentário\n\nTarefa A\n  Tarefa B  \n")
    assert carregar_tarefas([f]) == ["Tarefa A", "Tarefa B"]
    with pytest.raises(FileNotFoundError):
        carregar_tarefas([tmp_path / "nao_existe.txt"])


# ---------------------------------------------------------------- geração com teacher falso
class TeacherFalso:
    """Primeira resposta de cada tarefa é inválida; a segunda é boa. Registra o que recebeu."""
    def __init__(self, sempre_ruim=False):
        self.chamadas, self.sempre_ruim, self.vistos = 0, sempre_ruim, []

    def complete(self, prompt, system_prompt=None):
        self.vistos.append((prompt, system_prompt))
        self.chamadas += 1
        if self.sempre_ruim or "rejeitada" not in prompt:
            return "Claro! " + SPEC_BOA if not self.sempre_ruim else "lixo"
        return "```markdown\n" + SPEC_BOA + "\n```"


def test_teacher_recebe_system_privilegiado_e_o_prompt_real_do_agente(tmp_path):
    itens = [("Crie soma(a, b)", "(vazio)")]
    t = TeacherFalso()
    gerar_dados_brutos(itens, t, tmp_path / "raw.jsonl", max_tentativas=3, teacher_nome="falso")
    prompt1, sys1 = t.vistos[0]
    assert prompt1 == PROMPT_SPEC.format(tarefa="Crie soma(a, b)", contexto="(vazio)")
    assert sys1 == SYSTEM_TEACHER
    assert "rejeitada" in t.vistos[1][0] and "não começa" in t.vistos[1][0]      # feedback só para o teacher
    assert t.chamadas == 2
    assert [r["attempt"] for r in ler_cache(tmp_path / "raw.jsonl")[itens[0]]] == [1, 2]


def test_geracao_retoma_do_cache_e_respeita_o_limite_de_tentativas(tmp_path):
    cache = tmp_path / "raw.jsonl"
    itens = [("A", "(vazio)"), ("B", "(vazio)")]
    gerar_dados_brutos(itens, TeacherFalso(), cache)
    t2 = TeacherFalso()
    gerar_dados_brutos(itens, t2, cache)
    assert t2.chamadas == 0                                  # tudo já válido no cache
    ruim = TeacherFalso(sempre_ruim=True)
    gerar_dados_brutos([("C", "(vazio)")], ruim, cache, max_tentativas=2)
    assert ruim.chamadas == 2


def test_teacher_inacessivel_aborta_com_mensagem_clara(tmp_path):
    class Fora:
        def complete(self, *a, **k):
            raise ConnectionError("sem rede")
    with pytest.raises(RuntimeError, match="teacher inacessível"):
        gerar_dados_brutos([(f"t{i}", "(vazio)") for i in range(5)], Fora(), tmp_path / "raw.jsonl")


# ---------------------------------------------------------------- tratamento e split
@pytest.fixture
def cache_pronto(tmp_path):
    itens = [(f"Tarefa {i} única número {i}", "(vazio)") for i in range(20)]
    cache = tmp_path / "raw.jsonl"
    gerar_dados_brutos(itens, TeacherFalso(), cache)
    return itens, cache


def test_dataset_usa_o_prompt_do_agente_e_so_specs_estritas(cache_pronto, tmp_path):
    itens, cache = cache_pronto
    st = tratar_e_dividir(itens, cache, tmp_path / "out")
    assert st["itens_validos"] == 20 and st["teacher_primeira_tentativa_valida"] == 0.0
    for nome in ("train", "val", "test"):
        for l in (tmp_path / "out" / f"{nome}.jsonl").read_text().splitlines():
            ex = json.loads(l)
            assert [m["role"] for m in ex["messages"]] == ["user", "assistant"]
            assert ex["messages"][0]["content"] == PROMPT_SPEC.format(tarefa=ex["task"], contexto=ex["contexto"])
            assert validar_spec_estrita(ex["messages"][1]["content"]) == []     # 0 recusadas, ao contrário do dataset antigo


def test_split_por_tarefa_sem_vazamento_mesmo_com_varios_contextos(tmp_path):
    itens = montar_itens([f"Tarefa distinta {i} palavra{i}" for i in range(20)], 2, 42)
    cache = tmp_path / "raw.jsonl"
    gerar_dados_brutos(itens, TeacherFalso(), cache)
    tratar_e_dividir(itens, cache, tmp_path / "out")
    por_split = {n: {json.loads(l)["task"] for l in (tmp_path / "out" / f"{n}.jsonl").read_text().splitlines()}
                 for n in ("train", "val", "test")}
    assert not (por_split["train"] & por_split["test"] or por_split["train"] & por_split["val"]
                or por_split["val"] & por_split["test"])
    assert sum(len(v) for v in por_split.values()) == 20
    assert dividir_por_tarefa([f"t{i}" for i in range(20)], 1, 0.10, 0.15).keys() == {"test", "val", "train"}


def test_descartes_sao_contados_por_motivo(tmp_path):
    itens = [("boa", "(vazio)"), ("ruim", "(vazio)")]
    cache = tmp_path / "raw.jsonl"
    gerar_dados_brutos([itens[0]], TeacherFalso(), cache)
    gerar_dados_brutos([itens[1]], TeacherFalso(sempre_ruim=True), cache, max_tentativas=2)
    st = tratar_e_dividir(itens, cache, tmp_path / "out")
    assert st["itens_validos"] == 1 and st["descartados_por_motivo"]


def test_expandir_sementes_filtra_e_respeita_o_alvo():
    class Gerador:
        def complete(self, prompt, system_prompt=None):
            return ("1. Implemente uma função que inverta uma string palavra por palavra.\n"
                    "- Crie uma API com FastAPI para listar usuários cadastrados.\n"
                    "Implemente uma função que inverta uma string palavra por palavra.\n"
                    "curta\n"
                    "* Crie uma classe Matriz com soma e multiplicação de matrizes pequenas.\n")
    novas = expandir_sementes(Gerador(), 5, ["Crie uma função que calcule a média de uma lista de números."], rodadas=2)
    assert novas == ["Implemente uma função que inverta uma string palavra por palavra.",
                     "Crie uma classe Matriz com soma e multiplicação de matrizes pequenas."]


# ---------------------------------------------------------------- avaliação
def test_analisar_e_resumir_specs():
    boa, ruim = analisar_spec(SPEC_BOA), analisar_spec("# Especificação Técnica\ntexto")
    assert boa["valida_agente"] and boa["valida_estrita"] and boa["n_criterios"] == 4 and not boa["tem_codigo"]
    assert not ruim["valida_agente"] and ruim["problemas"]
    r = resumir_analises([boa, ruim])
    assert r["n"] == 2 and r["valida_agente"] == 0.5 and r["problemas_mais_comuns"]
    assert resumir_analises([]) == {"n": 0}


def test_avaliar_primeira_tentativa_usa_lote_quando_existe():
    class Modelo:
        def gerar_lote(self, prompts):
            return [SPEC_BOA] * len(prompts)
    assert avaliar_primeira_tentativa(Modelo(), ["p1", "p2", "p3"])["valida_estrita"] == 1.0

    class SoComplete:
        def complete(self, p):
            return "lixo"
    assert avaliar_primeira_tentativa(SoComplete(), ["p"])["valida_agente"] == 0.0


def test_avaliar_com_tentativas_usa_o_gerador_real_do_agente():
    class Sequencial:
        def __init__(self, respostas):
            self.respostas = list(respostas)

        def complete(self, prompt):
            return self.respostas.pop(0)

    m = Sequencial(["lixo", SPEC_BOA, "lixo", "lixo", "lixo"])
    r = avaliar_com_tentativas(m, [("t1", "(vazio)"), ("t2", "(vazio)")])
    assert r == {"n": 2, "taxa_sucesso": 0.5, "tentativas_media": 2.5}


def test_llm_spec_so_afeta_a_especificacao_nao_o_plano():
    class Principal:
        def __init__(self):
            self.prompts = []

        def complete(self, prompt, system_prompt=None):
            self.prompts.append(prompt)
            return "1. implementar\n2. testar"

    class Pequeno:
        def complete(self, prompt, system_prompt=None):
            return SPEC_BOA

    principal = Principal()
    g = GeradorSpec(principal, llm_spec=Pequeno())
    assert g.gerar_spec("t", "(vazio)") == SPEC_BOA.strip()
    assert principal.prompts == []                              # a spec não passou pelo 14B
    assert g.gerar_plano(SPEC_BOA, "(vazio)").startswith("1.")
    assert len(principal.prompts) == 1                          # o plano continua no 14B


# ---------------------------------------------------------------- tokenização
class TokenizadorFalso:
    eos_token = "#"

    def apply_chat_template(self, msgs, tokenize=False, add_generation_prompt=False):
        assert not tokenize and add_generation_prompt
        return "".join(f"<{m['role']}>{m['content']}" for m in msgs) + "<assistant>"

    def __call__(self, texto, add_special_tokens=True):
        assert add_special_tokens is False
        return {"input_ids": [ord(c) for c in texto]}


def test_tokenizacao_treina_so_a_spec_e_marca_truncamento():
    msgs = [{"role": "user", "content": "PEDIDO"}, {"role": "assistant", "content": SPEC_BOA}]
    out = tokenizar_exemplo(TokenizadorFalso(), msgs, max_len=100_000)
    treinados = "".join(chr(i) for i, l in zip(out["input_ids"], out["labels"]) if l != -100)
    assert treinados == SPEC_BOA + "#"
    n_prompt = len("<user>PEDIDO<assistant>")
    assert out["labels"][:n_prompt] == [-100] * n_prompt and out["truncado"] is False
    assert tokenizar_exemplo(TokenizadorFalso(), msgs, max_len=50)["truncado"] is True


# ---------------------------------------------------------------- teacher local (Ollama) e mensagens de erro
def test_teacher_ollama_auto_escolhe_o_maior_qwen_sem_precisar_de_openai(monkeypatch, capsys):
    from src.spec import dataset
    monkeypatch.setattr("src.modelo.descoberta.listar_modelos", lambda base, timeout=5.0: ["llama3", "qwen2.5-coder:1.5b", "qwen2.5-coder:7b"])
    t = dataset.TeacherOllama()
    assert t.modelo == "qwen2.5-coder:7b" and "AVISO" not in capsys.readouterr().out
    monkeypatch.setattr("src.modelo.descoberta.listar_modelos", lambda base, timeout=5.0: ["qwen2.5-coder:1.5b-instruct"])
    assert dataset.TeacherOllama().modelo == "qwen2.5-coder:1.5b-instruct"
    assert "autodestilação" in capsys.readouterr().out


def test_teacher_ollama_sem_qwen_explica_como_resolver(monkeypatch):
    from src.spec import dataset
    monkeypatch.setattr("src.modelo.descoberta.listar_modelos", lambda base, timeout=5.0: [])
    with pytest.raises(ValueError, match="ollama pull"):
        dataset.TeacherOllama()


def test_modelo_inexistente_no_ollama_gera_erro_legivel(monkeypatch):
    import io
    import urllib.error
    from src.spec import dataset

    def http404(req, timeout=None):
        raise urllib.error.HTTPError(req.full_url, 404, "Not Found", {}, io.BytesIO(b'{"error":"model not found"}'))
    monkeypatch.setattr("urllib.request.urlopen", http404)
    with pytest.raises(RuntimeError, match="ollama list"):
        dataset.TeacherOllama("qwen-inexistente").complete("oi")


def test_main_explica_as_alternativas_quando_o_teacher_nao_pode_ser_criado(monkeypatch, capsys, tmp_path):
    from src.spec import dataset

    def falha(nome, modelo):
        raise ValueError("Chave da API não encontrada")
    monkeypatch.setattr(dataset, "criar_teacher", falha)
    tarefas = tmp_path / "t.txt"
    tarefas.write_text("Implemente uma função que some dois números.\n")
    assert dataset.main(["--tarefas", str(tarefas), "--cache", str(tmp_path / "r.jsonl")]) == 2
    saida = capsys.readouterr().out
    assert "MINICODE_API_KEY" in saida and "--teacher ollama" in saida and "--etapa tratar" in saida


def test_main_mostra_a_pasta_atual_quando_as_tarefas_nao_sao_encontradas(monkeypatch, capsys, tmp_path):
    from src.spec import dataset
    monkeypatch.setattr(dataset, "criar_teacher", lambda *a: object())
    monkeypatch.chdir(tmp_path) if hasattr(monkeypatch, "chdir") else None
    assert dataset.main(["--tarefas", str(tmp_path / "nao_existe.txt"), "--etapa", "tratar"]) == 2
    saida = capsys.readouterr().out
    assert "pasta atual" in saida and "código em" in saida and "--tarefas" in saida
