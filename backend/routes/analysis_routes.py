import logging
from flask import Blueprint, jsonify, request
from services.llm_service import analyze_content, cross_verify_content, analyze_context, final_evaluation
from services.orchestrator_service import process_omni_input
from limiter import limiter

analysis_bp = Blueprint('analysis', __name__)
logger = logging.getLogger(__name__)

ALLOWED_CONTENT_TYPES = {'text', 'image', 'link'}
MAX_CONTENT_LENGTH = 10000

@analysis_bp.route('/preliminary', methods=['POST'])
@limiter.limit("10 per minute")
def preliminary_analysis():
    """Endpoint para análise preliminar do conteúdo"""
    data = request.json
    if not data or 'content' not in data or 'type' not in data:
        return jsonify({"error": "Faltando conteúdo ou tipo no Omni-Input"}), 400
    
    content_type = data['type']
    content = data['content']

    if content_type not in ALLOWED_CONTENT_TYPES:
        return jsonify({"error": "Tipo de conteúdo inválido"}), 400

    if not isinstance(content, str):
        return jsonify({"error": "Conteúdo deve ser texto"}), 400

    if len(content) > MAX_CONTENT_LENGTH:
        return jsonify({"error": "Conteúdo excede o tamanho máximo permitido"}), 400
    
    try:
        # Repassa para o orquestrador que lida com parsing/roteamento para agentes
        analysis_result = process_omni_input(content, content_type)
        return jsonify(analysis_result)
    except Exception as e:
        logger.exception("Erro na análise preliminar")
        return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500

@analysis_bp.route('/cross-verification', methods=['POST'])
@limiter.limit("10 per minute")
def cross_verification():
    """Endpoint para verificação cruzada com outras fontes"""
    data = request.json
    if not data or 'content' not in data or 'analysis' not in data:
        return jsonify({"error": "Dados incompletos para verificação cruzada"}), 400
    
    try:
        result = cross_verify_content(data['content'], data['analysis'])
        return jsonify(result)
    except Exception as e:
        logger.exception("Erro na verificação cruzada")
        return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500

@analysis_bp.route('/context', methods=['POST'])
@limiter.limit("10 per minute")
def context_analysis():
    """Endpoint para análise de contexto histórico e atual"""
    data = request.json
    if not data or 'content' not in data:
        return jsonify({"error": "Conteúdo não fornecido"}), 400
    
    try:
        result = analyze_context(data['content'])
        return jsonify(result)
    except Exception as e:
        logger.exception("Erro na análise de contexto")
        return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500

@analysis_bp.route('/final', methods=['POST'])
@limiter.limit("20 per minute")
def final_evaluation_route():
    """Endpoint para avaliação final combinando análises anteriores"""
    data = request.json
    if not data or 'user_perception' not in data or 'ai_analysis' not in data:
        return jsonify({"error": "Dados incompletos para avaliação final"}), 400
    
    try:
        result = final_evaluation(data['user_perception'], data['ai_analysis'])
        return jsonify(result)
    except Exception as e:
        logger.exception("Erro na avaliação final")
        return jsonify({"error": "Ocorreu um erro interno no servidor"}), 500
