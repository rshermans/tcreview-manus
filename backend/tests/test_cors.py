import unittest
import os
import sys
from unittest.mock import patch

# Define a constant for the secret key to avoid repeated os.environ sets
TEST_SECRET_KEY = 'test-secret-key'

class TestCORS(unittest.TestCase):
    def setUp(self):
        # We need to ensure we can load/reload the app and config with different environment settings
        self.modules_to_reload = ['config', 'app', 'routes.analysis_routes']
        for mod in self.modules_to_reload:
            if mod in sys.modules:
                del sys.modules[mod]
        os.environ['SECRET_KEY'] = TEST_SECRET_KEY

    def tearDown(self):
        for mod in self.modules_to_reload:
            if mod in sys.modules:
                del sys.modules[mod]

    @patch('dotenv.load_dotenv')
    def test_no_cors_by_default(self, mock_load_dotenv):
        """Verify that CORS is disabled if CORS_ORIGINS is not set."""
        with patch.dict(os.environ, {}, clear=False):
            if 'CORS_ORIGINS' in os.environ:
                del os.environ['CORS_ORIGINS']

            from app import app
            client = app.test_client()

            # Request from an origin that used to be the default
            response = client.get('/api/health', headers={'Origin': 'http://localhost:3000'})
            self.assertIsNone(response.headers.get('Access-Control-Allow-Origin'))

    @patch('dotenv.load_dotenv')
    def test_explicit_cors_single_origin(self, mock_load_dotenv):
        """Verify that a single configured origin is allowed."""
        with patch.dict(os.environ, {'CORS_ORIGINS': 'https://trusted.com'}):
            from app import app
            client = app.test_client()

            response = client.get('/api/health', headers={'Origin': 'https://trusted.com'})
            self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), 'https://trusted.com')

    @patch('dotenv.load_dotenv')
    def test_explicit_cors_multiple_origins(self, mock_load_dotenv):
        """Verify that multiple configured origins are allowed."""
        with patch.dict(os.environ, {'CORS_ORIGINS': 'https://a.com, https://b.com'}):
            from app import app
            client = app.test_client()

            for origin in ['https://a.com', 'https://b.com']:
                response = client.get('/api/health', headers={'Origin': origin})
                self.assertEqual(response.headers.get('Access-Control-Allow-Origin'), origin)

    @patch('dotenv.load_dotenv')
    def test_cors_disallows_other_origins(self, mock_load_dotenv):
        """Verify that origins not in the allowed list are rejected."""
        with patch.dict(os.environ, {'CORS_ORIGINS': 'https://trusted.com'}):
            from app import app
            client = app.test_client()

            response = client.get('/api/health', headers={'Origin': 'https://evil.com'})
            self.assertIsNone(response.headers.get('Access-Control-Allow-Origin'))

if __name__ == '__main__':
    unittest.main()
