import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { vi, describe, it, expect, beforeEach } from 'vitest';
import ContentSubmission from './ContentSubmission';
import * as api from '../services/api';

// Mock the API service
vi.mock('../services/api', () => ({
  analyzeContent: vi.fn(),
  crossVerifyContent: vi.fn(),
  analyzeContext: vi.fn(),
  getFinalEvaluation: vi.fn(),
}));

describe('ContentSubmission Component', () => {
  const mockOnAnalysisStart = vi.fn();
  const mockOnAnalysisComplete = vi.fn();

  beforeEach(() => {
    vi.clearAllMocks();
  });

  it('renders correctly with initial state', () => {
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    expect(screen.getByText('Verificação de Conteúdo')).toBeInTheDocument();
    expect(screen.getByText('Texto')).toBeInTheDocument();
    expect(screen.getByText('Link')).toBeInTheDocument();
    expect(screen.getByText('Imagem')).toBeInTheDocument();
    expect(screen.getByRole('button', { name: /Verificar agora/i })).toBeDisabled();
  });

  it('shows textarea when Texto is selected', async () => {
    const user = userEvent.setup();
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Texto'));

    expect(screen.getByLabelText(/Insira o texto para verificação:/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText(/Cole ou digite o texto aqui.../i)).toBeInTheDocument();
  });

  it('shows input when Link is selected', async () => {
    const user = userEvent.setup();
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Link'));

    expect(screen.getByLabelText(/Insira o link para verificação:/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText('https://exemplo.com/noticia')).toBeInTheDocument();
  });

  it('shows input when Imagem is selected', async () => {
    const user = userEvent.setup();
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Imagem'));

    expect(screen.getByLabelText(/Insira o URL da imagem para verificação:/i)).toBeInTheDocument();
    expect(screen.getByPlaceholderText('https://exemplo.com/imagem.jpg')).toBeInTheDocument();
  });

  it('enables submit button when content is provided', async () => {
    const user = userEvent.setup();
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Texto'));
    const textarea = screen.getByPlaceholderText(/Cole ou digite o texto aqui.../i);
    await user.type(textarea, 'Some content');

    expect(screen.getByRole('button', { name: /Verificar agora/i })).toBeEnabled();
  });

  it('shows error for invalid link', async () => {
    const user = userEvent.setup();
    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Link'));
    const input = screen.getByPlaceholderText('https://exemplo.com/noticia');
    await user.type(input, 'invalid-link');
    await user.click(screen.getByRole('button', { name: /Verificar agora/i }));

    expect(screen.getByText(/Por favor, insira um link válido começando com http:\/\/ ou https:\/\//i)).toBeInTheDocument();
    expect(mockOnAnalysisStart).not.toHaveBeenCalled();
  });

  it('calls API and completes analysis on successful submission', async () => {
    const user = userEvent.setup();
    const mockResult = { analysis: 'Fake analysis', score: 85 };
    vi.mocked(api.analyzeContent).mockResolvedValue(mockResult);

    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Texto'));
    const textarea = screen.getByPlaceholderText(/Cole ou digite o texto aqui.../i);
    await user.type(textarea, 'Valid content');
    await user.click(screen.getByRole('button', { name: /Verificar agora/i }));

    expect(mockOnAnalysisStart).toHaveBeenCalled();
    expect(api.analyzeContent).toHaveBeenCalledWith('text', 'Valid content');

    await waitFor(() => {
      expect(mockOnAnalysisComplete).toHaveBeenCalledWith(mockResult);
    });
  });

  it('shows error message when API call fails', async () => {
    const user = userEvent.setup();
    vi.mocked(api.analyzeContent).mockRejectedValue(new Error('API Error'));

    render(
      <ContentSubmission
        onAnalysisStart={mockOnAnalysisStart}
        onAnalysisComplete={mockOnAnalysisComplete}
      />
    );

    await user.click(screen.getByText('Texto'));
    const textarea = screen.getByPlaceholderText(/Cole ou digite o texto aqui.../i);
    await user.type(textarea, 'Valid content');
    await user.click(screen.getByRole('button', { name: /Verificar agora/i }));

    expect(mockOnAnalysisStart).toHaveBeenCalled();

    await waitFor(() => {
      expect(screen.getByText(/Ocorreu um erro ao analisar o conteúdo. Tente novamente./i)).toBeInTheDocument();
    });
    expect(mockOnAnalysisComplete).not.toHaveBeenCalled();
  });
});
