# ARQUIVO: SistemaRPA/celery.py

import os
from celery import Celery

# Define o módulo de configurações padrão do Django para o 'celery'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SistemaRPA.settings')

# Cria a instância do Celery e dá um nome
app = Celery('SistemaRPA')

# Carrega as configurações do Django (CELERY_BROKER_URL, etc.)
app.config_from_object('django.conf:settings', namespace='CELERY')

# Descobre tarefas automaticamente nos apps instalados (como o rpa_core)
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')