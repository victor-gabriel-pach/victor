# ✅ Checklist de Instalação e Configuração - Backend OBRIA

## 📋 Pré-requisitos

- [ ] Python 3.10 ou superior instalado
- [ ] pip atualizado (`python -m pip install --upgrade pip`)
- [ ] Git instalado (para controle de versão)
- [ ] Editor de código (VS Code, PyCharm, etc.)

## 🚀 Etapa 1: Preparação do Ambiente

### 1.1 Navegar até a pasta do backend
```bash
cd src/backend
```

### 1.2 Criar ambiente virtual
```bash
python -m venv venv
```

### 1.3 Ativar ambiente virtual

**Windows (CMD)**:
```cmd
venv\Scripts\activate.bat
```

**Windows (PowerShell)**:
```powershell
venv\Scripts\Activate.ps1
```

**Linux/Mac**:
```bash
source venv/bin/activate
```

✅ Verificar se o prompt mostra `(venv)` no início

## 📦 Etapa 2: Instalação de Dependências

### 2.1 Instalar dependências do projeto
```bash
pip install -r requirements.txt
```

**Tempo estimado**: 2-5 minutos

### 2.2 Verificar instalação
```bash
python -m django --version
```

✅ Deve mostrar: `5.1.3`

```bash
pip list | grep Django
```

✅ Deve listar: Django, djangorestframework, django-cors-headers, etc.

## ⚙️ Etapa 3: Configuração

### 3.1 Copiar arquivo de ambiente
```bash
cp .env.example .env
```

**Windows**:
```cmd
copy .env.example .env
```

### 3.2 Editar arquivo .env (opcional para dev)

Abra `.env` e ajuste se necessário:
```env
SECRET_KEY=sua-chave-secreta-aqui
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

Para desenvolvimento local, os valores padrão funcionam perfeitamente.

## 🗄️ Etapa 4: Banco de Dados

### 4.1 Criar migrations
```bash
python manage.py makemigrations
```

✅ Deve criar migrations para todos os apps

### 4.2 Aplicar migrations
```bash
python manage.py migrate
```

✅ Deve aplicar todas as migrations e criar `db.sqlite3`

### 4.3 Verificar banco de dados
```bash
python manage.py showmigrations
```

✅ Todas as migrations devem ter [X]

## 👤 Etapa 5: Criar Usuário Admin

### Opção A: Script Automatizado (Recomendado)
```bash
python setup_initial.py
```

✅ Cria admin, dados de exemplo e itens da loja

**Credenciais padrão**:
- Username: `admin`
- Password: `admin123`

### Opção B: Manualmente
```bash
python manage.py createsuperuser
```

Siga as instruções no terminal.

## 🧪 Etapa 6: Testar o Servidor

### 6.1 Iniciar servidor de desenvolvimento
```bash
python manage.py runserver
```

✅ Deve mostrar:
```
Starting development server at http://127.0.0.1:8000/
```

### 6.2 Verificar endpoints

Abra no navegador:

- [ ] http://localhost:8000/admin/ - Django Admin
- [ ] http://localhost:8000/api/docs/ - Documentação da API (Swagger)
- [ ] http://localhost:8000/api/schema/ - Schema OpenAPI

### 6.3 Fazer login no admin

1. Acesse http://localhost:8000/admin/
2. Use as credenciais criadas
3. Explore os modelos criados

✅ Deve ver: Users, Teams, Challenges, etc.

## 🔍 Etapa 7: Verificações

### 7.1 Verificar estrutura de apps
```bash
python manage.py showmigrations
```

✅ Todos os apps devem aparecer:
- users
- challenges
- courses
- feed
- leaderboard
- store
- notifications

### 7.2 Verificar configurações
```bash
python manage.py check
```

✅ Deve mostrar: `System check identified no issues (0 silenced).`

### 7.3 Verificar arquivos estáticos
```bash
python manage.py collectstatic --noinput
```

✅ Deve coletar arquivos do admin

## 🧪 Etapa 8: Testar API

### 8.1 Registrar usuário

**POST** http://localhost:8000/api/users/users/register/

```json
{
  "username": "teste",
  "nickname": "Usuário Teste",
  "email": "teste@example.com",
  "password": "senha123",
  "password2": "senha123",
  "user_type": "participant"
}
```

✅ Status 201 Created

### 8.2 Fazer login

**POST** http://localhost:8000/api/users/auth/login/

```json
{
  "username": "teste",
  "password": "senha123"
}
```

✅ Recebe access e refresh tokens

### 8.3 Testar endpoint autenticado

**GET** http://localhost:8000/api/users/users/me/

Headers:
```
Authorization: Bearer {seu_access_token}
```

✅ Retorna dados do usuário

## 📊 Etapa 9: Verificar Dados Iniciais

### 9.1 Verificar itens da loja
```bash
python manage.py shell
```

```python
from apps.store.models import StoreItem
print(StoreItem.objects.count())
```

✅ Deve retornar 5 (se usou setup_initial.py)

### 9.2 Verificar usuário admin
```python
from apps.users.models import User
admin = User.objects.get(username='admin')
print(admin.user_type)  # Deve ser 'admin'
```

## 🎯 Etapa 10: Próximos Passos

- [ ] Explorar documentação da API em /api/docs/
- [ ] Criar equipes de teste
- [ ] Cadastrar desafios de exemplo
- [ ] Testar submissões
- [ ] Configurar PostgreSQL (opcional para produção)
- [ ] Configurar Redis e Celery (opcional)

## 🐛 Troubleshooting

### Problema: `python: command not found`
**Solução**: Use `python3` no lugar de `python`

### Problema: `Permission denied` ao ativar venv (PowerShell)
**Solução**: Execute:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Problema: Import errors no código
**Solução**: Certifique-se de que o venv está ativado e as dependências instaladas

### Problema: `CSRF token missing`
**Solução**: Configure CORS corretamente ou desabilite CSRF para APIs

### Problema: Porta 8000 já em uso
**Solução**: Use outra porta:
```bash
python manage.py runserver 8001
```

### Problema: Migrations não aplicadas
**Solução**: 
```bash
python manage.py migrate --run-syncdb
```

## 📝 Notas Importantes

⚠️ **Ambiente Virtual**: Sempre ative o venv antes de trabalhar no projeto

⚠️ **Migrações**: Execute `makemigrations` e `migrate` após alterar models

⚠️ **Segurança**: Nunca commite o arquivo `.env` com credenciais reais

⚠️ **Produção**: Configure PostgreSQL, Redis e variáveis de ambiente adequadas

## 🎉 Conclusão

Parabéns! Se completou todos os itens acima, seu backend OBRIA está configurado e funcionando!

### Status Final

- [x] Ambiente virtual criado
- [x] Dependências instaladas
- [x] Banco de dados configurado
- [x] Admin criado
- [x] Servidor rodando
- [x] API testada
- [x] Documentação disponível

### Comandos Úteis

**Iniciar servidor**:
```bash
python manage.py runserver
```

**Criar novo admin**:
```bash
python manage.py createsuperuser
```

**Executar shell interativo**:
```bash
python manage.py shell
```

**Ver todas as URLs**:
```bash
python manage.py show_urls
```

---

**🚀 Backend pronto para desenvolvimento!**

Consulte a documentação completa em:
- README.md
- QUICKSTART.md
- API_EXAMPLES.md
