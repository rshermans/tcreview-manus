import os
import sys
import pytest

# Ensure we can import modules from the backend directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set environment variables for testing
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['LLM_API_KEY'] = 'test_llm_key'

@pytest.fixture
def client():
    from app import app
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
