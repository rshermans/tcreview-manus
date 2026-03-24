---
name: security-audit
version: 1.0.0
domain: security
triggers:
  - revisão de código com inputs externos
  - autenticação, autorização, dados sensíveis
  - "segurança", "vulnerabilidade", "OWASP"
requires:
  - código a ser auditado
produces:
  - relatório de vulnerabilidades (CRÍTICO → BAIXO)
  - código corrigido ou sugestões de correção
compatible_rules: [RULE-CORE-004]
---

## OBJETIVO
Identificar vulnerabilidades de segurança antes que cheguem à produção.

## CHECKLIST DE ANÁLISE

### Inputs e Outputs
- [ ] Todos os inputs externos são validados e sanitizados?
- [ ] Dados sensíveis são mascarados em logs?
- [ ] Outputs para o utilizador escapam caracteres especiais? (XSS)

### Autenticação e Autorização
- [ ] Endpoints sensíveis verificam autenticação?
- [ ] Autorização é verificada no nível de recurso? (não só de rota)
- [ ] Tokens têm expiração adequada?

### Dados
- [ ] Queries usam parâmetros? (SQL injection)
- [ ] Dados sensíveis são criptografados em repouso?
- [ ] Secrets estão em variáveis de ambiente? (não hardcodados)

### Dependências
- [ ] Bibliotecas têm vulnerabilidades conhecidas? (CVE check)

## SAÍDA ESPERADA
Relatório categorizado: CRÍTICO (bloqueia deploy), ALTO, MÉDIO, BAIXO, INFORMATIVO.
