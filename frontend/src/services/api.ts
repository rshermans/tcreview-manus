import axios from 'axios';

/*
 * Serviço API para comunicar com o backend TrueCheck.
 * A URL base é lida de VITE_API_URL, com fallback para localhost.
 */
const API_URL: string = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';
const API_KEY: string = import.meta.env.VITE_API_KEY || '';

const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'X-API-Key': API_KEY,
  },
});

export async function analyzeContent(contentType: string, content: string): Promise<any> {
  const response = await axiosInstance.post('/analysis/preliminary', {
    type: contentType,
    content: content,
  });
  return response.data;
}

export async function crossVerifyContent(content: string, analysis: any): Promise<any> {
  const response = await axiosInstance.post('/analysis/cross-verification', {
    content: content,
    analysis: analysis,
  });
  return response.data;
}

export async function analyzeContext(content: string): Promise<any> {
  const response = await axiosInstance.post('/analysis/context', { content });
  return response.data;
}

export async function getFinalEvaluation(userPerception: any, aiAnalysis: any): Promise<any> {
  const response = await axiosInstance.post('/analysis/final', {
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
