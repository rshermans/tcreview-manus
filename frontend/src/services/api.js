import axios from 'axios';

// Base da API. Em produção, configure REACT_APP_API_URL no arquivo .env.
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

const api = {
  // Análise preliminar
  analyzeContent: async (contentType, content) => {
    try {
      const response = await axios.post(`${API_URL}/analysis/preliminary`, {
        type: contentType,
        content: content,
      });
      return response.data;
    } catch (error) {
      console.error('Erro ao analisar conteúdo:', error);
      throw error;
    }
  },

  // Verificação cruzada
  crossVerifyContent: async (content, analysis) => {
    try {
      const response = await axios.post(`${API_URL}/analysis/cross-verification`, {
        content: content,
        analysis: analysis,
      });
      return response.data;
    } catch (error) {
      console.error('Erro na verificação cruzada:', error);
      throw error;
    }
  },

  // Análise de contexto
  analyzeContext: async (content) => {
    try {
      const response = await axios.post(`${API_URL}/analysis/context`, {
        content: content,
      });
      return response.data;
    } catch (error) {
      console.error('Erro na análise de contexto:', error);
      throw error;
    }
  },

  // Avaliação final
  getFinalEvaluation: async (userPerception, aiAnalysis) => {
    try {
      const response = await axios.post(`${API_URL}/analysis/final`, {
        user_perception: userPerception,
        ai_analysis: aiAnalysis,
      });
      return response.data;
    } catch (error) {
      console.error('Erro na avaliação final:', error);
      throw error;
    }
  }
};

export default api;
