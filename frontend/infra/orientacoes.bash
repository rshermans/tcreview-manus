git checkout -b fix/truecheck
# Crie/edite cada ficheiro conforme listado acima
git add backend config.py app.py wsgi.py services/llm_service.py \
        backend/routes/__init__.py backend/services/__init__.py backend/__init__.py \
        backend/.env.example backend/tests/test_api.py \
        frontend/src/services/api.js frontend/.env.example \
        backend/requirements.txt infra/Dockerfile infra/nginx.conf infra/truecheck.service infra/deploy.sh
git commit -m "Refatoração de segurança, config e deploy do TrueCheck"


Instalação de dependências e ambiente:
#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r backend/requirements.txt


Executar os testes:

cd backend
pytest -q


Comando para executar backend localmente:

export FLASK_DEBUG=True
cd backend
python app.py


Executar frontend:

cd frontend
cp .env.example .env  # Ajuste VITE_API_URL se necessário
npm install
npm run dev
# Para build de produção:
npm run build

