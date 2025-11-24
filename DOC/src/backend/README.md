# OBRIA - Plataforma de Olimpíadas de IA

Backend desenvolvido com Django e Django REST Framework para a plataforma de Olimpíadas de Inteligência Artificial Aplicada.

## 🚀 Tecnologias

- Python 3.x
- Django 5.1.3
- Django REST Framework 3.15.2
- PostgreSQL (produção) / SQLite (desenvolvimento)
- JWT para autenticação
- Celery para tarefas assíncronas
- Redis para cache e broker do Celery

## 📋 Pré-requisitos

- Python 3.10+
- pip
- virtualenv
- PostgreSQL (opcional para produção)
- Redis (opcional para tarefas assíncronas)

## 🔧 Instalação

### 1. Clone o repositório e entre na pasta do backend

```bash
cd src/backend
```

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure as variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e ajuste as configurações:

```bash
cp .env.example .env
```

### 5. Execute as migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário

```bash
python manage.py createsuperuser
```

### 7. Execute o servidor de desenvolvimento

```bash
python manage.py runserver
```

O servidor estará disponível em `http://localhost:8000`

## 📁 Estrutura do Projeto

```
backend/
├── apps/
│   ├── users/          # Usuários, equipes e autenticação
│   ├── challenges/     # Desafios e submissões
│   ├── courses/        # Cursos e módulos
│   ├── feed/           # Feed social e postagens
│   ├── leaderboard/    # Ranking e pontuações
│   ├── store/          # Loja de gamificação
│   └── notifications/  # Sistema de notificações
├── config/             # Configurações do Django
├── media/              # Arquivos de mídia
├── staticfiles/        # Arquivos estáticos
├── manage.py
└── requirements.txt
```

## 🔑 Autenticação

A API utiliza JWT (JSON Web Tokens) para autenticação. Para obter um token:

**POST** `/api/users/auth/login/`
```json
{
  "username": "seu_usuario",
  "password": "sua_senha"
}
```

Resposta:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

Use o token de acesso no header das requisições:
```
Authorization: Bearer <access_token>
```

## 📚 Documentação da API

A documentação interativa da API está disponível em:
- Swagger UI: `http://localhost:8000/api/docs/`
- Schema JSON: `http://localhost:8000/api/schema/`

## 🎯 Principais Endpoints

### Usuários
- `POST /api/users/users/register/` - Registro de novo usuário
- `POST /api/users/auth/login/` - Login
- `GET /api/users/users/me/` - Dados do usuário autenticado
- `GET /api/users/teams/my_teams/` - Equipes do usuário

### Desafios
- `GET /api/challenges/challenges/` - Lista de desafios
- `POST /api/challenges/copies/` - Criar cópia de desafio
- `POST /api/challenges/submissions/` - Submeter solução

### Cursos
- `GET /api/courses/` - Lista de cursos e módulos

### Feed
- `GET /api/feed/` - Feed de postagens
- `POST /api/feed/` - Criar postagem

### Leaderboard
- `GET /api/leaderboard/` - Ranking das equipes

### Loja
- `GET /api/store/` - Itens disponíveis
- `POST /api/store/purchase/` - Comprar item

### Notificações
- `GET /api/notifications/` - Notificações do usuário

## 👥 Tipos de Usuário

1. **Participante**: Resolve desafios e acessa cursos
2. **Tutor**: Acompanha equipes (1 ou mais)
3. **Administrador**: Gerencia conteúdo e competição

## 🏆 Sistema de Gamificação

- Moedas ganhas ao:
  - Concluir módulos do curso (10 moedas)
  - Submeter desafios (10 moedas)
  - Alcançar Top 3 no leaderboard (recompensas variáveis)

- Moedas podem ser trocadas por:
  - Selos de conquistas
  - Efeitos visuais de perfil
  - Fontes personalizadas

## 🧪 Testes

Para executar os testes:

```bash
python manage.py test
```

## 📝 Observações

- Os erros de lint sobre imports do Django são normais antes da instalação das dependências
- Configure o PostgreSQL para ambiente de produção
- Configure o Redis para usar filas de tarefas assíncronas
- Ajuste o CORS para permitir apenas domínios confiáveis em produção

## 🤝 Contribuindo

1. Crie uma branch para sua feature (`git checkout -b feature/MinhaFeature`)
2. Commit suas mudanças (`git commit -m 'Adiciona MinhaFeature'`)
3. Push para a branch (`git push origin feature/MinhaFeature`)
4. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT.
