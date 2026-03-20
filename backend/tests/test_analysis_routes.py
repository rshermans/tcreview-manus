import pytest
from unittest.mock import patch

def test_context_analysis_success(client):
    """Testa o sucesso da análise de contexto"""
    mock_response = {
        "context_summary": "summary",
        "historical_context": "history",
        "current_relevance": "relevance"
    }

    with patch('routes.analysis_routes.analyze_context', return_value=mock_response):
        response = client.post('/api/analysis/context', json={'content': 'test content'})

    assert response.status_code == 200
    assert response.get_json() == mock_response

def test_context_analysis_missing_content(client):
    """Testa erro quando o conteúdo não é fornecido"""
    response = client.post('/api/analysis/context', json={'wrong_key': 'test content'})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Conteúdo não fornecido"}

def test_context_analysis_no_data(client):
    """Testa erro quando nenhum dado é enviado (corpo JSON vazio)"""
    response = client.post('/api/analysis/context', json={})

    assert response.status_code == 400
    assert response.get_json() == {"error": "Conteúdo não fornecido"}

def test_context_analysis_error(client):
    """Testa erro interno do servidor na análise de contexto"""
    with patch('routes.analysis_routes.analyze_context', side_effect=Exception("Service Failure")):
        response = client.post('/api/analysis/context', json={'content': 'test content'})

    assert response.status_code == 500
    assert response.get_json() == {"error": "Service Failure"}
