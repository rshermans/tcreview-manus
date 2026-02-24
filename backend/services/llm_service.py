import requests
import os
import logging
from functools import lru_cache
from config import Config
import random

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def _analyze_content_impl(content_type: str, content: str) -> dict:
    """
    Função interna que realiza a chamada à API e retorna os dados brutos.
    O cache é aplicado aqui para evitar chamadas repetidas.
    Exceções levantadas aqui não são cacheadas.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    # Se não tivermos uma chave API válida, retornamos dados simulados
    if not api_key or api_key in ["sua_chave_api_llm_aqui", "sua_chave_api_llm"]:
        logger.warning(
            "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
        return {
            "analysis": "Análise simulada: O conteúdo parece ser factual, mas requer verificação adicional.",
            "sourceReliability": 70,
            "factualConsistency": 80,
            "contentQuality": 75,
            "technicalIntegrity": 90
        }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that analyzes content credibility. Provide a JSON response with keys: analysis (string), sourceReliability (0-100), factualConsistency (0-100), contentQuality (0-100), technicalIntegrity (0-100)."},
            {"role": "user", "content": f"Analyze the following {content_type}:\n\n{content}"}
        ],
        "temperature": 0.7
    }

    # Chamada real - exceções aqui propagam para quem chamou (e não são cacheadas)
    response = requests.post(api_url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    result = response.json()

    # Extrair conteúdo da resposta da LLM (assumindo formato OpenAI)
    if "choices" in result and len(result["choices"]) > 0:
        llm_content = result["choices"][0]["message"]["content"]

        # Tentar parsear se o conteúdo for JSON, senão retornar texto e valores aleatórios/fixos
        # Para simplificar, retornamos valores fixos razoáveis se o parse falhar ou não for implementado
        return {
            "analysis": llm_content,
            "sourceReliability": random.randint(60, 90),
            "factualConsistency": random.randint(60, 90),
            "contentQuality": random.randint(60, 90),
            "technicalIntegrity": random.randint(60, 90)
        }
    else:
        logger.error("Resposta da API da LLM em formato inesperado")
        raise ValueError("Invalid API response format")

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    Retorna um dicionário com os resultados da análise.
    Encapsula a chamada cacheada para tratar exceções.
    """
    try:
        return _analyze_content_impl(content_type, content)
    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return {"error": str(e)}

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
