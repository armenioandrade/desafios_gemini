# ARQUIVO: decorators.py

import functools # Módulo essencial para manipular funções

def log_execucao(func):
    """
    Decorator que adiciona logs de início e fim.
    """
    
    # A MÁGICA ACONTECE AQUI:
    # O @functools.wraps(func) diz ao Python: "A função 'wrapper' 
    # está substituindo 'func', então copie todos os metadados 
    # (nome, docstring, argumentos) de 'func' para 'wrapper'."
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # Passo 1: Imprime a mensagem de INÍCIO
        print(f"[{'='*15} LOG INÍCIO {'='*15}]")
        print(f"Função '{func.__name__}' iniciada.")
        
        # Passo 2: Executa a função original
        resultado = func(*args, **kwargs)
        
        # Passo 3: Imprime a mensagem de FIM
        print(f"Função '{func.__name__}' concluída com sucesso.")
        print(f"[{'='*15} LOG FIM {'='*15}]")
        
        return resultado
    
    # Retorna a função wrapper (que agora tem a identidade da função original)
    return wrapper