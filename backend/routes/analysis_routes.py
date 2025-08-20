from flask import Blueprint, jsonify, request
from services.llm_service import analyze_content, cross_verify_content, analyze_context, final_evaluation

analysis_bp = Blueprint('analysis', __name__)

@analysis_bp.route('/preliminary', methods=['POST'])
def preliminary_analysis():
    """Endpoint para análise preliminar do conteúdo"""
    data = request.json
    if not data or 'content' not in data or 'type' not in data:
        return jsonify({"error": "Faltando conteúdo ou tipo"}), 400
    
    content_type = data['type']
    content = data['content']
    
    try:
        analysis_result = analyze_content(content_type, content)
        return jsonify(analysis_result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@analysis_bp.route('/cross-verification', methods=['POST'])
def cross_verification():
    """Endpoint para verificação cruzada com outras fontes"""
    data = request.json
    if not data or 'content' not in data or 'analysis' not in data:
        return jsonify({"error": "Dados incompletos para verificação cruzada"}), 400
    
    try:
        result = cross_verify_content(data['content'], data['analysis'])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@analysis_bp.route('/context', methods=['POST'])
def context_analysis():
    """Endpoint para análise de contexto histórico e atual"""
    data = request.json
    if not data or 'content' not in data:
        return jsonify({"error": "Conteúdo não fornecido"}), 400
    
    try:
        result = analyze_context(data['content'])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@analysis_bp.route('/final', methods=['POST'])
def final_evaluation_route():
    """Endpoint para avaliação final combinando análises anteriores"""
    data = request.json
    if not data or 'user_perception' not in data or 'ai_analysis' not in data:
        return jsonify({"error": "Dados incompletos para avaliação final"}), 400
    
    try:
        result = final_evaluation(data['user_perception'], data['ai_analysis'])
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
