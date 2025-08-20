#!/bin/bash
# Script de provisionamento inicial de uma instância Ubuntu/Debian para o TrueCheck.
# Este script instala dependências, configura ambientes e inicia o serviço.

set -e

APP_DIR=/opt/truecheck

echo "Atualizando pacotes..."
sudo apt-get update -y
sudo apt-get upgrade -y

echo "Instalando dependências do sistema..."
sudo apt-get install -y python3 python3-venv python3-pip nginx git

echo "Clonando repositório..."
sudo mkdir -p "$APP_DIR"
sudo chown "$USER":"$USER" "$APP_DIR"
git clone <URL-DO-REPOSITORIO> "$APP_DIR"

cd "$APP_DIR/backend"
echo "Criando ambiente virtual..."
python3 -m venv venv
source venv/bin/activate

echo "Instalando dependências Python..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Copiando arquivo de exemplo .env..."
cp .env.example .env
echo "Edite o arquivo .env para adicionar segredos reais."

echo "Configurando serviço systemd..."
sudo cp "$APP_DIR/infra/truecheck.service" /etc/systemd/system/truecheck.service
sudo systemctl daemon-reload
sudo systemctl enable truecheck
sudo systemctl start truecheck

echo "Configurando Nginx..."
sudo cp "$APP_DIR/infra/nginx.conf" /etc/nginx/nginx.conf
sudo systemctl restart nginx

echo "Deploy concluído. A API está escutando na porta 80."
