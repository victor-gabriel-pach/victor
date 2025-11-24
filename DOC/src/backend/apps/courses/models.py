from django.db import models
from apps.users.models import User


class Course(models.Model):
    """Curso de Introdução à IA"""
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    ebook_file = models.FileField(upload_to='courses/ebooks/', verbose_name='E-book')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.title


class Module(models.Model):
    """Módulo do curso"""
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    title = models.CharField(max_length=200, verbose_name='Título')
    description = models.TextField(verbose_name='Descrição')
    order = models.IntegerField(default=0, verbose_name='Ordem')
    coins_reward = models.IntegerField(default=10, verbose_name='Recompensa em Moedas')
    is_active = models.BooleanField(default=True, verbose_name='Ativo')
    
    class Meta:
        verbose_name = 'Módulo'
        verbose_name_plural = 'Módulos'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.course.title} - {self.title}"


class Unit(models.Model):
    """Unidade dentro de um módulo"""
    module = models.ForeignKey(Module, on_delete=models.CASCADE, related_name='units')
    title = models.CharField(max_length=200, verbose_name='Título')
    video_url = models.URLField(verbose_name='URL do Vídeo')
    activity_url = models.URLField(blank=True, verbose_name='URL da Atividade')
    order = models.IntegerField(default=0, verbose_name='Ordem')
    
    class Meta:
        verbose_name = 'Unidade'
        verbose_name_plural = 'Unidades'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.module.title} - {self.title}"


class ModuleCompletion(models.Model):
    """Registro de conclusão de módulos"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='module_completions')
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['user', 'module']
        verbose_name = 'Conclusão de Módulo'
        verbose_name_plural = 'Conclusões de Módulos'
