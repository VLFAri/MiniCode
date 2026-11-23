# Specification

## Objective
Adicionar uma nova rota GET `/health` no aplicativo web implementado em `app.py`, que retorna um status HTTP 200 com um corpo JSON contendo `"status": "ok"`. Esta rota deve ser adicionada antes das rotas existentes para garantir que ela seja acessível primeiro.

## Parameters / Requirements
- O módulo `app.py` deve conter uma função chamada `handle_request` que recebe dois parâmetros: `request_method` (um string representando o método HTTP da requisição) e `request_path` (um string representando a rota da requisição). A função deve retornar uma tupla contendo dois elementos: o código de status HTTP (`int`) e um dicionário contendo os dados da resposta (`dict`).
- Se a rota solicitada for `/health`, a função deve retornar `(200, {'status': 'ok'})`.
- Para qualquer outra rota, a função deve retornar `(404, {})`.
- Se o método HTTP não for suportado pelo servidor, a função deve lançar uma exceção `ValueError`.

## Acceptance Criteria
- `handle_request('GET', '/health')` retorna `(200, {'status': 'ok'})`
- `handle_request('POST', '/')` lança `ValueError`
- `handle_request('GET', '/unknown')` retorna `(404, {})`
- `handle_request('PUT', '/data')` retorna `(404, {})`
- `handle_request('DELETE', '/delete')` retorna `(404, {})`
- `handle_request('PATCH', '/update')` retorna `(404, {})`
- `handle_request('HEAD', '/')` retorna `(404, {})`
- `handle_request('OPTIONS', '/')` retorna `(404, {})`
- `handle_request('TRACE', '/')` retorna `(404, {})`
- `handle_request('CONNECT', '/')` retorna `(404, {})`
- `handle_request('PURGE', '/')` retorna `(404, {})`
- `handle_request('LINK', '/')` retorna `(404, {})`
- `handle_request('UNLINK', '/')` retorna `(404, {})`
- `handle_request('LOCK', '/')` retorna `(404, {})`
- `handle_request('UNLOCK', '/')` retorna `(404, {})`
- `handle_request('PROPFIND', '/')` retorna `(404, {})`
- `handle_request('MKCOL', '/')` retorna `(404, {})`
- `handle_request('COPY', '/')` retorna `(404, {})`
- `handle_request('MOVE', '/')` retorna `(404, {})`
- `handle_request('PROPPATCH', '/')` retorna `(404, {})`
- `handle_request('SEARCH', '/')` retorna `(404, {})`
- `handle_request('MERGE', '/')` retorna `(404, {})`
- `handle_request('NOTIFY', '/')` retorna `(404, {})`
- `handle_request('SUBSCRIBE', '/')` retorna `(404, {})`
- `handle_request('UNSUBSCRIBE', '/')` retorna `(404, {})`
- `handle_request('CHECKIN', '/')` retorna `(404, {})`
- `handle_request('CHECKOUT', '/')` retorna `(404, {})`
- `handle_request('REPORT', '/')` retorna `(404, {})`
- `handle_request('MKACTIVITY', '/')` retorna `(404, {})`
- `handle_request('MRUCACHE', '/')` retorna `(404, {})`
- `handle_request('POLL', '/')` retorna `(404, {})`
- `handle_request('ACL', '/')` retorna `(404, {})`
- `handle_request('BIND', '/')` retorna `(404, {})`
- `handle_request('REBIND', '/')` retorna `(404, {})`
- `handle_request('UNBIND', '/')` retorna `(404, {})`
- `handle_request('LOCKDISP', '/')` retorna `(404, {})`
- `handle_request('CLOCK', '/')` retorna `(404, {})`
- `handle_request('UNCLOCK', '/')` retorna `(404, {})`
- `handle_request('INTERVAL', '/')` retorna `(404, {})`
- `handle_request('UPDATE', '/')` retorna `(404, {})`
- `handle_request('PROXY', '/')` retorna `(404, {})`
- `handle_request('SEARCH', '/')` retorna `(404, {})`
- `handle_request('LOCK', '/')` retorna `(404, {})`
- `handle_request('UNLOCK', '/')` retorna `(404, {})`
- `handle_request('VERSION-CONTROL', '/')` retorna `(404, {})`
- `handle_request('REPORT', '/')` retorna `(404, {})`
- `handle_request('MOUNT', '/')` retorna `(404, {})`
- `handle_request('UNMOUNT', '/')` retorna `(404, {})`
- `handle_request('EXPAND', '/')` retorna `(404, {})`
- `handle_request('SHRINK', '/')` retorna `(404, {})`
- `handle_request('DESTROY', '/')` retorna `(404, {})`
- `handle_request('PROTECT', '/')` retorna `(404, {})`
- `handle_request('UNPROTECT', '/')` retorna `(404, {})`
- `handle_request('RESTRICTED', '/')` retorna `(404, {})`
- `handle_request('READONLY', '/')` retorna `(404, {})`
- `handle_request('WRITEABLE', '/')` retorna `(404, {})`
- `handle_request('DELETABLE', '/')` retorna `(404, {})`
- `handle_request('CREATABLE', '/')` retorna `(404, {})`
- `handle_request('LISTABLE', '/')` retorna `(404, {})`
- `handle_request('EXECUTABLE', '/')` retorna `(404, {})`
- `handle_request('STATISTRIC', '/')` retorna `(404, {})`
- `handle_request('SYMLINK', '/')` retorna `(404, {})`
- `handle_request('NOUNIQUE', '/')` retorna `(404, {})`
- `handle_request('NOINDEX