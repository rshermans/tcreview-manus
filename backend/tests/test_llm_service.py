import unittest
from unittest.mock import patch, MagicMock
import json
import os
import sys

# Set SECRET_KEY before importing anything that might use Config
os.environ['SECRET_KEY'] = 'test-secret-key'

# Mocking Config before it's used if necessary, but here we will patch it.
from services.llm_service import analyze_content

class TestLLMService(unittest.TestCase):

    @patch('requests.post')
    def test_analyze_content_success(self, mock_post):
        # Configurar mock para resposta da API
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": json.dumps({
                        "analysis": "Conteúdo confiável",
                        "sourceReliability": 90,
                        "factualConsistency": 95,
                        "contentQuality": 85,
                        "technicalIntegrity": 80
                    })
                }
            }]
        }
        mock_post.return_value = mock_response

        # Configurar chave de API para forçar chamada real (mockada)
        with patch('services.llm_service.Config') as mock_config:
            mock_config.LLM_API_KEY = 'valid_key'
            mock_config.LLM_API_URL = 'https://api.openai.com/v1/chat/completions'
            mock_config.LLM_MODEL = 'gpt-3.5-turbo'
            result = analyze_content('text', 'Conteúdo de teste')

        self.assertEqual(result['analysis'], "Conteúdo confiável")
        self.assertEqual(result['sourceReliability'], 90)
        self.assertEqual(result['factualConsistency'], 95)
        self.assertEqual(result['contentQuality'], 85)
        self.assertEqual(result['technicalIntegrity'], 80)

    @patch('requests.post')
    def test_analyze_content_markdown_json(self, mock_post):
        # Testar quando a LLM retorna JSON envolto em markdown
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": "Aqui está a análise:\n```json\n{\n  \"analysis\": \"Markdown JSON\",\n  \"sourceReliability\": 70,\n  \"factualConsistency\": 70,\n  \"contentQuality\": 70,\n  \"technicalIntegrity\": 70\n}\n```"
                }
            }]
        }
        mock_post.return_value = mock_response

        with patch('services.llm_service.Config') as mock_config:
            mock_config.LLM_API_KEY = 'valid_key'
            mock_config.LLM_API_URL = 'https://api.openai.com/v1/chat/completions'
            mock_config.LLM_MODEL = 'gpt-3.5-turbo'
            result = analyze_content('text', 'Conteúdo de teste')

        self.assertEqual(result['analysis'], "Markdown JSON")
        self.assertEqual(result['sourceReliability'], 70)

    def test_analyze_content_no_api_key(self):
        # Testar fallback quando a chave da API está faltando
        with patch('services.llm_service.Config') as mock_config:
            mock_config.LLM_API_KEY = 'sua_chave_api_llm_aqui'
            result = analyze_content('text', 'Conteúdo de teste')

        self.assertIn("simulada", result['analysis'])
        self.assertEqual(result['sourceReliability'], 75)

    @patch('requests.post')
    def test_analyze_content_invalid_json(self, mock_post):
        # Testar fallback quando a LLM retorna JSON inválido
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "choices": [{
                "message": {
                    "content": "Resposta que não é JSON"
                }
            }]
        }
        mock_post.return_value = mock_response

        with patch('services.llm_service.Config') as mock_config:
            mock_config.LLM_API_KEY = 'valid_key'
            mock_config.LLM_API_URL = 'https://api.openai.com/v1/chat/completions'
            mock_config.LLM_MODEL = 'gpt-3.5-turbo'
            result = analyze_content('text', 'Conteúdo de teste')

        self.assertEqual(result['analysis'], "Resposta que não é JSON")
        self.assertEqual(result['sourceReliability'], 0)

if __name__ == '__main__':
    unittest.main()
