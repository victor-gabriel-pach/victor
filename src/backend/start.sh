#!/bin/bash

# Script de inicialização rápida do projeto

echo "🚀 Iniciando configuração do projeto OBRIA..."

# Ativa o ambiente virtual
if [ -d "venv" ]; then
    echo "✓ Ativando ambiente virtual..."
    source venv/Scripts/activate
else
    echo "❌ Ambiente virtual não encontrado. Execute: python -m venv venv"
    exit 1
fi

# Instala dependências
echo "📦 Instalando dependências..."
pip install -r requirements.txt

# Executa migrações
echo "🔄 Executando migrações..."
python manage.py makemigrations
python manage.py migrate

# Setup inicial
echo "⚙️ Configuração inicial..."
python setup_initial.py

# Coleta arquivos estáticos
echo "📁 Coletando arquivos estáticos..."
python manage.py collectstatic --noinput

echo "✅ Configuração concluída!"
echo ""
echo "Para iniciar o servidor, execute:"
echo "python manage.py runserver"
