import requests
import os
import logging
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    ...
    """
    # Construir prompt omitido para brevidade
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {...}

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key or api_key == "sua_chave_api_llm_aqui":
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return { ... }

        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response = result["choices"][0]["message"]["content"]
        # TODO: extrair pontuações reais
        return { ... }

    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return { ... }

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

    def calculate_average(data: dict) -> float:
        if not data:
            return 0.0

        valid_values = [v for v in data.values() if isinstance(v, (int, float))]
        if not valid_values:
            return 0.0

        return sum(valid_values) / len(valid_values)

    user_score = calculate_average(user_perception)
    ai_score = calculate_average(ai_analysis)

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
