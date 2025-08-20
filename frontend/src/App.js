import React, { useState } from 'react';
import './App.css';
import ProgressStepper from './components/ProgressStepper';
import ContentSubmission from './components/ContentSubmission';
import PreliminaryAnalysis from './components/PreliminaryAnalysis';
import ContentAnalysis from './components/ContentAnalysis';
import Results from './components/Results';

function App() {
  const [currentStep, setCurrentStep] = useState(1);
  const [contentData, setContentData] = useState(null);
  const [analysisResult, setAnalysisResult] = useState(null);
  const [userPerception, setUserPerception] = useState(null);

  const handleContentSubmit = (data) => {
    setContentData(data);
    setCurrentStep(2);
  };

  const handlePreliminaryAnalysisComplete = (result) => {
    setAnalysisResult(result);
    setCurrentStep(3);
  };

  const handleContentAnalysisComplete = (data) => {
    setUserPerception(data.userPerception);
    setCurrentStep(7); // Pulando algumas etapas para simplificar
  };

  const handleReset = () => {
    setCurrentStep(1);
    setContentData(null);
    setAnalysisResult(null);
    setUserPerception(null);
  };

  return (
    <div className="container">
      <header className="header">
        <h1 className="title">TrueCheck</h1>
        <p className="subtitle">Verificação de Factualidade e Educação Mediática</p>
      </header>
      
      <ProgressStepper currentStep={currentStep} />
      
      <main>
        {currentStep === 1 && (
          <ContentSubmission onSubmit={handleContentSubmit} />
        )}
        
        {currentStep === 2 && contentData && (
          <PreliminaryAnalysis 
            content={contentData} 
            onComplete={handlePreliminaryAnalysisComplete} 
          />
        )}
        
        {currentStep === 3 && analysisResult && (
          <ContentAnalysis 
            content={contentData}
            analysisResult={analysisResult}
            onComplete={handleContentAnalysisComplete}
          />
        )}
        
        {currentStep === 7 && userPerception && analysisResult && (
          <Results 
            content={contentData}
            userPerception={userPerception}
            aiAnalysis={{
              sourceReliability: analysisResult.sourceReliability,
              factualConsistency: analysisResult.factualConsistency,
              contentQuality: analysisResult.contentQuality,
              technicalIntegrity: analysisResult.technicalIntegrity
            }}
            onReset={handleReset}
          />
        )}
      </main>
      
      <footer className="footer">
        <p>TrueCheck © 2025 - Combatendo a desinformação e promovendo a educação mediática</p>
      </footer>
    </div>
  );
}

export default App;
