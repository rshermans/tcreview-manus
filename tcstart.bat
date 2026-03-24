@echo off
echo ===================================================
echo     Iniciando a Aplicacao TrueCheck
echo ===================================================

echo.
echo [1/2] Iniciando o Backend (Flask)...
start "TrueCheck Backend" cmd /k "cd backend && python -m pip install -r requirements.txt && python app.py"

echo.
echo [2/2] Iniciando o Frontend (Vite/React)...
start "TrueCheck Frontend" cmd /k "cd frontend && npm install && npm run dev"

echo.
echo ===================================================
echo A aplicacao estara disponivel em: http://localhost:5173
echo ===================================================
pause
