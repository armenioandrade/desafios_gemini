# Crie uma classe chamada Processador. Esta classe será um container de funções úteis e não precisa ter atributos de instância.

# 1. Método Estático (@staticmethod)
# Crie um método estático chamado limpar_texto.

# Ele deve receber uma string de entrada (texto).

# Deve remover todos os espaços em branco no início e no fim da string (usando o método .strip()).

# 2. Método de Classe (@classmethod)
# Crie um método de classe chamado processar_dados.

# Ele deve receber uma lista de strings sujas (lista_suja).

# O método deve iterar sobre a lista e chamar o método estático limpar_texto para limpar cada item.

# Deve retornar a nova lista de strings limpas.

# Dica: Lembre-se de que o @classmethod recebe cls. Você deve usar cls.limpar_texto(item) para chamar o método estático.

# 3. Exemplo de Uso Esperado:
# Python

# dados = ["  dado 1 ", " dado 2  ", "dado 3 "]
# limpos = Processador.processar_dados(dados)
# print(limpos) 
# # Saída esperada: ['dado 1', 'dado 2', 'dado 3']
# Foque na comunicação: o @classmethod (o gerente) chama o @staticmethod (o trabalhador) para fazer a tarefa.

class Processador():

    @staticmethod
    def limpar_texto(texto):
        return texto.strip()
    
    @classmethod
    def processar_dados(cls, lista_suja):
        lista_limpa = []
        for item in lista_suja:
            lista_limpa.append(cls.limpar_texto(item))
        return lista_limpa

dados = ["  dado 1 ", " dado 2  ", "dado 3 "]
limpos = Processador.processar_dados(dados)
print(limpos)