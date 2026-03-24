import React, { useState } from 'react';
import './OmniInput.css';

interface OmniInputProps {
    onAnalyze: (content: string, type: 'text' | 'url' | 'image') => void;
    isAnalyzing: boolean;
}

const OmniInput: React.FC<OmniInputProps> = ({ onAnalyze, isAnalyzing }) => {
    const [inputValue, setInputValue] = useState('');

    const detectType = (input: string): 'text' | 'url' | 'image' => {
        // Basic detection logic
        if (input.startsWith('http://') || input.startsWith('https://')) {
            return 'url';
        }
        // Assuming image drop/paste logic handles visual files separately later
        return 'text';
    };

    const handleAnalyzeClick = () => {
        if (!inputValue.trim()) return;
        const type = detectType(inputValue);
        onAnalyze(inputValue, type);
    };

    return (
        <div className="omni-input-container">
            <div className="omni-input-wrapper">
                <textarea
                    className="omni-textarea"
                    placeholder="Cole um texto, link ou arraste uma imagem aqui..."
                    value={inputValue}
                    onChange={(e) => setInputValue(e.target.value)}
                    disabled={isAnalyzing}
                    rows={4}
                />
                <button
                    className="omni-analyze-btn"
                    onClick={handleAnalyzeClick}
                    disabled={isAnalyzing || !inputValue.trim()}
                >
                    {isAnalyzing ? (
                        <span className="spinner-icon">🔄 Analisando...</span>
                    ) : (
                        <span>✨ Verificar Contexto</span>
                    )}
                </button>
            </div>
            <div className="omni-hints">
                <p>💡 <b>Agente Teach:</b> Estou pronto para analisar heurísticas, vieses e fontes.</p>
            </div>
        </div>
    );
};

export default OmniInput;
