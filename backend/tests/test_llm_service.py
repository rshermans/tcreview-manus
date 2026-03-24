import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Set SECRET_KEY before importing anything that uses Config
os.environ['SECRET_KEY'] = 'test-secret-key'

# Ensure backend is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.llm_service import analyze_content

class TestLLMService(unittest.TestCase):

    @patch('services.llm_service.Config')
    def test_analyze_content_no_api_key(self, mock_config):
        # Mock Config values
        mock_config.LLM_API_KEY = None
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        result = analyze_content("text", "Conteúdo de teste")

        self.assertIn("análise simulada", result["analysis"])
        self.assertEqual(result["sourceReliability"], 70)
        self.assertEqual(result["factualConsistency"], 70)

    @patch('services.llm_service.requests.post')
    @patch('services.llm_service.Config')
    def test_analyze_content_with_api_key(self, mock_config, mock_post):
        # Mock Config values
        mock_config.LLM_API_KEY = "fake_key"
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Análise real da LLM"
                    }
                }
            ]
        }
        mock_response.raise_for_status.return_value = None
        mock_post.return_value = mock_response

        result = analyze_content("text", "Conteúdo de teste")

        self.assertEqual(result["analysis"], "Análise real da LLM")
        self.assertEqual(result["sourceReliability"], 85)
        self.assertEqual(result["factualConsistency"], 85)
        mock_post.assert_called_once()

    @patch('services.llm_service.requests.post')
    @patch('services.llm_service.Config')
    def test_analyze_content_api_error(self, mock_config, mock_post):
        # Mock Config values
        mock_config.LLM_API_KEY = "fake_key"
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"
        mock_post.side_effect = Exception("API Error")

        result = analyze_content("text", "Conteúdo de teste")

        self.assertIn("Erro na análise", result["analysis"])
        self.assertEqual(result["sourceReliability"], 0)
        self.assertEqual(result["factualConsistency"], 0)

if __name__ == '__main__':
    unittest.main()
