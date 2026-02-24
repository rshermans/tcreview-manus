import { useState } from 'react';
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
  onAnalysisComplete: (data: any) => void;
}

const ContentSubmission = ({ onAnalysisStart, onAnalysisComplete }: ContentSubmissionProps) => {
  const [contentType, setContentType] = useState<string | null>(null);
  const [content, setContent] = useState<string>('');
  const [error, setError] = useState<string>('');

  const handleTypeSelection = (type: string) => {
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
    } catch (err) {
      setError('Ocorreu um erro ao analisar o conteúdo. Tente novamente.');
      // Optional: switch back to submission form on error
      // onNewAnalysis();
    }
  };

  return (
    <div className="card">
      <h2>Verificação de Conteúdo</h2>
      <p>Selecione o tipo de conteúdo que deseja verificar:</p>

      <div className="button-group">
        <button
          className={contentType === 'text' ? 'button active' : 'button secondary'}
          onClick={() => handleTypeSelection('text')}
        >
          Texto
        </button>
        <button
          className={contentType === 'link' ? 'button active' : 'button secondary'}
          onClick={() => handleTypeSelection('link')}
        >
          Link
        </button>
        <button
          className={contentType === 'image' ? 'button active' : 'button secondary'}
          onClick={() => handleTypeSelection('image')}
        >
          Imagem
        </button>
      </div>

      {contentType && (
        <div className="input-container">
          <label>
            {contentType === 'text' && 'Insira o texto para verificação:'}
            {contentType === 'link' && 'Insira o link para verificação:'}
            {contentType === 'image' && 'Insira o URL da imagem para verificação:'}
          </label>
          {contentType === 'text' ? (
            <textarea
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder="Cole ou digite o texto aqui..."
            />
          ) : (
            <input
              type="text"
              value={content}
              onChange={(e) => setContent(e.target.value)}
              placeholder={
                contentType === 'link'
                  ? 'https://exemplo.com/noticia'
                  : 'https://exemplo.com/imagem.jpg'
              }
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
