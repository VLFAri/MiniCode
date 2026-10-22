from __future__ import annotations

import os
import shlex
from pathlib import Path

class ViolacaoSeguranca(Exception):
    """Operação rejeitada pelo harness."""

def _eh_arquivo_env(nome: str) -> bool:
    return nome == ".env" or (nome.startswith(".env.") and nome != ".env.example")

class ValidadorCaminho:
    # Nunca escritos pelo agente (histórico git, credenciais, rastro de execução)
    PROTEGIDOS_ESCRITA = {".git", ".minicode"}
    
    def __init__(self, project_root):
        self.root = Path(project_root).resolve()

    def resolver(self, caminho, escrita: bool = False) -> Path:
        """Devolve o caminho absoluto e resolvido, ou levanta ViolacaoSeguranca."""
        if not isinstance(caminho, str) or not caminho.strip() or "\x00" in caminho:
            raise ViolacaoSeguranca("caminho inválido")

        # resolve() segue symlinks e remove '..', então '../x' e links para fora são detectados
        alvo = (self.root / caminho).resolve()
        try:
            rel = alvo.relative_to(self.root)
        except ValueError:
            raise ViolacaoSeguranca(f"caminho fora do diretório do projeto: {caminho}")

        for parte in rel.parts:
            if _eh_arquivo_env(parte):
                raise ViolacaoSeguranca(f"acesso a arquivo de credenciais proibido: {caminho}")
            if escrita and parte in self.PROTEGIDOS_ESCRITA:
                raise ViolacaoSeguranca(f"escrita proibida em '{parte}': {caminho}")
        return alvo

    def relativo(self, caminho: Path) -> str:
        return caminho.resolve().relative_to(self.root).as_posix()


class ValidadorComando:
    # Bloqueio explícito (mensagem clara), mesmo que a allowlist já os rejeitasse
    PROIBIDOS = {
        "sudo", "su", "rm", "rmdir", "mv", "dd", "mkfs", "shutdown", "reboot", "halt",
        "poweroff", "chmod", "chown", "kill", "killall", "curl", "wget", "ssh", "scp",
        "nc", "pip", "pip3", "apt", "apt-get", "bash", "sh", "zsh", "eval", "exec",
    }
    # Allowlist: o comando precisa começar com um destes prefixos
    PERMITIDOS = [
        ["pytest"],
        ["python", "-m", "pytest"],
        ["python3", "-m", "pytest"],
        ["git", "diff"],
        ["git", "status"],
        ["git", "log"],
    ]
    METACARACTERES = set(";&|<>`$\n\r")
    # Flags que permitiriam escrever/ler fora do escopo ou executar código arbitrário
    FLAGS_PROIBIDAS = ("--output", "--ext-diff", "--no-index", "--exec-path", "--basetemp", "-c")

    def validar(self, comando: str) -> list:
        if not isinstance(comando, str) or not comando.strip():
            raise ViolacaoSeguranca("comando vazio")

        if any(c in self.METACARACTERES for c in comando):
            raise ViolacaoSeguranca("metacaracteres de shell não são permitidos (; & | > < ` $)")

        try:
            argv = shlex.split(comando)
        except ValueError as e:
            raise ViolacaoSeguranca(f"comando malformado: {e}")
        if not argv:
            raise ViolacaoSeguranca("comando vazio")

        for token in argv:
            if os.path.basename(token) in self.PROIBIDOS:
                raise ViolacaoSeguranca(f"comando proibido: '{token}'")

        if not any(argv[: len(p)] == p for p in self.PERMITIDOS):
            raise ViolacaoSeguranca(
                "comando fora da allowlist. Permitidos: "
                + ", ".join(" ".join(p) for p in self.PERMITIDOS)
            )

        for token in argv[1:]:
            if token.startswith(self.FLAGS_PROIBIDAS):
                raise ViolacaoSeguranca(f"flag proibida: '{token}'")

        return argv


def ambiente_seguro() -> dict:
    """Variáveis de ambiente para subprocessos, sem chaves/segredos (o código do projeto não os vê)."""
    marcadores = ("KEY", "TOKEN", "SECRET", "PASSWORD", "CREDENTIAL")
    return {k: v for k, v in os.environ.items() if not any(m in k.upper() for m in marcadores)}