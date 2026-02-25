import json
from unittest.mock import patch

def test_cross_verification_success(client):
    """Testa o endpoint de verificação cruzada com dados válidos"""
    mock_response = {
        "cross_verification_summary": "Mocked summary",
        "verified_sources": ["Source 1", "Source 2"],
        "confidence_score": 80
    }

    with patch('routes.analysis_routes.cross_verify_content') as mock_verify:
        mock_verify.return_value = mock_response

        payload = {
            "content": "Conteúdo de teste",
            "analysis": {"some": "analysis"}
        }

        response = client.post('/api/analysis/cross-verification',
                               json=payload)

        assert response.status_code == 200
        assert response.get_json() == mock_response
        mock_verify.assert_called_once_with("Conteúdo de teste", {"some": "analysis"})

def test_cross_verification_missing_data(client):
    """Testa o endpoint de verificação cruzada com dados incompletos"""
    # Teste sem content
    payload = {"analysis": {"some": "analysis"}}
    response = client.post('/api/analysis/cross-verification',
                           json=payload)
    assert response.status_code == 400
    assert "Dados incompletos" in response.get_json()['error']

    # Teste sem analysis
    payload = {"content": "Conteúdo de teste"}
    response = client.post('/api/analysis/cross-verification',
                           json=payload)
    assert response.status_code == 400
    assert "Dados incompletos" in response.get_json()['error']

def test_cross_verification_empty_body(client):
    """Testa o endpoint de verificação cruzada com corpo vazio"""
    response = client.post('/api/analysis/cross-verification',
                           json={})
    assert response.status_code == 400
    assert "Dados incompletos" in response.get_json()['error']

def test_cross_verification_exception(client):
    """Testa o endpoint de verificação cruzada quando ocorre uma exceção"""
    with patch('routes.analysis_routes.cross_verify_content') as mock_verify:
        mock_verify.side_effect = Exception("Erro interno simulado")

        payload = {
            "content": "Conteúdo de teste",
            "analysis": {"some": "analysis"}
        }

        response = client.post('/api/analysis/cross-verification',
                               json=payload)

        assert response.status_code == 500
        assert "Erro interno simulado" in response.get_json()['error']
