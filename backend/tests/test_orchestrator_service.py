import unittest
from unittest.mock import MagicMock
import sys
import os

# Mock flask because it's not installed in the environment
sys.modules['flask'] = MagicMock()

# Add the backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.orchestrator_service import parse_input

class TestOrchestratorService(unittest.TestCase):
    def test_parse_input_text(self):
        content = "This is a simple text"
        content_type = "text"
        result = parse_input(content, content_type)

        self.assertEqual(result['raw_content'], content)
        self.assertEqual(result['type'], content_type)
        self.assertEqual(result['parsed_text'], content)

    def test_parse_input_url(self):
        content = "https://example.com"
        content_type = "url"
        result = parse_input(content, content_type)

        self.assertEqual(result['raw_content'], content)
        self.assertEqual(result['type'], content_type)
        self.assertEqual(result['parsed_text'], f"[Texto extraído da URL]: {content}")

    def test_parse_input_image(self):
        content = "image_data_here"
        content_type = "image"
        result = parse_input(content, content_type)

        self.assertEqual(result['raw_content'], content)
        self.assertEqual(result['type'], content_type)
        self.assertIn("[Descrição visual da imagem]", result['parsed_text'])

    def test_parse_input_unknown_type(self):
        content = "some content"
        content_type = "unknown"
        result = parse_input(content, content_type)

        self.assertEqual(result['raw_content'], content)
        self.assertEqual(result['type'], content_type)
        self.assertEqual(result['parsed_text'], content)

if __name__ == '__main__':
    unittest.main()
