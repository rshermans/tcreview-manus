---
name: context-scanner
version: 1.0.0
domain: meta
triggers:
  - início de qualquer sessão de trabalho
  - "analise o projeto", "entenda o codebase"
  - quando o DNA do projeto não está disponível
requires:
  - acesso a ficheiros do projeto (ou descrição textual)
produces:
  - project_dna.yaml atualizado
  - lista de skills recomendadas para o projeto
  - lista de rules recomendadas para o domínio
compatible_rules: [RULE-CORE-001]
---

## OBJETIVO
Construir ou atualizar a representação completa do DNA do projeto para alimentar todos os outros agentes.

## PROCESSO INTERNO

### Passo 1 — Varredura de estrutura
Analisar: package.json, requirements.txt, etc.
Inferir: linguagem, runtime, dependências principais.

### Passo 2 — Inferência de arquitetura
Analisar estrutura de diretórios.
Identificar padrões: MVC? Hexagonal? Feature-based? Monorepo?

### Passo 3 — Captura de convenções
Analisar ficheiros existentes para extrair: 
estilo de nomenclatura, abordagem de erros, padrões de comentário.

### Passo 4 — Identificação de domínio
A partir das dependências e estrutura, inferir o domínio de negócio.
Isso ativa rules e skills específicas de domínio.

### Passo 5 — Geração/atualização do DNA
Produzir ou atualizar `project_dna.yaml` e listar agentes recomendados.

## SAÍDA ESPERADA
Ficheiro `project_dna.yaml` atualizado que outros agentes consomem como fonte de verdade.

## ANTI-PADRÕES
- Assumir stack sem verificar ficheiros de configuração
- Não atualizar o DNA quando há mudanças significativas
- Ignorar sinais implícitos (nomenclatura, estrutura de pastas)
