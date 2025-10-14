# ARQUIVO: rpa_core/urls.py

from django.urls import path
from . import views # Importa as funções que você colocou em views.py

urlpatterns = [
    # Esta rota completa será: /api/iniciar/
    path('iniciar/', views.iniciar_rpa_remoto, name='iniciar_rpa'),
]