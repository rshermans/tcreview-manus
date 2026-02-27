---
name: fact-check
version: 0.1.0
domain: fact-checking
triggers:
  - "verifica", "fact-check", "é verdade?"
  - análise de conteúdo noticioso
  - input via OmniInput (texto, URL, imagem)
requires:
  - texto a ser verificado (ou texto extraído de URL/imagem)
  - acesso à LLM (llm_service.py)
produces:
  - trust_score (0-100, inteiro)
  - sumário da análise
  - evidências que suportam ou contradizem
  - categorização (confirmado / parcialmente verdadeiro / não verificável / falso)
compatible_rules: [RULE-CORE-004, RULE-TC-001, RULE-TC-002, RULE-TC-003]
---

## OBJETIVO
Verificar a veracidade de conteúdo noticioso usando análise LLM e verificação cruzada de fontes.

## CONTEXTO DE ATIVAÇÃO
Quando um utilizador submete conteúdo (texto, URL, imagem) via OmniInput para análise de veracidade. Esta skill é o core do produto TrueCheck.

## PROCESSO INTERNO

### Passo 1 — Parsing do input
Identificar o tipo de conteúdo e extrair texto analisável:
- **Texto**: usar diretamente
- **URL**: extrair via scraping (futuro: `source-credibility` primeiro)
- **Imagem**: OCR para extrair texto (futuro)

### Passo 2 — Análise factual via LLM
Enviar texto para LLM com prompt especializado em fact-checking.
Pedir: claims identificados, evidências a favor/contra, grau de confiança.

### Passo 3 — Verificação cruzada
Cruzar claims com fontes conhecidas (futuro: APIs de fact-check, bases de dados).
Usar `cross_verify_content()` do `llm_service.py`.

### Passo 4 — Scoring
Calcular trust_score como percentual inteiro (RULE-TC-001).
Nunca afirmar verdade absoluta (RULE-TC-002) — sempre graus.

### Passo 5 — Categorização
Classificar o conteúdo numa das categorias:
- ✅ **Confirmado** (trust_score ≥ 80)
- 🟡 **Parcialmente verdadeiro** (40 ≤ trust_score < 80)
- ⚪ **Não verificável** (dados insuficientes)
- 🔴 **Falso** (trust_score < 40 com evidências contrárias)

## SAÍDA ESPERADA
```json
{
  "trust_score": 65,
  "category": "parcialmente_verdadeiro",
  "summary": "O conteúdo contém claims verificáveis...",
  "claims": [...],
  "sources_checked": [...],
  "confidence": "medium"
}
```

## INTEGRAÇÃO NO BACKEND
- **Ficheiro**: `backend/services/llm_service.py` → `analyze_content()`
- **Orquestrador**: `backend/services/orchestrator_service.py` → `process_omni_input()`
- **Frontend**: `CognitiveResults.tsx` consome o output

## ANTI-PADRÕES
- Afirmar "isto é verdade" ou "isto é mentira" sem nuance
- Retornar trust_score com decimais (RULE-TC-001: sempre inteiros)
- Não citar fontes na análise
- Usar trust_score fixo/hardcoded (atual: "35%" no mock)
