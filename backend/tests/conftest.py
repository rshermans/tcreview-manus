import os
import pytest
import sys

# Adicionar o diretório backend ao sys.path para que os imports funcionem corretamente
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Definir SECRET_KEY antes de importar o app, pois o Config valida isso no import
os.environ['SECRET_KEY'] = 'test-secret-key'

from app import create_app

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    return app

@pytest.fixture
def client(app):
    return app.test_client()
