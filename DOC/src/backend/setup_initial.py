"""
Script de setup inicial do projeto
Execute este script após a primeira instalação para criar estrutura básica
"""
import os
import sys
import django

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from django.contrib.auth import get_user_model
from apps.challenges.models import Challenge
from apps.courses.models import Course, Module, Unit
from apps.store.models import StoreItem

User = get_user_model()


def create_admin_user():
    """Cria usuário administrador padrão"""
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser(
            username='admin',
            nickname='Administrador',
            email='admin@obria.com',
            password='admin123',
            user_type='admin'
        )
        print('✓ Usuário administrador criado')
        print('  Username: admin')
        print('  Password: admin123')
    else:
        print('✓ Usuário administrador já existe')


def create_sample_store_items():
    """Cria itens de exemplo na loja"""
    items = [
        {
            'name': 'Selo de Bronze',
            'description': 'Selo de conquista nível bronze',
            'item_type': 'badge',
            'price': 50
        },
        {
            'name': 'Selo de Prata',
            'description': 'Selo de conquista nível prata',
            'item_type': 'badge',
            'price': 100
        },
        {
            'name': 'Selo de Ouro',
            'description': 'Selo de conquista nível ouro',
            'item_type': 'badge',
            'price': 200
        },
        {
            'name': 'Efeito Brilho',
            'description': 'Adiciona brilho ao avatar',
            'item_type': 'avatar_effect',
            'price': 75
        },
        {
            'name': 'Fonte Futurista',
            'description': 'Fonte personalizada para nickname',
            'item_type': 'font',
            'price': 150
        },
    ]
    
    created = 0
    for item_data in items:
        if not StoreItem.objects.filter(name=item_data['name']).exists():
            StoreItem.objects.create(**item_data)
            created += 1
    
    if created > 0:
        print(f'✓ {created} itens criados na loja')
    else:
        print('✓ Itens da loja já existem')


def main():
    print('Configurando projeto OBRIA...\n')
    
    create_admin_user()
    print()
    
    create_sample_store_items()
    print()
    
    print('✓ Setup concluído!')
    print('\nPróximos passos:')
    print('1. Execute: python manage.py runserver')
    print('2. Acesse: http://localhost:8000/admin')
    print('3. API Docs: http://localhost:8000/api/docs/')


if __name__ == '__main__':
    main()
