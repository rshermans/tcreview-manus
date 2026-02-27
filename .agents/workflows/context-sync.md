---
description: Sincronizar contexto do projeto no início de sessão ou após mudanças significativas
---

# WF-META-002: Context Sync

> Workflow de baixa complexidade. Sem validação humana obrigatória.

## Quando Usar
- Início de uma nova sessão de trabalho
- Após mudança significativa (nova dependência, novo módulo, refator grande)
- Quando algo parece desalinhado com o DNA do projeto

## Etapas

### 1. Ler DNA atual
Ler `.vibe/project_dna.yaml` e `.vibe/VIBE_INDEX.md`.

### 2. Varrer sinais de mudança
Verificar:
- `package.json` e `requirements.txt` — novas dependências?
- Estrutura de diretórios — novos módulos ou pastas?
- Mudança de framework ou padrão?

### 3. Avaliar se DNA precisa de atualização
Se mudanças significativas foram detectadas → atualizar `project_dna.yaml`.
Se não → DNA atual é válido, continuar.

### 4. Verificar agentes ativos
Algum agente ficou obsoleto? Algum novo agente é necessário?
Consultar `.vibe/VIBE_INDEX.md`.

### 5. Atualizar VIBE_INDEX se necessário
Registrar novas skills/rules/workflows ou marcar como `deprecated` os obsoletos.

## Output
- `project_dna.yaml` atualizado (se necessário)
- `VIBE_INDEX.md` atualizado (se necessário)
- Resumo das mudanças detectadas
