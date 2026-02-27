import React from 'react';
import './GamificationBar.css';

interface GamificationBarProps {
  streak: number;
  tokens: number;
  level: string;
}

const GamificationBar: React.FC<GamificationBarProps> = ({ streak, tokens, level }) => {
  return (
    <div className="gamification-bar">
      <div className="gamification-item">
        <span className="icon">🔥</span>
        <span className="value">{streak}</span>
        <span className="label">Ofensiva</span>
      </div>
      <div className="gamification-item">
        <span className="icon">💎</span>
        <span className="value">{tokens}</span>
        <span className="label">Tokens</span>
      </div>
      <div className="gamification-item">
        <span className="icon">🎓</span>
        <span className="value">{level}</span>
        <span className="label">Nível</span>
      </div>
    </div>
  );
};

export default GamificationBar;
