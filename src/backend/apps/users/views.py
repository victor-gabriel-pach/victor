from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.db.models import Q
from .models import User, Team, TeamMember
from .serializers import (
    UserSerializer, UserRegistrationSerializer,
    TeamSerializer, TeamCreateSerializer, TeamMemberSerializer
)


class UserViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de usuários"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def get_permissions(self):
        if self.action in ['create', 'register']:
            return [permissions.AllowAny()]
        return [permissions.IsAuthenticated()]
    
    def get_serializer_class(self):
        if self.action == 'register':
            return UserRegistrationSerializer
        return UserSerializer
    
    @action(detail=False, methods=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        """Endpoint para registro de novos usuários"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(
            UserSerializer(user).data,
            status=status.HTTP_201_CREATED
        )
    
    @action(detail=False, methods=['get'])
    def me(self, request):
        """Retorna informações do usuário autenticado"""
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search(self, request):
        """Busca usuários por nickname ou username"""
        query = request.query_params.get('q', '')
        users = self.queryset.filter(
            Q(nickname__icontains=query) | Q(username__icontains=query)
        )
        serializer = self.get_serializer(users, many=True)
        return Response(serializer.data)


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de equipes"""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return TeamCreateSerializer
        return TeamSerializer
    
    @action(detail=True, methods=['post'])
    def add_member(self, request, pk=None):
        """Adiciona um membro à equipe"""
        team = self.get_object()
        participant_id = request.data.get('participant_id')
        
        if team.members.count() >= 3:
            return Response(
                {'error': 'A equipe já possui 3 membros.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            participant = User.objects.get(id=participant_id, user_type='participant')
        except User.DoesNotExist:
            return Response(
                {'error': 'Participante não encontrado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if hasattr(participant, 'team_membership'):
            return Response(
                {'error': 'Participante já está em uma equipe.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        TeamMember.objects.create(team=team, participant=participant)
        return Response(
            TeamSerializer(team).data,
            status=status.HTTP_200_OK
        )
    
    @action(detail=True, methods=['delete'])
    def remove_member(self, request, pk=None):
        """Remove um membro da equipe"""
        team = self.get_object()
        participant_id = request.data.get('participant_id')
        
        try:
            member = TeamMember.objects.get(team=team, participant_id=participant_id)
            member.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TeamMember.DoesNotExist:
            return Response(
                {'error': 'Membro não encontrado na equipe.'},
                status=status.HTTP_404_NOT_FOUND
            )
    
    @action(detail=False, methods=['get'])
    def my_teams(self, request):
        """Retorna as equipes do usuário (como tutor ou participante)"""
        user = request.user
        
        if user.user_type == 'tutor':
            teams = Team.objects.filter(tutor=user)
        elif user.user_type == 'participant':
            try:
                team_membership = user.team_membership
                teams = Team.objects.filter(id=team_membership.team.id)
            except TeamMember.DoesNotExist:
                teams = Team.objects.none()
        else:
            teams = Team.objects.all()
        
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)
