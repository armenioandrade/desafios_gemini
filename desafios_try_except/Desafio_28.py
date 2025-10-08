# Crie uma função chamada tentar_login(senha) que simula um processo de autenticação.

# 1. Bloco try (Onde o Erro é Gerado)
# Dentro do try, verifique se a senha é a string "12345".

# Se a senha não for "12345", lance um PermissionError (um erro comum em segurança) com uma mensagem clara: raise PermissionError("A senha está incorreta.").

# Se a senha estiver correta, imprima: "Autenticação bem-sucedida."

# 2. Bloco except (Captura e Inspeção)
# Capture o PermissionError e use a sintaxe as e para pegar a mensagem de erro.

# Imprima a mensagem de erro que você gerou, formatada assim: "FALHA NO LOGIN: [Mensagem de erro gerada]".

# 3. Bloco finally (Ação Garantida)
# O bloco finally deve sempre ser executado, independentemente do sucesso ou falha.

# Imprima: "Conexão com o servidor encerrada."

def tentar_login(senha):
    try:
        if senha == '12345':
            print('Autenticação bem sucedida')
        else:
            raise PermissionError('Senha incorreta!')
    except PermissionError as p:
        print('FALHA NO LOGIN: ',p)
    finally:
        print('conexão com servidor encerrada')


tentar_login('12345')