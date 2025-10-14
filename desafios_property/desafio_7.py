# Crie um sistema simples com duas classes: Sensor e Alarme.

# 1. Classe Componente: Sensor
# Esta classe monitora um valor.

# Construtor (__init__): Recebe e inicializa o atributo _temperatura.

# Propriedade (@property e @setter): temperatura

# Getter: Retorna self._temperatura.

# Setter: Deve garantir que a temperatura não seja menor que zero (0). Se for, lance um ValueError. Caso contrário, atribua a self._temperatura.

# 2. Classe Principal: Alarme
# Esta classe usa o sensor e define o estado do sistema.

# Construtor (__init__):

# Cria uma instância de Sensor com uma temperatura inicial (ex: 20). Esta é a Composição.

# Inicializa self.status como 'Desativado'.

# Método de Instância: verificar_alerta(limite)

# Este método deve:

# Acessar a temperatura do objeto Sensor (Composição).

# Se a temperatura do sensor for maior que o limite fornecido, mude o self.status do alarme para 'ALERTA - Temperatura Alta!'.

# Retorne o novo estado (self.status).

class Sensor():

    def __init__(self, temperatura):
        self.temperatura = temperatura

    @property
    def temperatura(self):
        return self._temperatura
    
    @temperatura.setter
    def temperatura(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Temperatura não pode ser inferior a zero.")
        self._temperatura = novo_valor

class Alarme():

    def __init__(self):
        self.sensor = Sensor(20)
        self.status = 'Desativado'
    
    def verificar_alerta(self, limite):
        temperatura_atual = self.sensor.temperatura
        if temperatura_atual > limite:
            self.status = 'ALERTA - Temperatura Alta!'
            return self.status