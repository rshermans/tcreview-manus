---
name: refactor
version: 1.0.0
domain: universal
triggers:
  - "refatore", código com alta complexidade
  - débito técnico identificado
  - complexidade ciclomática alta
requires:
  - código a ser refatorado
  - testes existentes (ou criá-los primeiro)
produces:
  - código reestruturado sem mudança de comportamento
  - comparação antes/depois (complexidade, legibilidade)
compatible_rules: [RULE-CORE-001, RULE-CORE-005, RULE-CORE-007]
---

## OBJETIVO
Melhorar o design interno do código sem alterar seu comportamento externo observável.

## PROCESSO INTERNO

### Passo 1 — Diagnóstico
Qual é o problema? Alta complexidade ciclomática? Acoplamento? Código duplicado? Abstrações vazadas?

### Passo 2 — Garantir cobertura de testes
Existem testes? Se não → criá-los primeiro (ativar SK-002 test-generation).

### Passo 3 — Snapshot de comportamento
Documentar: inputs/outputs conhecidos, comportamentos de borda.

### Passo 4 — Refatoração incremental
Uma mudança de cada vez. NUNCA múltiplas mudanças simultâneas.
Após cada passo: todos os testes passam?

### Passo 5 — Comparação
Complexidade melhorou? Legibilidade melhorou? Performance não regrediu?

## PRINCÍPIO FUNDAMENTAL
Refactor = "mudar como o código está escrito sem mudar o que ele faz". 
Se qualquer comportamento externo mudar, isso é uma feature (WF-CORE-001), não um refactor.

## ANTI-PADRÕES
- Refatorar sem testes (refatorar às cegas)
- Múltiplas mudanças simultâneas
- Mudar comportamento durante refator
- Não comparar antes/depois
