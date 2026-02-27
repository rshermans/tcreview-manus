import React, { useState } from 'react';
import './CognitiveResults.css';

interface CognitiveResultsProps {
    result: any;
    onNewAnalysis: () => void;
}

const CognitiveResults: React.FC<CognitiveResultsProps> = ({ result, onNewAnalysis }) => {
    const [activeTab, setActiveTab] = useState<'check' | 'learn' | 'study'>('check');

    return (
        <div className="cognitive-results-container">
            <div className="tabs-header">
                <button
                    className={`tab-btn ${activeTab === 'check' ? 'active' : ''}`}
                    onClick={() => setActiveTab('check')}
                >
                    🔘 Verificar (Check)
                </button>
                <button
                    className={`tab-btn ${activeTab === 'learn' ? 'active' : ''}`}
                    onClick={() => setActiveTab('learn')}
                >
                    🧠 Aprender (Teach Agent)
                </button>
                <button
                    className={`tab-btn ${activeTab === 'study' ? 'active' : ''}`}
                    onClick={() => setActiveTab('study')}
                >
                    🎓 Estudar (Trilhas)
                </button>
            </div>

            <div className="tab-content">
                {activeTab === 'check' && (
                    <div className="check-view fade-in">
                        <h2>Nível de Confiança: <span className="trust-score">{result.trust_score || '35%'}</span></h2>
                        <div className="summary-card">
                            <h3>Resumo</h3>
                            <p>{result.summary || 'A análise indica a presença de viés e linguagem sensacionalista. Faltam fontes para corroborar as afirmações centrais.'}</p>
                        </div>
                        <div className="sources-card">
                            <h3>Fontes Relacionadas</h3>
                            <ul>
                                <li>⚠️ Possível desinformação detectada nas bases verificadas.</li>
                            </ul>
                        </div>
                    </div>
                )}

                {activeTab === 'learn' && (
                    <div className="learn-view fade-in">
                        <div className="teach-agent-chat">
                            <div className="agent-bubble">
                                <span className="agent-icon">🤖 Teach:</span>
                                <p>Notei que este texto usa palavras como "chocante" e "nunca visto antes". Você sabe por que jornais sensacionalistas usam esse tipo de adjetivo em vez de apenas relatar o fato?</p>
                            </div>
                            <div className="user-scaffolding-opts">
                                <button>Para chamar atenção e cliques?</button>
                                <button>Para mostrar que é muito importante?</button>
                                <button>Não tenho certeza, me explique.</button>
                            </div>
                        </div>
                        <div className="text-highlight-view">
                            <h3>Cuidado com Vieses</h3>
                            <p className="highlighted-text">
                                O texto contém afirmações absolutas <mark className="bias-mark">sem apresentar os dados originais</mark>.
                            </p>
                        </div>
                    </div>
                )}

                {activeTab === 'study' && (
                    <div className="study-view fade-in">
                        <h3>Trilha Recomendada para Você</h3>
                        <div className="module-card">
                            <div className="module-icon">📊</div>
                            <div className="module-info">
                                <h4>Heurísticas Mentais e Estatísticas</h4>
                                <p>Aprenda como números podem ser manipulados para criar narrativas falsas.</p>
                                <div className="progress-bar-bg"><div className="progress-bar-fill" style={{ width: '20%' }}></div></div>
                            </div>
                            <button className="start-btn">Continuar (2 Mins)</button>
                        </div>
                    </div>
                )}
            </div>

            <button className="new-analysis-btn" onClick={onNewAnalysis}>
                🔙 Iniciar Nova Verificação
            </button>
        </div>
    );
};

export default CognitiveResults;
