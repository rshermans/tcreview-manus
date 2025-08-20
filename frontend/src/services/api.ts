import axios from 'axios';

/*
 * Serviço API para comunicar com o backend TrueCheck.
 * A URL base é lida de VITE_API_URL, com fallback para localhost.
 */
const API_URL: string = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

export async function analyzeContent(contentType: string, content: string): Promise<any> {
  const response = await axios.post(`${API_URL}/analysis/preliminary`, {
    type: contentType,
    content: content,
  });
  return response.data;
}

export async function crossVerifyContent(content: string, analysis: any): Promise<any> {
  const response = await axios.post(`${API_URL}/analysis/cross-verification`, {
    content: content,
    analysis: analysis,
  });
  return response.data;
}

export async function analyzeContext(content: string): Promise<any> {
  const response = await axios.post(`${API_URL}/analysis/context`, { content });
  return response.data;
}

export async function getFinalEvaluation(userPerception: any, aiAnalysis: any): Promise<any> {
  const response = await axios.post(`${API_URL}/analysis/final`, {
    user_perception: userPerception,
    ai_analysis: aiAnalysis,
  });
  return response.data;
}

const api = {
  analyzeContent,
  crossVerifyContent,
  analyzeContext,
  getFinalEvaluation,
};

export default api;
