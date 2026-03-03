import axios from 'axios';

/*
 * Serviço API para comunicar com o backend TrueCheck.
 * A URL base é lida de VITE_API_URL, com fallback para localhost.
 */
const API_URL: string = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';
const API_KEY: string = import.meta.env.VITE_API_KEY || '';

export const axiosInstance = axios.create({
  baseURL: API_URL,
  headers: {
    'X-API-Key': API_KEY,
  },
});
