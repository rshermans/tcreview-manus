/* eslint-disable @typescript-eslint/no-explicit-any */
import axios from 'axios';

/*
 * Serviço API para comunicar com o backend TrueCheck.
 * A URL base é lida de VITE_API_URL, com fallback para localhost.
 */
const API_URL: string = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

/**
 * Generic POST request wrapper.
 * Centralizes error handling and API URL construction.
 *
 * @param endpoint The API endpoint (e.g., '/analysis/preliminary')
 * @param data The data to be sent in the request body
 * @returns The response data
 */
async function post<T>(endpoint: string, data: any): Promise<T> {
  try {
    const response = await axios.post(`${API_URL}${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error(`Error requesting ${endpoint}:`, error);
    throw error;
  }
}

export async function analyzeContent(contentType: string, content: string): Promise<any> {
  return post('/analysis/preliminary', {
    type: contentType,
    content: content,
  });
}

export async function crossVerifyContent(content: string, analysis: any): Promise<any> {
  return post('/analysis/cross-verification', {
    content: content,
    analysis: analysis,
  });
}

export async function analyzeContext(content: string): Promise<any> {
  return post('/analysis/context', { content });
}

export async function getFinalEvaluation(userPerception: any, aiAnalysis: any): Promise<any> {
  return post('/analysis/final', {
    user_perception: userPerception,
    ai_analysis: aiAnalysis,
  });
}

const api = {
  analyzeContent,
  crossVerifyContent,
  analyzeContext,
  getFinalEvaluation,
};

export default api;
