import os
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes.analysis_routes import analysis_bp

# Configurar logging básico
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Criar a aplicação Flask
app = Flask(__name__)
app.config.from_object(Config)

# Configurar CORS de forma restritiva. Permite múltiplos domínios separados por vírgulas.
origins = [origin.strip() for origin in Config.CORS_ORIGINS.split(',')] if Config.CORS_ORIGINS else []
CORS(app, origins=origins)

# Registrar blueprints
app.register_blueprint(analysis_bp, url_prefix="/api/analysis")


@app.route("/api/health", methods=["GET"])
def health_check():
    """Endpoint simples para verificar a saúde da API."""
    return jsonify({"status": "ok", "message": "TrueCheck API está funcionando"})


def create_app():
    """
    Factory opcional para integração com frameworks de testes.

    Retorna a instância do aplicativo Flask.
    """
    return app


if __name__ == "__main__":
    # Executar servidor de desenvolvimento somente quando chamado diretamente.
    # O modo debug nunca deve ser ativado em produção.
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_DEBUG", "False").lower() == "true"
    logger.info(f"Iniciando aplicação na porta {port} (debug={debug})")
    app.run(host="0.0.0.0", port=port, debug=debug)
