# ARQUIVO: rpa_core/views.py (Ajustado)

from django.http import JsonResponse
from django.views.decorators.http import require_POST
# NOVO IMPORT DE SEGURANÇA:
from django.views.decorators.csrf import csrf_exempt 

from .tasks import disparar_download_xml, consultar_ie_no_db 

# ----------------------------------------------------------------------
# A nova ordem de Decorators
# 1. @csrf_exempt: Desativa a proteção CSRF para esta função (Permite POST puro de APIs)
# 2. @require_POST: Garante que só aceita POST, mantendo o método seguro
@csrf_exempt
@require_POST
def iniciar_rpa_remoto(request):
    """
    Função de API que recebe a requisição e dispara o RPA em background (simulado).
    """
    print("API: Requisição de execução recebida no Django.")
    
    # Simulação de captura do usuário que disparou a requisição (viria do request)
    usuario_executor = "AdminWeb" 
    
    try:
        # 1. Consulta ao Banco (seu código ORM)
        ies_para_processar = consultar_ie_no_db()
        
        # 2. Disparo do RPA (Na vida real, usaria .delay() de Celery/Worker)
        # Passamos o nome do usuário para o log.
        disparar_download_xml(ies_para_processar, usuario=usuario_executor) 
        
        # 3. Retorno Imediato: Converte o dicionário Python em uma resposta JSON.
        return JsonResponse({
            "status": "SUCESSO", 
            "mensagem": f"RPA iniciado com sucesso para {len(ies_para_processar)} clientes.",
            "task_id": "SIMULADO_12345"
        }, status=200)
        
    except Exception as e:
        # Retorno de erro formatado
        return JsonResponse({
            "status": "ERRO", 
            "mensagem": f"Falha interna ao iniciar RPA: {str(e)}",
            "detalhe": "Verifique o log do servidor."
        }, status=500)