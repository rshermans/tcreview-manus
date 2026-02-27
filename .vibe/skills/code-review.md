---
name: code-review
version: 1.0.0
domain: universal
triggers:
  - PR aberto, "revise este código"
  - code review solicitado
  - antes de merge
requires:
  - código a ser revisado
  - DNA do projeto
produces:
  - relatório categorizado (BLOQUEADOR / MELHORIA / ELOGIO)
  - sugestões de correção concretas
compatible_rules: [RULE-CORE-001, RULE-CORE-004, RULE-CORE-007]
---

## OBJETIVO
Produzir uma revisão de código que vai além de estilo — que identifica problemas de lógica, segurança, performance e manutenibilidade.

## PROCESSO INTERNO

### Passo 1 — Entendimento do propósito
"O que este código deveria fazer?" → "Ele faz o que se propõe?"

### Passo 2 — Análise estrutural
Separação de responsabilidades adequada? Acoplamento? Pode ser testado isoladamente?

### Passo 3 — Análise de lógica
Algoritmos corretos? Edge cases tratados? (null, empty, negative, overflow)

### Passo 4 — Análise de segurança (RULE-CORE-004)
Inputs validados? Dados sensíveis protegidos? Queries parametrizadas?

### Passo 5 — Análise de performance
Queries N+1? Operações desnecessariamente síncronas? Dados grandes em memória?

### Passo 6 — Análise de conformidade ao DNA
Nomenclatura alinhada? Padrões de erro consistentes? Estilo de comentários?

## SAÍDA ESPERADA
Relatório com três seções: **BLOQUEADOR** (impede merge), **MELHORIA** (considerar), **ELOGIO** (boas práticas a repetir).

## ANTI-PADRÕES
- Revisão que só comenta estilo/formatação
- Não verificar segurança em código com inputs externos
- Não reconhecer boas práticas (elogios calibram o time)
