import os
import sys
import pytest

# Adiciona o diretório backend ao sys.path para garantir que os módulos sejam encontrados
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Configura a SECRET_KEY antes de importar o app, pois o Config valida sua existência
os.environ['SECRET_KEY'] = 'test-key'

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
