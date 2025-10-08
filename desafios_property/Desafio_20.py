# Crie um pequeno sistema de gerenciamento para uma biblioteca que utilize a Composição e o @property.

# Crie duas classes: Item (o componente) e Biblioteca (o objeto principal).

# 1. Classe Componente: Item
# Esta classe representará um livro ou revista na biblioteca.

# Construtor (__init__): Recebe titulo e _copias_disponiveis.

# Propriedade (@property e @setter): copias_disponiveis

# Getter: Retorna self._copias_disponiveis.

# Setter:

# Deve garantir que o novo valor seja inteiro.

# Deve garantir que o novo valor não seja negativo.

# Se a validação falhar, lance ValueError ou TypeError.

# 2. Classe Principal: Biblioteca
# Esta classe gerencia a coleção de itens.

# Construtor (__init__): Inicializa um dicionário vazio chamado self.acervo. O acervo usará o título do item como chave e o objeto Item (a instância) como valor.

# Método de Instância: adicionar_item(titulo, copias)

# Cria uma nova instância de Item(titulo, copias) e armazena-a no self.acervo.

# Método de Instância: emprestar_item(titulo)

# Verifica se o titulo está no acervo. Se não estiver, retorna: "Item não encontrado."

# Se estiver, usa o setter de copias_disponiveis para diminuir em 1 a quantidade de cópias daquele item.

# Retorna: "Empréstimo realizado com sucesso."

# Método de Classe (@classmethod): horario_padrao(cls)

# Retorna uma string simples com o horário de funcionamento padrão: "Funcionamento: Segunda a Sexta, 9:00 - 18:00".


class Item:
    def __init__(self, titulo, copias):
        self.titulo = titulo
        # Chama o setter para validar as cópias iniciais
        self.copias_disponiveis = copias
        
    @property
    def copias_disponiveis(self):
        return self._copias_disponiveis
    
    @copias_disponiveis.setter
    def copias_disponiveis(self, novo_valor):
        
        # 1. Validação de Tipo
        if not isinstance(novo_valor, int):
            raise TypeError("O número de cópias deve ser um número inteiro.")
            
        # 2. Validação de Valor
        if novo_valor < 0:
            raise ValueError("O número de cópias não pode ser negativo.")
            
        # Atribuição segura ao atributo privado
        self._copias_disponiveis = novo_valor

    # Para fins de teste, adicionamos um método de descrição
    def __str__(self):
        return f"'{self.titulo}' | Cópias: {self.copias_disponiveis}"

class Biblioteca:
    def __init__(self):
        # Composição: armazena objetos Item neste dicionário
        self.acervo = {} 
    
    @classmethod
    def horario_padrao(cls):
        # Método que não usa self nem cls, apenas um valor constante
        return "Funcionamento: Segunda a Sexta, 9:00 - 18:00"
    
    def adicionar_item(self, titulo, copias):
        # Cria uma instância de Item (Composição)
        novo_item = Item(titulo, copias) 
        # Armazena o objeto no acervo
        self.acervo[titulo] = novo_item
        return f"Item '{titulo}' adicionado ao acervo."
    
    def emprestar_item(self, titulo):
        # 1. Checagem de Existência
        if titulo not in self.acervo:
            return "Item não encontrado."
            
        item = self.acervo[titulo]
        
        # 2. Checagem de Disponibilidade
        if item.copias_disponiveis < 1:
            return f"Empréstimo negado. '{titulo}' está esgotado."
            
        # 3. Delegação e Uso do SETTER do Item
        # Ao atribuir, chamamos o @copias_disponiveis.setter do objeto Item!
        item.copias_disponiveis -= 1 
        
        return f"Empréstimo realizado com sucesso. Cópias restantes de '{titulo}': {item.copias_disponiveis}"