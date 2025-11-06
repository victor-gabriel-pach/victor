#!/bin/bash

echo "🚀 Iniciando configuração do projeto OBRIA..."

if [ -d "venv" ]; then
    echo "✓ Ativando ambiente virtual..."
    source venv/Scripts/activate
else
    echo "❌ Ambiente virtual não encontrado. Execute: python -m venv venv"
    exit 1
fi

echo "📦 Instalando dependências..."
pip install -r requirements.txt

echo "🔄 Executando migrações..."
python manage.py makemigrations
python manage.py migrate

echo "⚙️ Configuração inicial..."
python setup_initial.py

echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Configuração concluída!"
echo ""
echo "Para iniciar o servidor, execute:"
echo "python manage.py runserver"
