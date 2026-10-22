from __future__ import annotations

import ast
import os
import re
import shlex
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


class ViolacaoSeguranca(Exception):
    pass


def _eh_arquivo_env(nome: str) -> bool:
    return nome == ".env" or (nome.startswith(".env.") and nome != ".env.example")


class ValidadorCaminho:
    PROTEGIDOS_ESCRITA = {".git", ".minicode"}

    def __init__(self, project_root):
        self.root = Path(project_root).resolve()

    def resolver(self, caminho, escrita: bool = False) -> Path:
        if not isinstance(caminho, str) or not caminho.strip() or "\x00" in caminho:
            raise ViolacaoSeguranca("caminho inválido")

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
    PROIBIDOS = {
        "sudo", "su", "rm", "rmdir", "mv", "dd", "mkfs", "shutdown", "reboot", "halt",
        "poweroff", "chmod", "chown", "kill", "killall", "curl", "wget", "ssh", "scp",
        "nc", "pip", "pip3", "apt", "apt-get", "bash", "sh", "zsh", "eval", "exec",
    }
    PERMITIDOS = [
        ["pytest"],
        ["python", "-m", "pytest"],
        ["python3", "-m", "pytest"],
        ["git", "diff"],
        ["git", "status"],
        ["git", "log"],
    ]
    GERENCIADORES_E_RUNTIMES = {
        "npm", "npx", "yarn", "pnpm", "node", "nodejs", "deno", "bun",
        "pip", "pip3", "poetry", "conda", "cargo", "rustc", "go", "gofmt",
        "mvn", "gradle", "gradlew", "dotnet", "ruby", "gem", "php", "composer",
        "java", "javac", "make", "cmake", "tsc",
    }
    METACARACTERES = set(";&|<>`$\n\r")
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

        primeiro = os.path.basename(argv[0])
        if primeiro in self.GERENCIADORES_E_RUNTIMES:
            raise ViolacaoSeguranca(
                f"'{primeiro}' não está disponível neste ambiente. O MiniCode só executa Python "
                "(biblioteca padrão) verificado por pytest, sem Node.js, Java, Go, Ruby, PHP e "
                "similares, e sem instalar pacotes (nenhum pip/npm/yarn/conda). Reescreva o projeto "
                "inteiramente em Python puro."
            )

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


def _compilar(padroes):
    return [(re.compile(regex, re.IGNORECASE | re.MULTILINE), descricao) for regex, descricao in padroes]


_PADROES_SHELL = _compilar([
    (r"(?<![\w.\-])rm\s+-\w", "'rm' com opções (rm -rf etc.)"),
    (r"(?<![\w.\-])rm\s+[\"']?(/|~|\$|\*|\.{1,2}/)", "'rm' em caminho perigoso"),
    (r"(?<![\w.\-])(rmdir|shred|unlink)\s+[\"'\w./~$*-]", "remoção de arquivos ou pastas"),
    (r"(?<![\w.\-])(sudo|doas)\b", "'sudo'"),
    (r"(?<![\w.\-])(shutdown|reboot|poweroff|halt)\s+(-\w|now|\+?\d)", "desligar ou reiniciar a máquina"),
    (r"^\s*(shutdown|reboot|poweroff|halt)\s*$", "desligar ou reiniciar a máquina"),
    (r"\bsystemctl\s+(poweroff|reboot|halt|stop|disable|mask)", "'systemctl' destrutivo"),
    (r"\b(mkfs(\.\w+)?|wipefs)\b", "formatação de disco"),
    (r"\bdd\s+if=", "'dd'"),
    (r">\s*/dev/(sd|hd|nvme|mmcblk)", "escrita direta em disco"),
    (r":\(\)\s*\{", "fork bomb"),
    (r"\bchmod\s+(-\w+\s+)*[0-7]*777\b", "'chmod 777'"),
    (r"\bchown\s+-\w*R", "'chown -R'"),
    (r"\b(curl|wget)\b[^\n|]*\|\s*(sudo\s+)?(ba|z|da)?sh\b", "baixar e executar script remoto"),
    (r"(?<![\w.\-])(killall|pkill)\b", "encerrar processos"),
    (r"(?<![\w.\-])kill\s+-\w", "'kill' com sinal"),
    (r"\b(iptables|nftables)\b|\bufw\s+disable", "alteração de firewall"),
    (r"\bcrontab\s+-", "alteração do crontab"),
    (r"\bdel\s+/[fsq]\b", "'del' destrutivo (Windows)"),
    (r"\b(rd|rmdir)\s+/s\b", "remoção recursiva (Windows)"),
    (r"(?<![\w.\-])format\s+[a-z]:", "formatar disco (Windows)"),
])

_ENFEITE = (
    r"(?:\s+(?:todos|todas|todo|toda|tudo|os|as|o|a|de|do|da|dos|das|no|na|nos|nas|meus|minhas|seus|suas|"
    r"esses|essas|estes|estas|existentes|inteiro|inteira|all|the|my|your|every|any|of|in|this|that|these|those))*"
)
_VERBO_DESTRUTIVO = (
    r"(?:apag|delet|exclu|remov|elimin|destru|limp|wip|eras|destroy|purg|nuk|shred)\w*"
)
_ALVO_SISTEMA = (
    r"(?:arquivos?|pastas?|diret[óo]rios?|disco|hd|ssd|parti[çc][ãõ]o|parti[çc][õo]es|sistema|home|raiz|"
    r"reposit[óo]rio|projeto|tudo|files?|folders?|director(?:y|ies)|disk|everything|system|repo(?:sitory)?|project)"
)

_PADROES_TAREFA = _compilar([
    (rf"\b{_VERBO_DESTRUTIVO}{_ENFEITE}\s+{_ALVO_SISTEMA}\b", "pedido para apagar arquivos, pastas ou o sistema"),
    (rf"\b(?:format\w*){_ENFEITE}\s+(?:disco|hd|ssd|parti[çc][ãõ]o|pen\s*drive|disk|drive|partition)\b", "formatar disco"),
    (rf"\b(?:desligu?\w*|reinici\w*|reboot\w*|shutdown|restart\w*|power\s*off){_ENFEITE}\s+(?:computador|m[áa]quina|servidor|sistema|pc|machine|computer|server)\b", "desligar ou reiniciar a máquina"),
    (rf"\b(?:mate|matar|mata|encerre|encerrar|finalize|finalizar|termine|kill){_ENFEITE}\s+(?:processos?|process(?:es)?)\b", "encerrar processos"),
    (r"\b(?:chmod|chown)\b|permiss[ãa]o\s+(?:total|777)|\b(?:como|com|as)\s+(?:root|administrador|sudo)\b|privil[ée]gios?\s+(?:de\s+)?(?:root|administrador)", "elevação de privilégios ou permissões"),
    (r"\b(?:ransomware|malware|keylogger|backdoor|trojan|rootkit|botnet|ddos|v[ií]rus|spyware)\b", "criação de malware"),
    (rf"\b(?:roub|exfiltr|vaz|steal|leak)\w*{_ENFEITE}\s+(?:senhas?|dados|credenciais|chaves?|tokens?|passwords?|credentials|secrets?)\b", "roubo de credenciais ou dados"),
    (r"/etc/(?:passwd|shadow)|~/\.ssh|\.ssh/id_", "acesso a arquivos sensíveis do sistema"),
    (r"(?:apag|delet|exclu|remov|elimin|destru|delete|remove)\w*[^.\n]{0,40}\.git\b", "apagar o histórico git"),
    (r"\bhack(?!athon)\w*\b", "tentativa de invasão ou acesso não autorizado"),
    (r"\b(?:invad\w*|crack\w*|bypass\w*)\b", "tentativa de invasão ou acesso não autorizado"),
    (rf"\b(?:quebr|crack)\w*{_ENFEITE}\s+(?:a\s+)?senha", "tentativa de quebrar senha"),
    (r"\bexploit\w*\b[^.\n]{0,30}\b(?:vulnerabilidade|vulnerability|falha|cve[-\s]?\d+|seguran[çc]a)\b", "exploração de vulnerabilidade"),
    (r"\b(?:vulnerabilidade|vulnerability|falha|cve[-\s]?\d+)\b[^.\n]{0,30}\bexploit\w*\b", "exploração de vulnerabilidade"),
    (r"\bgain\s+root\s+access\b|\bacess\w*\s+(?:[^.\n]{0,20}\b)?(?:n[ãa]o\s+autorizado|sem\s+autoriza[çc][ãa]o)\b", "acesso não autorizado"),
    (r"\bsem\s+autoriza[çc][ãa]o\b|\bwithout\s+authorization\b|\bunauthorized\s+access\b", "acesso não autorizado"),
    (r"\b(?:sql\s*injection|xss|csrf|rce|remote\s+code\s+execution)\b[^.\n]{0,40}\b(?:roub|steal|ganh|gain|exfiltr|explor|ataqu|attack)", "ataque de injeção ou exploração"),
    (rf"\bataqu\w*{_ENFEITE}\s+(?:ddos|dos|de\s+for[çc]a\s+bruta)\b", "ataque de negação de serviço ou força bruta"),
    (r"\bbrute[\s-]?force\s+attack\b", "ataque de força bruta"),
    (r"\bos\.(system|popen|remove|unlink|rmdir|removedirs|kill|chmod|chown|exec\w*|spawn\w*|fork)\b", "chamada perigosa do módulo os"),
    (r"\bsubprocess\b", "uso de subprocess"),
    (r"\bshutil\.rmtree\b", "shutil.rmtree"),
    (r"\b(eval|exec)\s*\(", "eval ou exec"),
    (r"\b__import__\b", "__import__"),
    (r"\bctypes\b", "ctypes"),
])


class ValidadorConteudo:

    MODULOS_PROIBIDOS = {
        "subprocess", "ctypes", "_ctypes", "_posixsubprocess", "pty", "commands",
        "importlib", "builtins", "runpy", "marshal",
    }
    BUILTINS_PROIBIDOS = {"eval", "exec", "__import__"}
    PREFIXOS_OS_PROIBIDOS = ("system", "popen", "exec", "spawn", "fork", "kill", "posix_spawn", "startfile")
    OS_DESTRUTIVOS = {"remove", "unlink", "rmdir", "removedirs", "chmod", "chown", "lchown", "truncate"}
    ATRIBUTOS_DESTRUTIVOS = {"rmtree", "unlink", "rmdir", "removedirs"}
    MAX_PROBLEMAS = 5

    def perigos_em_texto(self, texto: str) -> list:
        achados = [d for regex, d in _PADROES_SHELL if regex.search(texto)]
        achados += [d for regex, d in _PADROES_TAREFA if regex.search(texto)]
        return list(dict.fromkeys(achados))

    def problemas(self, caminho: str, texto: str) -> list:
        ext = os.path.splitext(caminho)[1].lower()
        achados = []
        if ext in ("", ".py", ".pyw"):
            achados += self._problemas_python(texto)
        for regex, descricao in _PADROES_SHELL:
            if regex.search(texto):
                achados.append(f"comando perigoso no texto: {descricao}")
        return list(dict.fromkeys(achados))[: self.MAX_PROBLEMAS]

    def validar(self, caminho: str, texto: str):
        achados = self.problemas(caminho, texto)
        if achados:
            raise ViolacaoSeguranca(
                f"conteúdo rejeitado para '{caminho}': " + "; ".join(achados)
                + ". Nunca escreva comandos ou chamadas perigosas em nenhum arquivo (use mocks nos testes)."
            )

    def _problemas_python(self, texto: str) -> list:
        try:
            arvore = ast.parse(texto)
        except SyntaxError:
            return []

        modulo_de = {}
        for no in ast.walk(arvore):
            if isinstance(no, ast.Import):
                for alias in no.names:
                    modulo_de[alias.asname or alias.name.split(".")[0]] = alias.name.split(".")[0]

        achados = []
        for no in ast.walk(arvore):
            if isinstance(no, ast.Import):
                for alias in no.names:
                    if alias.name.split(".")[0] in self.MODULOS_PROIBIDOS:
                        achados.append(f"import do módulo proibido '{alias.name}'")
            elif isinstance(no, ast.ImportFrom):
                raiz = (no.module or "").split(".")[0]
                if raiz in self.MODULOS_PROIBIDOS:
                    achados.append(f"import do módulo proibido '{no.module}'")
                elif raiz == "os":
                    for alias in no.names:
                        if alias.name.startswith(self.PREFIXOS_OS_PROIBIDOS) or alias.name in self.OS_DESTRUTIVOS:
                            achados.append(f"import de os.{alias.name}")
                elif raiz == "shutil":
                    for alias in no.names:
                        if alias.name in self.ATRIBUTOS_DESTRUTIVOS:
                            achados.append(f"import de shutil.{alias.name}")
            elif isinstance(no, ast.Attribute):
                if isinstance(no.value, ast.Name):
                    modulo = modulo_de.get(no.value.id, no.value.id)
                    if modulo == "os" and (no.attr.startswith(self.PREFIXOS_OS_PROIBIDOS) or no.attr in self.OS_DESTRUTIVOS):
                        achados.append(f"uso de os.{no.attr}")
                if no.attr in self.ATRIBUTOS_DESTRUTIVOS:
                    achados.append(f"remoção de arquivos ou pastas (.{no.attr})")
            elif isinstance(no, ast.Name):
                if no.id == "__builtins__":
                    achados.append("acesso a __builtins__")
            elif isinstance(no, ast.Call):
                f = no.func
                if isinstance(f, ast.Name) and f.id in self.BUILTINS_PROIBIDOS:
                    achados.append(f"chamada a {f.id}()")
                elif isinstance(f, ast.Name) and f.id == "getattr" and len(no.args) >= 2 \
                        and isinstance(no.args[1], ast.Constant) and isinstance(no.args[1].value, str) \
                        and (no.args[1].value.startswith(self.PREFIXOS_OS_PROIBIDOS)
                             or no.args[1].value in self.OS_DESTRUTIVOS | self.ATRIBUTOS_DESTRUTIVOS):
                    achados.append(f"getattr com '{no.args[1].value}'")
        return list(dict.fromkeys(achados))


def ambiente_seguro() -> dict:
    marcadores = ("KEY", "TOKEN", "SECRET", "PASSWORD", "CREDENTIAL")
    return {k: v for k, v in os.environ.items() if not any(m in k.upper() for m in marcadores)}


GUARDA_EXECUCAO = r'''
import os
import sys
import threading


def _instalar():
    raiz = os.environ.get("MINICODE_SANDBOX_ROOT")
    if not raiz:
        return

    sys.dont_write_bytecode = True
    realpath, fspath, fsdecode, sep = os.path.realpath, os.fspath, os.fsdecode, os.sep
    Negado = PermissionError

    raiz = realpath(raiz)
    protegidos = (os.path.join(raiz, ".git"), os.path.join(raiz, ".minicode"))
    tmp_ok = os.path.join(raiz, ".minicode", "tmp")
    dirs_sensiveis = frozenset({".ssh", ".aws", ".gnupg", ".kube", ".docker"})
    arqs_sensiveis = frozenset({"shadow", "gshadow", "id_rsa", "id_ed25519", "id_ecdsa",
                                ".bash_history", ".netrc", ".pgpass"})
    local = threading.local()

    def negar(msg):
        raise Negado(f"[MiniCode sandbox] {msg}")

    def norm(p):
        try:
            if isinstance(p, bytes):
                p = fsdecode(p)
            return realpath(fspath(p))
        except (TypeError, ValueError):
            return None

    def dentro(p, base):
        return p == base or p.startswith(base + sep)

    def eh_env(nome):
        return nome == ".env" or (nome.startswith(".env.") and nome != ".env.example")

    def pode_escrever(p):
        if p == "/dev/null":
            return True
        if not dentro(p, raiz):
            return False
        if dentro(p, tmp_ok):
            return True
        if any(dentro(p, pr) for pr in protegidos):
            return False
        return not eh_env(os.path.basename(p))

    def leitura_proibida(p):
        partes = p.split(sep)
        nome = partes[-1]
        return (any(x in dirs_sensiveis for x in partes) or nome in arqs_sensiveis or eh_env(nome)
                or (p.startswith("/proc/") and nome == "environ"))

    def modo_escrita(modo, flags):
        if isinstance(modo, str) and any(c in modo for c in "wax+"):
            return True
        mascara = os.O_WRONLY | os.O_RDWR | os.O_CREAT | os.O_APPEND | os.O_TRUNC
        return isinstance(flags, int) and bool(flags & mascara)

    def host_local(h, passivo=False):
        if h is None or h == "" or h == b"":
            return passivo
        if isinstance(h, bytes):
            h = fsdecode(h)
        if not isinstance(h, str):
            return False
        h = h.strip("[]").lower()
        return h in ("localhost", "::1") or h.startswith("127.")

    def host_de(endereco):
        return endereco[0] if isinstance(endereco, tuple) and endereco else object()

    escrita = {
        "os.remove": (0,), "os.rmdir": (0,), "os.rename": (0, 1), "os.mkdir": (0,), "os.chmod": (0,),
        "os.chown": (0,), "os.truncate": (0,), "os.symlink": (1,), "os.link": (0, 1), "os.utime": (0,),
        "os.mkfifo": (0,), "os.mknod": (0,), "os.setxattr": (0,), "os.removexattr": (0,),
        "os.chflags": (0,), "shutil.copyfile": (1,), "shutil.copymode": (1,), "shutil.copystat": (1,),
        "shutil.copytree": (1,), "shutil.move": (0, 1), "shutil.rmtree": (0,),
        "shutil.make_archive": (0,), "shutil.unpack_archive": (1,),
    }
    processos = frozenset({
        "os.system", "os.exec", "os.fork", "os.forkpty", "os.posix_spawn", "os.spawn", "os.kill",
        "os.killpg", "os.startfile", "subprocess.Popen", "pty.spawn",
    })
    processos_ctypes = frozenset({"ctypes.dlopen", "ctypes.dlsym", "ctypes.call_function"})

    def verificar(evento, args):
        if evento == "open":
            p = norm(args[0])
            if p is None:
                return
            if modo_escrita(args[1] if len(args) > 1 else None, args[2] if len(args) > 2 else None):
                if not pode_escrever(p):
                    negar(f"escrita bloqueada fora do projeto: {p}")
            elif leitura_proibida(p):
                negar(f"leitura de arquivo sensível bloqueada: {p}")
        elif evento in escrita:
            for i in escrita[evento]:
                if i < len(args):
                    p = norm(args[i])
                    if p is not None and not pode_escrever(p):
                        negar(f"{evento} bloqueado fora do projeto: {p}")
        elif evento in processos:
            negar(f"criação de processos/código nativo bloqueada ({evento})")
        elif evento in processos_ctypes:
            nome = args[0] if args else None
            if nome:  # dlopen(None) só pega um handle do processo atual (uso interno do Python/libc)
                negar(f"carregamento de biblioteca nativa bloqueado ({evento}: {nome!r})")
        elif evento in ("socket.connect", "socket.bind", "socket.sendto", "socket.sendmsg"):
            if not host_local(host_de(args[1] if len(args) > 1 else None)):
                negar(f"rede bloqueada (somente loopback): {args[1] if len(args) > 1 else '?'}")
        elif evento == "socket.getaddrinfo":
            if not host_local(args[0], passivo=True):
                negar(f"resolução de DNS bloqueada: {args[0]!r}")
        elif evento in ("socket.gethostbyname", "socket.gethostbyaddr"):
            if not host_local(args[0]):
                negar(f"resolução de DNS bloqueada: {args[0]!r}")
        elif evento == "socket.getnameinfo":
            if not host_local(host_de(args[0])):
                negar("resolução de DNS bloqueada")

    def hook(evento, args):
        if getattr(local, "ativo", False):
            return
        local.ativo = True
        try:
            verificar(evento, args)
        finally:
            local.ativo = False

    try:
        import _posixsubprocess

        def _bloqueado(*a, **k):
            negar("criação de processos bloqueada (fork_exec)")

        _posixsubprocess.fork_exec = _bloqueado
    except ImportError:
        pass

    sys.addaudithook(hook)


_instalar()
del _instalar
'''

_EXECUTAR_PYTEST = """
import runpy
runpy.run_module("pytest", run_name="__main__", alter_sys=True)
"""

SANDBOX_DESLIGADO = "MINICODE_SANDBOX"

_SONDA = """
import sys
try:
    open(os.path.expanduser("~/.ssh/__minicode_sonda__"))
except PermissionError:
    sys.exit(0)
except Exception:
    pass
sys.exit(1)
"""


def _aplicar_limites(cpu_segundos: int):
    def aplicar():
        import resource
        resource.setrlimit(resource.RLIMIT_CORE, (0, 0))
        resource.setrlimit(resource.RLIMIT_CPU, (cpu_segundos, cpu_segundos + 5))
        resource.setrlimit(resource.RLIMIT_FSIZE, (100 * 1024 * 1024,) * 2)
        resource.setrlimit(resource.RLIMIT_AS, (4 * 1024 ** 3,) * 2)
    return aplicar


@dataclass
class Contexto:
    root: Path
    caminhos: ValidadorCaminho
    comandos: ValidadorComando
    conteudo: ValidadorConteudo = field(default_factory=ValidadorConteudo)
    timeout: int = 120
    max_saida: int = 8000
    _sandbox_ok: bool = field(default=None, repr=False)

    def comando_pytest(self, extras=()) -> list:
        return [sys.executable, "-c", GUARDA_EXECUCAO + _EXECUTAR_PYTEST, *extras]

    def _spawn(self, argv: list, limite: int, sandbox: bool) -> tuple:
        env = ambiente_seguro()
        env.pop("PYTHONPATH", None)
        env["PYTHONDONTWRITEBYTECODE"] = "1"
        kwargs = {}

        if sandbox:
            tmp = self.root / ".minicode" / "tmp"
            tmp.mkdir(parents=True, exist_ok=True)
            env["MINICODE_SANDBOX_ROOT"] = str(self.root)
            env["TMPDIR"] = env["TMP"] = env["TEMP"] = str(tmp)
            if os.name == "posix":
                kwargs["preexec_fn"] = _aplicar_limites(limite + 10)

        try:
            proc = subprocess.run(
                argv, cwd=self.root, capture_output=True, text=True,
                timeout=limite, env=env, shell=False, **kwargs,
            )
        except subprocess.TimeoutExpired:
            return 124, f"Timeout: o comando excedeu {limite}s e foi interrompido."
        except FileNotFoundError as e:
            return 127, f"Executável não encontrado: {e}"
        return proc.returncode, (proc.stdout or "") + (proc.stderr or "")

    @staticmethod
    def sandbox_desligado() -> bool:
        return os.environ.get(SANDBOX_DESLIGADO, "").lower() == "off"

    def sandbox_ativo(self) -> bool:
        if self.sandbox_desligado():
            return True
        if self._sandbox_ok is None:
            codigo, _ = self._spawn([sys.executable, "-c", GUARDA_EXECUCAO + _SONDA], 20, sandbox=True)
            self._sandbox_ok = codigo == 0
        return self._sandbox_ok

    def rodar(self, argv: list, timeout: int = None, sandbox: bool = False) -> tuple:
        limite = timeout or self.timeout
        if sandbox and self.sandbox_desligado():
            print("⚠️  [Segurança] Guarda de execução DESATIVADA (MINICODE_SANDBOX=off): o código roda sem restrições.")
            sandbox = False
        if sandbox and not self.sandbox_ativo():
            return 126, ("Guarda de execução indisponível: por segurança, o código do projeto não foi executado. "
                         "Use MINICODE_SANDBOX=off apenas para depuração.")

        codigo, saida = self._spawn(argv, limite, sandbox)
        if len(saida) > self.max_saida:
            omitidos = len(saida) - self.max_saida
            saida = f"[... {omitidos} caracteres omitidos ...]\n" + saida[-self.max_saida:]
        return codigo, saida


class Tool:

    nome: str = ""
    descricao: str = ""
    parametros: dict = {}
    obrigatorios: tuple = ()

    def __init__(self, ctx: Contexto):
        self.ctx = ctx

    def run(self, **args) -> dict:
        raise NotImplementedError

    def executar(self, args: dict) -> dict:
        if not isinstance(args, dict):
            return {"ok": False, "saida": "args deve ser um objeto JSON."}

        faltando = [p for p in self.obrigatorios if p not in args]
        if faltando:
            return {"ok": False, "saida": f"Parâmetros obrigatórios ausentes: {faltando}"}

        desconhecidos = [p for p in args if p not in self.parametros]
        if desconhecidos:
            return {
                "ok": False,
                "saida": f"Parâmetros desconhecidos: {desconhecidos}. Aceitos: {list(self.parametros)}",
            }

        try:
            return self.run(**args)
        except ViolacaoSeguranca as e:
            return {"ok": False, "saida": f"BLOQUEADO pela segurança: {e}"}
        except Exception as e:
            return {"ok": False, "saida": f"Erro em {self.nome}: {type(e).__name__}: {e}"}

    def descricao_completa(self) -> str:
        params = ", ".join(
            f"{p}{'' if p in self.obrigatorios else ' (opcional)'}: {d}"
            for p, d in self.parametros.items()
        )
        return f"- {self.nome}({params}) -> {self.descricao}"