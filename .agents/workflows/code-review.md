---
description: Revisão profunda de código focada em lógica, segurança, performance e conformidade ao DNA
---

# WF-CORE-003: Code Review Profundo

> Workflow de complexidade média. Sem validação humana (o próprio workflow é a revisão).

## Quando Usar
- PR aberto
- "Revise este código"
- Code review solicitado

## Etapas

### 1. Entendimento do propósito
- "O que este código deveria fazer?"
- "Ele faz o que se propõe?"

### 2. Análise estrutural
- Separação de responsabilidades adequada?
- Acoplamento — módulo pode ser testado isoladamente?
- Abstrações fazem sentido? Over-engineering?

### 3. Análise de lógica
- Algoritmos corretos?
- Edge cases tratados? (null, empty, negative, overflow)
- Condições de corrida em código concorrente?

### 4. Análise de segurança (RULE-CORE-004)
- Inputs validados antes de uso?
- Dados sensíveis protegidos?
- Queries parametrizadas?
- Autorização verificada onde necessário?

### 5. Análise de performance
- Queries N+1?
- Operações desnecessariamente síncronas?
- Dados grandes em memória?

### 6. Análise de testabilidade
- Cobertura existente adequada?
- Casos críticos sem teste?
- Testes testam comportamento ou implementação?

### 7. Conformidade ao DNA
Verificar contra `.vibe/project_dna.yaml`:
- Nomenclatura alinhada? (camelCase JS, snake_case Python)
- Padrões de erro consistentes?
- Estilo de comentários compatível?

### 8. Relatório final
Produzir relatório com 3 categorias:

| Categoria | Significado |
|-----------|-------------|
| 🔴 **BLOQUEADOR** | Impede merge — segurança, bugs, violações críticas |
| 🟡 **MELHORIA** | Vale considerar mas não bloqueia |
| 🟢 **ELOGIO** | Boas práticas que o time deve repetir |
