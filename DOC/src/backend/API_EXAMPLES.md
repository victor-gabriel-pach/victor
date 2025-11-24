# 📚 Exemplos de Uso da API - OBRIA

## 🔐 Autenticação

### 1. Registrar Novo Usuário (Participante)

```http
POST /api/users/users/register/
Content-Type: application/json

{
  "username": "maria",
  "nickname": "Maria Santos",
  "email": "maria@example.com",
  "password": "senha123",
  "password2": "senha123",
  "user_type": "participant",
  "school": "Colégio Estadual"
}
```

### 2. Registrar Tutor

```http
POST /api/users/users/register/
Content-Type: application/json

{
  "username": "prof_carlos",
  "nickname": "Prof. Carlos",
  "email": "carlos@example.com",
  "password": "senha123",
  "password2": "senha123",
  "user_type": "tutor"
}
```

### 3. Login

```http
POST /api/users/auth/login/
Content-Type: application/json

{
  "username": "maria",
  "password": "senha123"
}
```

**Resposta**:
```json
{
  "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### 4. Refresh Token

```http
POST /api/users/auth/refresh/
Content-Type: application/json

{
  "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

## 👥 Gerenciamento de Equipes

### 1. Criar Equipe (Tutor)

```http
POST /api/users/teams/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "name": "Equipe Python Masters",
  "tutor": 2
}
```

### 2. Adicionar Membro à Equipe

```http
POST /api/users/teams/1/add_member/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "participant_id": 3
}
```

### 3. Minhas Equipes

```http
GET /api/users/teams/my_teams/
Authorization: Bearer {access_token}
```

### 4. Remover Membro

```http
DELETE /api/users/teams/1/remove_member/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "participant_id": 3
}
```

## 🎯 Desafios

### 1. Listar Desafios Publicados

```http
GET /api/challenges/challenges/
Authorization: Bearer {access_token}
```

### 2. Criar Cópia de Desafio (Participante)

```http
POST /api/challenges/copies/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "challenge": 1
}
```

**Resposta**:
```json
{
  "id": 1,
  "challenge": 1,
  "challenge_title": "Classificação de Imagens",
  "participant": 3,
  "participant_nickname": "Maria Santos",
  "copy_number": 1,
  "notebook_file": "/media/challenges/copies/...",
  "is_submitted": false,
  "created_at": "2025-10-28T10:00:00Z"
}
```

### 3. Submeter Solução

```http
POST /api/challenges/submissions/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "challenge_copy": 1,
  "accuracy": 0.92,
  "execution_time": 45.5,
  "code_snapshot": "import pandas as pd\n..."
}
```

**Resposta**:
```json
{
  "id": 1,
  "challenge_copy": 1,
  "team": 1,
  "team_name": "Equipe Python Masters",
  "challenge_title": "Classificação de Imagens",
  "participant_nickname": "Maria Santos",
  "accuracy": 0.92,
  "execution_time": 45.5,
  "submitted_at": "2025-10-28T11:30:00Z"
}
```

### 4. Minhas Cópias

```http
GET /api/challenges/copies/
Authorization: Bearer {access_token}
```

### 5. Submissões da Equipe

```http
GET /api/challenges/submissions/
Authorization: Bearer {access_token}
```

## 📚 Cursos

### 1. Listar Cursos

```http
GET /api/courses/
Authorization: Bearer {access_token}
```

### 2. Módulos de um Curso

```http
GET /api/courses/courses/1/modules/
Authorization: Bearer {access_token}
```

### 3. Marcar Módulo como Concluído

```http
POST /api/courses/modules/1/complete/
Authorization: Bearer {access_token}
```

## 📰 Feed Social

### 1. Ver Feed

```http
GET /api/feed/posts/
Authorization: Bearer {access_token}
```

### 2. Criar Postagem

```http
POST /api/feed/posts/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "content": "Acabei de resolver o desafio de classificação! 🎉"
}
```

### 3. Comentar em Postagem

```http
POST /api/feed/posts/1/comments/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "content": "Parabéns! Qual acurácia você conseguiu?"
}
```

### 4. Ver Comentários

```http
GET /api/feed/posts/1/comments/
Authorization: Bearer {access_token}
```

## 🏆 Leaderboard

### 1. Ver Ranking Geral

```http
GET /api/leaderboard/
Authorization: Bearer {access_token}
```

**Resposta**:
```json
{
  "count": 10,
  "results": [
    {
      "rank": 1,
      "team": {
        "id": 1,
        "name": "Equipe Python Masters"
      },
      "best_accuracy": 0.95,
      "total_submissions": 5,
      "updated_at": "2025-10-28T12:00:00Z"
    },
    ...
  ]
}
```

### 2. Ranking da Minha Equipe

```http
GET /api/leaderboard/my_team/
Authorization: Bearer {access_token}
```

### 3. Histórico de Submissões da Equipe

```http
GET /api/leaderboard/team/1/history/
Authorization: Bearer {access_token}
```

## 🛒 Loja

### 1. Listar Itens Disponíveis

```http
GET /api/store/items/
Authorization: Bearer {access_token}
```

**Resposta**:
```json
{
  "results": [
    {
      "id": 1,
      "name": "Selo de Bronze",
      "description": "Selo de conquista nível bronze",
      "item_type": "badge",
      "price": 50,
      "image": "/media/store/items/bronze.png",
      "is_available": true
    },
    ...
  ]
}
```

### 2. Comprar Item

```http
POST /api/store/purchase/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "item_id": 1
}
```

### 3. Meus Itens

```http
GET /api/store/my_items/
Authorization: Bearer {access_token}
```

### 4. Equipar Item

```http
POST /api/store/purchases/1/equip/
Authorization: Bearer {access_token}
```

## 🔔 Notificações

### 1. Minhas Notificações

```http
GET /api/notifications/
Authorization: Bearer {access_token}
```

**Resposta**:
```json
{
  "results": [
    {
      "id": 1,
      "notification": {
        "title": "Novo Desafio Disponível!",
        "message": "O desafio 'Previsão de Séries Temporais' foi liberado.",
        "notification_type": "challenge"
      },
      "is_read": false,
      "created_at": "2025-10-28T09:00:00Z"
    },
    ...
  ]
}
```

### 2. Marcar como Lida

```http
POST /api/notifications/1/mark_read/
Authorization: Bearer {access_token}
```

### 3. Criar Notificação (Admin)

```http
POST /api/notifications/notifications/
Authorization: Bearer {admin_token}
Content-Type: application/json

{
  "title": "Manutenção Programada",
  "message": "A plataforma ficará offline amanhã das 2h às 4h",
  "notification_type": "general",
  "target_all": true,
  "send_email": true
}
```

## 👤 Perfil de Usuário

### 1. Meu Perfil

```http
GET /api/users/users/me/
Authorization: Bearer {access_token}
```

### 2. Atualizar Perfil

```http
PATCH /api/users/users/me/
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "bio": "Estudante de IA apaixonado por machine learning",
  "school": "Colégio Técnico"
}
```

### 3. Ver Perfil de Outro Usuário

```http
GET /api/users/users/5/
Authorization: Bearer {access_token}
```

### 4. Buscar Usuários

```http
GET /api/users/users/search/?q=maria
Authorization: Bearer {access_token}
```

## 🎮 Informações de Gamificação

### 1. Meu Saldo de Moedas

```http
GET /api/users/users/me/
Authorization: Bearer {access_token}
```

Retorna o usuário com campo `coins`.

### 2. Histórico de Conquistas

```http
GET /api/store/my_items/?item_type=badge
Authorization: Bearer {access_token}
```

## 📊 Admin - Gestão de Conteúdo

### 1. Criar Desafio (Admin)

```http
POST /api/challenges/challenges/
Authorization: Bearer {admin_token}
Content-Type: multipart/form-data

{
  "title": "Classificação de Textos",
  "description": "Desafio de NLP...",
  "instructions": "Você deve...",
  "notebook_template": [arquivo .ipynb],
  "dataset_file": [arquivo .csv],
  "status": "published",
  "metric_type": "accuracy",
  "coins_reward": 10
}
```

### 2. Criar Módulo de Curso (Admin)

```http
POST /api/courses/modules/
Authorization: Bearer {admin_token}
Content-Type: application/json

{
  "course": 1,
  "title": "Introdução ao Machine Learning",
  "description": "Conceitos básicos...",
  "order": 1,
  "coins_reward": 10,
  "is_active": true
}
```

### 3. Auditar Submissões (Admin)

```http
GET /api/challenges/submissions/?team=1
Authorization: Bearer {admin_token}
```

### 4. Ver Todas as Equipes (Admin)

```http
GET /api/users/teams/
Authorization: Bearer {admin_token}
```

## 🔍 Filtros e Ordenação

### Filtrar Desafios por Status

```http
GET /api/challenges/challenges/?status=published
Authorization: Bearer {access_token}
```

### Ordenar Leaderboard por Data

```http
GET /api/leaderboard/?ordering=-updated_at
Authorization: Bearer {access_token}
```

### Buscar Postagens

```http
GET /api/feed/posts/?search=desafio
Authorization: Bearer {access_token}
```

### Paginação

```http
GET /api/feed/posts/?page=2
Authorization: Bearer {access_token}
```

## 🚨 Tratamento de Erros

### Erro de Autenticação (401)

```json
{
  "detail": "Authentication credentials were not provided."
}
```

### Erro de Permissão (403)

```json
{
  "detail": "You do not have permission to perform this action."
}
```

### Erro de Validação (400)

```json
{
  "password": ["As senhas não coincidem."],
  "email": ["Este campo é obrigatório."]
}
```

### Erro Not Found (404)

```json
{
  "detail": "Not found."
}
```

## 💡 Dicas

1. **Sempre use o token de acesso no header**: `Authorization: Bearer {token}`
2. **Tokens expiram após 5 horas**: Use o refresh token para obter um novo
3. **Participantes só podem submeter se estiverem em uma equipe**
4. **Cada cópia pode ser submetida apenas uma vez**
5. **Moedas são adicionadas automaticamente ao submeter ou concluir módulos**

## 🧪 Testar com cURL

```bash
# Login
curl -X POST http://localhost:8000/api/users/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username":"maria","password":"senha123"}'

# Listar desafios
curl -X GET http://localhost:8000/api/challenges/challenges/ \
  -H "Authorization: Bearer {seu_token}"
```

## 🎯 Próximos Passos

- Explore a documentação interativa em `/api/docs/`
- Teste os endpoints no Swagger UI
- Integre com o frontend
- Implemente testes automatizados
