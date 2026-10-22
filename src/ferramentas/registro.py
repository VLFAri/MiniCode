from __future__ import annotations

from pathlib import Path

from src.ferramentas.base import Contexto, Tool, ValidadorCaminho, ValidadorComando
from src.ferramentas.tools import TODAS_AS_FERRAMENTAS


class RegistroFerramentas:
    def __init__(self, project_root, timeout: int = 120):
        self.root = Path(project_root).resolve()
        self.ctx = Contexto(
            root=self.root,
            caminhos=ValidadorCaminho(self.root),
            comandos=ValidadorComando(),
            timeout=timeout,
        )
        self._ferramentas = {}
        for classe in TODAS_AS_FERRAMENTAS:
            self.registrar(classe(self.ctx))

    def registrar(self, ferramenta: Tool):
        if not ferramenta.nome:
            raise ValueError("Ferramenta sem nome.")
        self._ferramentas[ferramenta.nome] = ferramenta

    def nomes(self) -> list:
        return list(self._ferramentas)

    def descricoes(self, excluir=()) -> str:
        return "\n".join(
            f.descricao_completa() for n, f in self._ferramentas.items() if n not in excluir
        )

    def executar(self, nome: str, args: dict = None) -> dict:
        ferramenta = self._ferramentas.get(nome)
        if ferramenta is None:
            return {"ok": False, "saida": f"Ferramenta desconhecida: '{nome}'. Disponíveis: {self.nomes()}"}
        return ferramenta.executar(args or {})