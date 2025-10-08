# Crie uma classe chamada Config.

# Atributo de Classe:

# Crie um atributo de classe chamado AMBIENTE_PADRAO e defina o valor como 'Desenvolvimento'.

# Método de Classe (@classmethod):

# Crie mudar_ambiente_para_producao(cls).

# Este método deve modificar o atributo de classe AMBIENTE_PADRAO para 'Produção'.

# Deve retornar o novo valor.

# Método de Classe (@classmethod):

# Crie ver_ambiente(cls).

# Este método deve apenas retornar o valor atual de AMBIENTE_PADRAO.

# O foco aqui é no @classmethod acessando e modificando o estado da CLASSE.

class Config():
    AMBIENTE_PADRAO = 'Desenvolvimento'

    @classmethod
    def mudar_para_producao(cls):
        cls.AMBIENTE_PADRAO = 'Produção'
        return cls.AMBIENTE_PADRAO
    
    @classmethod
    def ver_ambiente(cls):
        return cls.AMBIENTE_PADRAO

print(Config.ver_ambiente())
print(Config.mudar_para_producao())