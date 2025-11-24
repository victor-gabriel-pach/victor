# Visão Geral da Arquitetura - Backend OBRIA

## 📋 Resumo

Backend desenvolvido em Django/DRF para a plataforma de Olimpíadas de IA Aplicada, seguindo as especificações das histórias de usuário.

## 🎯 Módulos Implementados

### 1. **Users** (`apps.users`)
**Responsabilidade**: Gerenciamento de usuários, equipes e autenticação

**Modelos**:
- `User`: Usuário customizado (Participante, Tutor, Admin)
- `Team`: Equipes de 3 participantes + 1 tutor
- `TeamMember`: Relacionamento participante-equipe

**Endpoints principais**:
- `POST /api/users/users/register/` - Registro
- `POST /api/users/auth/login/` - Login (JWT)
- `GET /api/users/users/me/` - Perfil do usuário
- `GET /api/users/teams/my_teams/` - Equipes do usuário
- `POST /api/users/teams/{id}/add_member/` - Adicionar membro

### 2. **Challenges** (`apps.challenges`)
**Responsabilidade**: Desafios de IA, cópias e submissões

**Modelos**:
- `Challenge`: Desafio criado por admin
- `ChallengeCopy`: Cópia editável do participante
- `Submission`: Submissão única por cópia

**Funcionalidades**:
- Participante cria múltiplas cópias
- Cada cópia pode ser submetida apenas uma vez
- Submissão adiciona moedas automaticamente
- Admin visualiza todos os códigos submetidos

**Endpoints principais**:
- `GET /api/challenges/challenges/` - Lista desafios
- `POST /api/challenges/copies/` - Criar cópia
- `POST /api/challenges/submissions/` - Submeter solução

### 3. **Courses** (`apps.courses`)
**Responsabilidade**: Curso de IA com módulos e unidades

**Modelos**:
- `Course`: Curso com e-book
- `Module`: Módulo do curso (recompensa: 10 moedas)
- `Unit`: Unidade com vídeo e atividade
- `ModuleCompletion`: Registro de conclusão

**Funcionalidades**:
- Admin controla visibilidade de módulos
- Participantes ganham moedas ao concluir módulos
- Tutores têm acesso opcional ao conteúdo

### 4. **Feed** (`apps.feed`)
**Responsabilidade**: Feed social da plataforma

**Modelos**:
- `Post`: Postagem (280 caracteres)
- `Comment`: Comentário em postagem

**Funcionalidades**:
- Participantes e tutores podem postar
- Comentários em postagens
- Admin pode moderar (deletar)

### 5. **Leaderboard** (`apps.leaderboard`)
**Responsabilidade**: Ranking de equipes

**Modelos**:
- `LeaderboardEntry`: Entrada no ranking por equipe

**Funcionalidades**:
- Ordenação por melhor acurácia
- Histórico de submissões da equipe
- Filtros por tutor e equipe

### 6. **Store** (`apps.store`)
**Responsabilidade**: Loja de gamificação

**Modelos**:
- `StoreItem`: Item disponível (selos, efeitos, fontes)
- `Purchase`: Registro de compra do usuário

**Funcionalidades**:
- Compra com moedas virtuais
- Itens equipáveis no perfil
- Sistema de inventário

### 7. **Notifications** (`apps.notifications`)
**Responsabilidade**: Sistema de notificações

**Modelos**:
- `Notification`: Notificação geral
- `UserNotification`: Notificação individual

**Funcionalidades**:
- Segmentação por tipo de usuário
- Envio automático de e-mail
- Marcação de lidas/não lidas
- Admin cria e envia notificações

## 🔐 Autenticação e Permissões

**JWT (Simple JWT)**:
- Access Token: 5 horas
- Refresh Token: 7 dias
- Rotação automática de tokens

**Níveis de Permissão**:
1. **Participante**:
   - Criar cópias e submeter desafios
   - Ver submissões da própria equipe
   - Acessar curso e feed
   - Comprar na loja

2. **Tutor**:
   - Ver progresso de suas equipes
   - Acessar leaderboard de suas equipes
   - Visualizar códigos submetidos
   - Não pode submeter desafios

3. **Admin**:
   - CRUD completo em todos os módulos
   - Criar desafios e cursos
   - Moderar feed
   - Enviar notificações
   - Visualizar métricas e auditoria

## 🎮 Sistema de Gamificação

**Formas de ganhar moedas**:
- Concluir módulo do curso: 10 moedas
- Submeter desafio: 10 moedas
- Top 3 no leaderboard: Recompensa variável

**Uso de moedas**:
- Comprar selos de conquista
- Adquirir efeitos visuais
- Fontes personalizadas para nickname

## 🔄 Fluxo de Trabalho

### Participante resolve um desafio:
1. Lista desafios disponíveis
2. Cria uma cópia do desafio
3. Edita o notebook (múltiplas vezes)
4. Submete a solução (apenas 1x por cópia)
5. Sistema calcula acurácia
6. Participante ganha 10 moedas
7. Leaderboard é atualizado

### Tutor acompanha equipe:
1. Acessa dashboard de suas equipes
2. Visualiza ranking no leaderboard
3. Vê submissões e códigos dos membros
4. Acompanha progresso no curso

### Admin gerencia competição:
1. Cria/edita desafios
2. Publica módulos do curso
3. Envia notificações segmentadas
4. Audita submissões
5. Modera feed

## 🗄️ Banco de Dados

**Desenvolvimento**: SQLite (padrão)
**Produção**: PostgreSQL (recomendado)

**Principais relacionamentos**:
- User → Team (1:N para tutores)
- Team → TeamMember → User (N:3 participantes)
- Challenge → ChallengeCopy → Submission (1:N:1)
- Team → Submission (1:N)
- User → Purchase → StoreItem (N:N)

## 🚀 Tecnologias e Bibliotecas

- **Django 5.1.3**: Framework web
- **DRF 3.15.2**: API REST
- **Simple JWT**: Autenticação
- **Pillow**: Processamento de imagens
- **Celery**: Tarefas assíncronas
- **Redis**: Cache e broker
- **drf-spectacular**: Documentação OpenAPI
- **django-cors-headers**: CORS
- **django-filter**: Filtros avançados

## 📊 Métricas e Monitoramento

**Logs de auditoria**:
- Todas ações de admin são registradas
- Submissões são imutáveis
- Histórico de modificações rastreado

**Métricas coletadas**:
- Acurácia das submissões
- Tempo de execução
- Taxa de conclusão de módulos
- Engajamento no feed

## 🔧 Próximas Melhorias Sugeridas

1. **Testes unitários** para todos os endpoints
2. **Cache Redis** para leaderboard
3. **WebSockets** para notificações em tempo real
4. **Elasticsearch** para busca avançada
5. **S3/Cloud Storage** para arquivos de mídia
6. **CI/CD** com GitHub Actions
7. **Docker** para containerização
8. **Monitoring** com Sentry/Prometheus

## 📝 Convenções de Código

- **Nomenclatura**: snake_case para funções/variáveis
- **Models**: CamelCase
- **Docstrings**: Todas as classes e métodos
- **Tipos**: Type hints quando possível
- **Commits**: Mensagens descritivas em português
- **Migrations**: Sempre revisar antes de aplicar

## 🤝 Integração com Frontend

**CORS configurado para**:
- http://localhost:3000 (React)
- http://localhost:5173 (Vite)

**Formato de resposta padrão**:
```json
{
  "id": 1,
  "field": "value",
  "created_at": "2025-10-28T10:00:00Z"
}
```

**Paginação**:
```json
{
  "count": 100,
  "next": "http://api.../page=2",
  "previous": null,
  "results": [...]
}
```

## 📞 Suporte

Para dúvidas sobre a implementação, consulte:
- README.md principal
- Documentação da API em /api/docs/
- Código-fonte com docstrings
