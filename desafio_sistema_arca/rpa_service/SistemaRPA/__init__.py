# ARQUIVO: SistemaRPA/__init__.py

# Importa a instância do Celery para que ela seja carregada quando o Django iniciar
from .celery import app as celery_app