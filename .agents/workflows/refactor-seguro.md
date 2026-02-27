---
description: Refatorar código de forma segura e incremental sem alterar comportamento externo
---

# WF-CORE-004: Refactor Seguro

> Workflow de alta complexidade. 2 pontos de validação humana.

## Quando Usar
- "Refatore [módulo/função]"
- Código com alta complexidade ciclomática
- Débito técnico identificado

## Etapas

### 1. Diagnóstico
Identificar o problema:
- Alta complexidade ciclomática?
- Acoplamento excessivo?
- Código duplicado?
- Abstrações vazadas?
- Nomenclatura confusa?

### 🔴 VALIDAÇÃO ① — Confirmar objetivo
> "Quero refatorar X para Y. O objetivo é Z. Concordam?"
> Apresentar: o que vai mudar, o que NÃO vai mudar, e por quê.

### 2. Verificar cobertura de testes
Existem testes cobrindo o comportamento a ser refatorado?
- **NÃO** → Escrever testes primeiro (ativar `/feature-development` para testes)
- **SIM** → Continuar

### 3. Snapshot de comportamento
Documentar: inputs/outputs conhecidos, comportamentos de borda.
Estes dados verificam que nada quebrou.

### 4. Refatoração incremental (loop)
Para cada passo:
1. Aplicar **uma mudança de cada vez** (renomear, extrair função, mover responsabilidade)
2. NUNCA múltiplas mudanças simultâneas
3. Verificar: todos os testes passam?
   - **SIM** → Próximo passo
   - **NÃO** → Reverter e analisar

### 5. Comparação antes/depois
- Complexidade ciclomática melhorou?
- Legibilidade melhorou?
- Performance não regrediu?

### 6. Atualização de documentação
Atualizar docstrings, comentários e documentação afetada.

### 🔴 VALIDAÇÃO ② — Apresentar diff final
> Mostrar o diff completo com métricas de melhoria.

## Princípio Fundamental
Refactor = "mudar como o código está escrito sem mudar o que ele faz".
Se comportamento externo mudar → é uma feature (usar `/feature-development`).
