# Círculo Dinâmico (Propriedade de Cálculo)
# Crie uma classe chamada Circulo.

# Construtor: Recebe e inicializa o atributo _raio.

# Propriedade (@property): Crie um método area.

# Este método não precisa de um setter.

# Ele deve calcular e retornar a área do círculo usando π≈3.14 e o raio (self._raio).

# Objetivo: A area deve ser acessada como se fosse um atributo (circulo.area), mas o valor é calculado dinamicamente toda vez que é lido.

class Circulo():

    def __init__(self, raio):
        self._raio = raio

    @property
    def area(self):
        return self._raio ** 2 * 3.14
    
        