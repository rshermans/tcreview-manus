import React, { useEffect, useState } from 'react';
import './PreliminaryAnalysis.css';
import api from '../services/api';

function PreliminaryAnalysis({ content, onComplete }) {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [result, setResult] = useState(null);

  useEffect(() => {
    const analyzeContent = async () => {
      try {
        const analysisResult = await api.analyzeContent(content.type, content.content);
        setResult(analysisResult);
        // Aguarda um pouco para mostrar o resultado antes de avançar
        setTimeout(() => {
          onComplete(analysisResult);
        }, 1500);
      } catch (err) {
        setError('Erro ao analisar o conteúdo. Por favor, tente novamente.');
        console.error(err);
      } finally {
        setLoading(false);
      }
    };

    analyzeContent();
  }, [content, onComplete]);

  return (
    <div className="card analysis-card">
      <h2>Análise Preliminar</h2>
      
      <div className="content-info">
        <div className="info-item">
          <div className="info-icon">📄</div>
          <div>
            <h3>Tipo de Conteúdo</h3>
            <p>{content.type === 'text' ? 'Texto' : content.type === 'link' ? 'Link' : 'Imagem'}</p>
          </div>
        </div>
        
        <div className="info-item">
          <div className="info-icon">ℹ️</div>
          <div>
            <h3>Conteúdo Analisado</h3>
            <p className="truncate">{content.content}</p>
          </div>
        </div>
      </div>
      
      {loading ? (
        <div className="analysis-progress">
          <h3>Verificando...</h3>
          
          <div className="progress-items">
            <div className="progress-item">
              <div className="spinner"></div>
              <p>Analisando fonte</p>
            </div>
            
            <div className="progress-item">
              <div className="spinner"></div>
              <p>Verificando consistência factual</p>
            </div>
            
            <div className="progress-item">
              <div className="spinner"></div>
              <p>Avaliando contexto</p>
            </div>
          </div>
        </div>
      ) : error ? (
        <div className="error-message">
          <p>{error}</p>
          <button className="button" onClick={() => window.location.reload()}>
            Tentar novamente
          </button>
        </div>
      ) : (
        <div className="analysis-result">
          <h3>Análise Concluída</h3>
          <p>A análise preliminar foi concluída com sucesso. Avançando para a próxima etapa...</p>
        </div>
      )}
      
      <p className="help-text">
        {loading 
          ? "O TrueCheck está analisando o conteúdo. Este processo é automático e leva apenas alguns segundos."
          : error 
            ? "Ocorreu um erro durante a análise. Por favor, tente novamente."
            : "Análise concluída! Avançando para a próxima etapa..."
        }
      </p>
    </div>
  );
}

export default PreliminaryAnalysis;
