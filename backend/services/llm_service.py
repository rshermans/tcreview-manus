import requests
import os
import json
import re
import logging
from functools import lru_cache
from config import Config
import random

logger = logging.getLogger(__name__)

# Dados de fallback em caso de falha ou falta de chave
mock_data = {
    "analysis": "Esta é uma análise simulada porque a API da LLM não foi chamada ou a configuração está ausente.",
    "sourceReliability": 75,
    "factualConsistency": 80,
    "contentQuality": 70,
    "technicalIntegrity": 85
}

@lru_cache(maxsize=128)
def _analyze_content_impl(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    Retorna um dicionário com a análise e pontuações de 0 a 100.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL
    model = Config.LLM_MODEL

    # Prompt detalhado para garantir retorno em JSON
    prompt = f"""
    Analise a veracidade e qualidade do seguinte conteúdo do tipo '{content_type}':

    "{content}"

    Responda estritamente em formato JSON com a seguinte estrutura:
    {{
      "analysis": "um resumo detalhado da análise em português",
      "sourceReliability": 0-100,
      "factualConsistency": 0-100,
      "contentQuality": 0-100,
      "technicalIntegrity": 0-100
    }}
    """

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
        "model": model,
        "messages": [
            {"role": "system", "content": "Você é um especialista em verificação de fatos e análise de conteúdo."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    # Se não tivermos uma chave API válida ou for um placeholder, retornamos dados simulados
    placeholders = ['sua_chave_api_llm', 'sua_chave_api_llm_aqui', 'YOUR_API_KEY_HERE']
    if not api_key or any(p in api_key for p in placeholders):
        logger.warning(
            "Chave API da LLM não configurada ou é um placeholder. Usando dados simulados para desenvolvimento.")
        return mock_data

    try:
        # Chamada real
        response = requests.post(api_url, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response = result["choices"][0]["message"]["content"]

        # Tentar extrair JSON da resposta (lidando com possíveis blocos de código markdown)
        json_match = re.search(r'\{.*\}', llm_response, re.DOTALL)
        if json_match:
            try:
                parsed_result = json.loads(json_match.group(0))
                # Garantir que todos os campos necessários existam
                required_fields = ["analysis", "sourceReliability", "factualConsistency", "contentQuality", "technicalIntegrity"]
                for field in required_fields:
                    if field not in parsed_result:
                        if field == "analysis":
                            parsed_result[field] = "Análise não disponível"
                        else:
                            parsed_result[field] = 0
                return parsed_result
            except json.JSONDecodeError:
                logger.error("Falha ao decodificar JSON da resposta da LLM")

        logger.warning("Resposta da LLM não contém um JSON válido. Tentando usar resposta bruta.")
        return {
            "analysis": llm_response[:1000],
            "sourceReliability": 0,
            "factualConsistency": 0,
            "contentQuality": 0,
            "technicalIntegrity": 0
        }
    except Exception as e:
        logger.error(f"Erro ao processar chamada à LLM: {str(e)}")
        raise

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
        return mock_data

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

    # Filtra apenas valores numéricos para o cálculo
    user_scores = [v for v in user_perception.values() if isinstance(v, (int, float)) and not isinstance(v, bool)]
    ai_scores = [v for v in ai_analysis.values() if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if not user_scores or not ai_scores:
        return {
            "final_score": 0,
            "summary": "Dados insuficientes para cálculo.",
            "user_vs_ai_discrepancy": 0
        }

    user_score = sum(user_scores) / len(user_scores)
    ai_score = sum(ai_scores) / len(ai_scores)

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual, com uma inclinação para a análise da IA.",
        "user_vs_ai_discrepancy": round(abs(user_score - ai_score), 2)
    }
