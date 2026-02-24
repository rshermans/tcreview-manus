import unittest
from unittest.mock import patch, MagicMock
import json
import sys
import os

# Add backend to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

# Mock Config
import config
config.Config = MagicMock()
config.Config.LLM_API_KEY = "valid_key"
config.Config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

from services.llm_service import analyze_content

class TestLLMService(unittest.TestCase):
    def setUp(self):
        config.Config.LLM_API_KEY = "valid_key"
        config.Config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

    @patch('requests.post')
    def test_analyze_content_success(self, mock_post):
        # Mock successful API response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": json.dumps({
                            "analysis": "Test analysis",
                            "sourceReliability": 90,
                            "factualConsistency": 95,
                            "contentQuality": 80,
                            "technicalIntegrity": 85
                        })
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = analyze_content("text", "Test content")

        self.assertEqual(result["analysis"], "Test analysis")
        self.assertEqual(result["sourceReliability"], 90)
        self.assertEqual(result["factualConsistency"], 95)
        self.assertEqual(result["contentQuality"], 80)
        self.assertEqual(result["technicalIntegrity"], 85)

    @patch('requests.post')
    def test_analyze_content_malformed_json(self, mock_post):
        # Mock API response with malformed JSON content
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "This is not JSON"
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = analyze_content("text", "Test content")

        self.assertEqual(result["analysis"], "This is not JSON")
        self.assertEqual(result["sourceReliability"], 50)
        self.assertEqual(result["factualConsistency"], 50)
        self.assertEqual(result["contentQuality"], 50)
        self.assertEqual(result["technicalIntegrity"], 50)

    @patch('requests.post')
    def test_analyze_content_api_error(self, mock_post):
        # Mock API error
        mock_post.side_effect = Exception("API Error")

        result = analyze_content("text", "Test content")

        self.assertIn("Erro técnico", result["analysis"])
        self.assertEqual(result["sourceReliability"], 0)

    def test_analyze_content_no_api_key(self):
        # Mock Config with default/missing key
        config.Config.LLM_API_KEY = "sua_chave_api_llm_aqui"

        result = analyze_content("text", "Test content")

        self.assertIn("Análise simulada", result["analysis"])
        self.assertEqual(result["sourceReliability"], 70)

if __name__ == '__main__':
    unittest.main()
