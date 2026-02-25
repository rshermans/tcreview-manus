import pytest
import os
import sys

# Adiciona o diretório backend ao sys.path para permitir importações
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_path not in sys.path:
    sys.path.insert(0, backend_path)

# Mock da SECRET_KEY necessária para importar o Config
os.environ['SECRET_KEY'] = 'test-secret-key'

from app import create_app

@pytest.fixture
def client():
    """Fixture que fornece um cliente de teste Flask"""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
