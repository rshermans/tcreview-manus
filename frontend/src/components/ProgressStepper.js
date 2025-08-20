import React from 'react';
import './ProgressStepper.css';

function ProgressStepper({ currentStep }) {
  const steps = [
    { id: 1, title: 'Submissão' },
    { id: 2, title: 'Análise Preliminar' },
    { id: 3, title: 'Análise de Conteúdo' },
    { id: 4, title: 'Verificação Cruzada' },
    { id: 5, title: 'Análise de Contexto' },
    { id: 6, title: 'Avaliação Final' },
    { id: 7, title: 'Resultados' }
  ];
  
  return (
    <div className="stepper">
      {steps.map((step, index) => (
        <div key={step.id} className="step-container">
          {index > 0 && (
            <div 
              className={`step-line ${step.id <= currentStep ? 'active' : ''}`}
            />
          )}
          <div 
            className={`step-circle ${
              step.id < currentStep 
                ? 'completed' 
                : step.id === currentStep 
                  ? 'active' 
                  : ''
            }`}
          >
            {step.id < currentStep ? '✓' : step.id}
          </div>
          <div className="step-title">{step.title}</div>
        </div>
      ))}
    </div>
  );
}

export default ProgressStepper;
