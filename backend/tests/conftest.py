import os
import sys
import pytest

# Adiciona o diretório backend ao path para garantir que os módulos sejam encontrados
backend_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

# Define a SECRET_KEY antes de importar o app ou config para evitar ValueError
os.environ['SECRET_KEY'] = 'test-secret-key-for-unit-tests'

from app import create_app

@pytest.fixture
def app():
    app_instance = create_app()
    app_instance.config.update({
        "TESTING": True,
    })
    return app_instance

@pytest.fixture
def client(app):
    return app.test_client()
