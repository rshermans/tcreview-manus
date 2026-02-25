import pytest
from unittest.mock import patch

def test_final_evaluation_route_success(client):
    """Testa o sucesso da rota de avaliação final"""
    payload = {
        'user_perception': {'reliability': 4, 'factual': 5},
        'ai_analysis': {'reliability': 4.5, 'factual': 4.8}
    }

    mock_result = {
        "final_score": 75,
        "summary": "Mocked summary",
        "user_vs_ai_discrepancy": 0.5
    }

    # O patch deve apontar para onde a função é usada
    with patch('routes.analysis_routes.final_evaluation') as mock_final_eval:
        mock_final_eval.return_value = mock_result

        response = client.post('/api/analysis/final', json=payload)

        assert response.status_code == 200
        assert response.json == mock_result
        mock_final_eval.assert_called_once_with(payload['user_perception'], payload['ai_analysis'])

def test_final_evaluation_route_missing_data(client):
    """Testa erro de dados ausentes na rota"""
    # Sem payload
    response = client.post('/api/analysis/final', json={})
    assert response.status_code == 400
    assert response.json['error'] == "Dados incompletos para avaliação final"

    # Faltando user_perception
    response = client.post('/api/analysis/final', json={'ai_analysis': {}})
    assert response.status_code == 400
    assert response.json['error'] == "Dados incompletos para avaliação final"

    # Faltando ai_analysis
    response = client.post('/api/analysis/final', json={'user_perception': {}})
    assert response.status_code == 400
    assert response.json['error'] == "Dados incompletos para avaliação final"

def test_final_evaluation_route_error(client):
    """Testa erro no serviço final_evaluation através da rota"""
    payload = {
        'user_perception': {'reliability': 4},
        'ai_analysis': {'reliability': 4.5}
    }

    with patch('routes.analysis_routes.final_evaluation') as mock_final_eval:
        mock_final_eval.side_effect = Exception("Erro interno simulado")

        response = client.post('/api/analysis/final', json=payload)

        assert response.status_code == 500
        assert response.json['error'] == "Erro interno simulado"
