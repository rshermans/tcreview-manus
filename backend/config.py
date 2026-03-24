import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

class Config:
    """
    Configuração da aplicação.

    Todas as variáveis sensíveis devem ser definidas via variáveis de ambiente.
    Caso uma variável obrigatória não esteja presente, um ValueError será lançado.
    """
    # A chave secreta deve sempre ser fornecida via variável de ambiente.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    if not SECRET_KEY:
        raise ValueError(
            "SECRET_KEY não definido. Configure uma variável de ambiente SECRET_KEY para uso em produção.")

    # Chave de API da LLM (pode ser nula em desenvolvimento)
    LLM_API_KEY = os.environ.get('LLM_API_KEY')

    # URL da API da LLM com fallback sensato
    LLM_API_URL = os.environ.get('LLM_API_URL', 'https://api.openai.com/v1/chat/completions')

    # Domínios permitidos para CORS, separados por vírgulas.
    # Por segurança, não há valor padrão. Deve ser explicitamente configurado.
    # Em produção defina por exemplo: "https://app.truecheck.com"
    CORS_ORIGINS = os.environ.get('CORS_ORIGINS')
