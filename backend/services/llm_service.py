import httpx
import os
import logging
import asyncio
from config import Config

logger = logging.getLogger(__name__)

async def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM de forma assíncrona.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Você é um especialista em verificação de fatos."},
            {"role": "user", "content": f"Analise o seguinte {content_type}: {content}"}
        ],
        "temperature": 0
    }

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key or api_key in ["sua_chave_api_llm", "sua_chave_api_llm_aqui"]:
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return {
                "analysis": "Esta é uma análise simulada. O conteúdo parece ser informativo, mas requer verificação adicional de fontes primárias.",
                "sourceReliability": 75,
                "factualConsistency": 80,
                "contentQuality": 85,
                "technicalIntegrity": 90
            }

        # Chamada real assíncrona
        async with httpx.AsyncClient() as client:
            response = await client.post(api_url, headers=headers, json=payload, timeout=30.0)
            response.raise_for_status()
            result = response.json()
            llm_response = result["choices"][0]["message"]["content"]

        return {
            "analysis": llm_response,
            "sourceReliability": 85,
            "factualConsistency": 85,
            "contentQuality": 85,
            "technicalIntegrity": 85
        }

    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return {
            "analysis": f"Erro ao processar a análise: {str(e)}",
            "sourceReliability": 0,
            "factualConsistency": 0,
            "contentQuality": 0,
            "technicalIntegrity": 0
        }

async def cross_verify_content(content: str, analysis: dict) -> dict:
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

async def analyze_context(content: str) -> dict:
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

async def final_evaluation(user_perception: dict, ai_analysis: dict) -> dict:
    """
    Placeholder for final evaluation logic.
    Combines AI and user analysis into a final score.
    Returns mock data.
    """
    logger.info("Calculando avaliação final (mock)...")

    # Filtra apenas valores numéricos para calcular a média (evitando booleanos)
    user_vals = [v for v in user_perception.values() if type(v) in [int, float]]
    ai_vals = [v for v in ai_analysis.values() if type(v) in [int, float]]

    user_score = sum(user_vals) / len(user_vals) if user_vals else 0
    ai_score = sum(ai_vals) / len(ai_vals) if ai_vals else 0

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
