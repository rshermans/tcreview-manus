import pytest
from unittest.mock import patch, MagicMock
from flask import json

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

def test_preliminary_analysis_missing_content(client):
    """Test preliminary analysis with missing 'content' field."""
    response = client.post('/api/analysis/preliminary', json={'type': 'text'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Faltando conteúdo ou tipo no Omni-Input'

def test_preliminary_analysis_missing_type(client):
    """Test preliminary analysis with missing 'type' field."""
    response = client.post('/api/analysis/preliminary', json={'content': 'some content'})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Faltando conteúdo ou tipo no Omni-Input'

def test_preliminary_analysis_empty_json(client):
    """Test preliminary analysis with empty JSON body."""
    response = client.post('/api/analysis/preliminary', json={})
    assert response.status_code == 400
    data = json.loads(response.data)
    assert 'error' in data
    assert data['error'] == 'Faltando conteúdo ou tipo no Omni-Input'

@patch('routes.analysis_routes.process_omni_input')
def test_preliminary_analysis_success(mock_process, client):
    """Test preliminary analysis with valid input."""
    # Mock the return value of process_omni_input
    mock_response = {
        "trust_score": "90%",
        "summary": "This is a test analysis",
        "teach_insights": [],
        "perception_insights": {},
        "original_type": "text",
        "provider": "openai"
    }
    mock_process.return_value = mock_response

    payload = {
        'content': 'This is some content to analyze',
        'type': 'text'
    }
    response = client.post('/api/analysis/preliminary', json=payload)

    assert response.status_code == 200
    data = json.loads(response.data)
    assert data == mock_response

    # Verify mock was called correctly
    mock_process.assert_called_once_with('This is some content to analyze', 'text')

def test_preliminary_analysis_internal_error(client):
    """Test preliminary analysis when LLM service fails."""
    with patch('routes.analysis_routes.process_omni_input') as mock_process:
        mock_process.side_effect = Exception("Internal Error")

        payload = {
            'content': 'This is some content to analyze',
            'type': 'text'
        }
        response = client.post('/api/analysis/preliminary', json=payload)

        assert response.status_code == 500
        data = json.loads(response.data)
        assert 'error' in data
        assert data['error'] == 'Ocorreu um erro interno no servidor'
