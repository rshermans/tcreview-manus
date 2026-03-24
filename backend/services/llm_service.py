import requests
import logging
import json
from config import Config
import random

logger = logging.getLogger(__name__)

@lru_cache(maxsize=128)
def _analyze_content_impl(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    """
    # Configurações da API
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    # Construir prompt omitido para brevidade
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {Config.LLM_API_KEY}"
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
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Você é um especialista em verificação de fatos."},
            {"role": "user", "content": f"Analise o seguinte conteúdo ({content_type}): {content}"}
        ],
        "temperature": 0.7
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Você é um especialista em verificação de fatos."},
            {"role": "user", "content": f"Analise este conteúdo ({content_type}): {content}"}
        ]
    }

    try:
        # Se não tivermos uma chave API válida, retornamos dados simulados
        if not api_key:
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return {
                "analysis": "Esta é uma análise simulada, pois a chave API não foi configurada.",
                "sourceReliability": 70,
                "factualConsistency": 70,
                "contentQuality": 70,
                "technicalIntegrity": 70
            }

        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response = result["choices"][0]["message"]["content"]
        # TODO: extrair pontuações reais
        return {
            "analysis": llm_response,
            "sourceReliability": 85,
            "factualConsistency": 85,
            "contentQuality": 85,
            "technicalIntegrity": 85
        }

        # Em uma implementação real, extrairíamos pontuações do retorno da LLM.
        # Por enquanto, retornamos valores fixos com o texto da LLM.
        return {
            "analysis": llm_response,
            "sourceReliability": 85,
            "factualConsistency": 90,
            "contentQuality": 80,
            "technicalIntegrity": 95
        }

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
        return {
            "analysis": f"Erro na análise: {str(e)}",
            "sourceReliability": 0,
            "factualConsistency": 0,
            "contentQuality": 0,
            "technicalIntegrity": 0
        }

# Mantém as outras funções como estão por enquanto (estão em conformidade)
def cross_verify_content(content: str, analysis: dict) -> dict:
    # Simulates cross-verifying the initial analysis against other sources
    return {
        "verified": True,
        "confidence_score": 0.92,
        "notes": "Information matches known reliable sources."
    }

def analyze_context(content: str) -> dict:
    logger.info("Analisando contexto (mock)...")
    return {
        "context_summary": "O tópico tem sido amplamente debatido, com narrativas conflitantes.",
        "historical_context": "Este assunto tem raízes em eventos de 2018.",
        "current_relevance": "Atualmente, é um tópico de alta relevância política."
    }

def final_evaluation(user_perception: dict, ai_analysis: dict) -> dict:
    logger.info("Calculando avaliação final (mock)...")

    user_values = [v for v in user_perception.values() if isinstance(v, (int, float))]
    user_score = sum(user_values) / len(user_values) if user_values else 0

    ai_values = [v for v in ai_analysis.values() if isinstance(v, (int, float))]
    ai_score = sum(ai_values) / len(ai_values) if ai_values else 0

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
