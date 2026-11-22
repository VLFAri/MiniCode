import pytest
from src.spec.gerador import GeradorSpec, limpar_cercas, validar_spec

SPEC_OK = """# Specification
## Objective
Somar dois números.
## Parameters / Requirements
a, b inteiros.
## Acceptance Criteria
soma(2, 3) deve retornar 5.
"""


class LLMSequencial:
    def __init__(self, respostas):
        self.respostas = list(respostas)
        self.chamadas = 0

    def complete(self, prompt, system_prompt=None):
        self.chamadas += 1
        return self.respostas.pop(0)


def test_limpar_cercas():
    assert limpar_cercas("```markdown\n# X\n```") == "# X"


def test_validar_spec():
    assert validar_spec(SPEC_OK) == []
    assert validar_spec("só texto")
    assert validar_spec("# Specification\n## Objective\nx\n## Parameters\ny\n## Acceptance Criteria\n")


def test_gerar_spec_tenta_de_novo():
    llm = LLMSequencial(["lixo", f"```markdown\n{SPEC_OK}\n```"])
    assert GeradorSpec(llm).gerar_spec("t", "ctx").startswith("# Specification")
    assert llm.chamadas == 2


def test_gerar_spec_desiste_apos_tentativas():
    llm = LLMSequencial(["lixo"] * 3)
    with pytest.raises(RuntimeError, match="especificação válida"):
        GeradorSpec(llm).gerar_spec("t", "ctx")


def test_plano_precisa_ser_numerado():
    with pytest.raises(RuntimeError):
        GeradorSpec(LLMSequencial(["texto solto"])).gerar_plano("spec", "ctx")
    assert GeradorSpec(LLMSequencial(["1. fazer\n2. testar"])).gerar_plano("spec", "ctx")