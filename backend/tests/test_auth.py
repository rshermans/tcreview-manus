import pytest
import os
from flask import Flask

# Mock Config before importing app
os.environ['SECRET_KEY'] = 'test-secret'
os.environ['API_KEY'] = 'test-api-key'

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_preliminary_analysis_no_auth(client):
    """Test that /preliminary returns 401 without X-API-Key header"""
    response = client.post('/api/analysis/preliminary', json={
        "type": "text",
        "content": "test content"
    })
    assert response.status_code == 401
    assert "Não autorizado" in response.get_json()['error']

def test_preliminary_analysis_correct_auth(client):
    """Test that /preliminary returns 200 with correct X-API-Key header"""
    response = client.post('/api/analysis/preliminary',
        headers={"X-API-Key": "test-api-key"},
        json={
            "type": "text",
            "content": "test content"
        }
    )
    assert response.status_code == 200

def test_health_check_unprotected(client):
    """Test that /health remains unprotected"""
    response = client.get('/api/health')
    assert response.status_code == 200
