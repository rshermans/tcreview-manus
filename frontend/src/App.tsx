import { useState } from 'react';
import './App.css';
import type { AnalysisResult } from './components/Results';
import ContentSubmission from './components/ContentSubmission';
import ContentAnalysis from './components/ContentAnalysis';
import Results from './components/Results';

// Define the possible states of the application
type AppState = 'submission' | 'analyzing' | 'results';

function App() {
  const [appState, setAppState] = useState<AppState>('submission');
  const [analysisResult, setAnalysisResult] = useState<AnalysisResult | null>(null);

  const handleAnalysisComplete = (result: AnalysisResult) => {
    setAnalysisResult(result);
    setAppState('results');
  };

  const handleNewAnalysis = () => {
    setAppState('submission');
    setAnalysisResult(null);
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>TrueCheck</h1>
      </header>
      <main>
        {appState === 'submission' && (
          <ContentSubmission
            onAnalysisStart={() => setAppState('analyzing')}
            onAnalysisComplete={handleAnalysisComplete}
          />
        )}
        {appState === 'analyzing' && <ContentAnalysis />}
        {appState === 'results' && analysisResult && (
          <Results
            result={analysisResult}
            onNewAnalysis={handleNewAnalysis}
          />
        )}
      </main>
    </div>
  );
}

export default App;
