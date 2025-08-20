import React from 'react';
import './ContentAnalysis.css';

const ContentAnalysis: React.FC = () => {
  return (
    <div className="card">
      <h2>Analisando...</h2>
      <p>Aguarde enquanto o conteúdo está sendo verificado.</p>
      {/* A more advanced version could include a progress bar or spinner */}
      <div className="spinner"></div>
    </div>
  );
};

export default ContentAnalysis;
