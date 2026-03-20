import pytest
from unittest.mock import patch

def test_cross_verification_missing_data(client):
    """Test cross_verification with empty JSON data."""
    # Sending empty JSON object {} results in data={} which is falsy
    response = client.post('/api/analysis/cross-verification', json={})
    assert response.status_code == 400
    assert response.json == {"error": "Dados incompletos para verificação cruzada"}

def test_cross_verification_missing_content(client):
    """Test cross_verification with missing 'content'."""
    data = {"analysis": {"some": "analysis"}}
    response = client.post('/api/analysis/cross-verification', json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Dados incompletos para verificação cruzada"}

def test_cross_verification_missing_analysis(client):
    """Test cross_verification with missing 'analysis'."""
    data = {"content": "some content"}
    response = client.post('/api/analysis/cross-verification', json=data)
    assert response.status_code == 400
    assert response.json == {"error": "Dados incompletos para verificação cruzada"}

@patch('routes.analysis_routes.cross_verify_content')
def test_cross_verification_success(mock_cross_verify, client):
    """Test cross_verification with valid data."""
    mock_result = {
        "cross_verification_summary": "Summary",
        "verified_sources": ["Source A"],
        "confidence_score": 80
    }
    mock_cross_verify.return_value = mock_result

    data = {
        "content": "Valid content",
        "analysis": {"score": 10}
    }
    response = client.post('/api/analysis/cross-verification', json=data)

    assert response.status_code == 200
    assert response.json == mock_result
    mock_cross_verify.assert_called_once_with("Valid content", {"score": 10})
