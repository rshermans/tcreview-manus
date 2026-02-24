export interface AnalysisResult {
  analysis: string;
  sourceReliability: number;
  factualConsistency: number;
  contentQuality: number;
  technicalIntegrity: number;
}

export interface CrossVerificationResult {
  cross_verification_summary: string;
  verified_sources: string[];
  confidence_score: number;
}

export interface ContextAnalysisResult {
  context_summary: string;
  historical_context: string;
  current_relevance: string;
}

export interface FinalEvaluationResult {
  final_score: number;
  summary: string;
  user_vs_ai_discrepancy: number;
}

export interface ScoreData {
  [key: string]: number;
}
