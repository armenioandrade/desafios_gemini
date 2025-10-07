# Desafio 6: Veículos (Herança de Múltiplos Níveis)
# Crie três classes em níveis: Veiculo, Carro e CarroEletrico.

# 1. Classe Base: Veiculo
# Atributos: marca e modelo.

# Métodos: __init__ para inicializar.

# 2. Classe Intermediária: Carro
# Deve herdar de Veiculo.

# Atributo Adicional: portas (número de portas).

# Métodos: __init__ para inicializar a marca e modelo via super(), e as portas diretamente.

# 3. Classe Derivada Final: CarroEletrico
# Deve herdar de Carro.

# Atributo Adicional: autonomia (em km).

# Métodos:

# Um __init__ que chama o construtor do Carro (que, por sua vez, chamará o de Veiculo), e inicializa a autonomia.

# Um método detalhes que retorna uma string com Marca, Modelo, Portas e Autonomia.

# Este desafio testa a capacidade de encadeamento de construtores em uma hierarquia de classes.

class Veiculo():

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

class Carro(Veiculo):
    
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = int(portas)

class CarroEletrico(Carro):

    def __init__(self, marca, modelo, portas, autonomia):
        super().__init__(marca, modelo, portas)
        self.autonomia = int(autonomia)

    def detalhes(self):
        return f'{self.marca}, {self.modelo}, {self.portas}, {self.autonomia}'

byd_dolphin = CarroEletrico('byd', 'dolphin', 4, 400)
print(byd_dolphin.detalhes())
