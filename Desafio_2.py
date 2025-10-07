# Desafio 2: Simulação de uma Conta Bancária
# Crie uma classe chamada ContaBancaria.

# Atributos: Deve ter um atributo para o saldo, que deve ser inicializado como 0 por padrão.

# Métodos:

# Um método __init__ (sem parâmetros além de self) para iniciar a conta.

# Um método depositar(valor) que aumenta o saldo.

# Um método sacar(valor) que diminui o saldo, mas apenas se o saldo for suficiente. Se não for, deve retornar uma mensagem de erro ou False.

# Um método ver_saldo que retorna o saldo atual.

# O desafio aqui é gerenciar o estado (saldo) de forma segura (encapsulamento básico).

class ContaBancaria():

    
    def __init__(self, agencia, numero_conta):
        self.saldo = float(0)
        self.agencia = int(agencia)
        self.numero_conta = int(numero_conta)
    
    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print('saque realizado')
            return True
        else:
            print('saque impossivel. saldo insuficiente')
            return False
    
    def ver_saldo(self):
        return self.saldo

    def detalhes_contas(self):
        return f'{self.agencia}, {self.numero_conta}, {self.saldo}'
    
cliente = ContaBancaria(1,1)
print(cliente.detalhes_contas())
cliente.depositar(10)
print(cliente.detalhes_contas())
cliente.sacar(1)
print(cliente.detalhes_contas())
cliente.sacar(100)
print(cliente.detalhes_contas())