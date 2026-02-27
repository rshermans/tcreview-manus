import requests
import os
import logging
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM, suportando múltiplos provedores (OpenAI, Gemini, DeepSeek).
    """
    provider = Config.LLM_PROVIDER
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    # Mock fallback
    if not api_key or api_key in ["sua_chave_api_llm", "sua_chave_api_llm_aqui"]:
        logger.warning(f"Chave API não configurada para o provedor {provider}. Usando dados simulados.")
        return get_mock_analysis()

    # Construir prompt
    prompt = (
        f"Analise o seguinte conteúdo do tipo '{content_type}' quanto à veracidade, "
        f"vieses e confiabilidade. Retorne um resumo e uma pontuação de confiança.\n\n"
        f"Conteúdo: {content}"
    )

    try:
        if provider == "openai" or provider == "deepseek":
            return call_openai_compatible_api(api_url, api_key, prompt, provider)
        elif provider == "gemini":
            return call_gemini_api(api_url, api_key, prompt)
        else:
            logger.error(f"Provedor desconhecido: {provider}")
            return get_mock_analysis()
            
    except Exception as e:
        logger.exception(f"Erro ao chamar a API do provedor {provider}")
        return {
            "summary": f"Erro na análise ({provider}): {str(e)}",
            "trust_score": 0,
            "bias_indicators": [],
            "fact_check_status": "error",
            "recommendations": ["Tentar novamente mais tarde"]
        }

def call_openai_compatible_api(url, key, prompt, provider):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {key}"
    }
    
    # DeepSeek cost control: uses deepseek-chat (V3) by default
    model = "gpt-4o-mini" if provider == "openai" else "deepseek-chat"
    
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Você é um assistente de fact-checking especializado em avaliar a veracidade de notícias e conteúdos."},
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
        llm_response = result['candidates'][0]['content']['parts'][0]['text']
    except (KeyError, IndexError):
        llm_response = "Erro ao processar resposta do Gemini."

    return {
        "summary": llm_response,
        "trust_score": 80,
        "bias_indicators": [],
        "fact_check_status": "analyzed",
        "recommendations": [],
        "provider": "gemini"
    }

def get_mock_analysis():
    return {
        "summary": "Análise simulada: O conteúdo apresenta elementos que requerem verificação factual. "
                   "Foram identificados possíveis vieses de confirmação e uso de linguagem sensacionalista.",
        "trust_score": 45,
        "bias_indicators": ["linguagem emocional", "fontes não citadas", "generalização excessiva"],
        "fact_check_status": "mock",
        "recommendations": ["Verificar fontes primárias", "Comparar com veículos de referência"],
        "provider": "mock"
    }

# Mantém as outras funções como estão por enquanto (estão em conformidade)
def cross_verify_content(content: str, analysis: dict) -> dict:
    logger.info("Executando verificação cruzada (mock)...")
    return {
        "cross_verification_summary": "A verificação cruzada com fontes de notícias simuladas indica uma cobertura mista.",
        "verified_sources": ["Fonte A (Confiável)", "Fonte B (Duvidosa)"],
        "confidence_score": 65
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
    user_score = sum(user_perception.values()) / len(user_perception.values())
    ai_score = sum(ai_analysis.values()) / len(ai_analysis.values())
    final_score = (user_score * 0.3) + (ai_score * 0.7)
    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
