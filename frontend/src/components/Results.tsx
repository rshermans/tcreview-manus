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

type ScoreKey = Exclude<keyof AnalysisResult, 'analysis'>;

const scoreConfig: { key: ScoreKey; label: string }[] = [
  { key: 'sourceReliability', label: 'Confiabilidade da Fonte' },
  { key: 'factualConsistency', label: 'Consistência Factual' },
  { key: 'contentQuality', label: 'Qualidade do Conteúdo' },
  { key: 'technicalIntegrity', label: 'Integridade Técnica' },
];

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
          {scoreConfig.map(({ key, label }) => (
            <div key={key} className="score-item">
              <h4>{label}</h4>
              <div className="score-value" style={{ color: getScoreColor(result[key]) }}>
                {result[key]}/100
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
