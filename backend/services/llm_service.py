import requests
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
        "Authorization": f"Bearer {Config.LLM_API_KEY}"
    }
    payload = {...}

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not Config.LLM_API_KEY or Config.LLM_API_KEY == "sua_chave_api_llm_aqui":
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return { ... }

        # Chamada real
        response = requests.post(Config.LLM_API_URL, headers=headers, json=payload, timeout=30)
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
    user_score = sum(user_perception.values()) / len(user_perception.values())
    ai_score = sum(ai_analysis.values()) / len(ai_analysis.values())

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
