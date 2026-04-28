import os
import sys
from unittest.mock import MagicMock
import pytest

# Set necessary environment variables BEFORE any imports that rely on them
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['LLM_API_KEY'] = 'test_llm_key'
os.environ['CORS_ORIGINS'] = '*'

# Mock missing modules to allow imports
sys.modules['requests'] = MagicMock()
sys.modules['dotenv'] = MagicMock()

# Add backend directory to sys.path so that modules can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
