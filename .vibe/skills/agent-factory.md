---
name: agent-factory
version: 1.0.0
domain: meta
triggers:
  - padrão repetitivo identificado (3+ ocorrências)
  - capacidade não coberta por skills existentes
  - "crie uma skill para", "adicione uma rule que", "workflow para"
requires:
  - DNA do projeto capturado
  - índice de agentes existentes (VIBE_INDEX.md)
produces:
  - nova Skill, Rule ou Workflow
  - entrada no VIBE_INDEX.md
  - 3 casos de teste para o novo agente
compatible_rules: [RULE-CORE-001, RULE-CORE-007]
---

## OBJETIVO
Expandir o framework com novos agentes que são coerentes com o DNA do projeto.

## PROCESSO INTERNO

### Passo 1 — Diagnóstico da necessidade
"O que está faltando? É uma capacidade (Skill), uma restrição (Rule) 
ou um fluxo de execução (Workflow)?"

### Passo 2 — Verificação de duplicidade
Consultar VIBE_INDEX.md: existe algo similar? Seria melhor especializar 
um agente existente do que criar um novo?

### Passo 3 — Estruturação usando templates
Usar o template do tipo correto (ver catálogos em `.vibe/skills/`, `.vibe/rules/`, `.vibe/workflows/`).
Preencher todos os campos obrigatórios.

### Passo 4 — Teste de coerência
O novo agente viola alguma Rule existente?
Ele é compatível com os Workflows ativos?
O nome é claro e não ambíguo?

### Passo 5 — Proposta para validação
Apresentar o novo agente ao time antes de oficializar.
Incluir: propósito, exemplos de uso, impacto nos agentes existentes.

### Passo 6 — Registo
Adicionar ao VIBE_INDEX.md e criar ficheiro individual na pasta correta.

## ANTI-PADRÕES
- Criar agentes muito genéricos que fazem muitas coisas
- Duplicar capacidades já existentes com nome diferente
- Criar agentes sem pelo menos um caso de uso concreto
- Não registrar no VIBE_INDEX.md após criação
