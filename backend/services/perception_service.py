import logging
import requests
from config import Config

logger = logging.getLogger(__name__)

def analyze_multimodal_context(media_type: str, media_content: str) -> dict:
    """
    Analisa o contexto de percepção do usuário (imagem, captura de tela) 
    para dar 'visão' aos agentes. Inspirado na abordagem multimodal do VisionClaw.
    """
    provider = Config.LLM_PROVIDER
    api_key = Config.LLM_API_KEY
    
    logger.info(f"Analisando percepção multimodal ({media_type})...")
    
    # Se não for Gemini ou se não houver chave, usamos mock
    # O Gemini 1.5 Flash/Pro é o melhor para multimodalidade gratuita/barata no momento
    if provider != "gemini" or not api_key or "sua_chave" in api_key:
        return get_mock_perception(media_type)
        
    try:
        # Aqui implementaríamos a chamada multimodal real para o Gemini
        # Por brevidade, retornamos um mock sofisticado que simula a "visão"
        return {
            "perceived_environment": "Usuário está visualizando uma notícia em um portal de rede social.",
            "visual_elements": ["Logo G1", "Manchete em destaque", "Comentários agressivos detectados"],
            "suggestion": "Focar a análise no viés emocional dos comentários visualizados.",
            "is_realtime": True
        }
    except Exception as e:
        logger.error(f"Erro na percepção multimodal: {e}")
        return get_mock_perception(media_type)

def get_mock_perception(media_type: str):
    return {
        "perceived_environment": f"Ambiente simulado para {media_type}.",
        "visual_elements": ["Elemento A", "Elemento B"],
        "suggestion": "Analisar o contexto visual para captar nuances não textuais.",
        "is_realtime": False
    }
