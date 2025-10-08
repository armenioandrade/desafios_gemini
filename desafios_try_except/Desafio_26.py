# Crie duas partes: uma classe Pedido e uma função registrar_compra.

# 1. Classe Componente: Pedido
# Construtor: Recebe _quantidade. (Use o setter na inicialização).

# Propriedade (@property e @setter): quantidade

# Setter:

# Deve garantir que a quantidade seja um inteiro. Se não for, lance um TypeError("A quantidade deve ser um número inteiro.").

# Deve garantir que a quantidade seja maior que zero. Se for 0 ou negativo, lance um ValueError("A quantidade deve ser maior que zero.").

# Se passar nas duas validações, atribua a self._quantidade.

# 2. Função Principal: registrar_compra(valor_entrada)
# Esta função deve encapsular o processo de criação de um pedido.

# Bloco try:

# Tente criar uma instância de Pedido usando o valor_entrada como quantidade.

# Se for bem-sucedido, imprima: "Pedido registrado com sucesso. Quantidade: [valor]"

# Bloco except:

# Capture dois tipos de exceção: TypeError e ValueError.

# Para ambos os tipos, imprima uma mensagem genérica de falha: "Falha ao registrar pedido: O valor fornecido é inválido ou de um tipo incorreto."

# Testes a Serem Realizados:
# registrar_compra(5) → Sucesso (Entra no try/else).

# registrar_compra("dez") → Erro (O Pedido.__init__ lança TypeError ou ValueError dependendo de como você faz a checagem).

# registrar_compra(-2) → Erro (O setter lança ValueError).

class Relatorio():
    total_relatorios_criados = 0

    def __init__(self, titulo):
        self.titulo = titulo
        self.total_relatorios_criados += 1
    
    @staticmethod
    def gerar_identificador(titulo):
        return f'ID_{titulo}'.upper().replace(' ', '')

    @classmethod
    def criar_relatorio_padrao(cls, ano):
        titulo = f'Relatorio Anual {ano}'
        return cls(titulo)
    
    def imprimir_info(self):
        return f'titulo: {self.titulo} - {self.gerar_identificador(self.titulo)} - {self.total_relatorios_criados}'
    
rel1 = Relatorio.criar_relatorio_padrao('rel1')
print(rel1.imprimir_info())