# WORKFLOWS CATALOG — Vibe Code Framework

> Workflows são partituras de execução. Eles definem não apenas *o que* fazer,
> mas *quando*, *em que ordem* e *onde pausar para validação humana*.

---

## ANATOMIA DE UM WORKFLOW

Um workflow é composto por três tipos de nós:

**Nó de Execução** → O agente executa autonomamente (verde)
**Nó de Decisão** → O agente avalia e escolhe um caminho (amarelo)
**Nó de Validação** → Execução pausa, humano valida antes de continuar (vermelho)

A presença de Nós de Validação é intencional e não deve ser removida. Eles existem porque o agente tem limitações de contexto que o humano não tem.

---

## TEMPLATE DE WORKFLOW

```markdown
---
workflow_id: WF-[DOMÍNIO]-[NNN]
name: [Nome descritivo em português]
version: 0.1.0
trigger: [O que inicia este workflow]
skills_activated: [lista de skills usadas]
rules_enforced: [lista de rules verificadas]
estimated_time: [estimativa realista]
complexity: low | medium | high
requires_human_validation: true | false
---

## OBJETIVO
[O que este workflow entrega ao final — em termos de negócio, não técnicos]

## PRÉ-CONDIÇÕES
[O que deve ser verdadeiro antes de iniciar]

## DIAGRAMA DE FLUXO

[Representação textual clara do fluxo com bifurcações]

## ETAPAS DETALHADAS

### Etapa N — [Nome]
**Tipo**: execução | decisão | validação
**Skill ativada**: [nome-da-skill]
**Input**: [o que esta etapa recebe]
**Processo**: [o que acontece internamente]
**Output**: [o que esta etapa produz]
**Critério de sucesso**: [como saber que esta etapa foi bem-sucedida]
**Em caso de falha**: [o que fazer]

## PÓS-CONDIÇÕES
[O que deve ser verdadeiro após o workflow completar]

## MÉTRICAS
[Como medir a qualidade do output deste workflow]
```

---

## WF-CORE-001: Feature Development

```
trigger: "implemente [feature]", nova user story, ticket de desenvolvimento
complexity: high
requires_human_validation: true
estimated_time: varia conforme feature
```

### Objetivo
Implementar uma nova funcionalidade de forma estruturada, garantindo que o código seja correto, testado, documentado e alinhado ao projeto antes de ir para revisão.

### Pré-condições
O requisito está suficientemente claro para implementação? Os contratos de interface com outros sistemas estão definidos? O DNA do projeto foi capturado?

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Capturar e confirmar requisito
    → O agente reformula o requisito com suas próprias palavras
    → "Entendo que preciso de X que faz Y quando Z. Correto?"
    ↓
[VALIDAÇÃO ①] Time confirma entendimento
    ↓
[EXEC] Design de interfaces
    → Definir: tipos de dados, assinaturas, contratos de API
    → Nenhum código de implementação ainda
    ↓
[DECISÃO] Existem 2+ abordagens arquiteturais viáveis?
    → SIM → [VALIDAÇÃO ②] Apresentar trade-offs → aguardar escolha
    → NÃO → Continuar com a abordagem única, documentando o racional
    ↓
[EXEC] Implementação — lógica core
    → Apenas regras de negócio, sem I/O
    → Funções puras quando possível
    ↓
[EXEC] Implementação — camada de infraestrutura
    → Conectar com banco, APIs, serviços externos
    → Tratamento de erros e casos de borda
    ↓
[EXEC] Geração de testes
    → Unitários para lógica core
    → Integração para fluxos completos
    → Todos os testes passam antes de continuar
    ↓
[EXEC] Atualização de documentação
    → JSDoc/docstrings atualizados
    → README ou wiki se impacto for maior
    ↓
[EXEC] Auto-revisão
    → Verificar conformidade com Rules do projeto
    → Verificar alinhamento ao DNA (nomenclatura, estilo)
    ↓
[VALIDAÇÃO ③] Apresentar código para revisão humana
    → Incluir: o que foi implementado, decisões tomadas, trade-offs
    ↓
[FIM] Feature pronta para PR
```

### Pontos de Validação Humana

A validação ① garante que o agente entendeu o requisito antes de qualquer trabalho — erros de entendimento descobertos aqui custam minutos; descobertos no final custam horas.

A validação ② envolve o time em decisões arquiteturais com impacto de longo prazo — o agente não tem visibilidade do roadmap ou das limitações de negócio que o time tem.

A validação ③ é a revisão final — o agente pode ter interpretado algo de forma diferente do esperado, e olhos humanos pegam o que o agente não vê.

---

## WF-CORE-002: Debug Investigation

```
trigger: bug reportado, erro em produção, comportamento inesperado
complexity: medium
requires_human_validation: true
estimated_time: 30min - 4h dependendo da complexidade
```

### Objetivo
Identificar a causa raiz de um problema (não apenas o sintoma), corrigi-lo de forma que não regresse, e documentar o aprendizado.

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Coleta de evidências
    → Reunir: mensagem de erro exata, stack trace completo
    → Reunir: passos para reprodução, ambiente (dev/staging/prod)
    → Reunir: quando começou, o que mudou recentemente
    ↓
[EXEC] Geração de hipóteses
    → Produzir 3-5 hipóteses ordenadas por probabilidade
    → Para cada: "Se esta hipótese for verdadeira, esperaría ver X"
    ↓
[VALIDAÇÃO ①] Time adiciona contexto adicional
    → O time pode conhecer mudanças recentes que o agente desconhece
    ↓
[EXEC] Criação de teste de reprodução
    → Escrever o menor código possível que reproduz o problema
    → Se não consegue reproduzir → problema de ambiente (investigar separado)
    ↓
[LOOP] Para cada hipótese (da mais para menos provável):
    │
    ├─[EXEC] Testar hipótese com evidências
    │   → Buscar no código, logs, ou testar isoladamente
    │
    ├─[DECISÃO] Hipótese confirmada?
    │   → SIM → Saír do loop
    │   → NÃO → Próxima hipótese
    │
    └─[DECISÃO] Todas hipóteses esgotadas?
        → SIM → [VALIDAÇÃO ②] Precisamos de mais contexto
        → NÃO → Continuar loop
    ↓
[EXEC] Identificação da causa raiz
    → Documentar: o que falhou, por que falhou, por que não foi detectado antes
    → Distinguir: sintoma vs causa (corrigir apenas o sintoma recria o bug)
    ↓
[EXEC] Implementação da correção
    → Corrigir a causa raiz, não o sintoma
    → O teste de reprodução deve passar após a correção
    ↓
[EXEC] Adição de teste de regressão
    → O bug não pode voltar sem que um teste falhe
    ↓
[VALIDAÇÃO ③] Revisão da correção
    ↓
[EXEC] Post-mortem (para bugs de produção)
    → Documenta: causa, impacto, correção, prevenção futura
    ↓
[FIM]
```

### Princípio-Guia
"Nunca conserte o código sem primeiro entender por que ele falhou." Uma correção sem entendimento é uma correção que voltará.

---

## WF-CORE-003: Code Review Profundo

```
trigger: PR aberto, "revise este código", code review solicitado
complexity: medium
requires_human_validation: false (o próprio workflow é a revisão)
estimated_time: 20min - 2h dependendo do tamanho
```

### Objetivo
Produzir uma revisão de código que vai além de estilo — que identifica problemas de lógica, segurança, performance e manutenibilidade, com evidências concretas.

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Entendimento do propósito
    → "O que este código deveria fazer?"
    → "Ele faz o que se propõe?"
    ↓
[EXEC] Análise estrutural
    → Separação de responsabilidades adequada?
    → Acoplamento — este módulo pode ser testado isoladamente?
    → Abstrações fazem sentido? Não há over-engineering?
    ↓
[EXEC] Análise de lógica
    → Os algoritmos produzem o resultado correto?
    → Edge cases são tratados? (null, empty, negative, overflow)
    → Condições de corrida em código concorrente?
    ↓
[EXEC] Análise de segurança (RULE-CORE-004)
    → Inputs validados antes de uso?
    → Dados sensíveis protegidos?
    → Queries parametrizadas?
    → Autorização verificada onde necessário?
    ↓
[EXEC] Análise de performance
    → Queries N+1 (loop com query dentro)?
    → Operações desnecessariamente síncronas?
    → Dados grandes sendo processados em memória?
    ↓
[EXEC] Análise de testabilidade
    → Cobertura existente é adequada?
    → Casos críticos sem teste?
    → Testes testam comportamento ou implementação?
    ↓
[EXEC] Análise de conformidade ao DNA
    → Nomenclatura alinhada ao projeto?
    → Padrões de erro consistentes com o resto?
    → Estilo de comentários compatível?
    ↓
[EXEC] Produção do relatório
    → Categorias: BLOQUEADOR | MELHORIA | ELOGIO
    → Para cada problema: onde está, por que é problema, como corrigir
    ↓
[FIM]
```

### Formato do Relatório de Saída

O relatório deve ter uma seção por categoria. Bloqueadores são itens que impedem o merge — segurança, bugs, violações críticas de arquitetura. Melhorias são oportunidades que deveriam ser consideradas mas não bloqueiam. Elogios são reconhecimentos de boas práticas — importantes para calibrar o que o time está fazendo bem e deve repetir.

---

## WF-CORE-004: Refactor Seguro

```
trigger: "refatore", código com alta complexidade, débito técnico identificado
complexity: high
requires_human_validation: true
estimated_time: 1h - 1 dia
```

### Objetivo
Melhorar o design interno do código sem alterar seu comportamento externo observável. A palavra-chave é *seguro* — cada passo é verificável e reversível.

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Diagnóstico do problema atual
    → Qual é o problema? Alta complexidade ciclomática? Acoplamento?
    → Código duplicado? Abstrações vazadas? Nomenclatura confusa?
    ↓
[VALIDAÇÃO ①] Confirmar o objetivo do refactor com o time
    → "Quero refatorar X para Y. O objetivo é Z. Concordam?"
    ↓
[DECISÃO] Existem testes cobrindo o comportamento a ser refatorado?
    → NÃO → [EXEC] Escrever testes que capturam comportamento atual
    → SIM → Continuar
    ↓
[EXEC] Snapshot de comportamento
    → Documentar: inputs/outputs conhecidos, comportamentos de borda
    → Estes dados serão usados para verificar que nada quebrou
    ↓
[LOOP] Para cada passo de refatoração (pequenos e verificáveis):
    │
    ├─[EXEC] Aplicar uma mudança de cada vez
    │   → Renomear, extrair função, mover responsabilidade, etc.
    │   → NUNCA múltiplas mudanças simultâneas
    │
    └─[DECISÃO] Todos os testes passam?
        → SIM → Próximo passo
        → NÃO → Reverter e analisar o que quebrou
    ↓
[EXEC] Comparação antes/depois
    → Complexidade ciclomática melhorou?
    → Legibilidade melhorou?
    → Performance não regrediu?
    ↓
[EXEC] Atualização de documentação
    ↓
[VALIDAÇÃO ②] Apresentar diff final para aprovação
    ↓
[FIM]
```

### Princípio Fundamental
Refactor significa "mudar como o código está escrito sem mudar o que ele faz". Se qualquer comportamento externo mudar — mesmo para melhor — isso é uma feature, não um refactor, e deve ser tratado como WF-CORE-001.

---

## WF-META-001: Agent Genesis

```
trigger: padrão repetitivo 3+ vezes, necessidade não coberta identificada
complexity: medium
requires_human_validation: true
estimated_time: 30min - 2h
```

### Objetivo
Criar um novo agente (Skill, Rule ou Workflow) que expande o framework de forma coerente com o DNA do projeto.

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Identificação da necessidade
    → Qual padrão se repete? Qual problema o novo agente resolve?
    → "Tenho feito X manualmente N vezes — isso deveria ser uma Skill"
    ↓
[EXEC] Classificação do tipo
    → É uma capacidade (Skill)?
    → É uma restrição ou princípio (Rule)?
    → É um fluxo de execução (Workflow)?
    ↓
[EXEC] Verificação de duplicidade
    → Consultar VIBE_INDEX.md
    → Existe algo similar? É melhor especializar do que criar?
    ↓
[EXEC] Estruturação usando template
    → Usar o template do tipo correto
    → Preencher TODOS os campos — incluindo anti-padrões e exceções
    ↓
[EXEC] Validação de coerência
    → O novo agente viola alguma Rule existente?
    → Ele é compatível com os Workflows ativos?
    → O nome é claro e não conflita com nomes existentes?
    ↓
[EXEC] Criação de casos de teste
    → Escrever 3 cenários concretos onde o novo agente seria usado
    → Para cada: input → processo esperado → output esperado
    ↓
[VALIDAÇÃO ①] Apresentar ao time para aprovação
    → Incluir: propósito, exemplos, impacto em agentes existentes
    ↓
[EXEC] Registro no VIBE_INDEX.md
    ↓
[FIM]
```

---

## WF-META-002: Context Sync

```
trigger: início de nova sessão, mudança significativa no projeto
complexity: low
requires_human_validation: false
estimated_time: 5-15min
```

### Objetivo
Atualizar o DNA do projeto para que todos os agentes operem com contexto atual e preciso.

### Fluxo de Execução

```
[INÍCIO]
    ↓
[EXEC] Ler project_dna.yaml existente (se houver)
    ↓
[EXEC] Varrer sinais de mudança
    → Novas dependências? Nova estrutura de diretórios?
    → Mudança de framework? Novo domínio de negócio?
    → Novo membro no time com convenções diferentes?
    ↓
[DECISÃO] Mudanças significativas detectadas?
    → NÃO → DNA atual é válido, continuar
    → SIM → Atualizar DNA e notificar sobre mudanças
    ↓
[EXEC] Verificar se skills/rules ainda fazem sentido
    → Algum agente ficou obsoleto com as mudanças?
    → Algum novo agente é necessário?
    ↓
[EXEC] Atualizar VIBE_INDEX.md se necessário
    ↓
[FIM]
```

---

## COMPOSIÇÃO DE WORKFLOWS

Workflows podem ser compostos — a saída de um se torna a entrada de outro:

```
WF-META-002 (Context Sync)
    ↓
WF-CORE-001 (Feature Development)
    → internamente chama: skill/code-generation + skill/test-generation
    ↓
WF-CORE-003 (Code Review)
    → internamente chama: skill/security-audit + skill/code-review
    ↓
[Deploy Pipeline] — definido pelo projeto
```

Essa composição cria um fluxo de desenvolvimento completo que mantém qualidade em cada etapa sem requerer que o time se lembre de executar cada verificação manualmente.
