---
name: pedagogical-insights
version: 0.1.0
domain: education
triggers:
  - após análise de facto (fact-check)
  - "explica", "ensina", "por que isso é importante?"
  - componente pedagógico do resultado
requires:
  - resultado do fact-check
  - conteúdo original analisado
produces:
  - insights pedagógicos neutros
  - explicação acessível do processo de verificação
  - dicas de literacia mediática
compatible_rules: [RULE-TC-002, RULE-TC-004]
---

## OBJETIVO
Transformar o resultado do fact-check em conteúdo educativo que ajuda o utilizador a desenvolver pensamento crítico e literacia mediática.

## CONTEXTO DE ATIVAÇÃO
Após o fact-check agent produzir um resultado, o teach agent gera insights que ajudam o utilizador a entender *porquê* um conteúdo é considerado verdadeiro/falso e *como* verificar autonomamente.

## PROCESSO INTERNO

### Passo 1 — Contextualização
Explicar o tópico num contexto mais amplo. O que está em jogo? Por que é importante verificar?

### Passo 2 — Explicação do processo
Mostrar ao utilizador como a verificação foi feita:
- Que fontes foram consultadas?
- Que indicadores foram avaliados?
- Por que o score é este e não outro?

### Passo 3 — Dicas de literacia mediática
Dar ao utilizador ferramentas para verificar sozinho no futuro:
- "Antes de partilhar, verifique se..."
- "Fontes credíveis geralmente..."
- "Sinais de alerta incluem..."

### Passo 4 — Neutralidade (RULE-TC-004)
Insights são sempre neutros e baseados em evidência.
Nunca tomar partido — apresentar factos e deixar o utilizador decidir.

## SAÍDA ESPERADA
```json
{
  "context": "Este tópico tem sido debatido desde...",
  "verification_explainer": "Verificámos consultando...",
  "media_literacy_tips": [
    "Verifique sempre a data de publicação",
    "Compare com pelo menos 3 fontes diferentes"
  ],
  "think_about": "Pergunte-se: quem beneficia com esta narrativa?"
}
```

## INTEGRAÇÃO NO BACKEND
- **Ficheiro**: `backend/services/teach_agent.py` → `generate_pedagogical_insights()`
- **Frontend**: Componente dentro de `CognitiveResults.tsx`

## ANTI-PADRÕES
- Tomar partido ou expressar opinião
- Linguagem condescendente ("você deveria saber que...")
- Assumir nível de educação do utilizador
- Não citar fontes nas explicações
