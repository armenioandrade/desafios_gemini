from Pessoa import Cliente, Funcionario
from Item import Item

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