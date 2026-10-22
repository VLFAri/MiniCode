import json
import time
from pathlib import Path


class GerenciadorEstado:
    ESTADOS_VALIDOS = [
        "RECEIVED",
        "SPECIFIED",
        "PLANNED",
        "IMPLEMENTING",
        "VERIFYING",
        "REPAIRING",
        "DONE",
        "FAILED",
    ]
    ESTADOS_TERMINAIS = {"DONE", "FAILED"}

    TRANSICOES_PERMITIDAS = {
        "RECEIVED": ["SPECIFIED"],
        "SPECIFIED": ["PLANNED"],
        "PLANNED": ["IMPLEMENTING"],
        "IMPLEMENTING": ["VERIFYING"],
        "VERIFYING": ["REPAIRING", "DONE"],
        "REPAIRING": ["VERIFYING"],
    }

    def __init__(self, tarefa: str, project_root: str = ".", max_reparos: int = 3):
        self.tarefa = tarefa
        self.project_root = Path(project_root).resolve()
        self.minicode_dir = self.project_root / ".minicode"
        self.minicode_dir.mkdir(parents=True, exist_ok=True)
        self.max_reparos = max_reparos

        self.estado_atual = "RECEIVED"
        self.extras = {}

        self.tentativas_reparo = 0
        self.arquivos_alterados = set()
        self.testes_executados = False
        self.testes_passaram = False
        self.testes_atualizados = False
        self.execucoes_de_teste = 0

        (self.minicode_dir / "actions.jsonl").write_text("", encoding="utf-8")
        self.salvar_estado()


    def salvar_estado(self, extras: dict = None):
        if extras:
            self.extras.update(extras)

        dados = {
            "state": self.estado_atual,
            "task": self.tarefa,
            "repair_attempts": self.tentativas_reparo,
            "files_changed": sorted(self.arquivos_alterados),
            "tests_run": self.execucoes_de_teste,
            "last_tests_passed": self.testes_passaram,
        }
        dados.update(self.extras)

        with open(self.minicode_dir / "state.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)

    def log_acao(self, tipo: str, **dados):
        registro = {"ts": time.time(), "state": self.estado_atual, "type": tipo}
        registro.update(dados)
        with open(self.minicode_dir / "actions.jsonl", "a", encoding="utf-8") as f:
            f.write(json.dumps(registro, ensure_ascii=False) + "\n")


    def registrar_alteracao(self, caminho: str):
        self.arquivos_alterados.add(str(caminho))
        self.testes_atualizados = False

    def registrar_testes(self, passou: bool, resumo: str = ""):
        self.testes_executados = True
        self.testes_passaram = bool(passou)
        self.testes_atualizados = True
        self.execucoes_de_teste += 1
        self.log_acao("run_tests", passed=bool(passou), summary=resumo[:1000])
        self.salvar_estado()


    def _arquivo_preenchido(self, nome: str) -> bool:
        caminho = self.minicode_dir / nome
        return caminho.exists() and caminho.read_text(encoding="utf-8").strip() != ""

    def _checar_precondicoes(self, novo_estado: str):
        if novo_estado == "SPECIFIED" and not self._arquivo_preenchido("specification.md"):
            raise RuntimeError("Hard Gate violado: SPECIFIED exige specification.md não vazio.")

        if novo_estado == "PLANNED" and not self._arquivo_preenchido("plan.md"):
            raise RuntimeError("Hard Gate violado: PLANNED exige plan.md não vazio.")

        if novo_estado == "IMPLEMENTING":
            if not (self._arquivo_preenchido("specification.md") and self._arquivo_preenchido("plan.md")):
                raise RuntimeError("Hard Gate violado: IMPLEMENTING exige especificação e plano.")

        if novo_estado == "REPAIRING":
            if not (self.testes_executados and not self.testes_passaram):
                raise RuntimeError("Hard Gate violado: REPAIRING só ocorre após testes que falharam.")
            if self.tentativas_reparo >= self.max_reparos:
                raise RuntimeError("Hard Gate violado: limite de tentativas de reparo atingido.")

        if novo_estado == "DONE":
            if not self.testes_executados:
                raise RuntimeError("Hard Gate violado: DONE exige testes executados.")
            if not self.testes_atualizados:
                raise RuntimeError("Hard Gate violado: houve alterações após a última execução de testes.")
            if not self.testes_passaram:
                raise RuntimeError("Hard Gate violado: DONE exige testes aprovados.")

    def mudar_estado(self, novo_estado: str):
        if novo_estado not in self.ESTADOS_VALIDOS:
            raise ValueError(f"Estado desconhecido: {novo_estado}")

        if novo_estado == "FAILED":
            raise RuntimeError("Use falhar(motivo) para transitar para FAILED.")

        permitidos = self.TRANSICOES_PERMITIDAS.get(self.estado_atual, [])
        if novo_estado not in permitidos:
            raise RuntimeError(
                f"Hard Gate violado: transição proibida de '{self.estado_atual}' para '{novo_estado}'."
            )

        self._checar_precondicoes(novo_estado)

        if novo_estado == "REPAIRING":
            self.tentativas_reparo += 1

        anterior = self.estado_atual
        self.estado_atual = novo_estado
        self.salvar_estado()
        self.log_acao("transition", **{"from": anterior, "to": novo_estado})
        print(f"[Hard Gate] {anterior} -> {novo_estado}")

    def falhar(self, motivo: str):
        if self.estado_atual in self.ESTADOS_TERMINAIS:
            return
        anterior = self.estado_atual
        self.estado_atual = "FAILED"
        self.salvar_estado({"error": motivo})
        self.log_acao("transition", **{"from": anterior, "to": "FAILED"}, error=motivo)
        print(f"[Hard Gate] {anterior} -> FAILED ({motivo})")