import json
from unittest.mock import patch

def test_preliminary_analysis_success(client):
    """Testa o endpoint de análise preliminar com sucesso"""
    mock_result = {
        "analysis": "Análise mockada com sucesso.",
        "sourceReliability": 85,
        "factualConsistency": 90,
        "contentQuality": 80,
        "technicalIntegrity": 95
    }

    with patch('routes.analysis_routes.analyze_content') as mock_analyze:
        mock_analyze.return_value = mock_result

        response = client.post('/api/analysis/preliminary',
                               data=json.dumps({
                                   'type': 'text',
                                   'content': 'Conteúdo de teste para análise'
                               }),
                               content_type='application/json')

        assert response.status_code == 200
        assert response.get_json() == mock_result
        mock_analyze.assert_called_once_with('text', 'Conteúdo de teste para análise')

def test_preliminary_analysis_missing_data(client):
    """Testa o endpoint de análise preliminar com dados faltando"""
    # Faltando 'type'
    response = client.post('/api/analysis/preliminary',
                           data=json.dumps({
                               'content': 'Conteúdo sem tipo'
                           }),
                           content_type='application/json')
    assert response.status_code == 400
    assert "error" in response.get_json()

    # Faltando 'content'
    response = client.post('/api/analysis/preliminary',
                           data=json.dumps({
                               'type': 'text'
                           }),
                           content_type='application/json')
    assert response.status_code == 400
    assert "error" in response.get_json()

    # Payload vazio
    response = client.post('/api/analysis/preliminary',
                           data=json.dumps({}),
                           content_type='application/json')
    assert response.status_code == 400

def test_preliminary_analysis_error(client):
    """Testa o endpoint de análise preliminar quando ocorre um erro no serviço"""
    with patch('routes.analysis_routes.analyze_content') as mock_analyze:
        mock_analyze.side_effect = Exception("Erro interno simulado")

        response = client.post('/api/analysis/preliminary',
                               data=json.dumps({
                                   'type': 'text',
                                   'content': 'Conteúdo que causará erro'
                               }),
                               content_type='application/json')

        assert response.status_code == 500
        assert response.get_json() == {"error": "Erro interno simulado"}
