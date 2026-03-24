import unittest
from unittest.mock import patch, MagicMock
import os
import sys
import json

# Set environment variables for testing
os.environ["SECRET_KEY"] = "test-secret-key"

# Mock dependencies that might be missing in the environment
# We do this before importing the application code
sys.modules["requests"] = MagicMock()
sys.modules["dotenv"] = MagicMock()
sys.modules["flask"] = MagicMock()

# Adiciona o diretório backend ao path para importar modules corretamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import application code after mocking
from services.llm_service import analyze_content
from config import Config

class TestLLMService(unittest.TestCase):

    def setUp(self):
        # Reset the mock for requests.post before each test
        sys.modules["requests"].post.reset_mock()

    def test_analyze_content_no_api_key(self):
        """Testa se dados simulados são retornados quando não há chave de API."""
        # Salva o valor original
        original_key = Config.LLM_API_KEY
        Config.LLM_API_KEY = None

        try:
            result = analyze_content("text", "Teste de conteúdo")
            self.assertIn("analysis", result)
            self.assertIn("sourceReliability", result)
            self.assertIn("factualConsistency", result)
            self.assertIn("contentQuality", result)
            self.assertIn("technicalIntegrity", result)
            self.assertEqual(result["sourceReliability"], 85) # Valor do mock
        finally:
            # Restaura o valor original
            Config.LLM_API_KEY = original_key

    def test_analyze_content_success(self):
        """Testa o fluxo de sucesso com chamada de API mockada."""
        # Configura API key mockada
        original_key = Config.LLM_API_KEY
        Config.LLM_API_KEY = "test-key"

        expected_response = {
            "analysis": "Conteúdo verificado.",
            "sourceReliability": 90,
            "factualConsistency": 95,
            "contentQuality": 88,
            "technicalIntegrity": 92
        }

        # Configura o mock do requests
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": json.dumps(expected_response)
                    }
                }
            ]
        }
        mock_response.raise_for_status.return_value = None

        # Como requests é um mock global, configuramos ele diretamente
        sys.modules["requests"].post.return_value = mock_response

        try:
            result = analyze_content("text", "Conteúdo real")
            self.assertEqual(result, expected_response)
            sys.modules["requests"].post.assert_called_once()
        finally:
            Config.LLM_API_KEY = original_key

    def test_analyze_content_json_error(self):
        """Testa o comportamento quando a LLM retorna JSON inválido."""
        original_key = Config.LLM_API_KEY
        Config.LLM_API_KEY = "test-key"

        # Configura o mock para retornar string inválida
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "choices": [
                {
                    "message": {
                        "content": "Isso não é um JSON válido"
                    }
                }
            ]
        }

        sys.modules["requests"].post.return_value = mock_response

        try:
            result = analyze_content("text", "Conteúdo")
            # Deve retornar o mock data em caso de erro
            self.assertIn("analysis", result)
            self.assertEqual(result["sourceReliability"], 85) # Valor do mock
        finally:
            Config.LLM_API_KEY = original_key

if __name__ == '__main__':
    unittest.main()
