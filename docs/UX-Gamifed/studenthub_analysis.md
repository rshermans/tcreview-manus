# Análise de UX e Fluxo: StudentHub

## 1. Estrutura de Navegação (Flow)
O site utiliza uma estrutura de **Single Page Application (SPA)** com navegação lateral persistente.

### Fluxo Principal do Usuário:
1.  **Landing/Home**: Seleção de Disciplina (Matemática, Físico-Química, etc.).
2.  **Modo de Estudo**: Após escolher a disciplina, o usuário escolhe entre:
    *   **Praticar**: Exercícios, Testes, Exames.
    *   **Estudar**: Aprender (Aulas), Resumos, Vídeos.
    *   **Suporte**: Professor AI.
3.  **Granularidade de Conteúdo**: Seleção de Ano (10º, 11º, 12º) -> Tópico -> Subtópico.
4.  **Interface de Execução**:
    *   **Exercícios**: Questão -> Campo de Resposta -> Autoavaliação/Análise AI -> Feedback.
    *   **Vídeos**: Playlist de vídeos curtos e focados.
    *   **Resumos**: Texto estruturado com diagramas e fórmulas.

## 2. Componentes de UX (Interface)
*   **Sidebar**: Menu lateral com ícones claros (Início, Exercícios, Testes, Exames, Leaderboard, Estatísticas, Professor AI).
*   **Cards de Disciplina**: Uso de cores vibrantes e ilustrações temáticas para cada matéria.
*   **Progress Bars**: Indicadores visuais de conclusão em cada tópico e subtópico (ex: "0/24 exercícios").
*   **Modais de Retenção**: "Já vais embora?" - Resumo da sessão (tempo, acertos, feitos) ao tentar sair de uma atividade.
*   **Interface de Exercício**:
    *   Timer persistente no topo.
    *   Botão de "Resolução" disponível.
    *   Integração de Chat AI ("Professor AI") diretamente na página de exercícios para dúvidas contextuais.

## 3. Mecânicas e Dinâmicas (Gamificação)
*   **Chamas (Streaks)**: Mecânica de retenção diária (login/atividade consecutiva).
*   **Leaderboard**: Dinâmica competitiva baseada em pontos ou exercícios concluídos.
*   **Estatísticas**: Visualização de desempenho (Semanal, Mensal, Anual) para auto-monitoramento.
*   **Feedback Instantâneo**: Uso de AI para analisar respostas abertas, não apenas múltipla escolha.

## 4. Elementos de Conversão
*   **Paywall/Login Wall**: Acesso limitado sem conta; modais de login frequentes ao tentar acessar funcionalidades profundas.
*   **Social Proof**: Menção a "Conteúdo criado por professores especializados".
