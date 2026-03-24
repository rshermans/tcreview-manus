import { useState } from 'react';
import './App.css';
import GamificationBar from './components/GamificationBar';
import OmniInput from './components/OmniInput';
import CognitiveResults from './components/CognitiveResults';

type AppState = 'input' | 'analyzing' | 'results';

function App() {
  const [appState, setAppState] = useState<AppState>('input');
  const [analysisResult, setAnalysisResult] = useState<any>(null);

  // Mocked User Gamification Data (would come from Auth/Backend)
  const userStats = {
    streak: 12,
    tokens: 450,
    level: 'Investigador Junior'
  };

  const handleAnalyze = async (content: string, type: 'text' | 'url' | 'image') => {
    setAppState('analyzing');

    try {
      const response = await fetch('http://localhost:5000/api/analysis/omni', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ content, type })
      });

      if (!response.ok) {
        throw new Error('Falha na análise');
      }

      const backendResult = await response.json();

      const formattedResult = {
        trust_score: backendResult.trust_score || 'N/A',
        summary: backendResult.summary || 'A análise indica a presença de viés e linguagem sensacionalista.',
        teach_insights: backendResult.teach_insights,
        details: content
      };

      setAnalysisResult(formattedResult);
      setAppState('results');
    } catch (error) {
      console.error("Erro ao comunicar com backend:", error);
      setAppState('input'); // Reset on error
    }
  };

  const resetToInput = () => {
    setAppState('input');
    setAnalysisResult(null);
  };

  return (
    <div className="App">
      <GamificationBar
        streak={userStats.streak}
        tokens={userStats.tokens}
        level={userStats.level}
      />

      <main className="app-main">
        {appState !== 'results' && (
          <div className="hero-section">
            <h1>O que vamos verificar hoje?</h1>
            <p>Descubra a veracidade de notícias, links ou imagens.</p>
          </div>
        )}

        {(appState === 'input' || appState === 'analyzing') && (
          <OmniInput
            onAnalyze={handleAnalyze}
            isAnalyzing={appState === 'analyzing'}
          />
        )}

        {appState === 'results' && analysisResult && (
          <CognitiveResults
            result={analysisResult}
            onNewAnalysis={resetToInput}
          />
        )}
      </main>
    </div>
  );
}

export default App;
