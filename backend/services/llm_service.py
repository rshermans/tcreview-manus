import requests
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
        "Authorization": f"Bearer {Config.LLM_API_KEY}"
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "Você é um especialista em verificação de fatos e análise de conteúdo."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
    result = response.json()
    llm_response = result["choices"][0]["message"]["content"]
    
    return {
        "summary": llm_response,
        "trust_score": 75, # Placeholder, idealmente extraído via regex ou structured output
        "bias_indicators": [],
        "fact_check_status": "analyzed",
        "recommendations": [],
        "provider": provider
    }

    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that analyzes content credibility."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

def call_gemini_api(url, key, prompt):
    # Gemini API Studio format
    if "api.openai.com" in url:
        # Se estiver usando a URL da OpenAI por engano, redirecionamos para call_openai_compatible_api
        return call_openai_compatible_api(url, key, prompt, "gemini-openai-compat")

    # Endpoint padrão Google AI Studio (Gemini 1.5 Flash para custo)
    actual_url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={key}"
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }],
        "generationConfig": {
            "temperature": 0.3,
            "maxOutputTokens": 1000,
        }
    }

    response = requests.post(actual_url, json=payload, timeout=30)
    response.raise_for_status()
    result = response.json()
    
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
        response = requests.post(Config.LLM_API_URL, headers=headers, json=payload, timeout=30)
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
