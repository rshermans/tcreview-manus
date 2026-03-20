import pytest
from unittest.mock import patch

class TestFinalEvaluationRoute:

    def test_final_evaluation_missing_user_perception(self, client):
        response = client.post('/api/analysis/final', json={
            'ai_analysis': {'score': 80}
        })
        assert response.status_code == 400
        assert response.json == {"error": "Dados incompletos para avaliação final"}

    def test_final_evaluation_missing_ai_analysis(self, client):
        response = client.post('/api/analysis/final', json={
            'user_perception': {'score': 70}
        })
        assert response.status_code == 400
        assert response.json == {"error": "Dados incompletos para avaliação final"}

    def test_final_evaluation_empty_json(self, client):
        response = client.post('/api/analysis/final', json={})
        assert response.status_code == 400
        assert response.json == {"error": "Dados incompletos para avaliação final"}

    def test_final_evaluation_no_json(self, client):
        # Sending null JSON payload
        response = client.post('/api/analysis/final', data='null', content_type='application/json')
        assert response.status_code == 400
        assert response.json == {"error": "Dados incompletos para avaliação final"}

    @patch('routes.analysis_routes.final_evaluation')
    def test_final_evaluation_success(self, mock_final_evaluation, client):
        mock_final_evaluation.return_value = {
            "final_score": 75,
            "summary": "Test Summary",
            "user_vs_ai_discrepancy": 5
        }

        payload = {
            'user_perception': {'score': 70},
            'ai_analysis': {'score': 80}
        }
        response = client.post('/api/analysis/final', json=payload)

        assert response.status_code == 200
        assert response.json == {
            "final_score": 75,
            "summary": "Test Summary",
            "user_vs_ai_discrepancy": 5
        }
        mock_final_evaluation.assert_called_once_with({'score': 70}, {'score': 80})
