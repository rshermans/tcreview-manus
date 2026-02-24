import React, { useState } from 'react';
import './ContentSubmission.css';
import { analyzeContent } from '../services/api';

/**
 * Componente de submissão inicial.
 * Permite ao usuário escolher entre texto, link ou imagem e introduzir o conteúdo.
 * Faz validações básicas antes de enviar ao backend.
 */
export interface ContentData {
  type: string;
  content: string;
}

interface ContentSubmissionProps {
  onAnalysisStart: () => void;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  onAnalysisComplete: (data: any) => void;
}

type ContentType = 'text' | 'link' | 'image';

interface ContentTypeConfig {
  id: ContentType;
  label: string;
  inputLabel: string;
  placeholder: string;
}

const CONTENT_TYPES: ContentTypeConfig[] = [
  {
    id: 'text',
    label: 'Texto',
    inputLabel: 'Insira o texto para verificação:',
    placeholder: 'Cole ou digite o texto aqui...',
  },
  {
    id: 'link',
    label: 'Link',
    inputLabel: 'Insira o link para verificação:',
    placeholder: 'https://exemplo.com/noticia',
  },
  {
    id: 'image',
    label: 'Imagem',
    inputLabel: 'Insira o URL da imagem para verificação:',
    placeholder: 'https://exemplo.com/imagem.jpg',
  },
];

const ContentSubmission: React.FC<ContentSubmissionProps> = ({ onAnalysisStart, onAnalysisComplete }) => {
  const [contentType, setContentType] = useState<ContentType | null>(null);
  const [content, setContent] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleTypeSelection = (type: ContentType) => {
    setContentType(type);
    setError('');
  };

  const handleSubmit = async () => {
    if (!contentType) {
      setError('Por favor, selecione um tipo de conteúdo');
      return;
    }
    if (!content.trim()) {
      setError('Por favor, insira o conteúdo para verificação');
      return;
    }
    if (contentType === 'link' && !content.startsWith('http')) {
      setError('Por favor, insira um link válido começando com http:// ou https://');
      return;
    }

    setError('');
    onAnalysisStart();

    try {
      const result = await analyzeContent(contentType, content);
      onAnalysisComplete(result);
    } catch {
      setError('Ocorreu um erro ao analisar o conteúdo. Tente novamente.');
      // Optional: switch back to submission form on error
      // onNewAnalysis();
    }
  };

  const currentTypeConfig = CONTENT_TYPES.find(t => t.id === contentType);

  return (
    <div className="card">
      <h2>Verificação de Conteúdo</h2>
      <p>Selecione o tipo de conteúdo que deseja verificar:</p>

      <div className="button-group">
        {CONTENT_TYPES.map((type) => (
          <button
            key={type.id}
            className={contentType === type.id ? 'button active' : 'button secondary'}
            onClick={() => handleTypeSelection(type.id)}
          >
            {type.label}
          </button>
        ))}
      </div>

      {contentType && (
        <div className="input-container">
          <label>
            {currentTypeConfig?.inputLabel}
          </label>
          {contentType === 'text' ? (
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder={currentTypeConfig?.placeholder}
            />
          ) : (
            <input
              type="text"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder={currentTypeConfig?.placeholder}
            />
          )}
          {error && <p className="error-message">{error}</p>}
        </div>
      )}

      <div className="footer">
        <p className="help-text">O TrueCheck ajuda a verificar a factualidade de conteúdos.</p>
        <button
          className="button"
          disabled={!contentType || !content.trim()}
          onClick={handleSubmit}
        >
          Verificar agora
        </button>
      </div>
    </div>
  );
};

export default ContentSubmission;
