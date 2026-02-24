import pytest
import os
from unittest.mock import patch, MagicMock

# Set environment variables before importing app
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['LLM_API_KEY'] = 'test_llm_key'

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch('routes.analysis_routes.analyze_context')
def test_context_analysis_missing_payload(mock_analyze_context, client):
    """Test context analysis with missing JSON payload."""
    response = client.post('/api/analysis/context', json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Conteúdo não fornecido"}
    mock_analyze_context.assert_not_called()

@patch('routes.analysis_routes.analyze_context')
def test_context_analysis_missing_content(mock_analyze_context, client):
    """Test context analysis with JSON missing 'content' field."""
    response = client.post('/api/analysis/context', json={'other': 'value'})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Conteúdo não fornecido"}
    mock_analyze_context.assert_not_called()

@patch('routes.analysis_routes.analyze_context')
def test_context_analysis_valid_request(mock_analyze_context, client):
    """Test context analysis with valid request."""
    # Setup mock return value
    mock_response = {
        "context_summary": "Test Summary",
        "historical_context": "Test History",
        "current_relevance": "Test Relevance"
    }
    mock_analyze_context.return_value = mock_response

    response = client.post('/api/analysis/context', json={'content': 'Test content'})

    assert response.status_code == 200
    assert response.get_json() == mock_response
    mock_analyze_context.assert_called_once_with('Test content')
