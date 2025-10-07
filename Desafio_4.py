# Crie duas classes: Pessoa e Funcionario.

# 1. Classe Base: Pessoa
# Atributos: nome e idade.

# Métodos: Um __init__ para inicializar os atributos.

# 2. Classe Derivada: Funcionario
# Deve herdar de Pessoa.

# Atributo Adicional: salario.

# Métodos:

# Um __init__ que inicializa o nome e a idade usando super(), e o salario diretamente.

# Um método apresentar que retorna uma string dizendo: "Olá, meu nome é [nome], tenho [idade] anos e meu salário é R$[salario]."

# O foco aqui é na correta passagem de parâmetros via super() e na adição de um método próprio.

class Pessoa():

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = int(idade)

class Funcionario(Pessoa):
    
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = float(salario)

    def apresentar(self):
        return f'Olá meu nome é {self.nome}, tenho {self.idade} anos e meu salário é R${self.salario}'

armenio = Funcionario('armenio', 35, 8999)
print(armenio.apresentar())