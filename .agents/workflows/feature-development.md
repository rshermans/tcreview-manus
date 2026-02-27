---
description: Implementar uma nova funcionalidade de forma estruturada com 3 pontos de validação humana
---

# WF-CORE-001: Feature Development

> Workflow de alta complexidade. 3 pontos de validação humana.

## Quando Usar
- "Implemente [feature]"
- Nova user story ou ticket de desenvolvimento
- Qualquer funcionalidade nova

## Pré-condições
- Requisito suficientemente claro
- DNA do projeto capturado (executar `/context-sync` se necessário)

## Etapas

### 1. Capturar e confirmar requisito
Reformular o requisito com palavras próprias:
"Entendo que preciso de X que faz Y quando Z. Correto?"

### 🔴 VALIDAÇÃO ① — Time confirma entendimento
> Pausar e aguardar confirmação antes de continuar.
> Erros de entendimento aqui custam minutos; no final custam horas.

### 2. Design de interfaces
Definir: tipos de dados, assinaturas de funções, contratos de API.
Nenhum código de implementação ainda — apenas contratos.

### 3. Decisão arquitetural
Se existem 2+ abordagens viáveis:

### 🔴 VALIDAÇÃO ② — Apresentar trade-offs
> Apresentar opções com prós/contras. Aguardar escolha do time.
> O agente não tem visibilidade do roadmap ou limitações de negócio.

Se existe apenas uma abordagem → continuar, documentando o racional.

### 4. Implementação — lógica core
- Apenas regras de negócio, sem I/O
- Funções puras quando possível
- Seguir convenções: camelCase (JS/TS), snake_case (Python)

### 5. Implementação — camada de infraestrutura
- Conectar com APIs, serviços externos
- Tratamento de erros padronizado (JSON)
- Casos de borda

### 6. Geração de testes
Ativar skill `test-generation`:
- Unitários para lógica core
- Integração para fluxos completos
- Todos os testes passam antes de continuar

### 7. Atualização de documentação
Ativar skill `documentation`:
- JSDoc/docstrings atualizados
- README se impacto for maior

### 8. Auto-revisão
Ativar skill `code-review`:
- Conformidade com Rules do projeto
- Alinhamento ao DNA (nomenclatura, estilo)

### 🔴 VALIDAÇÃO ③ — Apresentar código para revisão humana
> Incluir: o que foi implementado, decisões tomadas, trade-offs.
> O agente pode ter interpretado algo diferente do esperado.

## Output
- Código implementado, testado e documentado
- Pronto para PR
