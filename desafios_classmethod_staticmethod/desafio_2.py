# Crie uma classe chamada Conversor. Esta classe será um container de funções e não terá atributos de instância.

# Método Estático (@staticmethod):

# Crie celsius_para_fahrenheit(celsius).

# Ele deve receber a temperatura em Celsius e retornar a conversão usando a fórmula: F=C×1.8+32.

# Método Estático (@staticmethod):

# Crie fahrenheit_para_celsius(fahrenheit).

# Ele deve receber a temperatura em Fahrenheit e retornar a conversão usando a fórmula: C=(F−32)/1.8.

# O foco aqui é apenas no uso do @staticmethod para funções utilitárias.

class Conversor():

    @staticmethod
    def celsius_para_fahrenheit(celsius):
        f = celsius * 1.8 + 32
        return f
    
    @staticmethod
    def fahrenheit_para_celsius(fahrenheit):
        c = (fahrenheit-32)/1.8
        return c