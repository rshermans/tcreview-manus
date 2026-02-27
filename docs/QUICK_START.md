# VIBE CODE — QUICK START
> Como usar o framework no seu projeto em 15 minutos

---

## PASSO 1 — Copie os arquivos para o seu projeto

```
seu-projeto/
├── .vibe/                          ← Criar esta pasta
│   ├── MASTER_SKILL.md             ← Núcleo do framework
│   ├── VIBE_INDEX.md               ← Índice vivo (personalize!)
│   ├── skills/
│   │   └── SKILLS_CATALOG.md       ← Capacidades disponíveis
│   ├── rules/
│   │   └── RULES_CATALOG.md        ← Leis do sistema
│   └── workflows/
│       └── WORKFLOWS_CATALOG.md    ← Fluxos de execução
├── src/
└── ...
```

---

## PASSO 2 — Configure o DNA do projeto

Abra `VIBE_INDEX.md` e preencha a seção **DNA DO PROJETO** com as informações reais do seu projeto. Isso é o que todos os agentes usarão como fonte de verdade.

---

## PASSO 3 — Adicione ao contexto do agente

Quando iniciar uma sessão de trabalho, inclua no contexto:

```
"Leia os arquivos em .vibe/ antes de começar. 
Especialmente: MASTER_SKILL.md e VIBE_INDEX.md.
Use o DNA do projeto para todas as suas decisões."
```

---

## PASSO 4 — Use os Workflows

Em vez de pedir "implemente X", use os workflows:

| Situação | Comando |
|----------|---------|
| Nova feature | "Execute WF-CORE-001 para implementar [feature]" |
| Bug reportado | "Execute WF-CORE-002 para investigar [erro]" |
| Preciso revisar | "Execute WF-CORE-003 neste código" |
| Refatorar algo | "Execute WF-CORE-004 em [arquivo/função]" |
| Padrão repetitivo | "Execute WF-META-001 para criar um agente para [padrão]" |

---

## PASSO 5 — Deixe o framework crescer

Quando o `agent-factory` (SK-008) identificar padrões e propuser novos agentes, avalie e adicione ao VIBE_INDEX.md. O framework cresce com o projeto.

---

## DICA: Prompt de sistema recomendado

Cole este texto no início de cada sessão para ativar o framework completo:

```
Você é um agente de engenharia de código operando dentro do framework 
Vibe Code. Antes de qualquer ação:

1. Leia .vibe/VIBE_INDEX.md para entender o DNA do projeto
2. Identifique qual Workflow se aplica à tarefa atual
3. Siga as Rules ativas — especialmente as CRITICAL
4. Ative as Skills necessárias na ordem correta
5. Pause nos Nós de Validação e aguarde confirmação humana

Se encontrar um padrão recorrente não coberto pelos agentes existentes,
ative SK-008 (agent-factory) e proponha um novo agente antes de continuar.

O objetivo é: código que parece ter sido escrito pelo time, não por uma IA.
```
