"""
Configuração do Celery para o projeto OBRIA
"""
import os
from celery import Celery

# Define as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

app = Celery('obria')

# Carrega as configurações do Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Autodescobre tasks nos apps
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
