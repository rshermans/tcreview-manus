import unittest
import sys
import os
from unittest.mock import patch, MagicMock

# Add the parent directory (backend) to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

class TestAnalysisVulnerability(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

        # Mock the analyze_content function
        self.patcher = patch('routes.analysis_routes.analyze_content')
        self.mock_analyze = self.patcher.start()
        self.mock_analyze.return_value = {
            "sourceReliability": 8,
            "factualConsistency": 9,
            "contentQuality": 8,
            "technicalIntegrity": 9,
            "analysis": "This is a mocked analysis result."
        }

    def tearDown(self):
        self.patcher.stop()

    def test_preliminary_analysis_valid(self):
        """Test with valid input."""
        response = self.app.post('/api/analysis/preliminary', json={
            'type': 'text',
            'content': 'This is a valid test content.'
        })
        self.assertEqual(response.status_code, 200, f"Valid request should return 200, got {response.status_code}")

    def test_preliminary_analysis_invalid_type(self):
        """Test with invalid type."""
        response = self.app.post('/api/analysis/preliminary', json={
            'type': 'invalid_type',
            'content': 'This content has an invalid type.'
        })
        self.assertEqual(response.status_code, 400, "Should return 400 for invalid type")

    def test_preliminary_analysis_excessive_length(self):
        """Test with excessive content length."""
        long_content = 'a' * 20000
        response = self.app.post('/api/analysis/preliminary', json={
            'type': 'text',
            'content': long_content
        })
        self.assertEqual(response.status_code, 400, "Should return 400 for excessive length")

    def test_preliminary_analysis_non_string_content(self):
        """Test with non-string content (e.g., int)."""
        response = self.app.post('/api/analysis/preliminary', json={
            'type': 'text',
            'content': 12345
        })
        self.assertEqual(response.status_code, 400, "Should return 400 for non-string content")

if __name__ == '__main__':
    unittest.main()
