---
description: Investigar e corrigir bugs com foco na causa raiz e prevenção de regressão
---

# WF-CORE-002: Debug Investigation

> Workflow de complexidade média. 2 pontos de validação humana.

## Quando Usar
- Bug reportado
- Erro em produção ou desenvolvimento
- Comportamento inesperado
- "Não funciona", "está a dar erro"

## Etapas

### 1. Coleta de evidências
Reunir:
- Mensagem de erro exata e stack trace completo
- Passos para reprodução
- Ambiente (dev/staging/prod)
- Quando começou, o que mudou recentemente

### 2. Geração de hipóteses
Produzir 3-5 hipóteses ordenadas por probabilidade.
Para cada: "Se esta hipótese for verdadeira, esperaria ver X".

### 🔴 VALIDAÇÃO ① — Time adiciona contexto
> O time pode conhecer mudanças recentes que o agente desconhece.
> Pausar e pedir: "Houve alguma mudança recente que possa estar relacionada?"

### 3. Teste de reprodução
Escrever o menor código possível que reproduz o problema.
Se não consegue reproduzir → investigar problema de ambiente separadamente.

### 4. Testar hipóteses (loop)
Para cada hipótese (da mais para menos provável):
- Testar com evidências concretas
- Hipótese confirmada? → Sair do loop
- Todas esgotadas sem confirmação? →

### 🔴 VALIDAÇÃO ② — Precisamos de mais contexto
> Se todas as hipóteses falharam, pedir ao time mais informação.

### 5. Causa raiz
Documentar: o que falhou, por que falhou, por que não foi detectado antes.
Distinguir: sintoma vs causa.

### 6. Correção
Corrigir a **causa raiz**, não o sintoma.
O teste de reprodução deve passar após a correção.

### 7. Teste de regressão
Adicionar teste que garante que o bug não volta.

### 8. Post-mortem (para bugs de produção)
Documentar: causa, impacto, correção, prevenção futura.

## Princípio-Guia
"Nunca conserte o código sem primeiro entender por que ele falhou."
