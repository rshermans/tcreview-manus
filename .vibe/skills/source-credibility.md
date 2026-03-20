---
name: source-credibility
version: 0.1.0
domain: fact-checking
triggers:
  - URL submetida para análise
  - avaliação de fontes durante fact-check
  - "esta fonte é confiável?"
requires:
  - URL ou nome da fonte
  - base de conhecimento de fontes (futuro)
produces:
  - score de credibilidade da fonte (0-100)
  - classificação (confiável / mista / duvidosa / desconhecida)
  - histórico da fonte (quando disponível)
compatible_rules: [RULE-TC-003, RULE-TC-002]
---

## OBJETIVO
Avaliar a credibilidade de fontes de informação antes de usar os seus conteúdos na verificação de factos.

## CONTEXTO DE ATIVAÇÃO
Quando uma URL é submetida ou quando o fact-check agent precisa avaliar a confiabilidade de fontes usadas como evidência.

## PROCESSO INTERNO

### Passo 1 — Identificação da fonte
Extrair domínio, nome da publicação, autor (quando disponível).

### Passo 2 — Avaliação de reputação
Verificar contra indicadores de credibilidade:
- Domínio registrado há quanto tempo?
- Tem política de correções?
- É reconhecida por organizações de fact-checking?
- Histórico de retrações?

### Passo 3 — Análise de sinais
- Presença de anúncios excessivos ou clickbait
- Uso de linguagem sensacionalista
- Citação de fontes primárias
- Transparência editorial

### Passo 4 — Classificação
- 🟢 **Confiável** (score ≥ 75): fontes com track record verificável
- 🟡 **Mista** (50 ≤ score < 75): fontes com qualidade inconsistente
- 🔴 **Duvidosa** (score < 50): fontes com histórico de desinformação
- ⚪ **Desconhecida**: sem dados suficientes para classificar

## SAÍDA ESPERADA
```json
{
  "source_name": "Example News",
  "domain": "example.com",
  "credibility_score": 72,
  "classification": "mista",
  "signals": [...],
  "recommendation": "Usar com cautela — cruzar com outras fontes"
}
```

## ANTI-PADRÕES
- Classificar fonte como "confiável" ou "não confiável" sem evidências
- Assumir que fontes grandes são automaticamente confiáveis
- Ignorar a diferença entre secções de opinião e notícias factuais
