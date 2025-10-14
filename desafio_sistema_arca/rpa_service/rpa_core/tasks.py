import time
from .models import Cliente
from .decorators import log_execucao

def consultar_ie_no_db():
    model = Cliente
    ie = model.objects.all()
    lista_inscricoes = ie.values_list('inscricao_estadual', flat=True)
    return list(lista_inscricoes)

@log_execucao
def disparar_download_xml(ie_lista: list, usuario: str = "Sistema"):
    print(f"RPA processando {len(ie_lista)} IEs para o usuário: {usuario}")
    
    for ie in ie_lista:
        print(f"  -> Consultando IE: {ie}")
        time.sleep(0.1) # Simula o trabalho
        
    return f"Download XML concluído para {len(ie_lista)} IEs."