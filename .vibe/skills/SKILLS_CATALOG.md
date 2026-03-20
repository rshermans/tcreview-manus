# SKILLS CATALOG — Vibe Code Framework

> Skills são capacidades atômicas. Cada uma faz **uma coisa** e faz bem.
> Combine-as para criar comportamentos complexos.

---

## COMO CRIAR UMA NOVA SKILL

Use este template como ponto de partida:

```markdown
---
name: [kebab-case-name]
version: 0.1.0
domain: [ex: frontend | backend | database | devops | testing | meta]
triggers:
  - [situação 1 que ativa esta skill]
  - [situação 2 que ativa esta skill]
requires:
  - [contexto ou skill necessária antes]
produces:
  - [artefato 1 que esta skill gera]
  - [artefato 2 que esta skill gera]
compatible_rules: [RULE-001, RULE-004]
---

## OBJETIVO
[Uma frase clara: "Esta skill gera X a partir de Y para Z"]

## CONTEXTO DE ATIVAÇÃO
[Descreva em linguagem natural quando e por que usar esta skill]

## PROCESSO INTERNO
[Como o agente pensa ao executar esta skill — passo a passo]

### Passo 1 — [Nome]
[Descrição detalhada]

### Passo 2 — [Nome]
[Descrição detalhada]

## SAÍDA ESPERADA
[Formato, qualidade mínima, critérios de aceitação]

## EXEMPLOS
[1-2 exemplos concretos de input → output]

## ANTI-PADRÕES
[O que esta skill deve recusar ou evitar ativamente]

## EVOLUÇÃO
[Como esta skill pode ser expandida ou especializada no futuro]
```

---

## SKILL: code-generation

```markdown
---
name: code-generation
domain: universal
triggers:
  - "implemente", "crie", "escreva", "adicione"
  - qualquer pedido de produção de código novo
requires:
  - DNA do projeto capturado (Fase 0)
produces:
  - código fonte alinhado ao projeto
  - comentários explicativos onde necessário
compatible_rules: [RULE-001, RULE-002, RULE-004, RULE-005]
---

## OBJETIVO
Gerar código que pareça ter sido escrito por um membro sênior do time do projeto.

## PROCESSO INTERNO

### Passo 1 — Entender antes de escrever
Antes de qualquer linha de código: "Entendo o requisito? Conheço os contratos 
de interface? Sei quais dependências existem no projeto?" Se não → perguntar.

### Passo 2 — Design de interfaces primeiro
Definir tipos, assinaturas de funções e contratos antes da implementação.
Isso expõe ambiguidades cedo, quando são baratas de resolver.

### Passo 3 — Implementação incremental
Escrever o caso feliz primeiro, depois tratamento de erros, depois edge cases.
Nunca misturar os três — isso gera código difícil de revisar.

### Passo 4 — Auto-revisão antes de entregar
Verificar: nomenclatura consistente? Segurança tratada? Testável? 
Fiel ao estilo do projeto?

## ANTI-PADRÕES
- Importar bibliotecas não presentes no projeto sem avisar
- Usar padrões diferentes dos que já existem no codebase
- Gerar código "genérico" que não considera o contexto específico
- Misturar lógica de negócio com I/O no mesmo lugar
```

---

## SKILL: test-generation

```markdown
---
name: test-generation
domain: universal
triggers:
  - após geração de código
  - "teste", "spec", "coverage", "TDD"
requires:
  - código a ser testado
  - DNA do projeto (framework de testes)
produces:
  - testes unitários
  - testes de integração (quando aplicável)
  - descrição da estratégia de testes adotada
compatible_rules: [RULE-001, RULE-004]
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
```

---

## SKILL: agent-factory

```markdown
---
name: agent-factory
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
compatible_rules: [RULE-001, RULE-007]
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
Usar o template do tipo correto. Preencher todos os campos obrigatórios.
Deixar explícito o que é opcional.

### Passo 4 — Teste de coerência
O novo agente viola alguma Rule existente?
Ele é compatível com os Workflows ativos?
O nome é claro e não ambíguo?

### Passo 5 — Proposta para validação
Apresentar o novo agente ao time antes de oficializar.
Incluir: propósito, exemplos de uso, impacto nos agentes existentes.

## ANTI-PADRÕES
- Criar agentes muito genéricos que fazem muitas coisas
- Duplicar capacidades já existentes com nome diferente
- Criar agentes sem pelo menos um caso de uso concreto
- Não registrar no VIBE_INDEX.md após criação
```

---

## SKILL: context-scanner

```markdown
---
name: context-scanner
domain: meta
triggers:
  - início de qualquer sessão de trabalho
  - "analise o projeto", "entenda o codebase"
  - quando o DNA do projeto não está disponível
requires:
  - acesso a arquivos do projeto (ou descrição textual)
produces:
  - project_dna.yaml
  - lista de skills recomendadas para o projeto
  - lista de rules recomendadas para o domínio
compatible_rules: [RULE-001]
---

## OBJETIVO
Construir uma representação completa do DNA do projeto para alimentar todos 
os outros agentes.

## PROCESSO INTERNO

### Passo 1 — Varredura de estrutura
Analisar: package.json, Cargo.toml, requirements.txt, go.mod, etc.
Inferir: linguagem, runtime, dependências principais.

### Passo 2 — Inferência de arquitetura
Analisar estrutura de diretórios.
Identificar padrões: MVC? Hexagonal? Feature-based? Monorepo?

### Passo 3 — Captura de convenções
Analisar arquivos existentes para extrair: 
estilo de nomenclatura, abordagem de erros, padrões de comentário.

### Passo 4 — Identificação de domínio
A partir das dependências e estrutura, inferir o domínio de negócio.
Isso ativa rules e skills específicas de domínio.

### Passo 5 — Geração do DNA
Produzir project_dna.yaml completo e listar agentes recomendados.

## SAÍDA
Um arquivo project_dna.yaml que outros agentes consomem como fonte de verdade.
```

---

## SKILL: security-audit

```markdown
---
name: security-audit  
domain: security
triggers:
  - revisão de código com inputs externos
  - autenticação, autorização, dados sensíveis
  - "segurança", "vulnerabilidade", "OWASP"
requires:
  - código a ser auditado
produces:
  - relatório de vulnerabilidades (críticas → baixas)
  - código corrigido ou sugestões de correção
compatible_rules: [RULE-004]
---

## OBJETIVO
Identificar vulnerabilidades de segurança antes que cheguem à produção.

## CHECKLIST DE ANÁLISE

### Inputs e Outputs
- [ ] Todos os inputs externos são validados e sanitizados?
- [ ] Dados sensíveis são mascarados em logs?
- [ ] Outputs para o usuário escapam caracteres especiais? (XSS)

### Autenticação e Autorização
- [ ] Endpoints sensíveis verificam autenticação?
- [ ] Autorização é verificada no nível de recurso? (não só de rota)
- [ ] Tokens têm expiração adequada?

### Dados
- [ ] Queries usam parâmetros? (SQL injection)
- [ ] Dados sensíveis são criptografados em repouso?
- [ ] Secrets estão em variáveis de ambiente? (não hardcodados)

### Dependências
- [ ] Bibliotecas têm vulnerabilidades conhecidas? (CVE check)

## SAÍDA
Relatório categorizado: CRÍTICO (bloqueia deploy), ALTO, MÉDIO, BAIXO, INFORMATIVO.
```
