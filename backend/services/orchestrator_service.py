import logging
import urllib.parse
from flask import current_app

logger = logging.getLogger(__name__)

def parse_input(content: str, content_type: str) -> dict:
    """
    Simula o parsing do input baseado no tipo detectado pelo frontend.
    """
    logger.info(f"Fazendo parse do input tipo: {content_type}")
    
    parsed_text = content
    if content_type == 'url':
        parsed_text = f"[Texto extraído da URL]: {content}"
    elif content_type == 'image':
        parsed_text = f"[Descrição visual da imagem]: O conteúdo visual indica um compartilhamento de rede social com título chamativo."
        
    return {
        "raw_content": content,
        "type": content_type,
        "parsed_text": parsed_text
    }

def process_omni_input(content: str, content_type: str) -> dict:
    """
    Ponto de entrada único. Processa o conteúdo e delega para os agentes.
    Integra a percepção multimodal para enriquecer a análise.
    """
    logger.info(f"Orquestrando conteúdo ({content_type}): {content[:30]}...")
    
    # 1. Parsing
    parsed_data = parse_input(content, content_type)
    text_to_analyze = parsed_data["parsed_text"]
    
    # 2. Percepção Multimodal (Nova "Visão" do Agente)
    from services.perception_service import analyze_multimodal_context
    perception_result = analyze_multimodal_context(content_type, content)
    
    # 3. Roteamento para Fact Check Agent (Confiança)
    from services.llm_service import analyze_content
    # Passamos o texto parsed e, se houver, o contexto visual
    analysis_input = text_to_analyze
    if perception_result.get("perceived_environment"):
        analysis_input += f"\n[Contexto Visual]: {perception_result['perceived_environment']}"
        
    fact_check_result = analyze_content(content_type, analysis_input)
    
    # 4. Roteamento para Teach Agent (Pedagogia)
    from services.teach_agent import generate_pedagogical_insights
    teach_result = generate_pedagogical_insights(text_to_analyze)
    
    # 5. Agrega e retorna o formato esperado pelo CognitiveResults.tsx
    return {
        "trust_score": f"{fact_check_result.get('trust_score', 0)}%",
        "summary": fact_check_result.get("summary", ""),
        "teach_insights": teach_result,
        "perception_insights": perception_result,
        "original_type": content_type,
        "provider": fact_check_result.get("provider", "unknown")
    }
