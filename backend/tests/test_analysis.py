import pytest
from app import create_app

@pytest.fixture
def app():
    app_instance = create_app()
    app_instance.config.update({
        "TESTING": True,
    })
    return app_instance

@pytest.fixture
def client(app):
    return app.test_client()

def test_health_check(client):
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.json["status"] == "ok"

def test_preliminary_analysis(client):
    response = client.post(
        "/api/analysis/preliminary",
        json={"type": "text", "content": "teste de unidade"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "analysis" in data
    assert "sourceReliability" in data

def test_cross_verification(client):
    response = client.post(
        "/api/analysis/cross-verification",
        json={"content": "teste", "analysis": {"some": "data"}}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "cross_verification_summary" in data

def test_context_analysis(client):
    response = client.post(
        "/api/analysis/context",
        json={"content": "teste"}
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "context_summary" in data

def test_final_evaluation(client):
    response = client.post(
        "/api/analysis/final",
        json={
            "user_perception": {"trust": 80},
            "ai_analysis": {"sourceReliability": 70}
        }
    )
    assert response.status_code == 200
    data = response.get_json()
    assert "final_score" in data
