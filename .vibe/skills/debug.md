---
name: debug
version: 1.0.0
domain: universal
triggers:
  - erro reportado, stack trace
  - comportamento inesperado
  - "não funciona", "está a dar erro"
requires:
  - mensagem de erro ou descrição do problema
  - contexto de reprodução (quando disponível)
produces:
  - diagnóstico com causa raiz identificada
  - correção proposta
  - teste de regressão
compatible_rules: [RULE-CORE-003, RULE-CORE-004]
---

## OBJETIVO
Identificar a causa raiz de um problema (não apenas o sintoma), corrigi-lo de forma que não regresse.

## PROCESSO INTERNO

### Passo 1 — Coleta de evidências
Reunir: mensagem de erro exata, stack trace, passos para reprodução, ambiente.

### Passo 2 — Geração de hipóteses
Produzir 3-5 hipóteses ordenadas por probabilidade.
Para cada: "Se esta hipótese for verdadeira, esperaría ver X".

### Passo 3 — Teste de hipóteses
Para cada hipótese (da mais para menos provável), testar com evidências concretas.

### Passo 4 — Causa raiz vs sintoma
Distinguir: sintoma (o que aparece) vs causa (o que gerou). Corrigir apenas o sintoma recria o bug.

### Passo 5 — Correção + teste de regressão
Corrigir a causa raiz. O teste de reprodução deve passar após a correção.

## ANTI-PADRÕES
- Corrigir sem entender por que falhou
- Tratar o sintoma e não a causa
- Não criar teste de regressão
- Mudar código "que parece errado" sem evidência
