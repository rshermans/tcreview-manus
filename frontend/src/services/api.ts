import axios from 'axios';
import type { AnalysisResult } from '../components/Results';

/*
 * Serviço API para comunicar com o backend TrueCheck.
 * A URL base é lida de VITE_API_URL, com fallback para localhost.
 */
const API_URL: string = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

/**
 * Helper genérico para requisições POST.
 * Centraliza a construção da URL, logging de erros e extração de dados do axios.
 */
async function post<T>(endpoint: string, data: Record<string, unknown>): Promise<T> {
  try {
    const response = await axios.post<T>(`${API_URL}${endpoint}`, data);
    return response.data;
  } catch (error) {
    console.error(`Erro na requisição POST para ${endpoint}:`, error);
    throw error;
  }
}

export async function analyzeContent(contentType: string, content: string): Promise<AnalysisResult> {
  return post<AnalysisResult>('/analysis/preliminary', {
    type: contentType,
    content: content,
  });
}

export async function crossVerifyContent(content: string, analysis: unknown): Promise<unknown> {
  return post<unknown>('/analysis/cross-verification', {
    content: content,
    analysis: analysis,
  });
}

export async function analyzeContext(content: string): Promise<unknown> {
  return post<unknown>('/analysis/context', { content });
}

export async function getFinalEvaluation(userPerception: unknown, aiAnalysis: unknown): Promise<unknown> {
  return post<unknown>('/analysis/final', {
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
