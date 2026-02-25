import React from 'react';
import './Results.css';
import type { AnalysisResult } from '../services/api';

interface ResultsProps {
  result: AnalysisResult;
  onNewAnalysis: () => void;
}

const Results: React.FC<ResultsProps> = ({ result, onNewAnalysis }) => {
  // A simple function to get a color based on the score
  const getScoreColor = (score: number) => {
    if (score < 40) return '#ef4444'; // red
    if (score < 70) return '#f59e0b'; // yellow
    return '#10b981'; // green
  };

  return (
    <div className="card results-card">
      <h2>Resultados da Verificação Preliminar</h2>

      <div className="analysis-section">
        <h3>Resumo da Análise da IA</h3>
        <p className="analysis-text">{result.analysis}</p>

        <div className="scores-grid">
          <div className="score-item">
            <h4>Confiabilidade da Fonte</h4>
            <div className="score-value" style={{ color: getScoreColor(result.sourceReliability) }}>
              {result.sourceReliability}/100
            </div>
          </div>
          <div className="score-item">
            <h4>Consistência Factual</h4>
            <div className="score-value" style={{ color: getScoreColor(result.factualConsistency) }}>
              {result.factualConsistency}/100
            </div>
          </div>
          <div className="score-item">
            <h4>Qualidade do Conteúdo</h4>
            <div className="score-value" style={{ color: getScoreColor(result.contentQuality) }}>
              {result.contentQuality}/100
            </div>
          </div>
          <div className="score-item">
            <h4>Integridade Técnica</h4>
            <div className="score-value" style={{ color: getScoreColor(result.technicalIntegrity) }}>
              {result.technicalIntegrity}/100
            </div>
          </div>
        </div>
      </div>

      <div className="footer">
        <button className="button" onClick={onNewAnalysis}>
          Nova Verificação
        </button>
      </div>
    </div>
  );
};

export default Results;
