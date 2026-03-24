import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import { vi, describe, it, expect, beforeEach } from 'vitest';
import ContentSubmission from './ContentSubmission';
import * as api from '../services/api';

vi.mock('../services/api', () => ({
  analyzeContent: vi.fn(),
  default: {
    analyzeContent: vi.fn(),
  }
}));

describe('ContentSubmission', () => {
  const mockOnAnalysisStart = vi.fn();
  const mockOnAnalysisComplete = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders correctly in its initial state', () => {
    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    expect(screen.getByText('Verificação de Conteúdo')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Texto/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Link/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Imagem/i })).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Verificar agora/i })).toBeDisabled();
  });

  it('shows input field when a content type is selected', () => {
    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    fireEvent.click(screen.getByRole('button', { name: /Texto/i }));

    expect(screen.getByPlaceholderText(/Cole ou digite o texto aqui/i)).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Verificar agora/i })).toBeDisabled();
  });

  it('enables the submit button when content is entered', () => {
    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    fireEvent.click(screen.getByRole('button', { name: /Texto/i }));
    fireEvent.change(screen.getByPlaceholderText(/Cole ou digite o texto aqui/i), { target: { value: 'Some content' } });

    expect(screen.getByRole('button', { name: /Verificar agora/i })).toBeEnabled();
  });

  it('shows error when link does not start with http', async () => {
    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    fireEvent.click(screen.getByRole('button', { name: /Link/i }));
    fireEvent.change(screen.getByPlaceholderText(/https:\/\/exemplo.com\/noticia/i), { target: { value: 'invalid-link' } });

    const submitButton = screen.getByRole('button', { name: /Verificar agora/i });
    expect(submitButton).toBeEnabled();

    fireEvent.click(submitButton);

    expect(screen.getByText(/Por favor, insira um link válido/i)).toBeInTheDocument();
    expect(mockOnAnalysisStart).not.toHaveBeenCalled();
  });

  it('calls API and completes analysis on valid submission', async () => {
    const mockResult = { id: '123', status: 'completed' };
    vi.mocked(api.analyzeContent).mockResolvedValue(mockResult);

    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    fireEvent.click(screen.getByRole('button', { name: /Texto/i }));
    fireEvent.change(screen.getByPlaceholderText(/Cole ou digite o texto aqui/i), { target: { value: 'Valid text content' } });

    fireEvent.click(screen.getByRole('button', { name: /Verificar agora/i }));

    expect(mockOnAnalysisStart).toHaveBeenCalled();
    await waitFor(() => {
      expect(api.analyzeContent).toHaveBeenCalledWith('text', 'Valid text content');
      expect(mockOnAnalysisComplete).toHaveBeenCalledWith(mockResult);
    });
  });

  it('shows error message when API call fails', async () => {
    vi.mocked(api.analyzeContent).mockRejectedValue(new Error('API Error'));

    render(<ContentSubmission onAnalysisStart={mockOnAnalysisStart} onAnalysisComplete={mockOnAnalysisComplete} />);

    fireEvent.click(screen.getByRole('button', { name: /Texto/i }));
    fireEvent.change(screen.getByPlaceholderText(/Cole ou digite o texto aqui/i), { target: { value: 'Valid text content' } });

    fireEvent.click(screen.getByRole('button', { name: /Verificar agora/i }));

    await waitFor(() => {
      expect(screen.getByText(/Ocorreu um erro ao analisar o conteúdo/i)).toBeInTheDocument();
    });
    expect(mockOnAnalysisComplete).not.toHaveBeenCalled();
  });
});
