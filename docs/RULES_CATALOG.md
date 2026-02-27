# RULES CATALOG — Vibe Code Framework

> Rules são as leis do sistema. Elas não sugerem — elas **exigem**.
> Quando uma Rule e uma preferência entram em conflito, a Rule vence.

---

## HIERARQUIA DE RULES

As rules seguem uma hierarquia de prioridade clara:

```
CRITICAL  → Violação para o trabalho imediatamente
HIGH      → Violação exige revisão antes de continuar
MEDIUM    → Violação gera alerta mas não bloqueia
LOW       → Sugestão com justificativa — pode ser ignorada conscientemente
```

---

## TEMPLATE DE RULE

```markdown
---
rule_id: RULE-[DOMÍNIO]-[NNN]
name: [Nome descritivo]
priority: critical | high | medium | low
scope: global | [domínio específico]
created_from: [contexto que originou esta rule]
---

## PRINCÍPIO
[A lei em uma frase. Deve ser memorável e não ambígua.]

## RACIONAL
[Por que esta rule existe? Qual problema ela previne?]

## APLICAÇÃO PRÁTICA
[Como esta rule se manifesta em código, decisões e comportamento?]

## EXEMPLOS

### ✅ Em conformidade
[Exemplo concreto]

### ❌ Em violação
[Exemplo concreto]

## EXCEÇÕES
[Casos onde a rule pode ser relaxada — com critérios explícitos]

## CONSEQUÊNCIA DE VIOLAÇÃO
[O que acontece quando esta rule é quebrada?]
```

---

## RULES GLOBAIS (Aplicam a todos os projetos)

---

### RULE-CORE-001: Fidelidade ao DNA

```
priority: critical
scope: global
```

**Princípio**: Todo output gerado deve ser indistinguível do que o time escreveria.

**Racional**: Código inconsistente com o estilo do projeto aumenta a carga cognitiva de todos. Um agente que gera código "genérico" está criando débito técnico, não valor. A melhor contribuição de um agente é ser invisível — integrada tão naturalmente que ninguém pergunta "quem escreveu isso?".

**Aplicação Prática**: Antes de gerar qualquer código, verifique: qual é a convenção de nomenclatura? Qual é o padrão de tratamento de erros? Como o time organiza imports? Como comentários são escritos? Somente depois de responder essas perguntas, escreva.

```javascript
// ✅ CORRETO — segue o padrão do projeto (camelCase, async/await, error handling explícito)
async function fetchUserById(userId: string): Promise<User> {
  const user = await userRepository.findById(userId)
  if (!user) throw new NotFoundError(`User ${userId} not found`)
  return user
}

// ❌ ERRADO — estilo diferente do projeto (Promise chain, nomenclatura inconsistente)
function GetUser(id) {
  return db.users.find(id).then(u => u).catch(e => null)
}
```

**Exceções**: Quando um padrão novo é explicitamente aprovado pelo time como uma mudança de estilo intencional e documentada.

---

### RULE-CORE-002: Mínimo de Surpresa

```
priority: high
scope: global
```

**Princípio**: Nunca introduza o que não foi pedido sem sinalizar explicitamente.

**Racional**: Agentes que "melhoram" código não solicitado geram desconfiança e revisões extras. A autonomia do agente deve ser proporcional à clareza do pedido. Surpresas, mesmo bem-intencionadas, têm custo.

**Aplicação Prática**: Se ao implementar uma feature você percebe que outra coisa deveria ser refatorada, sinalize — não faça. "Notei que a função `parseDate` ao lado poderia ser simplificada. Quer que eu faça isso também?" é a abordagem correta.

**Exceções**: Correções de bugs críticos de segurança encontrados durante o trabalho devem ser sinalizadas imediatamente e, se o risco for alto, podem ser corrigidas junto com a sinalização.

---

### RULE-CORE-003: Evidência antes de Ação

```
priority: high
scope: global
```

**Princípio**: Para decisões arquiteturais, apresente caminhos e trade-offs antes de implementar.

**Racional**: O agente não tem contexto de negócio completo. Uma decisão técnica que parece óbvia pode ter implicações de prazo, compliance ou estratégia que o agente desconhece. O time decide; o agente executa com excelência.

**Aplicação Prática**: Para qualquer escolha que afete mais de 10 linhas de código ou envolva uma abstração nova, apresente: "Tenho duas abordagens — A (mais simples, menor flexibilidade) e B (mais flexível, maior complexidade inicial). Qual faz mais sentido para vocês?" Só então implemente.

---

### RULE-CORE-004: Segurança por Padrão

```
priority: critical
scope: global
```

**Princípio**: Assuma sempre que inputs são hostis, dados são sensíveis e falhas são possíveis.

**Racional**: Segurança adicionada depois é exponencialmente mais cara que segurança desde o início. Um agente que gera código sem tratar segurança está criando vulnerabilidades, não features.

**Aplicação Prática**: Toda função que recebe input externo valida antes de processar. Dados sensíveis nunca aparecem em logs. Queries usam parâmetros, nunca concatenação. Tokens têm expiração. Erros não expõem detalhes internos ao usuário.

```typescript
// ✅ CORRETO
async function updateUserEmail(userId: string, newEmail: string) {
  // Validação antes de qualquer operação
  const validated = emailSchema.parse(newEmail) // throws se inválido
  const user = await findUserOrThrow(userId)    // throws se não existe
  
  await db.users.update({
    where: { id: userId },
    data: { email: validated }
  })
  
  // Log sem dado sensível
  logger.info('User email updated', { userId }) // sem o email no log
}

// ❌ ERRADO
async function updateEmail(userId, email) {
  await db.query(`UPDATE users SET email = '${email}' WHERE id = '${userId}'`)
  console.log(`Updated ${userId} to ${email}`) // email em log + SQL injection
}
```

---

### RULE-CORE-005: Reversibilidade

```
priority: medium
scope: global
```

**Princípio**: Prefira sempre a solução mais reversível entre opções de custo similar.

**Racional**: O futuro é incerto. Feature flags custam pouco e valem muito. Uma migration sem rollback pode custar horas de downtime. O código que pode ser desfeito sem catástrofe é código saudável.

**Aplicação Prática**: Database migrations sempre têm `down()`. Features novas ficam atrás de feature flags. Abstrações são introduzidas com interfaces estáveis mesmo que a implementação mude. Breaking changes são versionados.

---

### RULE-CORE-006: Documentação Acoplada

```
priority: medium
scope: global
```

**Princípio**: Código sem contexto é dívida técnica. O "porquê" é mais valioso que o "o quê".

**Racional**: Código descreve o que acontece; comentários devem explicar por que foi essa a escolha. Em seis meses, a pessoa que lerá o código pode ser você mesmo. A melhor documentação é aquela que responde perguntas antes que sejam feitas.

**Aplicação Prática**: Funções públicas têm JSDoc/docstring com propósito, parâmetros e casos de erro. Decisões não-óbvias têm comentário explicando o racional. TODOs têm contexto ("TODO: Remover após migração para v2 da API — ref: ticket #123").

---

### RULE-CORE-007: Composição sobre Monólito

```
priority: medium
scope: global
```

**Princípio**: Funções pequenas e composáveis superam funções grandes e completas.

**Racional**: Uma função que faz uma coisa pode ser testada, reutilizada e substituída. Uma função que faz dez coisas precisa ser entendida completamente antes de qualquer alteração. Complexidade emerge da composição; não deve ser escondida dentro de um único bloco.

**Aplicação Prática**: Se uma função passa de 30 linhas ou tem mais de 3 níveis de indentação, questione se ela está fazendo mais de uma coisa. Se estiver, extraia. Se a extração parecer artificial, talvez o problema seja o design — não o tamanho.

---

## RULES DE DOMÍNIO (Geradas pelo Agent Factory)

### Fintech

**RULE-FIN-001**: Cálculos financeiros nunca usam floating point — sempre inteiros em centavos ou bibliotecas decimais precisas.

**RULE-FIN-002**: Toda operação de débito/crédito tem idempotency key para prevenir processamento duplicado.

**RULE-FIN-003**: Auditoria completa de todas as transações — quem fez, quando, de onde, valor antes e depois.

**RULE-FIN-004**: Valores monetários exibidos ao usuário são sempre formatados com locale e símbolo correto — nunca números crus.

---

### Saúde (Healthcare)

**RULE-HLT-001**: Dados de identificação de pacientes (nome, CPF, diagnóstico) nunca aparecem em logs, erros ou URLs.

**RULE-HLT-002**: Todo acesso a prontuário é registrado com: quem acessou, quando, qual dado, e motivo quando aplicável.

**RULE-HLT-003**: Algoritmos clínicos têm testes de validação contra datasets conhecidos antes de entrar em produção.

---

### E-commerce

**RULE-ECO-001**: Preços sempre armazenados em centavos (inteiros). Nunca `19.99` — sempre `1999`.

**RULE-ECO-002**: Estoque negativo é um estado de erro que deve ser tratado explicitamente — nunca ignorado silenciosamente.

**RULE-ECO-003**: Cupons e descontos têm validação de data, uso máximo e exclusividade (não acumulável por padrão).

---

### APIs Públicas

**RULE-API-001**: Toda API pública tem versionamento desde o primeiro endpoint (`/v1/`, `/v2/`).

**RULE-API-002**: Erros retornam estrutura consistente com: código, mensagem legível e referência para documentação.

**RULE-API-003**: Rate limiting é implementado antes de ir para produção — não é feature opcional.

**RULE-API-004**: Campos de resposta seguem convenção consistente (camelCase ou snake_case — nunca misturado).

---

## GERAÇÃO DINÂMICA DE RULES

Quando o `agent-factory` detecta um padrão recorrente que deveria ser codificado como rule, ele segue este processo:

**Trigger**: Padrão observado 3+ vezes, ou problema de qualidade recorrente, ou violação de princípio do time.

**Processo de criação**:
O agent-factory primeiro nomeia o princípio em uma frase (se não couber em uma frase, a rule está fazendo mais de uma coisa). Depois define a prioridade com honestidade — reserva "critical" para coisas que realmente param o trabalho. Em seguida, escreve um exemplo positivo e negativo concretos do projeto atual (não genéricos). Por fim, define exceções reais — toda rule tem pelo menos uma.

**Validação antes de adicionar**:
A nova rule conflita com alguma rule existente? Ela é específica o suficiente para guiar decisões reais? Existe um caso de uso concreto que a motivou? Ela sobreviveria a um time novo sem explicação adicional?

Somente após passar por essas perguntas a rule é adicionada ao VIBE_INDEX.md e passa a ser respeitada pelos agentes.
