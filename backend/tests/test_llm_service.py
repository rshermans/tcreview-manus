import os
import unittest
from unittest.mock import patch, MagicMock

# Set SECRET_KEY before importing anything that might use Config
os.environ['SECRET_KEY'] = 'test-secret-key'

# Adjust sys.path to find the backend modules if necessary
import sys
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.dirname(current_dir)
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from services.llm_service import analyze_content

class TestLLMService(unittest.TestCase):

    @patch('services.llm_service.Config')
    def test_analyze_content_missing_api_key(self, mock_config):
        # Case 1: api_key is None
        mock_config.LLM_API_KEY = None
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        result = analyze_content("text", "Conteúdo de teste")

        self.assertIn("resumo simulado", result["analysis"])
        self.assertEqual(result["sourceReliability"], 50)

    @patch('services.llm_service.Config')
    def test_analyze_content_placeholder_api_key(self, mock_config):
        # Case 2: api_key is the placeholder string
        mock_config.LLM_API_KEY = "sua_chave_api_llm_aqui"
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        result = analyze_content("text", "Conteúdo de teste")

        self.assertIn("resumo simulado", result["analysis"])
        self.assertEqual(result["factualConsistency"], 50)

    @patch('services.llm_service.requests.post')
    @patch('services.llm_service.Config')
    def test_analyze_content_success(self, mock_config, mock_post):
        # Case 3: Valid API key and successful response
        mock_config.LLM_API_KEY = "valid_key"
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Análise real da LLM"
                    }
                }
            ]
        }
        mock_post.return_value = mock_response

        result = analyze_content("text", "Conteúdo real")

        self.assertEqual(result["analysis"], "Análise real da LLM")
        self.assertEqual(result["sourceReliability"], 85)
        mock_post.assert_called_once()

    @patch('services.llm_service.requests.post')
    @patch('services.llm_service.Config')
    def test_analyze_content_error(self, mock_config, mock_post):
        # Case 4: API call raises an exception
        mock_config.LLM_API_KEY = "valid_key"
        mock_config.LLM_API_URL = "https://api.openai.com/v1/chat/completions"

        mock_post.side_effect = Exception("Conexão falhou")

        result = analyze_content("text", "Conteúdo real")

        self.assertIn("Erro ao processar a análise", result["analysis"])
        self.assertEqual(result["sourceReliability"], 0)

if __name__ == '__main__':
    unittest.main()
