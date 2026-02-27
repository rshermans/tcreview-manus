# VIBE CODE INDEX
> Índice vivo de agentes do projeto. Mantenha este arquivo atualizado.
> *Última atualização: [data]*

---

## DNA DO PROJETO

```yaml
project_name: "TrueCheck"
domain: "fact-checking / news-verification SaaS"
phase: "scaling / refactor"

stack:
  frontend: "React + Vite + Tailwind CSS + TypeScript"
  backend: "Python + Flask"
  database: "N/A (to be defined - currently API driven analysis)"
  infra: "Local dev setup currently"

architecture: "Client-Server (REST API)"
team_level: "mixed"

conventions:
  naming: "camelCase para JS/TS, snake_case para Python"
  tests: "Playwright para E2E"
  api_style: "REST"
  error_handling: "Retorno padronizado JSON com descritivo claro"
  
dna_version: "1.0.0"
```

---

## SKILLS ATIVAS

| ID     | Nome                   | Domínio    | Trigger Principal                        | Status |
|--------|------------------------|------------|------------------------------------------|--------|
| SK-001 | code-generation        | universal  | Toda geração de código                   | stable |
| SK-002 | test-generation        | universal  | Após code-generation, pedido de testes   | stable |
| SK-003 | code-review            | universal  | Revisão de código, PR aberto             | stable |
| SK-004 | debug                  | universal  | Erros, comportamento inesperado          | stable |
| SK-005 | security-audit         | security   | Código com inputs externos, auth         | stable |
| SK-006 | documentation          | universal  | Após implementação, docs desatualizados  | stable |
| SK-007 | context-scanner        | meta       | Início de sessão, onboarding             | stable |
| SK-008 | agent-factory          | meta       | Padrão repetitivo, necessidade nova      | stable |
| SK-009 | refactor               | universal  | Débito técnico, alta complexidade        | stable |
<!-- Adicione novas skills abaixo conforme são criadas pelo agent-factory -->

---

## RULES ATIVAS

| ID              | Princípio                        | Prioridade | Escopo       |
|-----------------|----------------------------------|------------|--------------|
| RULE-CORE-001   | Fidelidade ao DNA do projeto     | critical   | global       |
| RULE-CORE-002   | Mínimo de Surpresa               | high       | global       |
| RULE-CORE-003   | Evidência antes de Ação          | high       | global       |
| RULE-CORE-004   | Segurança por Padrão             | critical   | global       |
| RULE-CORE-005   | Reversibilidade                  | medium     | global       |
| RULE-CORE-006   | Documentação Acoplada            | medium     | global       |
| RULE-CORE-007   | Composição sobre Monólito        | medium     | global       |
<!-- Rules de domínio são adicionadas abaixo conforme o projeto -->
<!-- Ex: RULE-FIN-001 | Sem magic numbers financeiros | high | fintech -->

---

## WORKFLOWS ATIVOS

| ID            | Nome                    | Trigger                          | Complexidade | Validação Humana |
|---------------|-------------------------|----------------------------------|-------------|-----------------|
| WF-CORE-001   | Feature Development     | Nova feature, user story         | high        | 3 pontos        |
| WF-CORE-002   | Debug Investigation     | Bug, erro, comportamento estranho| medium      | 2 pontos        |
| WF-CORE-003   | Code Review Profundo    | PR aberto, revisão solicitada    | medium      | não             |
| WF-CORE-004   | Refactor Seguro         | Débito técnico, complexidade alta| high        | 2 pontos        |
| WF-META-001   | Agent Genesis           | Padrão repetitivo, gap detectado | medium      | 1 ponto         |
| WF-META-002   | Context Sync            | Início de sessão, mudança major  | low         | não             |
<!-- Adicione workflows específicos do projeto abaixo -->

---

## HISTÓRICO DE EVOLUÇÃO

```
v0.1.0 — [data] — Inicialização do framework com agentes core
v0.2.0 — [data] — [Skills/Rules/Workflows adicionados e motivo]
```

---

## DECISÕES ARQUITETURAIS REGISTRADAS

| Data | Decisão | Alternativa Considerada | Racional |
|------|---------|------------------------|----------|
| [data] | [o que foi decidido] | [o que foi rejeitado] | [por que] |

---

*Este arquivo é mantido pelo `agent-factory` e pelo time. Não apague entradas — marque como `deprecated` quando necessário.*
