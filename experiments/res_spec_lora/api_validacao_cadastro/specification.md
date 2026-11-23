# Specification

## Objective
Implementar uma função que registre usuários com validações específicas sobre os dados fornecidos.

## Parameters / Requirements
A função `cadastrar` recebe dois parâmetros: `nome` e `email`. Ambos são strings. A função deve validar os seguintes requisitos:
1. O nome não pode estar vazio após remoção de espaços nas extremidades.
2. O e-mail deve seguir o formato padrão (`algo@dominio.ext`) sem espaços.
3. O e-mail deve ser único, ignorando maiúsculas.

Se qualquer desses requisitos for violado, a função deve lançar uma exceção `ValueError`.

A função deve retornar um dicionário contendo os dados do usuário registrado, incluindo o e-mail convertido para minúsculas.

## Acceptance Criteria
- `cadastrar("João", "joao@example.com")` retorna `{ 'nome': 'João', 'email': 'joao@example.com' }`
- `cadastrar("", "joao@example.com")` lança `ValueError('Nome não pode estar vazio')`
- `cadastrar("João", "joao@exampel.com")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@EXAMPLE.COM")` lança `ValueError('Email já existente')`
- `cadastrar("João", "joao@examplo.co.uk")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.org")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.net")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.info")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.biz")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.us")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.ca")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.co")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.io")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.museum")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.edu")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.school")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.college")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.institute")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.foundation")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.network")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.space")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.planet")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.star")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.starsystem")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.universe")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.cosmos")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.photon")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.light")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.energy")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.force")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.gravity")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.time")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.speed")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.distance")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.magnitude")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.concentration")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.intensity")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.flux")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.power")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.current")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.voltage")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.resistance")` lança `ValueError('Email inválido')`
- `cadastrar("João", "joao@examplo.capacitance")` lança `