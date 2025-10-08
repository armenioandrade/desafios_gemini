# Crie uma classe chamada Livro.

# Atributos: Deve ter atributos para título, autor, e páginas.

# Métodos:

# Um método __init__ para inicializar o livro com o título e o autor fornecidos, e as páginas como um número inteiro.

# Um método chamado descricao que retorna uma string formatada com o título e o autor do livro.

class Livro():

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = int(paginas)

    def descricao(self):
        return f'titulo: {self.titulo} autor: {self.autor}'

livro_alice = Livro('Alice no país das maravilhas', 'Lewis Carrot', 1000)
print(livro_alice.descricao())