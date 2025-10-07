# Desafio 7: Composição de um Computador
# Crie três classes: CPU, Memoria e Computador.

# O objetivo é que a classe Computador utilize instâncias das outras classes como seus atributos, em vez de herdar delas.
# 1. Classe Componente: CPU
# Atributo: nucleos (número inteiro).

# Método: Um __init__ para inicializar.

# Método: processar que retorna uma string: "CPU de [nucleos] núcleos processando dados."

# 2. Classe Componente: Memoria
# Atributo: tamanho_gb (número inteiro).

# Método: Um __init__ para inicializar.

# Método: acessar_dados que retorna uma string: "Memória de [tamanho_gb]GB acessando dados."

# 3. Classe Principal: Computador
# Atributos:

# cpu: Será uma instância da classe CPU.

# memoria: Será uma instância da classe Memoria.

# Método: Um __init__ que recebe o número de núcleos e o tamanho da memória. Dentro deste __init__, você deve instanciar e atribuir os objetos CPU e Memoria aos atributos correspondentes.

# Método: ligar que chama e retorna o resultado dos métodos processar da CPU e acessar_dados da Memoria, combinando-os em uma única string formatada.

# O desafio aqui é gerenciar o ciclo de vida dos objetos componentes (CPU e Memoria) dentro do objeto principal (Computador).

# Boa sorte! Avise-me quando terminar!

class CPU():

    def __init__(self, nucleos):
        self.nucleos = nucleos

    def processar(self):
        return f'CPU de {self.nucleos} núcleos processando dados.'

class Memoria():

    def __init__(self, tamanho_gb):
        self.tamanho_gb = tamanho_gb
    
    def acessar_dados(self):
        return f'Memória de {self.tamanho_gb} acessando dados.'
    
class Computador():

    def __init__(self, nucleos, memoria):
        self.cpu = CPU(nucleos)
        self.memoria = Memoria(memoria)
    
    def ligar(self):
        return f'Ligando pc...\n{self.cpu.processar()}\n{self.memoria.acessar_dados()}'

dell = Computador(4,16)
print(dell.ligar())