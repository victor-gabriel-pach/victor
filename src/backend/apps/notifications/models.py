from django.db import models
from apps.users.models import User


class Notification(models.Model):
    """Notificações para usuários"""
    NOTIFICATION_TYPE_CHOICES = [
        ('general', 'Geral'),
        ('challenge', 'Desafio'),
        ('course', 'Curso'),
        ('team', 'Equipe'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='Título')
    message = models.TextField(verbose_name='Mensagem')
    notification_type = models.CharField(max_length=20, choices=NOTIFICATION_TYPE_CHOICES)
    
    # Segmentação
    target_all = models.BooleanField(default=False, verbose_name='Enviar para Todos')
    target_participants = models.BooleanField(default=False, verbose_name='Enviar para Participantes')
    target_tutors = models.BooleanField(default=False, verbose_name='Enviar para Tutores')
    specific_users = models.ManyToManyField(User, blank=True, related_name='specific_notifications')
    
    send_email = models.BooleanField(default=True, verbose_name='Enviar E-mail')
    
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        limit_choices_to={'user_type': 'admin'},
        related_name='created_notifications'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Notificação'
        verbose_name_plural = 'Notificações'
        ordering = ['-created_at']
    
    def __str__(self):
        return self.title


class UserNotification(models.Model):
    """Notificações individuais dos usuários"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False, verbose_name='Lida')
    read_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Notificação do Usuário'
        verbose_name_plural = 'Notificações dos Usuários'
        ordering = ['-created_at']
        unique_together = ['user', 'notification']
    
    def __str__(self):
        return f"{self.user.nickname} - {self.notification.title}"
