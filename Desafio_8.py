from datetime import datetime

class Tarefa():
    
    # 1. Construtor Padrão (Método de Instância)
    def __init__(self, nome, status='pendente'):
        # 'self' referencia a instância que está sendo criada.
        self.nome = nome
        self.status = status
    
    # 2. Construtor Alternativo (Método de Classe)
    @classmethod
    def criar_concluida(cls, nome):
        # 'cls' referencia a própria CLASSE Tarefa.
        # cls(nome, 'concluída') é o mesmo que chamar Tarefa(nome, 'concluída').
        # Ele retorna uma nova instância JÁ inicializada.
        return cls(nome, 'concluída')

    # 3. Função Utilitária (Método Estático)
    @staticmethod
    def data_atual():
        # NÃO recebe self (instância) nem cls (classe). 
        # É uma função genérica que vive na classe.
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 4. Método de Instância
    def detalhes(self):
        # 'self' permite acessar os atributos da instância
        data = self.data_atual() # Chama o método estático usando a instância (ou Tarefa.data_atual())
        return f'{self.nome} - Status: {self.status} (Data: {data})'
    
    def __str__(self):
        return f'Tarefa: {self.nome} | Status: {self.status}'

# --- USOS E PORQUÊS ---

# Uso 1: Construtor Padrão
# 'task_pendente' é a instância, e o 'self' dentro do __init__ refere-se a ela.
task_pendente = Tarefa('Comprar pão') 
print(task_pendente.detalhes()) 
# Saída: Comprar pão - Status: pendente (Data: 2025-...)

# Uso 2: Construtor Alternativo
# Chamamos o método pela CLASSE. Ele usa 'cls' para criar a instância.
task_concluida = Tarefa.criar_concluida('Finalizar projeto POO')
print(task_concluida.detalhes()) 
# Saída: Finalizar projeto POO - Status: concluída (Data: 2025-...)