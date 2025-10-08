# Crie duas classes: ItemBiblioteca e DVD.

# 1. Classe Base: ItemBiblioteca
# Atributos: título e ano_publicacao.

# Métodos: Um __init__ para inicializar os atributos.

# 2. Classe Derivada: DVD
# Esta classe deve herdar de ItemBiblioteca.

# Atributo Adicional: duracao (em minutos).

# Métodos:

# Um __init__ que chama o construtor da classe base (super().__init__) e também inicializa a duração.

# Um método informacoes que retorna uma string com o título, ano de publicação e a duração do DVD.

# O desafio aqui é aplicar a herança de forma eficaz.

class ItemBiblioteca():
    

    def __init__(self, titulo, ano_publicacao):
        self.titulo = titulo
        self.ano_publicacao = int(ano_publicacao)
    

class DVD(ItemBiblioteca):

    
    def __init__(self, titulo, ano_publicacao, duracao):
        super().__init__(titulo, ano_publicacao)
        self.duracao = int(duracao)

    def informacoes(self):
        return f'{self.titulo}, {self.ano_publicacao}, {self.duracao}'

dvd_filme_top_gun = DVD('top gun', 2024, 240)

print(dvd_filme_top_gun.informacoes())