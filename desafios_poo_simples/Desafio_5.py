# Crie três classes: Forma, Retangulo e Circulo.

# 1. Classe Base: Forma
# Métodos:

# Um método area que deve retornar 0 ou lançar um erro (indicando que a classe base não tem uma área definida).

# Um método perimetro que também retorna 0 ou lança um erro.

# 2. Classe Derivada: Retangulo
# Deve herdar de Forma.

# Atributos: largura e altura.

# Métodos: Sobrescreva (override) os métodos area e perimetro para calcular corretamente a área e o perímetro de um retângulo.

# 3. Classe Derivada: Circulo
# Deve herdar de Forma.

# Atributo: raio.

# Métodos: Sobrescreva (override) os métodos area e perimetro para calcular corretamente a área e o perímetro de um círculo. (Você pode usar π≈3.14 ou importar math.pi).

# O foco aqui é em Polimorfismo, onde classes diferentes (Retângulo e Círculo) implementam a mesma interface (area e perimetro) de maneiras diferentes.

class Forma():
    
    def area(self):
        return 0
    def perimetro(self):
        return 0

class Retangulo(Forma):
    ...
    def __init__(self, altura, largura):
        self.altura = altura
        self.largura = largura

    def area(self):
        return self.altura * self.largura
    
    def perimetro(self):
        return 2 * (self.altura + self.largura)

class Circulo(Forma):
    ...
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * self.raio ** 2
    
    def perimetro(self):
        return 2 * 3.14 * self.raio


forma = Forma()
print(f'perimetro {forma.perimetro()}, area {forma.area()}')

papel = Retangulo(2, 3)
print(f'perimetro {papel.perimetro()}, area {papel.area()}')

prato = Circulo(2)
print(f'perimetro {prato.perimetro()}, area {prato.area()}')
