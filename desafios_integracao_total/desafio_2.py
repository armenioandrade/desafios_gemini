# Crie um sistema para criar orçamento
# O sistema deve ter quatro classes: Pessoa, Funcionário, Cliente, Orcamento, Item

# Pessoa deve ter um construtor com nome

# Funcionario e Cliente devem herdar de pessoa adicionando os seguinte atributos:
# Para Funcionario: login e senha
# Para Cliente: cpf

# Item deve ter um construtor com nome do item e valor
# Orçamento deve ter um Item, um Cliente e um Funcionario

# Faça seu melhor para usar todos os conceitos aprendidos

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

class Item():

    quantidade = 0    

    def __init__(self, nome_item, valor_item):
        self.nome_item = nome_item
        self.valor_item = valor_item

    @property
    def nome_item(self):
        return self._nome_item

    @nome_item.setter
    def nome_item(self, novo_nome):
        try:
            if not isinstance(novo_nome, str):
                raise TypeError('Tipo precisa ser texto')
        except TypeError as t:
            print('Erro no cadastro do item: ',t)
        else:
            self._nome_item = novo_nome
            print('item cadastrado!')

    @property
    def valor_item(self):
        return self._valor_item
    
    @valor_item.setter
    def valor_item(self, novo_valor):
        try:
            if not isinstance(novo_valor, (float, int)):
                raise TypeError('Tipo do item precisa ser numérico')

            if novo_valor <= 0:
                raise ValueError('valor do item não pode ser menor ou igual a zero')
        
        except TypeError as t:
            print('Erro no tipo do item: ', t)
        except ValueError as v:
            print('Erro no valor do item: ', v)
        else:
            self._valor_item = novo_valor
            print('valor do item cadastrado!')
 
    def adicionar_quantidade(self, quantidade):
        self.quantidade = quantidade
    
    def listar_itens(self):
        return f'QUANTIDADE - NOME DO ITEM\n{self.quantidade} | {self.nome_item}'

class Orcamento():
    def __init__(self, nome_cliente, cpf, nome_funcionario, login, senha, nome_item, valor_item):
        self.cliente = Cliente(nome_cliente, cpf)
        self.funcionario = Funcionario(nome_funcionario, login, senha)
        self.item = Item(nome_item, valor_item)
    
    def gerar_orcamento(self):
        try:
            with open('orcamento.txt', 'w') as f:
                f.write('ORCAMENTO SIMPLES\n')
                f.write('*' * 30 + '\n')
                f.write('DADOS DO CLIENTE' + '\n')
                f.write(f'NOME: {self.cliente.nome}\n')
                f.write(f'CPF: {self.cliente.cpf}\n')
                f.write('*' * 30 + '\n')
                f.write('DADOS DO FUNCIONARIO' + '\n')
                f.write(f'NOME: {self.funcionario.nome}\n')
                f.write(f'LOGIN: {self.funcionario.login}\n')
                f.write('*' * 30 + '\n')
                f.write('ITENS DO ORCAMENTO\n')
                f.write(self.item.listar_itens())
        except Exception as e:
            print('Erro a tratar ', e)
        
orc1 = Orcamento('amaro','12345','armenio','armenio.andrade', 1234, 'iphone', 1000)
orc1.item.adicionar_quantidade(10)
orc1.gerar_orcamento()
                
