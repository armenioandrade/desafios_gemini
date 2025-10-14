# Crie uma classe chamada Relatorio.

# 1. Atributo de Classe (Contagem Global)
# Crie um atributo de classe chamado total_relatorios_criados e inicialize-o com 0.

# 2. Construtor Padrão (__init__)
# Atributo de Instância: titulo.

# No __init__, incremente o atributo de classe total_relatorios_criados em 1.

# 3. Método Estático (@staticmethod)
# Crie um método estático chamado gerar_identificador.

# Ele deve receber o título do relatório.

# Deve retornar uma string em maiúsculas com a palavra "ID_" seguida do título sem espaços (ex: "ID_RELATORIOVENDAS").

# Dica: Use .upper() e .replace(' ', '').

# 4. Método de Classe (Construtor Alternativo)
# Crie um método de classe chamado criar_relatorio_padrao.

# Ele deve receber apenas o ano (ex: 2024).

# O método deve gerar um titulo padrão (ex: "Relatorio Anual [ano]") e, em seguida, retornar uma nova instância da classe chamando o construtor padrão com esse título.

# 5. Método de Instância
# Crie um método de instância chamado imprimir_info que retorna uma string contendo:

# O título do relatório.

# O ID (usando o método estático para gerá-lo a partir do título).

# O total de relatórios criados até o momento (acessando o atributo de classe).

# O foco é ver o @classmethod criar um título padrão, o __init__ contar o objeto criado, e o método de instância usar o @staticmethod e o atributo de classe.

class Relatorio():
    total_relatorios_criados = 0

    def __init__(self, titulo):
        self.titulo = titulo
        Relatorio.total_relatorios_criados += 1
    
    @staticmethod
    def gerar_identificador(titulo):
        return f'ID_{titulo.replace(' ', '').upper()}'
    
    @classmethod
    def criar_relatorio_padrao(cls, ano):
        titulo = f'Relatorio Anual {ano}'
        return cls(titulo)
    
    def imprimir_info(self):
        return f'titulo: {self.titulo} - ID: {self.gerar_identificador(self.titulo)} - total {self.total_relatorios_criados}'