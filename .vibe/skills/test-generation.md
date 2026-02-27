---
name: test-generation
version: 1.0.0
domain: universal
triggers:
  - após geração de código
  - "teste", "spec", "coverage", "TDD"
requires:
  - código a ser testado
  - DNA do projeto (framework de testes — Playwright para E2E)
produces:
  - testes unitários
  - testes de integração (quando aplicável)
  - descrição da estratégia de testes adotada
compatible_rules: [RULE-CORE-001, RULE-CORE-004]
---

## OBJETIVO
Gerar testes que documentam o comportamento esperado e previnem regressões.

## PROCESSO INTERNO

### Passo 1 — Mapear comportamentos
Listar: casos felizes, casos de erro, edge cases, estados de fronteira.
Um teste por comportamento — não por linha de código.

### Passo 2 — Nomenclatura descritiva
"should return error when input is negative" — nunca "test1" ou "testCalc".
O nome do teste é documentação executável.

### Passo 3 — Estrutura AAA
Arrange (preparar estado) → Act (executar) → Assert (verificar).
Cada seção claramente separada.

### Passo 4 — Independência
Cada teste deve poder rodar isolado. Sem dependência de ordem de execução.

## ANTI-PADRÕES
- Testar detalhes de implementação (não comportamento)
- Testes que só passam na máquina do dev
- Mock de tudo — quando possível, usar implementações reais
- Um teste que verifica múltiplas coisas não relacionadas
