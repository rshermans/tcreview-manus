---
name: documentation
version: 1.0.0
domain: universal
triggers:
  - após implementação de feature ou correção
  - documentação desatualizada detectada
  - "documenta", "README", "docstring"
requires:
  - código implementado
  - DNA do projeto 
produces:
  - JSDoc/docstrings atualizados
  - README ou wiki se impacto for maior
  - ADR (Architecture Decision Record) quando aplicável
compatible_rules: [RULE-CORE-006]
---

## OBJETIVO
Gerar documentação que responde perguntas antes que sejam feitas. O "porquê" é mais valioso que o "o quê".

## PROCESSO INTERNO

### Passo 1 — Identificar o que precisa de documentação
Funções públicas sem docstring? README desatualizado? Decisão arquitetural não registrada?

### Passo 2 — Gerar documentação contextualizada
- **Funções**: JSDoc/docstring com propósito, parâmetros e casos de erro
- **Módulos**: README com propósito, como usar, dependências
- **Decisões**: ADR com contexto, alternativas, racional

### Passo 3 — Verificar completude
TODOs têm contexto? Comentários explicam "porquê" e não "o quê"?

## ANTI-PADRÕES
- Comentários que repetem o código ("incrementa i" acima de `i++`)
- Documentação genérica que não ajuda ninguém
- TODOs sem contexto ou referência
