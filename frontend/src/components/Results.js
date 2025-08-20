import React, { useEffect, useState } from 'react';
import './Results.css';
import api from '../services/api';

function Results({ content, userPerception, aiAnalysis, onReset }) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [comparisonResult, setComparisonResult] = useState(null);

  useEffect(() => {
    const getFinalEvaluation = async () => {
      try {
        const result = await api.getFinalEvaluation(userPerception, aiAnalysis);
        setComparisonResult(result);
      } catch (err) {
        setError('Erro ao obter a avaliação final. Por favor, tente novamente.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    getFinalEvaluation();
  }, [userPerception, aiAnalysis]);

  // Função para determinar a categoria de factualidade com base no score
  const getFactualityCategory = (score) => {
    if (score <= 20) return { 
      label: "Não Factual", 
      color: "#ef4444" // vermelho
    };
    if (score <= 40) return { 
      label: "Pouco Factual", 
      color: "#f97316" // laranja
    };
    if (score <= 60) return { 
      label: "Parcialmente Factual", 
      color: "#f59e0b" // amarelo
    };
    if (score <= 80) return { 
      label: "Majoritariamente Factual", 
      color: "#84cc16" // verde claro
    };
    return { 
      label: "Tendencialmente Factual", 
      color: "#10b981" // verde
    };
  };

  if (loading) {
    return (
      <div className="card">
        <h2>Resultados</h2>
        <div className="loading-container">
          <div className="spinner large"></div>
          <p>Calculando resultados finais...</p>
        </div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="card">
        <h2>Resultados</h2>
        <div className="error-message">
          <p>{error}</p>
          <button className="button" onClick={onReset}>
            Tentar novamente
          </button>
        </div>
      </div>
    );
  }

  const userCategory = getFactualityCategory(comparisonResult.userScore);
  const aiCategory = getFactualityCategory(comparisonResult.aiScore);

  return (
    <div className="card results-card">
      <h2>Resultados da Verificação</h2>
      
      <div className="comparison-section">
        <h3>Comparação de Avaliações</h3>
        
        <div className="results-grid">
          <div className="result-column">
            <h4>Sua Avaliação</h4>
            <div 
              className="score-circle" 
              style={{ backgroundColor: userCategory.color }}
            >
              {comparisonResult.userScore}
            </div>
            <p className="category-label">{userCategory.label}</p>
            
            <div className="detail-scores">
              <div className="detail-score-item">
                <span>Credibilidade da Fonte:</span>
                <span>{userPerception.sourceCredibility}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Análise Crítica:</span>
                <span>{userPerception.criticalAnalysis}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Avaliação Contextual:</span>
                <span>{userPerception.contextEvaluation}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Julgamento Final:</span>
                <span>{userPerception.finalJudgment}/100</span>
              </div>
            </div>
          </div>
          
          <div className="result-column">
            <h4>Verificação Automatizada</h4>
            <div 
              className="score-circle" 
              style={{ backgroundColor: aiCategory.color }}
            >
              {comparisonResult.aiScore}
            </div>
            <p className="category-label">{aiCategory.label}</p>
            
            <div className="detail-scores">
              <div className="detail-score-item">
                <span>Confiabilidade da Fonte:</span>
                <span>{aiAnalysis.sourceReliability}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Consistência Factual:</span>
                <span>{aiAnalysis.factualConsistency}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Qualidade do Conteúdo:</span>
                <span>{aiAnalysis.contentQuality}/100</span>
              </div>
              <div className="detail-score-item">
                <span>Integridade Técnica:</span>
                <span>{aiAnalysis.technicalIntegrity}/100</span>
              </div>
            </div>
          </div>
        </div>
        
        <div className="discrepancy-analysis">
          <h4>Análise de Discrepância</h4>
          <p>
            <strong>Diferença:</strong> {comparisonResult.discrepancy} pontos ({comparisonResult.discrepancyLevel})
          </p>
          <p>{comparisonResult.feedback}</p>
        </div>
      </div>
      
      <div className="learning-section">
        <h3>Aprendizagens</h3>
        
        <div className="learning-items">
          <div className="learning-item">
            <div className="learning-icon">✓</div>
            <div>
              <h4>Verificação de Fontes</h4>
              <p>Sempre verifique a credibilidade da fonte antes de confiar em uma informação.</p>
            </div>
          </div>
          
          <div className="learning-item">
            <div className="learning-icon">✓</div>
            <div>
              <h4>Verificação Cruzada</h4>
              <p>Compare a informação com outras fontes confiáveis para confirmar sua veracidade.</p>
            </div>
          </div>
          
          <div className="learning-item">
            <div className="learning-icon">✓</div>
            <div>
              <h4>Contexto Completo</h4>
              <p>Considere o contexto histórico e atual para compreender completamente a informação.</p>
            </div>
          </div>
          
          <div className="learning-item">
            <div className="learning-icon">✓</div>
            <div>
              <h4>Separação de Fatos e Opiniões</h4>
              <p>Identifique o que são fatos verificáveis e o que são opiniões ou interpretações.</p>
            </div>
          </div>
        </div>
      </div>
      
      <div className="footer">
        <button className="button" onClick={onReset}>
          Nova Verificação
        </button>
      </div>
    </div>
  );
}

export default Results;
