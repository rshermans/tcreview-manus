import requests
import os
import logging
import json
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    Retorna um dicionário com chaves:
    - analysis: str
    - sourceReliability: int
    - factualConsistency: int
    - contentQuality: int
    - technicalIntegrity: int
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    prompt = f"""
    Analyze the following {content_type} content:
    "{content}"

    Provide a JSON response with the following keys:
    - analysis: A brief text summary of the analysis.
    - sourceReliability: An integer score (0-100).
    - factualConsistency: An integer score (0-100).
    - contentQuality: An integer score (0-100).
    - technicalIntegrity: An integer score (0-100).
    """

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that analyzes content credibility."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key or api_key.startswith("sua_chave") or "your_key" in api_key:
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return {
                "analysis": "Análise simulada: O conteúdo parece ser parcialmente confiável, mas carece de fontes verificáveis.",
                "sourceReliability": 60,
                "factualConsistency": 70,
                "contentQuality": 80,
                "technicalIntegrity": 90
            }

        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()

        content_text = result["choices"][0]["message"]["content"]

        # Tentar fazer o parse do JSON retornado pela LLM
        try:
            analysis_result = json.loads(content_text)
            if not isinstance(analysis_result, dict):
                raise ValueError("Resposta da LLM não é um JSON válido (dicionário).")

            # Garantir que todas as chaves esperadas existam
            expected_keys = ["analysis", "sourceReliability", "factualConsistency", "contentQuality", "technicalIntegrity"]
            for key in expected_keys:
                if key not in analysis_result:
                    analysis_result[key] = 0 if key != "analysis" else "Análise incompleta."
            return analysis_result
        except (json.JSONDecodeError, ValueError):
            logger.error("Falha ao decodificar JSON ou formato inválido da resposta da LLM: %s", content_text)
            return {
                "analysis": content_text, # Retorna o texto cru se não for JSON válido
                "sourceReliability": 50,
                "factualConsistency": 50,
                "contentQuality": 50,
                "technicalIntegrity": 50
            }

    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return {
            "analysis": "Erro na análise.",
            "sourceReliability": 0,
            "factualConsistency": 0,
            "contentQuality": 0,
            "technicalIntegrity": 0
        }

def cross_verify_content(content: str, analysis: dict) -> dict:
    """
    Placeholder for cross-verification logic.
    Returns mock data.
    """
    logger.info("Executando verificação cruzada (mock)...")
    return {
        "cross_verification_summary": "A verificação cruzada com fontes de notícias simuladas indica uma cobertura mista.",
        "verified_sources": ["Fonte A (Confiável)", "Fonte B (Duvidosa)"],
        "confidence_score": 65
    }

def analyze_context(content: str) -> dict:
    """
    Placeholder for context analysis logic.
    Returns mock data.
    """
    logger.info("Analisando contexto (mock)...")
    return {
        "context_summary": "O tópico tem sido amplamente debatido, com narrativas conflitantes.",
        "historical_context": "Este assunto tem raízes em eventos de 2018.",
        "current_relevance": "Atualmente, é um tópico de alta relevância política."
    }

def final_evaluation(user_perception: dict, ai_analysis: dict) -> dict:
    """
    Placeholder for final evaluation logic.
    Combines AI and user analysis into a final score.
    Returns mock data.
    """
    logger.info("Calculando avaliação final (mock)...")

    user_values = [v for v in user_perception.values() if isinstance(v, (int, float))]
    user_score = sum(user_values) / len(user_values) if user_values else 0

    ai_values = [v for v in ai_analysis.values() if isinstance(v, (int, float))]
    ai_score = sum(ai_values) / len(ai_values) if ai_values else 0

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
