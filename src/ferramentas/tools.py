from __future__ import annotations

import os
import re
import sys
from pathlib import Path

from src.ferramentas.base import Tool, _eh_arquivo_env

IGNORAR_DIRS = {".git", ".minicode", "__pycache__", ".pytest_cache", "node_modules", "venv", ".venv"}
MAX_ARQUIVOS_LISTA = 300
MAX_LEITURA = 20_000
MAX_ESCRITA = 200_000
MAX_MATCHES = 50


class ListFiles(Tool):
    nome = "list_files"
    descricao = "Lista os arquivos do projeto (caminhos relativos)."
    parametros = {"path": "diretório a listar, padrão '.'"}

    def run(self, path: str = ".") -> dict:
        base = self.ctx.caminhos.resolver(path)
        if not base.is_dir():
            return {"ok": False, "saida": f"Não é um diretório: {path}"}

        encontrados = []
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = sorted(d for d in dirnames if d not in IGNORAR_DIRS)
            for f in sorted(filenames):
                if _eh_arquivo_env(f):
                    continue
                encontrados.append(self.ctx.caminhos.relativo(Path(dirpath) / f))

        total = len(encontrados)
        encontrados = encontrados[:MAX_ARQUIVOS_LISTA]
        saida = "\n".join(encontrados) if encontrados else "(vazio)"
        if total > MAX_ARQUIVOS_LISTA:
            saida += f"\n... e mais {total - MAX_ARQUIVOS_LISTA} arquivos"
        return {"ok": True, "saida": saida}


class ReadFile(Tool):
    nome = "read_file"
    descricao = "Lê o conteúdo de um arquivo de texto."
    parametros = {"path": "caminho do arquivo"}
    obrigatorios = ("path",)

    def run(self, path: str) -> dict:
        alvo = self.ctx.caminhos.resolver(path)
        if not alvo.is_file():
            return {"ok": False, "saida": f"Arquivo não encontrado: {path}"}
        texto = alvo.read_text(encoding="utf-8", errors="replace")
        if len(texto) > MAX_LEITURA:
            texto = texto[:MAX_LEITURA] + f"\n... [truncado: arquivo com {len(texto)} caracteres]"
        return {"ok": True, "saida": texto}


class WriteFile(Tool):
    nome = "write_file"
    descricao = "Escreve (cria ou sobrescreve) um arquivo com o conteúdo completo informado."
    parametros = {"path": "caminho do arquivo", "content": "conteúdo completo do arquivo"}
    obrigatorios = ("path", "content")

    def run(self, path: str, content: str) -> dict:
        if not isinstance(content, str):
            return {"ok": False, "saida": "content deve ser texto."}
        if len(content) > MAX_ESCRITA:
            return {"ok": False, "saida": f"Conteúdo grande demais (máx. {MAX_ESCRITA} caracteres)."}
        alvo = self.ctx.caminhos.resolver(path, escrita=True)
        if alvo.is_dir():
            return {"ok": False, "saida": f"'{path}' é um diretório."}
        self.ctx.conteudo.validar(path, content)
        alvo.parent.mkdir(parents=True, exist_ok=True)
        alvo.write_text(content, encoding="utf-8")
        return {"ok": True, "saida": f"Arquivo escrito: {path} ({len(content)} caracteres)"}


class CreateFile(Tool):
    nome = "create_file"
    descricao = "Cria um arquivo novo. Falha se o arquivo já existir."
    parametros = {"path": "caminho do novo arquivo", "content": "conteúdo do arquivo"}
    obrigatorios = ("path", "content")

    def run(self, path: str, content: str) -> dict:
        alvo = self.ctx.caminhos.resolver(path, escrita=True)
        if alvo.exists():
            return {"ok": False, "saida": f"O arquivo já existe: {path}. Use write_file ou replace_text."}
        return WriteFile(self.ctx).run(path=path, content=content)


class ReplaceText(Tool):
    nome = "replace_text"
    descricao = "Substitui um trecho de texto (que deve ocorrer exatamente uma vez) em um arquivo."
    parametros = {"path": "caminho do arquivo", "old": "texto a substituir", "new": "texto novo"}
    obrigatorios = ("path", "old", "new")

    def run(self, path: str, old: str, new: str) -> dict:
        alvo = self.ctx.caminhos.resolver(path, escrita=True)
        if not alvo.is_file():
            return {"ok": False, "saida": f"Arquivo não encontrado: {path}"}
        if not isinstance(old, str) or not old:
            return {"ok": False, "saida": "'old' não pode ser vazio."}
        texto = alvo.read_text(encoding="utf-8")
        ocorrencias = texto.count(old)
        if ocorrencias == 0:
            return {"ok": False, "saida": (
                f"O trecho 'old' NÃO existe em {path}. Conteúdo atual do arquivo:\n{texto[:3000]}\n"
                "Copie o trecho exatamente como está, ou reescreva o arquivo inteiro com write_file."
            )}
        if ocorrencias > 1:
            return {"ok": False, "saida": (
                f"'old' ocorre {ocorrencias} vezes em {path}; inclua mais contexto para que seja único, "
                "ou reescreva o arquivo inteiro com write_file."
            )}
        novo_texto = texto.replace(old, str(new))
        self.ctx.conteudo.validar(path, novo_texto)
        alvo.write_text(novo_texto, encoding="utf-8")
        return {"ok": True, "saida": f"Trecho substituído em {path}."}


class SearchCode(Tool):
    nome = "search_code"
    descricao = "Busca um padrão (regex ou texto) nos arquivos do projeto."
    parametros = {"pattern": "regex ou texto a buscar", "path": "diretório base, padrão '.'"}
    obrigatorios = ("pattern",)

    def run(self, pattern: str, path: str = ".") -> dict:
        base = self.ctx.caminhos.resolver(path)
        try:
            regex = re.compile(pattern)
        except re.error:
            regex = re.compile(re.escape(pattern))

        resultados = []
        for dirpath, dirnames, filenames in os.walk(base):
            dirnames[:] = [d for d in dirnames if d not in IGNORAR_DIRS]
            for f in sorted(filenames):
                if _eh_arquivo_env(f):
                    continue
                arq = Path(dirpath) / f
                try:
                    if arq.stat().st_size > 200_000:
                        continue
                    linhas = arq.read_text(encoding="utf-8").splitlines()
                except (UnicodeDecodeError, OSError):
                    continue
                for n, linha in enumerate(linhas, 1):
                    if regex.search(linha):
                        resultados.append(f"{self.ctx.caminhos.relativo(arq)}:{n}: {linha.strip()[:200]}")
                        if len(resultados) >= MAX_MATCHES:
                            return {"ok": True, "saida": "\n".join(resultados) + "\n... (limite atingido)"}
        return {"ok": True, "saida": "\n".join(resultados) or "Nenhuma ocorrência."}


class GitDiff(Tool):
    nome = "git_diff"
    descricao = "Mostra as alterações atuais do projeto (git diff)."
    parametros = {}

    def run(self) -> dict:
        codigo, saida = self.ctx.rodar(["git", "diff", "--no-ext-diff", "--no-textconv"])
        if "not a git repository" in saida.lower():
            return {"ok": True, "saida": "(o projeto não é um repositório git)"}
        return {"ok": codigo == 0, "saida": saida or "(sem alterações)"}


class RunCommand(Tool):
    nome = "run_command"
    descricao = "Executa um comando permitido (allowlist: pytest, git diff/status/log). Sem shell."
    parametros = {"command": "comando a executar"}
    obrigatorios = ("command",)

    def run(self, command: str) -> dict:
        argv = self.ctx.comandos.validar(command)
        for token in argv[1:]:
            if not token.startswith("-") and (".." in token or token.startswith(("/", "~"))):
                self.ctx.caminhos.resolver(token)
        if argv[0] == "git":
            codigo, saida = self.ctx.rodar(argv)
        else:
            extras = argv[1:] if argv[0] == "pytest" else argv[3:]
            codigo, saida = self.ctx.rodar(self.ctx.comando_pytest(extras), sandbox=True)
        return {"ok": codigo == 0, "saida": f"[exit {codigo}]\n{saida}"}


class RunTests(Tool):
    nome = "run_tests"
    descricao = "Executa a suíte de testes (pytest) do projeto."
    parametros = {"target": "arquivo ou diretório de testes (opcional)"}

    def run(self, target: str = None) -> dict:
        extras = ["-q", "--tb=short", "-p", "no:cacheprovider"]
        if target:
            alvo = self.ctx.caminhos.resolver(target)
            extras.append(self.ctx.caminhos.relativo(alvo))
        codigo, saida = self.ctx.rodar(self.ctx.comando_pytest(extras), sandbox=True)
        if codigo == 126:
            return {"ok": False, "passou": False, "codigo": codigo, "saida": saida}
        return {"ok": True, "passou": codigo == 0, "codigo": codigo, "saida": f"[exit {codigo}]\n{saida}"}


TODAS_AS_FERRAMENTAS = [
    ListFiles, ReadFile, WriteFile, CreateFile, ReplaceText,
    SearchCode, GitDiff, RunCommand, RunTests,
]