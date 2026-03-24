from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from config import Config

# Inicializa o Limiter sem o app para evitar importações circulares.
# O app será vinculado posteriormente usando limiter.init_app(app).
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"],
    storage_uri=Config.RATELIMIT_STORAGE_URL,
)
