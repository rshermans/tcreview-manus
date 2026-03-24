import requests
import logging
from config import Config

logger = logging.getLogger(__name__)

def analyze_content(content_type: str, content: str) -> dict:
    """
    Analisa o conteúdo usando a LLM.
    Retorna um dicionário com a análise e pontuações.
    """
    api_key = Config.LLM_API_KEY
    api_url = Config.LLM_API_URL

    # Construir prompt
    prompt = f"""
    Analise o seguinte conteúdo ({content_type}):
    {content}

    Forneça uma análise detalhada e pontuações de 0 a 100 para os seguintes critérios:
    - Confiabilidade da Fonte (sourceReliability)
    - Consistência Factual (factualConsistency)
    - Qualidade do Conteúdo (contentQuality)
    - Integridade Técnica (technicalIntegrity)

    A resposta deve ser estritamente em formato JSON com a seguinte estrutura:
    {{
        "analysis": "texto da análise",
        "sourceReliability": 85,
        "factualConsistency": 90,
        "contentQuality": 80,
        "technicalIntegrity": 95
    }}
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
        if not Config.LLM_API_KEY or Config.LLM_API_KEY == "sua_chave_api_llm_aqui":
            logger.warning(
                "Chave API da LLM não configurada. Usando dados simulados para desenvolvimento.")
            return {
                "analysis": "Esta é uma análise simulada porque a chave API da LLM não foi configurada. O conteúdo parece ser informativo, mas requer verificação adicional.",
                "sourceReliability": 70,
                "factualConsistency": 80,
                "contentQuality": 75,
                "technicalIntegrity": 90
            }

        # Chamada real
        response = requests.post(Config.LLM_API_URL, headers=headers, json=payload, timeout=30)
        response.raise_for_status()
        result = response.json()
        llm_response = result["choices"][0]["message"]["content"]

        try:
            # Tentar extrair JSON da resposta da LLM
            # Às vezes a LLM pode incluir texto antes ou depois do JSON,
            # mas pedimos estritamente JSON no prompt.
            data = json.loads(llm_response)
            return {
                "analysis": data.get("analysis", "Sem análise disponível"),
                "sourceReliability": data.get("sourceReliability", 50),
                "factualConsistency": data.get("factualConsistency", 50),
                "contentQuality": data.get("contentQuality", 50),
                "technicalIntegrity": data.get("technicalIntegrity", 50)
            }
        except json.JSONDecodeError:
            logger.error(f"Falha ao decodificar JSON da resposta da LLM: {llm_response}")
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
            "analysis": f"Erro ao processar a análise: {str(e)}",
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

    if not user_perception:
        user_score = 0
    else:
        user_score = sum(user_perception.values()) / len(user_perception.values())

    if not ai_analysis:
        ai_score = 0
    else:
        ai_score = sum(ai_analysis.values()) / len(ai_analysis.values())

    final_score = (user_score * 0.3) + (ai_score * 0.7) # Ponderado para a IA

    return {
        "final_score": round(final_score),
        "summary": "A análise combinada sugere que o conteúdo é parcialmente factual.",
        "user_vs_ai_discrepancy": abs(user_score - ai_score)
    }
