# Crie uma classe chamada Usuario.

# 1. Construtor (__init__)
# Deve receber nome e _idade.

# Inicialize o nome e o atributo privado _idade.

# Lembrete: O underscore inicial (_idade) é apenas uma convenção em Python que sinaliza: "Este atributo não deve ser acessado diretamente fora da classe."

# 2. Getter (@property)
# Crie um método chamado idade e decore-o com @property.

# Este método deve apenas retornar o valor de self._idade.

# Função: Permite ler a idade como se fosse um atributo (ex: usuario.idade).

# 3. Setter (@idade.setter)
# Crie outro método chamado idade (com o mesmo nome do getter) e decore-o com @idade.setter.

# Este método deve receber um valor (novo_valor).

# Regra de Validação: Se novo_valor for menor que zero (idade negativa), lance um erro (raise ValueError("A idade não pode ser negativa.")).

# Se for válido, atribua o valor a self._idade.

# Função: Permite escrever no atributo (ex: usuario.idade = 30), mas garante que a validação seja aplicada primeiro.

class Usuario():

    def __init__(self, nome, idade_inicial, peso_inicial):
        self.nome = nome
        self.idade = idade_inicial
        self.peso = peso_inicial

    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("A idade não pode ser negativa")
        else:
            self._idade = novo_valor
    
    @property
    def peso(self):
        return self._peso
    
    @peso.setter
    def peso(self, novo_peso):
        self._peso = novo_peso # Atribui ao atributo privado '_peso'
    
armenio = Usuario('armenio', 35)
print(armenio.idade)
armenio.idade = 36
print(armenio.idade)
armenio.idade = -5
