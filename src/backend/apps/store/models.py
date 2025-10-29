from django.db import models
from apps.users.models import User


class StoreItem(models.Model):
    """Itens disponíveis na loja de gamificação"""
    ITEM_TYPE_CHOICES = [
        ('badge', 'Selo'),
        ('avatar_effect', 'Efeito de Avatar'),
        ('font', 'Fonte Personalizada'),
    ]
    
    name = models.CharField(max_length=100, verbose_name='Nome')
    description = models.TextField(verbose_name='Descrição')
    item_type = models.CharField(max_length=20, choices=ITEM_TYPE_CHOICES)
    price = models.IntegerField(verbose_name='Preço em Moedas')
    image = models.ImageField(upload_to='store/items/', verbose_name='Imagem')
    is_available = models.BooleanField(default=True, verbose_name='Disponível')
    
    class Meta:
        verbose_name = 'Item da Loja'
        verbose_name_plural = 'Itens da Loja'
    
    def __str__(self):
        return f"{self.name} ({self.price} moedas)"


class Purchase(models.Model):
    """Registro de compras dos usuários"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchases')
    item = models.ForeignKey(StoreItem, on_delete=models.CASCADE)
    purchased_at = models.DateTimeField(auto_now_add=True)
    is_equipped = models.BooleanField(default=False, verbose_name='Equipado')
    
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        unique_together = ['user', 'item']
    
    def __str__(self):
        return f"{self.user.nickname} - {self.item.name}"
