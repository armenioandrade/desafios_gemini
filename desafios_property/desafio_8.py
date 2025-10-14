# Crie um sistema para um controle remoto que gerencia o volume de uma TV.

# 1. Classe Componente: Volume
# Esta classe representa o nível do volume.

# Construtor (__init__): Recebe e inicializa o atributo _nivel.

# Propriedade (@property e @setter): nivel

# Getter: Retorna self._nivel.

# Setter:

# Deve garantir que o novo valor esteja entre 0 e 100 (incluído).

# Se o valor for menor que 0, atribua 0. Se for maior que 100, atribua 100.

# Caso contrário, atribua o novo_valor a self._nivel.

# 2. Classe Principal: Controle
# Esta classe usa o componente Volume.

# Construtor (__init__):

# Cria uma instância de Volume com um nível inicial (ex: 50). Esta é a Composição.

# Inicializa self.status_tv como 'Ligada'.

# Método de Instância: aumentar_volume()

# Este método deve:

# Acessar o nível atual do objeto Volume.

# Usar o setter de Volume para aumentar o nível em 5.

# Retornar o novo nível.

# Método de Instância: diminuir_volume()

# Este método deve:

# Acessar o nível atual do objeto Volume.

# Usar o setter de Volume para diminuir o nível em 5.

# Retornar o novo nível.

class Volume():
    
    def __init__(self, nivel):
        self._nivel = nivel
    
    @property
    def nivel(self):
        return self._nivel
    
    @nivel.setter
    def nivel(self, novo_valor):
        if novo_valor < 0:
            self._nivel = 0
        elif novo_valor > 100:
            self._nivel = 100
        else:
            # Se estiver dentro do limite (0 a 100), define o valor
            self._nivel = novo_valor
        
    def __str__(self):
        return f'Nível: {self._nivel}'

class Controle():

    def __init__(self, status_tv='Ligada'):
        self.volume = Volume(50) 
        self.status_tv =status_tv
    
    def aumentar_volume(self):
        # LÊ o nível atual, SOMA 5, e ATRIBUI (chamando o SETTER)
        self.volume_inicial.nivel += 5 
        # Retorna o nível usando o GETTER
        return self.volume_inicial.nivel 
    
    def diminuir_volume(self):
        self.volume_inicial._nivel -= 5
        return self.volume_inicial._nivel
    
    def __str__(self):
        return f'Sua TV está {self.status_tv} e o volume atual é {self.volume_inicial._nivel}'
    

meu_controle = Controle()
print(meu_controle)
meu_controle.aumentar_volume()
print(meu_controle)
meu_controle.diminuir_volume()
print(meu_controle)