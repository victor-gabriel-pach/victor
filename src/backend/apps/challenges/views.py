from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Max
from .models import Challenge, ChallengeCopy, Submission
from .serializers import ChallengeSerializer, ChallengeCopySerializer, SubmissionSerializer


class ChallengeViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de desafios"""
    queryset = Challenge.objects.filter(status='published')
    serializer_class = ChallengeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.user_type == 'admin':
            return Challenge.objects.all()
        return Challenge.objects.filter(status='published')


class ChallengeCopyViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de cópias de desafios"""
    serializer_class = ChallengeCopySerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return ChallengeCopy.objects.all()
        elif user.user_type == 'participant':
            return ChallengeCopy.objects.filter(participant=user)
        elif user.user_type == 'tutor':
            # Tutores podem ver cópias dos membros de suas equipes
            team_members = user.tutored_teams.values_list('members__participant', flat=True)
            return ChallengeCopy.objects.filter(participant__in=team_members)
        return ChallengeCopy.objects.none()
    
    def create(self, request, *args, **kwargs):
        """Cria uma nova cópia de desafio para o participante"""
        challenge_id = request.data.get('challenge')
        
        try:
            challenge = Challenge.objects.get(id=challenge_id, status='published')
        except Challenge.DoesNotExist:
            return Response(
                {'error': 'Desafio não encontrado ou não publicado.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        # Determina o próximo número de cópia
        max_copy = ChallengeCopy.objects.filter(
            challenge=challenge,
            participant=request.user
        ).aggregate(Max('copy_number'))['copy_number__max']
        
        next_copy_number = (max_copy or 0) + 1
        
        # Cria a cópia
        copy = ChallengeCopy.objects.create(
            challenge=challenge,
            participant=request.user,
            copy_number=next_copy_number,
            notebook_file=challenge.notebook_template  # Copia o template
        )
        
        serializer = self.get_serializer(copy)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SubmissionViewSet(viewsets.ModelViewSet):
    """ViewSet para gerenciamento de submissões"""
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        if user.user_type == 'admin':
            return Submission.objects.all()
        elif user.user_type == 'participant':
            # Participantes veem submissões da própria equipe
            try:
                team = user.team_membership.team
                return Submission.objects.filter(team=team)
            except:
                return Submission.objects.none()
        elif user.user_type == 'tutor':
            # Tutores veem submissões de suas equipes
            return Submission.objects.filter(team__tutor=user)
        return Submission.objects.none()
    
    def create(self, request, *args, **kwargs):
        """Cria uma nova submissão"""
        copy_id = request.data.get('challenge_copy')
        
        try:
            copy = ChallengeCopy.objects.get(id=copy_id, participant=request.user)
        except ChallengeCopy.DoesNotExist:
            return Response(
                {'error': 'Cópia de desafio não encontrada.'},
                status=status.HTTP_404_NOT_FOUND
            )
        
        if copy.is_submitted:
            return Response(
                {'error': 'Esta cópia já foi submetida.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Verifica se o participante está em uma equipe
        try:
            team = request.user.team_membership.team
        except:
            return Response(
                {'error': 'Você precisa estar em uma equipe para submeter.'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        # Cria a submissão
        submission_data = {
            'challenge_copy': copy.id,
            'team': team.id,
            'accuracy': request.data.get('accuracy'),
            'execution_time': request.data.get('execution_time'),
            'code_snapshot': request.data.get('code_snapshot', '')
        }
        
        serializer = self.get_serializer(data=submission_data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
