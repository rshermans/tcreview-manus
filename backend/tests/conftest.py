import os
import sys
import pytest

# Adicionar o diretório backend ao sys.path para que as importações funcionem
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configurar SECRET_KEY antes de importar o app ou config
os.environ['SECRET_KEY'] = 'test-secret-key'
# Evitar carregar o .env real durante os testes
os.environ['LLM_API_KEY'] = 'test-api-key'

from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    yield app

@pytest.fixture
def client(app):
    return app.test_client()
