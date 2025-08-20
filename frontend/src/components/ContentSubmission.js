import React, { useState } from 'react';
import './ContentSubmission.css';

function ContentSubmission({ onSubmit }) {
  const [contentType, setContentType] = useState(null);
  const [content, setContent] = useState('');
  const [error, setError] = useState('');

  const handleTypeSelection = (type) => {
    setContentType(type);
    setError('');
  };

  const handleSubmit = () => {
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

    onSubmit({ type: contentType, content });
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
              placeholder={contentType === 'link' ? 'https://exemplo.com/noticia' : 'https://exemplo.com/imagem.jpg'}
            />
          )}
          
          {error && (
            <p className="error-message">{error}</p>
          )}
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
}

export default ContentSubmission;
