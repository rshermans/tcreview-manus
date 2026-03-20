# VIBE CODE INDEX
> Índice vivo de agentes do projeto TrueCheck. Mantenha este ficheiro atualizado.
> *Última atualização: 2026-02-26*

---

## DNA DO PROJETO

📁 **Ficheiro completo**: [project_dna.yaml](file:///.vibe/project_dna.yaml)

```yaml
project_name: "TrueCheck"
domain: "fact-checking / news-verification SaaS"
phase: "scaling / refactor"
stack:
  frontend: "React + Vite + Tailwind CSS + TypeScript"
  backend: "Python + Flask"
architecture: "Client-Server (REST API)"
dna_version: "1.1.0"
```

---

## SKILLS ATIVAS

### Core (Universais)

| ID     | Nome                   | Domínio    | Trigger                                  | Ficheiro | Status |
|--------|------------------------|------------|------------------------------------------|----------|--------|
| SK-001 | code-generation        | universal  | Toda geração de código                   | `skills/code-generation.md` | stable |
| SK-002 | test-generation        | universal  | Após code-generation, pedido de testes   | `skills/test-generation.md` | stable |
| SK-003 | code-review            | universal  | Revisão de código, PR aberto             | `skills/code-review.md` | stable |
| SK-004 | debug                  | universal  | Erros, comportamento inesperado          | `skills/debug.md` | stable |
| SK-005 | security-audit         | security   | Código com inputs externos, auth         | `skills/security-audit.md` | stable |
| SK-006 | documentation          | universal  | Após implementação, docs desatualizados  | `skills/documentation.md` | stable |
| SK-007 | context-scanner        | meta       | Início de sessão, onboarding             | `skills/context-scanner.md` | stable |
| SK-008 | agent-factory          | meta       | Padrão repetitivo, necessidade nova      | `skills/agent-factory.md` | stable |
| SK-009 | refactor               | universal  | Débito técnico, alta complexidade        | `skills/refactor.md` | stable |

### Domínio TrueCheck

| ID       | Nome                   | Domínio       | Trigger                                    | Ficheiro | Status |
|----------|------------------------|---------------|--------------------------------------------|----------|--------|
| SK-TC-001 | fact-check            | fact-checking | Verificação de factos, análise de conteúdo | `skills/fact-check.md` | beta |
| SK-TC-002 | source-credibility    | fact-checking | Avaliação de fontes, URLs                  | `skills/source-credibility.md` | beta |
| SK-TC-003 | pedagogical-insights  | education     | Geração de insights educativos             | `skills/pedagogical-insights.md` | beta |

---

## RULES ATIVAS

### Core

| ID              | Princípio                        | Prioridade | Escopo       |
|-----------------|----------------------------------|------------|--------------|
| RULE-CORE-001   | Fidelidade ao DNA do projeto     | critical   | global       |
| RULE-CORE-002   | Mínimo de Surpresa               | high       | global       |
| RULE-CORE-003   | Evidência antes de Ação          | high       | global       |
| RULE-CORE-004   | Segurança por Padrão             | critical   | global       |
| RULE-CORE-005   | Reversibilidade                  | medium     | global       |
| RULE-CORE-006   | Documentação Acoplada            | medium     | global       |
| RULE-CORE-007   | Composição sobre Monólito        | medium     | global       |

### Domínio TrueCheck

| ID              | Princípio                                              | Prioridade | Escopo         |
|-----------------|---------------------------------------------------------|------------|----------------|
| RULE-TC-001     | Trust scores são sempre percentuais inteiros (0-100)    | high       | fact-checking  |
| RULE-TC-002     | Análise nunca afirma verdade absoluta — sempre graus    | critical   | fact-checking  |
| RULE-TC-003     | Fontes são categorizadas por credibilidade antes de uso | high       | fact-checking  |
| RULE-TC-004     | Insights pedagógicos são neutros e baseados em evidência| high       | education      |

---

## WORKFLOWS ATIVOS

| ID            | Nome                    | Trigger                          | Complexidade | Validação Humana | Ficheiro Gemini |
|---------------|-------------------------|----------------------------------|-------------|-----------------|-----------------|
| WF-META-002   | Context Sync            | Início de sessão, mudança major  | low         | não             | `.agents/workflows/context-sync.md` |
| WF-CORE-001   | Feature Development     | Nova feature, user story         | high        | 3 pontos        | `.agents/workflows/feature-development.md` |
| WF-CORE-002   | Debug Investigation     | Bug, erro, comportamento estranho| medium      | 2 pontos        | `.agents/workflows/debug-investigation.md` |
| WF-CORE-003   | Code Review Profundo    | PR aberto, revisão solicitada    | medium      | não             | `.agents/workflows/code-review.md` |
| WF-CORE-004   | Refactor Seguro         | Débito técnico, complexidade alta| high        | 2 pontos        | `.agents/workflows/refactor-seguro.md` |
| WF-META-001   | Agent Genesis           | Padrão repetitivo, gap detectado | medium      | 1 ponto         | `.agents/workflows/agent-genesis.md` |

---

## HISTÓRICO DE EVOLUÇÃO

```
v0.1.0 — 2026-02-20 — Inicialização do framework com agentes core (documentação)
v1.0.0 — 2026-02-26 — Estruturação .vibe/ com skills individuais, rules de domínio TrueCheck,
                        project_dna.yaml standalone, e preparação para .agents/workflows/
```

---

## DECISÕES ARQUITETURAIS REGISTRADAS

| Data | Decisão | Alternativa Considerada | Racional |
|------|---------|------------------------|----------|
| 2026-02-26 | Separar `.vibe/` (documentação) de `.agents/` (execução) | Tudo junto em `.vibe/` | `.agents/workflows/` é a convenção Gemini para slash commands e workflows executáveis |
| 2026-02-26 | Skills de domínio TrueCheck (SK-TC-*) separadas das core | Incluir no catálogo genérico | Domínio fact-checking tem necessidades específicas que justificam skills dedicadas |
| 2026-02-26 | Rules TrueCheck com foco em "graus de verdade" vs "verdade absoluta" | Rule genérica de outputs | Fact-checking responsável nunca afirma verdade absoluta — é princípio fundacional |

---

*Este ficheiro é mantido pelo `agent-factory` e pelo time. Não apague entradas — marque como `deprecated` quando necessário.*
