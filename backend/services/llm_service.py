import requests
import os
import logging
import json
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    system_prompt = (
        "You are an expert content verification assistant. "
        "Analyze the following content and return a valid JSON object (no markdown, no extra text) with the following fields: "
        "analysis (string summary), sourceReliability (integer 0-100), factualConsistency (integer 0-100), "
        "contentQuality (integer 0-100), technicalIntegrity (integer 0-100)."
    )

    user_prompt = f"Type: {content_type}\nContent: {content}"

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.3
    }

    mock_data = {
        "analysis": "Análise simulada: O conteúdo parece verídico, mas requer verificação adicional.",
        "sourceReliability": 85,
        "factualConsistency": 90,
        "contentQuality": 80,
        "technicalIntegrity": 95
    }

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key or api_key == "sua_chave_api_llm_aqui":
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return mock_data

        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response_content = result["choices"][0]["message"]["content"]

        try:
            # Tenta fazer o parse do JSON retornado pela LLM
            analysis_data = json.loads(llm_response_content)
            return analysis_data
        except json.JSONDecodeError:
            logger.error(f"Erro ao decodificar JSON da LLM: {llm_response_content}")
            return mock_data

    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return mock_data

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
    user_score = sum(user_perception.values()) / len(user_perception.values())
    ai_score = sum(ai_analysis.values()) / len(ai_analysis.values())

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
