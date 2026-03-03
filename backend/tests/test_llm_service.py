import unittest
from unittest.mock import MagicMock, patch
import sys

# We need to mock these before importing services.llm_service
# because they are imported at the module level there.
with patch.dict('sys.modules', {
    'requests': MagicMock(),
    'flask': MagicMock(),
    'flask_cors': MagicMock(),
    'python-dotenv': MagicMock(),
    'dotenv': MagicMock()
}):
    from services.llm_service import cross_verify_content

class TestLLMService(unittest.TestCase):
    def test_cross_verify_content_returns_expected_structure(self):
        content = "test content"
        analysis = {"summary": "test summary"}
        result = cross_verify_content(content, analysis)

        self.assertIn("verified", result)
        self.assertIn("confidence_score", result)
        self.assertIn("notes", result)
        self.assertIsInstance(result["verified"], bool)
        self.assertIsInstance(result["confidence_score"], float)
        self.assertIsInstance(result["notes"], str)

    def test_cross_verify_content_values(self):
        content = "test content"
        analysis = {"summary": "test summary"}
        result = cross_verify_content(content, analysis)

        self.assertTrue(result["verified"])
        self.assertEqual(result["confidence_score"], 0.92)
        self.assertEqual(result["notes"], "Information matches known reliable sources.")

if __name__ == "__main__":
    unittest.main()
