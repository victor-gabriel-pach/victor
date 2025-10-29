from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Modelo de usuário customizado que estende AbstractUser.
    Representa todos os tipos de usuário: Participante, Tutor e Admin.
    """
    
    USER_TYPE_CHOICES = [
        ('participant', 'Participante'),
        ('tutor', 'Tutor'),
        ('admin', 'Administrador'),
    ]
    
    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPE_CHOICES,
        default='participant',
        verbose_name='Tipo de Usuário'
    )
    nickname = models.CharField(max_length=50, unique=True, verbose_name='Apelido')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name='Avatar')
    bio = models.TextField(max_length=500, blank=True, verbose_name='Biografia')
    coins = models.IntegerField(default=0, verbose_name='Moedas')
    
    # Campos específicos para participantes
    school = models.CharField(max_length=200, blank=True, verbose_name='Escola')
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.nickname} ({self.get_user_type_display()})"
    
    def add_coins(self, amount):
        """Adiciona moedas ao usuário"""
        self.coins += amount
        self.save()
    
    def remove_coins(self, amount):
        """Remove moedas do usuário (para compras na loja)"""
        if self.coins >= amount:
            self.coins -= amount
            self.save()
            return True
        return False


class Team(models.Model):
    """
    Modelo de equipe. Uma equipe tem 3 participantes e 1 tutor.
    """
    name = models.CharField(max_length=100, unique=True, verbose_name='Nome da Equipe')
    tutor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tutored_teams',
        limit_choices_to={'user_type': 'tutor'},
        verbose_name='Tutor'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Criação')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Data de Atualização')
    
    class Meta:
        verbose_name = 'Equipe'
        verbose_name_plural = 'Equipes'
        ordering = ['name']
    
    def __str__(self):
        return self.name
    
    @property
    def members_count(self):
        """Retorna o número de membros da equipe"""
        return self.members.count()
    
    @property
    def is_complete(self):
        """Verifica se a equipe está completa (3 membros + 1 tutor)"""
        return self.members.count() == 3 and self.tutor is not None


class TeamMember(models.Model):
    """
    Modelo intermediário para relacionar participantes e equipes.
    Um participante pode estar em apenas uma equipe por vez.
    """
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='members')
    participant = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'user_type': 'participant'},
        related_name='team_membership'
    )
    joined_at = models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')
    
    class Meta:
        verbose_name = 'Membro da Equipe'
        verbose_name_plural = 'Membros das Equipes'
        unique_together = ['team', 'participant']
    
    def __str__(self):
        return f"{self.participant.nickname} - {self.team.name}"
