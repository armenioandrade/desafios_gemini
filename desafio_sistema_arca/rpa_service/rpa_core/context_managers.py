# ARQUIVO: context_managers.py (Novo Módulo Simulado)

import contextlib

@contextlib.contextmanager
def driver_seguro(nome_driver: str):
    print(f"[{'='*10}] INICIANDO DRIVER {nome_driver} [{'='*10}]")
    
    # Simulação da inicialização do driver:
    driver_object = f"Driver Simulado para {nome_driver}"
    
    try:
        # O 'yield' é onde o controle é passado para o bloco 'with'
        yield driver_object # O valor retornado para o 'as'
    
    except Exception as e:
        print(f"ERRO CATASTRÓFICO DURANTE O USO DO DRIVER: {e}")
        # O código de limpeza no 'finally' ainda rodará!

    finally:
        # Simulação do driver.quit() ou de qualquer código de limpeza
        print(f"[{'='*10}] ENCERRANDO DRIVER {nome_driver} [{'='*10}]")


# ----------------------------------------------------
# 2. TESTE DE EXECUÇÃO: Tente rodar com e sem erro!
# ----------------------------------------------------

if __name__ == "__main__":
    
    # Caso 1: Uso normal (o driver deve ser fechado após o print)
    print("--- CASO 1: EXECUÇÃO COM SUCESSO ---")
    with driver_seguro("Chrome") as driver:
        print(f"RPA está usando: {driver}")
        print("RPA executando consultas...")
    print("FIM do bloco with.\n")

    # Caso 2: Uso que gera erro (o encerramento deve ser garantido, mesmo com o erro)
    print("--- CASO 2: EXECUÇÃO COM ERRO ---")
    try:
        with driver_seguro("Firefox") as driver:
            print(f"RPA está usando: {driver}")
            # Simula um erro grave no meio do RPA
            raise Exception("Página de login não encontrada!")
    except Exception as e:
        print(f"Exceção capturada na Main: {e}")
    print("FIM do bloco with, mesmo com erro.")