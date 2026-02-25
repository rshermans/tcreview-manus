import sys
import os
import unittest
from unittest.mock import patch, MagicMock

# Adicionar o diretório backend ao sys.path para importações funcionarem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.llm_service import analyze_content, final_evaluation

class TestLLMService(unittest.TestCase):
    @patch('services.llm_service.Config')
    @patch('services.llm_service.requests.post')
    def test_analyze_content_success(self, mock_post, mock_config):
        # Configurar mocks
        mock_config.LLM_API_KEY = "test_key"
        mock_config.LLM_API_URL = "http://test-api.com"

        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": '{"analysis": "Good content", "sourceReliability": 90, "factualConsistency": 85, "contentQuality": 80, "technicalIntegrity": 95}'
                }
            }]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = analyze_content("text", "Some content")

        self.assertEqual(result["analysis"], "Good content")
        self.assertEqual(result["sourceReliability"], 90)
        self.assertEqual(result["factualConsistency"], 85)
        self.assertEqual(result["contentQuality"], 80)
        self.assertEqual(result["technicalIntegrity"], 95)

    @patch('services.llm_service.Config')
    def test_analyze_content_mock_fallback(self, mock_config):
        # Testar quando a chave API é a padrão (simulada)
        mock_config.LLM_API_KEY = "sua_chave_api_llm_aqui"

        result = analyze_content("text", "Some content")

        self.assertIn("análise simulada", result["analysis"])
        self.assertEqual(result["sourceReliability"], 70)

    @patch('services.llm_service.Config')
    @patch('services.llm_service.requests.post')
    def test_analyze_content_json_error(self, mock_post, mock_config):
        # Testar quando a LLM retorna algo que não é JSON
        mock_config.LLM_API_KEY = "test_key"

        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": "Isso não é um JSON"
                }
            }]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = analyze_content("text", "Some content")

        self.assertEqual(result["analysis"], "Isso não é um JSON")
        self.assertEqual(result["sourceReliability"], 50)

    def test_final_evaluation_with_mixed_data(self):
        user_perception = {"score": 80, "comment": "Good"}
        ai_analysis = {
            "analysis": "Some text",
            "sourceReliability": 90,
            "factualConsistency": 100
        }

        result = final_evaluation(user_perception, ai_analysis)

        # User values: [80] -> score 80
        # AI values: [90, 100] -> score 95
        # Final: 80 * 0.3 + 95 * 0.7 = 24 + 66.5 = 90.5 -> round 90 (Python 3 round to even)
        self.assertEqual(result["final_score"], 90)

if __name__ == '__main__':
    unittest.main()
