class Pessoa():

    def __init__(self, nome):
        self.nome = nome
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novo_nome):
        try:
            if not isinstance(novo_nome, (str)):
                raise TypeError('O tipo precisa ser texto')
        except TypeError as t:
            print('Erro na definição do nome: ', t)
        else:
            self._nome = novo_nome
            print('nome cadastrado!')

class Cliente(Pessoa):

    def __init__(self, nome, cpf):
        super().__init__(nome)
        self.cpf = cpf
    
    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, novo_cpf):
        try:
            if not isinstance(novo_cpf, str):
                raise TypeError('Tipo precisa ser texto')
        except TypeError as t:
            print('Erro no cadastro do cpf: ',t)
        else:
            self._cpf = novo_cpf.replace('.','').replace('-','')
            print('cpf cadastrado!')

class Funcionario(Pessoa):

    def __init__(self, nome, login, senha):
        super().__init__(nome)
        self.login = login
        self.senha = senha
    
    @property
    def login(self):
        return self._login
    
    @login.setter
    def login(self, novo_login):
        try:
            if not isinstance(novo_login, (str)):
                raise TypeError('O tipo precisa ser texto')
        except TypeError as t:
            print('Erro na definição do login: ', t)
        else:
            self._login = novo_login
            print('login cadastrado!')
    
    @property
    def senha(self):
        return self._senha
    
    @senha.setter
    def senha(self, nova_senha):
        try:
            if not isinstance(nova_senha, int):
                raise TypeError('Senha precisa ser numérica')
            
            if nova_senha <= 1000:
                raise ValueError('Senha precisa ter no mínimo 4 dígitos')
        except TypeError as t:
            print('Erro na definição da senha: ', t)
        except ValueError as v:
            print('Erro na definição da senha: ', v)
        else:
            self._senha = nova_senha
            print('senha cadastrada!')