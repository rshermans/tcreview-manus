import React, { useState } from 'react';
import './ContentAnalysis.css';

function ContentAnalysis({ content, analysisResult, onComplete }) {
  const [userRating, setUserRating] = useState({
    sourceCredibility: 50,
    criticalAnalysis: 50,
    contextEvaluation: 50,
    finalJudgment: 50
  });

  const handleSliderChange = (field, value) => {
    setUserRating(prev => ({
      ...prev,
      [field]: parseInt(value)
    }));
  };

  const handleSubmit = () => {
    // Passa tanto a análise da IA quanto a avaliação do usuário
    onComplete({
      userPerception: userRating,
      aiAnalysis: {
        sourceReliability: analysisResult.sourceReliability,
        factualConsistency: analysisResult.factualConsistency,
        contentQuality: analysisResult.contentQuality,
        technicalIntegrity: analysisResult.technicalIntegrity
      }
    });
  };

  return (
    <div className="card">
      <h2>Análise de Conteúdo</h2>
      
      <div className="analysis-section">
        <h3>Análise da IA</h3>
        <p className="analysis-text">{analysisResult.analysis}</p>
        
        <div className="scores-grid">
          <div className="score-item">
            <h4>Confiabilidade da Fonte</h4>
            <div className="score-value">{analysisResult.sourceReliability}/100</div>
          </div>
          <div className="score-item">
            <h4>Consistência Factual</h4>
            <div className="score-value">{analysisResult.factualConsistency}/100</div>
          </div>
          <div className="score-item">
            <h4>Qualidade do Conteúdo</h4>
            <div className="score-value">{analysisResult.contentQuality}/100</div>
          </div>
          <div className="score-item">
            <h4>Integridade Técnica</h4>
            <div className="score-value">{analysisResult.technicalIntegrity}/100</div>
          </div>
        </div>
      </div>
      
      <div className="user-evaluation-section">
        <h3>Sua Avaliação</h3>
        <p>Com base na sua análise do conteúdo, avalie os seguintes aspectos:</p>
        
        <div className="slider-container">
          <label>
            <span>Credibilidade da Fonte</span>
            <span className="slider-value">{userRating.sourceCredibility}</span>
          </label>
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={userRating.sourceCredibility} 
            onChange={(e) => handleSliderChange('sourceCredibility', e.target.value)}
          />
        </div>
        
        <div className="slider-container">
          <label>
            <span>Análise Crítica</span>
            <span className="slider-value">{userRating.criticalAnalysis}</span>
          </label>
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={userRating.criticalAnalysis} 
            onChange={(e) => handleSliderChange('criticalAnalysis', e.target.value)}
          />
        </div>
        
        <div className="slider-container">
          <label>
            <span>Avaliação Contextual</span>
            <span className="slider-value">{userRating.contextEvaluation}</span>
          </label>
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={userRating.contextEvaluation} 
            onChange={(e) => handleSliderChange('contextEvaluation', e.target.value)}
          />
        </div>
        
        <div className="slider-container">
          <label>
            <span>Julgamento Final</span>
            <span className="slider-value">{userRating.finalJudgment}</span>
          </label>
          <input 
            type="range" 
            min="0" 
            max="100" 
            value={userRating.finalJudgment} 
            onChange={(e) => handleSliderChange('finalJudgment', e.target.value)}
          />
        </div>
      </div>
      
      <div className="footer">
        <p className="help-text">Sua avaliação ajuda a comparar a percepção humana com a análise automatizada.</p>
        <button className="button" onClick={handleSubmit}>
          Continuar
        </button>
      </div>
    </div>
  );
}

export default ContentAnalysis;
