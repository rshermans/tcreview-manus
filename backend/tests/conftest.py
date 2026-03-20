import pytest
import sys
import os

# Ensure backend directory is in python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Set environment variables early to avoid Config errors during import
os.environ['SECRET_KEY'] = 'test_secret_key'
os.environ['LLM_API_KEY'] = 'test_api_key'

@pytest.fixture
def app():
    from app import create_app
    app = create_app()
    app.config.update({
        "TESTING": True,
    })

    yield app

@pytest.fixture
def client(app):
    return app.test_client()
