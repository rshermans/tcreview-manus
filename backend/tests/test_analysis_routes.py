import pytest
from unittest.mock import patch, MagicMock

def test_context_analysis_success(client):
    """Test context analysis endpoint with valid data."""
    mock_response = {
        "context_summary": "Test summary",
        "historical_context": "Test history",
        "current_relevance": "Test relevance"
    }

    with patch('routes.analysis_routes.analyze_context') as mock_analyze:
        mock_analyze.return_value = mock_response

        response = client.post('/api/analysis/context', json={
            'content': 'Test content for analysis'
        })

        assert response.status_code == 200
        assert response.json == mock_response
        mock_analyze.assert_called_once_with('Test content for analysis')

def test_context_analysis_missing_content(client):
    """Test context analysis endpoint with missing content."""
    response = client.post('/api/analysis/context', json={
        'other_field': 'value'
    })

    assert response.status_code == 400
    assert response.json == {"error": "Conteúdo não fornecido"}

def test_context_analysis_service_error(client):
    """Test context analysis endpoint when service raises an exception."""
    with patch('routes.analysis_routes.analyze_context') as mock_analyze:
        mock_analyze.side_effect = Exception("Service failure")

        response = client.post('/api/analysis/context', json={
            'content': 'Test content'
        })

        assert response.status_code == 500
        assert response.json == {"error": "Service failure"}
