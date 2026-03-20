# 🧠 VIBE CODE — MASTER SKILL
> Framework Meta-Inteligente de Engenharia de Código para Agentes Dinâmicos

---

## IDENTIDADE DO FRAMEWORK

Este é o **núcleo operacional** do sistema Vibe Code. Sua função é compreender o contexto completo de qualquer projeto — linguagem, arquitetura, domínio, padrões — e a partir disso **gerar, compor e evoluir** Skills, Rules e Workflows compatíveis com o trabalho em curso.

Pense nele como o "sistema nervoso central": ele não apenas executa tarefas — ele aprende o DNA do projeto e cria novos agentes especializados que compartilham essa mesma essência.

---

## ANATOMIA DO FRAMEWORK

O sistema é composto por três camadas interdependentes:

```
┌─────────────────────────────────────────────────────────────┐
│                    CAMADA META (MASTER)                     │
│     Lê contexto → Gera agentes → Orquestra execução         │
├──────────────────┬──────────────────┬───────────────────────┤
│   SKILLS         │    RULES         │    WORKFLOWS           │
│  O QUE fazer     │  COMO se portar  │  QUANDO e em que ordem │
│  (capacidades)   │  (restrições)    │  (fluxo de execução)   │
├──────────────────┴──────────────────┴───────────────────────┤
│                    CAMADA DE CONTEXTO                       │
│   Stack · Arquitetura · Domínio · Convenções · História     │
└─────────────────────────────────────────────────────────────┘
```

### Referências de Ficheiros

| Recurso | Localização |
|---------|-------------|
| DNA do Projeto | `.vibe/project_dna.yaml` |
| Índice Vivo | `.vibe/VIBE_INDEX.md` |
| Skills | `.vibe/skills/` |
| Rules | `.vibe/rules/` |
| Workflows | `.vibe/workflows/` |
| Workflows Executáveis | `.agents/workflows/` |

---

## FASE 0 — LEITURA DE CONTEXTO (OBRIGATÓRIA)

Antes de qualquer ação, o agente DEVE:

1. Ler `.vibe/project_dna.yaml` para captar o DNA do projeto
2. Ler `.vibe/VIBE_INDEX.md` para conhecer os agentes ativos
3. Identificar qual Workflow se aplica à tarefa atual
4. Ativar as Skills necessárias na ordem correta
5. Seguir as Rules ativas — especialmente as CRITICAL

### Sinais Implícitos de Contexto
- Extensões de arquivo → inferir linguagem e framework
- Nomenclatura de variáveis/funções → inferir convenções do time
- Estrutura de pastas → inferir arquitetura
- Mensagens de erro → inferir ambiente de execução

---

## FASE 1 — SKILLS (Capacidades Especializadas)

Skills são capacidades atômicas e reutilizáveis. Cada uma faz **uma coisa** e faz bem.

### Skills Core (Sempre Ativas)
| ID | Ficheiro | Função |
|----|----------|--------|
| SK-001 | `skills/code-generation.md` | Geração de código alinhado ao DNA |
| SK-002 | `skills/test-generation.md` | Criação de testes |
| SK-003 | `skills/code-review.md` | Revisão crítica de código |
| SK-004 | `skills/debug.md` | Análise e correção de erros |
| SK-005 | `skills/security-audit.md` | Audit de segurança |
| SK-006 | `skills/documentation.md` | Documentação contextualizada |
| SK-007 | `skills/context-scanner.md` | Varredura de contexto e DNA |
| SK-008 | `skills/agent-factory.md` | Criação de novos agentes |
| SK-009 | `skills/refactor.md` | Refatoração segura |

### Skills de Domínio TrueCheck
| ID | Ficheiro | Função |
|----|----------|--------|
| SK-TC-001 | `skills/fact-check.md` | Verificação de factos via LLM |
| SK-TC-002 | `skills/source-credibility.md` | Avaliação de credibilidade de fontes |
| SK-TC-003 | `skills/pedagogical-insights.md` | Geração de insights pedagógicos |

---

## FASE 2 — RULES (Restrições e Princípios)

Rules definem **como o agente deve se comportar**. São guardrails, não sugestões.

### Hierarquia
```
CRITICAL  → Violação para o trabalho imediatamente
HIGH      → Violação exige revisão antes de continuar
MEDIUM    → Violação gera alerta mas não bloqueia
LOW       → Sugestão — pode ser ignorada conscientemente
```

Ver: `.vibe/rules/RULES_CATALOG.md`

---

## FASE 3 — WORKFLOWS (Fluxos de Execução)

Workflows coordenam múltiplas Skills numa sequência definida.

### Workflows Executáveis
| ID | Ficheiro Gemini | Trigger |
|----|----------------|---------|
| WF-META-002 | `.agents/workflows/context-sync.md` | Início de sessão |
| WF-CORE-001 | `.agents/workflows/feature-development.md` | Nova feature |
| WF-CORE-002 | `.agents/workflows/debug-investigation.md` | Bug reportado |
| WF-CORE-003 | `.agents/workflows/code-review.md` | PR aberto |
| WF-CORE-004 | `.agents/workflows/refactor-seguro.md` | Débito técnico |
| WF-META-001 | `.agents/workflows/agent-genesis.md` | Padrão repetitivo |

---

## FASE 4 — AGENT FACTORY (Motor de Crescimento)

Quando o agente identifica um padrão repetitivo (3+ vezes) ou uma necessidade não coberta, ativa `skill/agent-factory` para propor um novo agente.

---

## FASE 5 — ORQUESTRAÇÃO

### Padrões de Comunicação
- **Pipeline**: `skill A → skill B → skill C`
- **Fork**: `skill A → [skill B, skill C, skill D]` (paralelo)
- **Guard**: `skill A → RULE check → continuar ou rever`
- **Loop**: `workflow → condição não atingida → repete`

---

## MANIFESTO

1. **Contexto é Soberano** — Nenhuma decisão sem entender o ambiente
2. **Composição sobre Complexidade** — Agentes pequenos, combinados
3. **Reversibilidade como Virtude** — Projete para poder desfazer
4. **Evolução Dirigida por Evidências** — Agentes nascem de padrões observados
5. **Humano no Loop** — Decisões arquiteturais passam por validação humana

---

*Este é um documento vivo. Evolua-o conforme o projeto cresce.*
