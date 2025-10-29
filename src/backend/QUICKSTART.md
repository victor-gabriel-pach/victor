# 🚀 Guia de Início Rápido - Backend OBRIA

## ✅ Pré-requisitos Instalados

- ✓ Ambiente virtual criado em `venv/`
- ✓ Estrutura de arquivos Django criada
- ✓ Apps configurados: users, challenges, courses, feed, leaderboard, store, notifications
- ✓ Modelos definidos baseados nas histórias de usuário
- ✓ Sistema de autenticação JWT configurado
- ✓ Documentação API (Swagger) configurada

## 📦 Próximos Passos

### 1. Instalar Dependências

**Windows (PowerShell ou CMD)**:
```cmd
cd src\backend
venv\Scripts\activate
pip install -r requirements.txt
```

**Linux/Mac (Bash)**:
```bash
cd src/backend
source venv/bin/activate
pip install -r requirements.txt
```

### 2. Configurar Variáveis de Ambiente

```bash
cp .env.example .env
```

Edite o arquivo `.env` com suas configurações. Para desenvolvimento local, pode deixar os valores padrão.

### 3. Executar Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Criar Usuário Administrador e Dados Iniciais

```bash
python setup_initial.py
```

Ou manualmente:
```bash
python manage.py createsuperuser
```

### 5. Iniciar o Servidor

```bash
python manage.py runserver
```

O servidor estará disponível em: **http://localhost:8000**

## 🔍 Testando a API

### Acesse a Documentação Interativa

Abra no navegador: **http://localhost:8000/api/docs/**

### Exemplo: Registrar um Usuário

**POST** `http://localhost:8000/api/users/users/register/`

```json
{
  "username": "joao",
  "nickname": "João Silva",
  "email": "joao@example.com",
  "password": "senha123",
  "password2": "senha123",
  "user_type": "participant",
  "school": "Escola Exemplo"
}
```

### Exemplo: Fazer Login

**POST** `http://localhost:8000/api/users/auth/login/`

```json
{
  "username": "joao",
  "password": "senha123"
}
```

Resposta:
```json
{
  "access": "eyJ0eXAiOiJKV1Qi...",
  "refresh": "eyJ0eXAiOiJKV1Qi..."
}
```

### Exemplo: Acessar Dados do Usuário

**GET** `http://localhost:8000/api/users/users/me/`

Headers:
```
Authorization: Bearer eyJ0eXAiOiJKV1Qi...
```

## 🎯 Estrutura Criada

```
src/backend/
├── apps/
│   ├── users/           ✅ Usuários, equipes, autenticação
│   ├── challenges/      ✅ Desafios, cópias, submissões
│   ├── courses/         ✅ Cursos, módulos, unidades
│   ├── feed/            ✅ Feed social, postagens, comentários
│   ├── leaderboard/     ✅ Ranking de equipes
│   ├── store/           ✅ Loja de gamificação
│   └── notifications/   ✅ Sistema de notificações
├── config/
│   ├── settings.py      ✅ Configurações Django
│   ├── urls.py          ✅ Rotas da API
│   ├── wsgi.py          ✅ WSGI
│   └── celery.py        ✅ Configuração Celery
├── venv/                ✅ Ambiente virtual
├── manage.py            ✅ CLI do Django
├── requirements.txt     ✅ Dependências
├── .env.example         ✅ Exemplo de variáveis de ambiente
├── .gitignore           ✅ Arquivos ignorados
├── README.md            ✅ Documentação principal
├── ARCHITECTURE.md      ✅ Visão geral da arquitetura
├── setup_initial.py     ✅ Script de configuração inicial
├── start.bat            ✅ Script de início (Windows)
└── start.sh             ✅ Script de início (Linux/Mac)
```

## 🔧 Modelos Implementados

### Users App
- ✅ `User` - Usuário customizado (Participante, Tutor, Admin)
- ✅ `Team` - Equipes (3 participantes + 1 tutor)
- ✅ `TeamMember` - Relacionamento participante-equipe

### Challenges App
- ✅ `Challenge` - Desafios de IA
- ✅ `ChallengeCopy` - Cópias editáveis dos participantes
- ✅ `Submission` - Submissões (1 por cópia)

### Courses App
- ✅ `Course` - Curso de IA
- ✅ `Module` - Módulos do curso
- ✅ `Unit` - Unidades com vídeos e atividades
- ✅ `ModuleCompletion` - Registro de conclusão

### Feed App
- ✅ `Post` - Postagens (280 caracteres)
- ✅ `Comment` - Comentários em postagens

### Leaderboard App
- ✅ `LeaderboardEntry` - Entrada no ranking por equipe

### Store App
- ✅ `StoreItem` - Itens da loja (selos, efeitos, fontes)
- ✅ `Purchase` - Registro de compras

### Notifications App
- ✅ `Notification` - Notificações gerais
- ✅ `UserNotification` - Notificações individuais

## 🎮 Funcionalidades Implementadas

### Sistema de Gamificação
- ✅ Moedas ganhas ao concluir módulos (10 moedas)
- ✅ Moedas ganhas ao submeter desafios (10 moedas)
- ✅ Sistema de compras na loja
- ✅ Itens equipáveis no perfil

### Autenticação e Permissões
- ✅ JWT com access e refresh tokens
- ✅ 3 tipos de usuário (Participante, Tutor, Admin)
- ✅ Permissões específicas por tipo

### Sistema de Desafios
- ✅ Criação de múltiplas cópias por participante
- ✅ Submissão única por cópia
- ✅ Cálculo automático de acurácia
- ✅ Histórico de submissões

### Leaderboard
- ✅ Ranking por melhor acurácia
- ✅ Filtros por equipe e tutor
- ✅ Histórico de evolução

## 📚 Documentação

- 📄 **README.md** - Documentação principal e instruções de instalação
- 🏗️ **ARCHITECTURE.md** - Visão geral da arquitetura e módulos
- 📖 **API Docs** - Documentação interativa em /api/docs/

## 🐛 Troubleshooting

### Erro: "Import 'django' could not be resolved"
**Solução**: Instale as dependências com `pip install -r requirements.txt`

### Erro: "No module named 'apps'"
**Solução**: Execute os comandos dentro da pasta `src/backend/`

### Erro: "DJANGO_SETTINGS_MODULE is not set"
**Solução**: O manage.py já define isso automaticamente. Certifique-se de estar na pasta correta.

### Erro ao criar migrations
**Solução**: 
```bash
python manage.py makemigrations users
python manage.py makemigrations challenges
python manage.py makemigrations courses
python manage.py makemigrations feed
python manage.py makemigrations leaderboard
python manage.py makemigrations store
python manage.py makemigrations notifications
python manage.py migrate
```

## 🎉 Pronto!

Você agora tem uma base funcional completa do backend OBRIA com:

- ✅ 7 apps Django totalmente configurados
- ✅ Sistema de autenticação JWT
- ✅ API REST completa com documentação
- ✅ Modelos baseados nas histórias de usuário
- ✅ Sistema de gamificação
- ✅ Gerenciamento de desafios e submissões
- ✅ Leaderboard e ranking
- ✅ Feed social
- ✅ Sistema de notificações

**Próximo passo**: Desenvolver o frontend ou expandir as funcionalidades do backend!

## 🤝 Contato

Para dúvidas ou sugestões, consulte a documentação ou abra uma issue no repositório.
