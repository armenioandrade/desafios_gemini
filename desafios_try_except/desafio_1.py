# Crie uma função chamada processar_idade(idade_str).

# 1. Bloco try (O Código Suspeito)
# Dentro do try, você deve:

# Tentar converter a idade_str (string) para um inteiro (int).

# Verificar se esse número é negativo. Se for, lance um ValueError("A idade não pode ser negativa.").

# 2. Blocos except (Gerenciando os Erros)
# Você deve ter dois blocos except específicos:

# Captura de ValueError: Se um ValueError for lançado (seja pela conversão ou pela sua validação), imprima: "Erro de Valor: A idade fornecida é inválida (negativa ou formato incorreto).".

# Lembre-se: int("texto") lança ValueError.

# Captura de TypeError: Se a função receber algo que não seja uma string (ex: uma lista), imprima: "Erro de Tipo: A entrada não é uma string válida para conversão.".

# 3. Bloco else (Execução Limpa)
# Se nenhuma exceção for lançada (idade válida e positiva), imprima: "Sucesso! Idade processada: [idade]".

def processar_idade(idade_str):
    try:
        idade_int = int(idade_str)
        if idade_int < 0:
            raise ValueError('Idade não pode ser negativa')
    except ValueError:
        print('erro de valor: a idade fornecida é inválida (negativa ou formato incorreto)')
    except TypeError:
        print('erro de tipo: a entrada não é uma string válida para conversão')
    else:
        print(f'Sucesso! Idade processada: [{idade_int}]')

# lista = {}
# processar_idade(lista)

# idade = -8
# processar_idade(idade)

# idade = 18
# processar_idade(idade)