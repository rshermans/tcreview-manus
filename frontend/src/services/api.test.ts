import { describe, it, expect, vi, beforeEach } from 'vitest';
import axios from 'axios';
import { analyzeContent, crossVerifyContent, analyzeContext, getFinalEvaluation } from './api';

vi.mock('axios');

describe('api service', () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  describe('analyzeContent', () => {
    it('calls the correct endpoint with correct parameters', async () => {
      const mockData = {
        analysis: 'Test analysis',
        sourceReliability: 80,
        factualConsistency: 90,
        contentQuality: 85,
        technicalIntegrity: 95
      };
      vi.mocked(axios.post).mockResolvedValue({ data: mockData });

      const contentType = 'text';
      const content = 'Hello world';
      const result = await analyzeContent(contentType, content);

      expect(axios.post).toHaveBeenCalledWith(
        expect.stringContaining('/analysis/preliminary'),
        {
          type: contentType,
          content: content,
        }
      );
      expect(result).toEqual(mockData);
    });

    it('handles errors', async () => {
      const errorMessage = 'Network Error';
      vi.mocked(axios.post).mockRejectedValue(new Error(errorMessage));

      await expect(analyzeContent('text', 'content')).rejects.toThrow(errorMessage);
    });
  });

  describe('crossVerifyContent', () => {
    it('calls the correct endpoint with correct parameters', async () => {
      const mockData = { result: 'verified' };
      vi.mocked(axios.post).mockResolvedValue({ data: mockData });

      const content = 'Hello world';
      const analysis = { some: 'analysis' };
      const result = await crossVerifyContent(content, analysis);

      expect(axios.post).toHaveBeenCalledWith(
        expect.stringContaining('/analysis/cross-verification'),
        {
          content: content,
          analysis: analysis,
        }
      );
      expect(result).toEqual(mockData);
    });
  });

  describe('analyzeContext', () => {
    it('calls the correct endpoint with correct parameters', async () => {
      const mockData = { context: 'important' };
      vi.mocked(axios.post).mockResolvedValue({ data: mockData });

      const content = 'Hello world';
      const result = await analyzeContext(content);

      expect(axios.post).toHaveBeenCalledWith(
        expect.stringContaining('/analysis/context'),
        { content }
      );
      expect(result).toEqual(mockData);
    });
  });

  describe('getFinalEvaluation', () => {
    it('calls the correct endpoint with correct parameters', async () => {
      const mockData = { final: 'good' };
      vi.mocked(axios.post).mockResolvedValue({ data: mockData });

      const userPerception = { user: 'score' };
      const aiAnalysis = { ai: 'score' };
      const result = await getFinalEvaluation(userPerception, aiAnalysis);

      expect(axios.post).toHaveBeenCalledWith(
        expect.stringContaining('/analysis/final'),
        {
          user_perception: userPerception,
          ai_analysis: aiAnalysis,
        }
      );
      expect(result).toEqual(mockData);
    });
  });
});
