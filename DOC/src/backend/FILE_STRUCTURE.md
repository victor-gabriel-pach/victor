# 📁 Estrutura de Arquivos - Backend OBRIA

```
src/backend/
│
├── 📄 manage.py                    # CLI do Django
├── 📄 requirements.txt             # Dependências Python
├── 📄 .env.example                 # Exemplo de variáveis de ambiente
├── 📄 .gitignore                   # Arquivos ignorados pelo Git
├── 📄 setup_initial.py             # Script de configuração inicial
├── 📄 start.sh                     # Script de início (Linux/Mac)
├── 📄 start.bat                    # Script de início (Windows)
│
├── 📚 README.md                    # Documentação principal
├── 📚 QUICKSTART.md                # Guia de início rápido
├── 📚 ARCHITECTURE.md              # Arquitetura detalhada
├── 📚 API_EXAMPLES.md              # Exemplos de uso da API
├── 📚 SUMMARY.md                   # Resumo da implementação
│
├── 📁 venv/                        # Ambiente virtual Python
│   ├── Scripts/                    # Executáveis (Windows)
│   ├── bin/                        # Executáveis (Linux/Mac)
│   └── Lib/                        # Bibliotecas instaladas
│
├── 📁 config/                      # Configurações do projeto Django
│   ├── 📄 __init__.py
│   ├── 📄 settings.py              # Configurações principais
│   ├── 📄 urls.py                  # URLs principais
│   ├── 📄 wsgi.py                  # Configuração WSGI
│   ├── 📄 asgi.py                  # Configuração ASGI
│   └── 📄 celery.py                # Configuração Celery
│
└── 📁 apps/                        # Aplicações Django
    ├── 📄 __init__.py
    │
    ├── 📁 users/                   # 👥 Usuários e Equipes
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py              # Configuração do app
    │   ├── 📄 models.py            # User, Team, TeamMember
    │   ├── 📄 admin.py             # Admin do Django
    │   ├── 📄 serializers.py       # Serializers DRF
    │   ├── 📄 views.py             # ViewSets e endpoints
    │   └── 📄 urls.py              # Rotas do app
    │
    ├── 📁 challenges/              # 🎯 Desafios e Submissões
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py
    │   ├── 📄 models.py            # Challenge, ChallengeCopy, Submission
    │   ├── 📄 admin.py
    │   ├── 📄 serializers.py
    │   ├── 📄 views.py
    │   └── 📄 urls.py
    │
    ├── 📁 courses/                 # 📚 Cursos e Módulos
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py
    │   ├── 📄 models.py            # Course, Module, Unit, ModuleCompletion
    │   ├── 📄 admin.py
    │   ├── 📄 serializers.py       # (a ser implementado)
    │   ├── 📄 views.py             # (a ser implementado)
    │   └── 📄 urls.py
    │
    ├── 📁 feed/                    # 📰 Feed Social
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py
    │   ├── 📄 models.py            # Post, Comment
    │   ├── 📄 admin.py
    │   ├── 📄 serializers.py       # (a ser implementado)
    │   ├── 📄 views.py             # (a ser implementado)
    │   └── 📄 urls.py
    │
    ├── 📁 leaderboard/             # 🏆 Ranking
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py
    │   ├── 📄 models.py            # LeaderboardEntry
    │   ├── 📄 admin.py
    │   ├── 📄 serializers.py       # (a ser implementado)
    │   ├── 📄 views.py             # (a ser implementado)
    │   └── 📄 urls.py
    │
    ├── 📁 store/                   # 🛒 Loja de Gamificação
    │   ├── 📄 __init__.py
    │   ├── 📄 apps.py
    │   ├── 📄 models.py            # StoreItem, Purchase
    │   ├── 📄 admin.py
    │   ├── 📄 serializers.py       # (a ser implementado)
    │   ├── 📄 views.py             # (a ser implementado)
    │   └── 📄 urls.py
    │
    └── 📁 notifications/           # 🔔 Notificações
        ├── 📄 __init__.py
        ├── 📄 apps.py
        ├── 📄 models.py            # Notification, UserNotification
        ├── 📄 admin.py
        ├── 📄 serializers.py       # (a ser implementado)
        ├── 📄 views.py             # (a ser implementado)
        └── 📄 urls.py
```

## 📊 Estatísticas da Estrutura

### Arquivos por Tipo

| Tipo | Quantidade |
|------|------------|
| Python (.py) | 50+ |
| Markdown (.md) | 5 |
| Config (.example, .bat, .sh) | 4 |
| Total | 59+ |

### Arquivos por App

| App | Arquivos |
|-----|----------|
| users | 7 |
| challenges | 7 |
| courses | 7 |
| feed | 7 |
| leaderboard | 7 |
| store | 7 |
| notifications | 7 |
| config | 6 |

## 🔑 Arquivos Principais

### Configuração
- `config/settings.py` - Todas as configurações do Django
- `.env.example` - Template de variáveis de ambiente
- `requirements.txt` - Dependências do projeto

### Documentação
- `README.md` - Documentação principal e instalação
- `QUICKSTART.md` - Guia rápido de início
- `ARCHITECTURE.md` - Arquitetura e design
- `API_EXAMPLES.md` - Exemplos práticos de uso
- `SUMMARY.md` - Resumo da implementação

### Gerenciamento
- `manage.py` - CLI do Django
- `setup_initial.py` - Configuração inicial automatizada
- `start.sh` / `start.bat` - Scripts de inicialização

## 📁 Diretórios Criados Automaticamente

Após executar as migrações e coletar arquivos estáticos:

```
src/backend/
├── 📁 media/                       # Arquivos de mídia (uploads)
│   ├── avatars/                    # Avatars dos usuários
│   ├── challenges/
│   │   ├── templates/              # Templates de notebooks
│   │   ├── datasets/               # Datasets dos desafios
│   │   └── copies/                 # Cópias dos participantes
│   ├── courses/
│   │   └── ebooks/                 # E-books dos cursos
│   └── store/
│       └── items/                  # Imagens dos itens da loja
│
└── 📁 staticfiles/                 # Arquivos estáticos coletados
    └── admin/                      # Assets do Django Admin
```

## 🗄️ Banco de Dados

```
db.sqlite3                          # Banco SQLite (desenvolvimento)
```

Tabelas criadas:
- `users_user` - Usuários
- `users_team` - Equipes
- `users_teammember` - Membros das equipes
- `challenges_challenge` - Desafios
- `challenges_challengecopy` - Cópias de desafios
- `challenges_submission` - Submissões
- `courses_course` - Cursos
- `courses_module` - Módulos
- `courses_unit` - Unidades
- `courses_modulecompletion` - Conclusões
- `feed_post` - Postagens
- `feed_comment` - Comentários
- `leaderboard_leaderboardentry` - Ranking
- `store_storeitem` - Itens da loja
- `store_purchase` - Compras
- `notifications_notification` - Notificações
- `notifications_usernotification` - Notificações dos usuários

## 🎨 Estrutura de URLs

```
http://localhost:8000/
├── /admin/                         # Django Admin
├── /api/
│   ├── /schema/                    # Schema OpenAPI
│   ├── /docs/                      # Swagger UI
│   ├── /users/
│   │   ├── /users/                 # CRUD de usuários
│   │   ├── /teams/                 # CRUD de equipes
│   │   └── /auth/                  # Login e refresh token
│   ├── /challenges/
│   │   ├── /challenges/            # Lista de desafios
│   │   ├── /copies/                # Cópias dos participantes
│   │   └── /submissions/           # Submissões
│   ├── /courses/                   # Cursos e módulos
│   ├── /feed/                      # Feed social
│   ├── /leaderboard/               # Ranking
│   ├── /store/                     # Loja
│   └── /notifications/             # Notificações
└── /media/                         # Arquivos de mídia
```

## 💾 Arquivos de Migração

```
apps/
├── users/migrations/
│   └── 0001_initial.py             # Criação inicial de User, Team, TeamMember
├── challenges/migrations/
│   └── 0001_initial.py             # Criação de Challenge, Copy, Submission
├── courses/migrations/
│   └── 0001_initial.py             # Criação de Course, Module, Unit
├── feed/migrations/
│   └── 0001_initial.py             # Criação de Post, Comment
├── leaderboard/migrations/
│   └── 0001_initial.py             # Criação de LeaderboardEntry
├── store/migrations/
│   └── 0001_initial.py             # Criação de StoreItem, Purchase
└── notifications/migrations/
    └── 0001_initial.py             # Criação de Notification, UserNotification
```

## 🔧 Arquivos de Configuração

- `.gitignore` - Ignora venv, db.sqlite3, .env, etc.
- `.env.example` - Template de variáveis de ambiente
- `requirements.txt` - Dependências Python

## 📈 Evolução do Projeto

### ✅ Implementado
- Estrutura completa de apps
- Modelos de dados
- Sistema de autenticação
- Endpoints básicos (users, challenges)
- Documentação abrangente

### 🚧 A Implementar (ViewSets e Serializers Restantes)
- Views e serializers completos para:
  - Courses
  - Feed
  - Leaderboard
  - Store
  - Notifications

### 🔜 Melhorias Futuras
- Testes unitários e de integração
- Cache com Redis
- WebSockets para notificações em tempo real
- CI/CD com GitHub Actions
- Containerização com Docker

---

**Esta estrutura fornece uma base sólida e escalável para o projeto OBRIA!** 🚀
