import os
import re

def renomear_arquivos_sequencial(diretorio, prefixo_novo='desafio_', extensao_alvo='.py'):
    """
    Renomeia arquivos em um diretório de forma sequencial, mantendo a extensão.

    Args:
        diretorio (str): O caminho completo para o diretório (pasta) dos arquivos.
        prefixo_novo (str): O prefixo para o novo nome do arquivo (ex: 'desafio_').
        extensao_alvo (str): A extensão dos arquivos a serem renomeados (ex: '.py').
                             A busca diferencia maiúsculas de minúsculas.
    """
    print(f"--- Iniciando renomeação no diretório: {diretorio} ---")

    # 1. Obter a lista de todos os arquivos/pastas no diretório
    try:
        itens = os.listdir(diretorio)
    except FileNotFoundError:
        print(f"ERRO: O diretório '{diretorio}' não foi encontrado.")
        return
    except Exception as e:
        print(f"ERRO ao acessar o diretório: {e}")
        return

    # 2. Filtrar apenas os arquivos que terminam com a extensão desejada e garantir que seja um arquivo
    arquivos_para_renomear = []
    for item in itens:
        caminho_completo = os.path.join(diretorio, item)
        # Verifica se é um arquivo E se termina com a extensão alvo
        if os.path.isfile(caminho_completo) and item.endswith(extensao_alvo):
            arquivos_para_renomear.append(item)

    if not arquivos_para_renomear:
        print(f"Nenhum arquivo encontrado com a extensão '{extensao_alvo}' para renomear.")
        return

    # 3. Ordenar os arquivos. Isso é importante para que a numeração sequencial faça sentido.
    arquivos_para_renomear.sort()

    print(f"Foram encontrados {len(arquivos_para_renomear)} arquivos para renomear.")

    # 4. Iniciar o processo de renomeação sequencial
    contador = 1
    for nome_antigo in arquivos_para_renomear:
        # Construir o novo nome (ex: desafio_1.py)
        novo_nome = f"{prefixo_novo}{contador}{extensao_alvo}"

        # Criar os caminhos completos
        caminho_antigo = os.path.join(diretorio, nome_antigo)
        caminho_novo = os.path.join(diretorio, novo_nome)

        # 5. Renomear o arquivo
        try:
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: '{nome_antigo}' para '{novo_nome}'")
            contador += 1
        except Exception as e:
            print(f"AVISO: Não foi possível renomear '{nome_antigo}'. Erro: {e}")

    print("--- Renomeação concluída! ---")

# --- Exemplo de Uso (Configurações que você pode ajustar) ---
# ATENÇÃO: Substitua 'C:\\desafios_python\\poo' pelo caminho real da sua pasta.
CAMINHO_DO_DIRETORIO = r'C:\Users\armen\poo_python\desafios_gemini\desafios_poo_simples' 
NOVO_PREFIXO = 'desafio_' # O prefixo do novo nome
EXTENSAO = '.py' # A extensão dos arquivos a serem renomeados

# Chamada da função com os seus parâmetros
renomear_arquivos_sequencial(CAMINHO_DO_DIRETORIO, NOVO_PREFIXO, EXTENSAO)