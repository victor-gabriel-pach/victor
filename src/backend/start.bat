@echo off
REM Script de inicialização rápida do projeto para Windows

echo 🚀 Iniciando configuração do projeto OBRIA...

REM Ativa o ambiente virtual
if exist "venv\" (
    echo ✓ Ativando ambiente virtual...
    call venv\Scripts\activate.bat
) else (
    echo ❌ Ambiente virtual não encontrado. Execute: python -m venv venv
    exit /b 1
)

REM Instala dependências
echo 📦 Instalando dependências...
pip install -r requirements.txt

REM Executa migrações
echo 🔄 Executando migrações...
python manage.py makemigrations
python manage.py migrate

REM Setup inicial
echo ⚙️ Configuração inicial...
python setup_initial.py

REM Coleta arquivos estáticos
echo 📁 Coletando arquivos estáticos...
python manage.py collectstatic --noinput

echo ✅ Configuração concluída!
echo.
echo Para iniciar o servidor, execute:
echo python manage.py runserver

pause
