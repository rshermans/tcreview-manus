import requests
import os
import logging
import json
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM para verificar sua veracidade e qualidade.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL
    model = Config.LLM_MODEL

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": (
                    "Você é um analista de fatos experiente. Analise o conteúdo fornecido e "
                    "retorne EXCLUSIVAMENTE um objeto JSON com os seguintes campos: "
                    "analysis (string com resumo da análise), "
                    "sourceReliability (número 0-100), "
                    "factualConsistency (número 0-100), "
                    "contentQuality (número 0-100), "
                    "technicalIntegrity (número 0-100)."
                )
            },
            {
                "role": "user",
                "content": f"Tipo de conteúdo: {content_type}\nConteúdo: {content}"
            }
        ],
        "temperature": 0.2
    }

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key or api_key == "sua_chave_api_llm_aqui":
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return {
                "analysis": "Análise simulada: O conteúdo parece informativo, mas a verificação real requer uma chave de API configurada.",
                "sourceReliability": 70,
                "factualConsistency": 80,
                "contentQuality": 85,
                "technicalIntegrity": 90
            }

        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response = result["choices"][0]["message"]["content"]

        try:
            parsed_result = json.loads(llm_response)
            return {
                "analysis": parsed_result.get("analysis", "Sem resumo disponível"),
                "sourceReliability": parsed_result.get("sourceReliability", 0),
                "factualConsistency": parsed_result.get("factualConsistency", 0),
                "contentQuality": parsed_result.get("contentQuality", 0),
                "technicalIntegrity": parsed_result.get("technicalIntegrity", 0)
            }
        except (json.JSONDecodeError, ValueError):
            logger.error("Falha ao parsear resposta da LLM como JSON")
            return {
                "analysis": llm_response,
                "sourceReliability": 50,
                "factualConsistency": 50,
                "contentQuality": 50,
                "technicalIntegrity": 50
            }

    except Exception as e:
        logger.exception("Erro ao chamar a API da LLM")
        return {
            "analysis": f"Erro técnico ao processar a análise: {str(e)}",
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
    user_score = sum(user_perception.values()) / len(user_perception.values())
    ai_score = sum(ai_analysis.values()) / len(ai_analysis.values())

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
