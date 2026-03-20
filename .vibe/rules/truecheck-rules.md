---
domain: TrueCheck (fact-checking / news-verification)
version: 1.0.0
created: 2026-02-26
---

# Rules de Domínio — TrueCheck

> Rules específicas para o domínio de fact-checking e verificação de notícias.

---

## RULE-TC-001: Trust Scores Inteiros

```
priority: high
scope: fact-checking
```

**Princípio**: Trust scores são sempre percentuais inteiros (0-100). Nunca decimais, nunca strings com "%".

**Racional**: Scores com decimais transmitem falsa precisão. O utilizador não distingue confiança entre 65.3% e 65.7%, mas a interface fica mais limpa e consistente com inteiros.

**Aplicação Prática**:
```python
# ✅ CORRETO
trust_score = 65  # inteiro

# ❌ ERRADO
trust_score = "35%"   # string com %
trust_score = 65.3    # decimal falsa precisão
```

**Exceções**: Nenhuma. Scores são sempre inteiros.

---

## RULE-TC-002: Graus, Nunca Absolutos

```
priority: critical
scope: fact-checking
```

**Princípio**: A análise nunca afirma verdade absoluta — sempre apresenta graus de confiança.

**Racional**: Fact-checking responsável reconhece limitações. Afirmar "VERDADE" ou "MENTIRA" sem nuance é epistemologicamente desonesto e legalmente arriscado. Graus de confiança respeitam a complexidade da informação.

**Aplicação Prática**:
```
# ✅ CORRETO
"Com base nas fontes consultadas, este conteúdo tem um grau de confiança de 65%."
"A análise indica que este claim é parcialmente suportado por evidências."

# ❌ ERRADO
"Este conteúdo é VERDADEIRO."
"Isto é FALSO."
"Confirmamos que esta notícia é real."
```

**Exceções**: Factos matemáticos ou científicos universalmente aceites podem ter linguagem mais assertiva, mas ainda com referência a fontes.

---

## RULE-TC-003: Fontes Primeiro

```
priority: high
scope: fact-checking
```

**Princípio**: Fontes são categorizadas por credibilidade antes de serem usadas como evidência.

**Racional**: Usar uma fonte duvidosa como evidência de veracidade é circular. A credibilidade da análise depende diretamente da credibilidade das fontes consultadas.

**Aplicação Prática**: Antes de citar uma fonte na análise, avaliar com `skill/source-credibility`. Incluir a classificação da fonte no resultado.

---

## RULE-TC-004: Neutralidade Pedagógica

```
priority: high
scope: education
```

**Princípio**: Insights pedagógicos são neutros e baseados em evidência. Nunca tomam partido.

**Racional**: O objetivo do TrueCheck é capacitar o utilizador a pensar criticamente — não dizer-lhe o que pensar. Tomar partido destrói a credibilidade da plataforma e viola o princípio educativo.

**Aplicação Prática**:
```
# ✅ CORRETO
"Fontes A e B apresentam perspetivas diferentes sobre este tópico. 
Considere comparar ambas antes de formar uma opinião."

# ❌ ERRADO
"A fonte A está claramente errada."
"Deveria acreditar na fonte B porque tem razão."
```

**Exceções**: Quando há consenso científico estabelecido (ex: vacinação, alterações climáticas), é aceitável apresentar o consenso como tal, citando as fontes.
