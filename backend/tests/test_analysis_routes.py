import pytest
from unittest.mock import patch

def test_preliminary_analysis_success(client):
    """
    Test successful preliminary analysis.
    """
    mock_response = {
        "analysis": "This is a test analysis.",
        "score": 0.95
    }

    # Patch where it is imported in the routes module
    with patch('routes.analysis_routes.analyze_content') as mock_analyze:
        mock_analyze.return_value = mock_response

        data = {
            "content": "This is some test content.",
            "type": "text"
        }

        response = client.post('/api/analysis/preliminary', json=data)

        assert response.status_code == 200
        assert response.json == mock_response
        mock_analyze.assert_called_once_with("text", "This is some test content.")

def test_preliminary_analysis_missing_data(client):
    """
    Test preliminary analysis with missing data.
    """
    # Missing content
    data = {
        "type": "text"
    }
    response = client.post('/api/analysis/preliminary', json=data)
    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"] == "Faltando conteúdo ou tipo"

    # Missing type
    data = {
        "content": "Some content"
    }
    response = client.post('/api/analysis/preliminary', json=data)
    assert response.status_code == 400
    assert "error" in response.json
    assert response.json["error"] == "Faltando conteúdo ou tipo"

    # Missing both (empty json)
    data = {}
    response = client.post('/api/analysis/preliminary', json=data)
    assert response.status_code == 400
    assert "error" in response.json

def test_preliminary_analysis_service_error(client):
    """
    Test preliminary analysis when the service raises an exception.
    """
    # Patch where it is imported in the routes module
    with patch('routes.analysis_routes.analyze_content') as mock_analyze:
        mock_analyze.side_effect = Exception("Service unavailable")

        data = {
            "content": "This is some test content.",
            "type": "text"
        }

        response = client.post('/api/analysis/preliminary', json=data)

        assert response.status_code == 500
        assert "error" in response.json
        assert response.json["error"] == "Service unavailable"
