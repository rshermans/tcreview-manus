import React from 'react';
import './Results.css';

// Define the expected structure of the analysis result
interface AnalysisResult {
  analysis: string;
  sourceReliability: number;
  factualConsistency: number;
  contentQuality: number;
  technicalIntegrity: number;
}

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

  const scoreConfig: { label: string; key: Exclude<keyof AnalysisResult, 'analysis'> }[] = [
    { label: 'Confiabilidade da Fonte', key: 'sourceReliability' },
    { label: 'Consistência Factual', key: 'factualConsistency' },
    { label: 'Qualidade do Conteúdo', key: 'contentQuality' },
    { label: 'Integridade Técnica', key: 'technicalIntegrity' },
  ];

  return (
    <div className="card results-card">
      <h2>Resultados da Verificação Preliminar</h2>

      <div className="analysis-section">
        <h3>Resumo da Análise da IA</h3>
        <p className="analysis-text">{result.analysis}</p>

        <div className="scores-grid">
          {scoreConfig.map((item) => (
            <div key={item.key} className="score-item">
              <h4>{item.label}</h4>
              <div className="score-value" style={{ color: getScoreColor(result[item.key]) }}>
                {result[item.key]}/100
              </div>
            </div>
          ))}
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
