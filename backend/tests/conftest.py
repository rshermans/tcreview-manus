import os
import sys
import pytest

# Add backend directory to sys.path so imports in app.py work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Ensure SECRET_KEY is set before importing app
os.environ["SECRET_KEY"] = "testing"

from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
