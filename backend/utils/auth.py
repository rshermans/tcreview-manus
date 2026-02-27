from functools import wraps
from flask import request, jsonify
from config import Config

def auth_required(f):
    """
    Decorador para exigir uma chave de API válida nos cabeçalhos da requisição.
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')

        if not api_key or api_key != Config.API_KEY:
            return jsonify({"error": "Não autorizado. Chave de API inválida ou ausente."}), 401

        return f(*args, **kwargs)

    return decorated_function
