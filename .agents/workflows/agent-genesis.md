---
description: Criar um novo agente (Skill, Rule ou Workflow) que expande o framework de forma coerente
---

# WF-META-001: Agent Genesis

> Workflow de complexidade média. 1 ponto de validação humana.

## Quando Usar
- Padrão repetitivo identificado (3+ vezes)
- Necessidade não coberta pelos agentes existentes
- "Crie uma skill para...", "Adicione uma rule que...", "Workflow para..."

## Etapas

### 1. Identificar necessidade
- Qual padrão se repete?
- Qual problema o novo agente resolve?
- "Tenho feito X manualmente N vezes — isso deveria ser uma Skill"

### 2. Classificar tipo
- É uma **capacidade** → Skill (`.vibe/skills/`)
- É uma **restrição ou princípio** → Rule (`.vibe/rules/`)
- É um **fluxo de execução** → Workflow (`.vibe/workflows/` + `.agents/workflows/`)

### 3. Verificar duplicidade
Consultar `.vibe/VIBE_INDEX.md`:
- Existe algo similar?
- É melhor especializar do que criar?

### 4. Estruturar usando template
- Skill → usar template de `.vibe/skills/SKILLS_CATALOG.md`
- Rule → usar template de `.vibe/rules/RULES_CATALOG.md`
- Workflow → usar template de `.vibe/workflows/WORKFLOWS_CATALOG.md`
- Preencher TODOS os campos, incluindo anti-padrões e exceções

### 5. Validar coerência
- Viola alguma Rule existente?
- É compatível com Workflows ativos?
- Nome claro e sem conflitos?

### 6. Criar casos de teste
Escrever 3 cenários concretos: input → processo esperado → output esperado.

### 🔴 VALIDAÇÃO ① — Apresentar ao time
> Incluir: propósito, exemplos, impacto em agentes existentes.

### 7. Registrar
- Criar ficheiro na pasta correta (`.vibe/skills/`, `.vibe/rules/`, ou `.agents/workflows/`)
- Adicionar entrada no `.vibe/VIBE_INDEX.md`

## Output
- Novo agente criado e registrado
- VIBE_INDEX.md atualizado
