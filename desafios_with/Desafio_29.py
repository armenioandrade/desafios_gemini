# Crie uma função chamada escrever_relatorio(nome_arquivo, dados_lista).

# 1. Bloco try (Escrita de Arquivo)
# Use o bloco with open para abrir o nome_arquivo no modo de escrita ('w'). Use o apelido arquivo para o objeto do arquivo.

# Dentro do with e do try, itere sobre a dados_lista (que será uma lista de números) e use arquivo.write() para escrever cada item.

# Regra de Erro: Se algum item na lista for maior que 1000, lance um ValueError("Valor do relatório excede o limite permitido.").

# 2. Bloco except (Capturando Erros)
# Capture o ValueError lançado e imprima: "ERRO NO ARQUIVO: O relatório não foi salvo devido a um valor inválido."

# Capture qualquer TypeError (se a lista tiver um tipo de dado não conversível para string) e imprima: "ERRO NO ARQUIVO: O tipo de dado na lista está incorreto."

# 3. Bloco else (Sucesso)
# Se tudo correr bem, imprima: "Relatório salvo com sucesso em [nome_arquivo]".

# Lembrete: O with open garante que o arquivo seja fechado mesmo se o ValueError ou o TypeError for lançado! Seu foco é na lógica do try/except.

def escrever_relatorio(nome_arquivo, dados_lista):
    # A variável 'dado_int' precisa ser acessível no 'else'
    dado_int = None 
    
    try:
        # Abre o arquivo: o 'with' garante que ele será FECHADO!
        with open(nome_arquivo, 'w') as arquivo: 
            for dado in dados_lista:
                
                # Tenta converter o dado para int. Se falhar (ex: 'dez'), 
                # o Python LANÇA ValueError, que será capturado abaixo.
                dado_int = int(dado) 
                
                # Regra de Erro: Se o valor for maior que 1000
                if dado_int > 1000:
                    # Lança o erro que será capturado pelo bloco except
                    raise ValueError("Valor do relatório excede o limite permitido.")
                
                # Se não houve erro, escreve no arquivo (precisa ser string)
                arquivo.write(str(dado_int) + '\n') 
                
    except ValueError as e:
        # Captura: 1) O 'raise' acima ou 2) int('texto')
        print(f"ERRO NO ARQUIVO: O relatório não foi salvo devido a um valor inválido. Detalhe: {e}")
        
    except TypeError:
        # Captura: Se o dado for um objeto complexo que nem o int() consegue processar (ex: int([1]))
        print("ERRO NO ARQUIVO: O tipo de dado na lista está incorreto.")
        
    except Exception as e:
        # Boa Prática: Captura qualquer outro erro inesperado.
        print(f"ERRO DESCONHECIDO: {e}")
        
    else:
        # CORREÇÃO 1: Executa APENAS se o TRY for 100% bem-sucedido
        print(f"Relatório salvo com sucesso em {nome_arquivo}")

# --- Testes de Cenário ---

# Cenário 1: Sucesso
escrever_relatorio('relatorio_sucesso.txt', [10, 500, 999])

# Cenário 2: Erro de Valor (raise)
escrever_relatorio('relatorio_valor_alto.txt', [10, 1001, 500])

# Cenário 3: Erro de Valor (int() falha)
escrever_relatorio('relatorio_texto.txt', [10, 'quinhentos', 500])

# Cenário 4: Erro de Tipo (lista com lista)
escrever_relatorio('relatorio_tipo.txt', [10, [20], 30])