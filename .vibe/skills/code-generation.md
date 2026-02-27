---
name: code-generation
version: 1.0.0
domain: universal
triggers:
  - "implemente", "crie", "escreva", "adicione"
  - qualquer pedido de produção de código novo
requires:
  - DNA do projeto capturado (project_dna.yaml)
produces:
  - código fonte alinhado ao projeto
  - comentários explicativos onde necessário
compatible_rules: [RULE-CORE-001, RULE-CORE-002, RULE-CORE-004, RULE-CORE-005]
---

## OBJETIVO
Gerar código que pareça ter sido escrito por um membro sênior do time do projeto.

## CONTEXTO DE ATIVAÇÃO
Sempre que for necessário produzir código novo — seja uma função, componente, endpoint, ou módulo inteiro. A skill garante que o output é indistinguível do que o time escreveria.

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

## SAÍDA ESPERADA
Código que segue o DNA do projeto: camelCase para JS/TS, snake_case para Python. Comentários em português para lógica de negócio. Tratamento de erros padronizado com JSON.

## ANTI-PADRÕES
- Importar bibliotecas não presentes no projeto sem avisar
- Usar padrões diferentes dos que já existem no codebase
- Gerar código "genérico" que não considera o contexto específico
- Misturar lógica de negócio com I/O no mesmo lugar
