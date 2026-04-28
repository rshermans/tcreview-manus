import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import GamificationBar from './GamificationBar';

describe('GamificationBar', () => {
  const defaultProps = {
    streak: 5,
    tokens: 150,
    level: 'Bronze'
  };

  it('renders all gamification items with correct values', () => {
    render(<GamificationBar {...defaultProps} />);

    expect(screen.getByText('5')).toBeInTheDocument();
    expect(screen.getByText('150')).toBeInTheDocument();
    expect(screen.getByText('Bronze')).toBeInTheDocument();
  });

  it('renders the correct labels', () => {
    render(<GamificationBar {...defaultProps} />);

    expect(screen.getByText('Ofensiva')).toBeInTheDocument();
    expect(screen.getByText('Tokens')).toBeInTheDocument();
    expect(screen.getByText('Nível')).toBeInTheDocument();
  });

  it('renders the correct icons', () => {
    render(<GamificationBar {...defaultProps} />);

    expect(screen.getByText('🔥')).toBeInTheDocument();
    expect(screen.getByText('💎')).toBeInTheDocument();
    expect(screen.getByText('🎓')).toBeInTheDocument();
  });

  it('updates when props change', () => {
    const { rerender } = render(<GamificationBar {...defaultProps} />);

    expect(screen.getByText('5')).toBeInTheDocument();

    rerender(<GamificationBar streak={10} tokens={200} level="Prata" />);

    expect(screen.getByText('10')).toBeInTheDocument();
    expect(screen.getByText('200')).toBeInTheDocument();
    expect(screen.getByText('Prata')).toBeInTheDocument();
  });
});
