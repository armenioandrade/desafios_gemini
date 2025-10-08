# Crie uma classe chamada ItemEstoque.

# 1. Construtor
# Recebe nome e quantidade. Inicialize self.nome e use o setter para inicializar self.quantidade.

# 2. Propriedade quantidade (Getter e Setter)
# Getter (@property): Retorna self._quantidade.

# Setter (@quantidade.setter): Deve aplicar duas regras de validação ao novo_valor:

# Validação de Tipo: Verifique se o novo_valor é um número inteiro (int). Se não for, lance um erro: raise TypeError("Quantidade deve ser um número inteiro.").

# Validação de Valor: Verifique se o novo_valor é menor que zero. Se for, lance um erro: raise ValueError("Quantidade não pode ser negativa.").

# Se passar nas duas validações, atribua a self._quantidade.

# 3. Propriedade status (Cálculo Dinâmico)
# Crie uma propriedade somente leitura (@property) chamada status.

# Esta propriedade deve retornar dinamicamente:

# "Baixo" se self._quantidade for menor que 10.

# "Suficiente" se self._quantidade for maior ou igual a 10.

class ItemEstoque():

    def __init__(self, nome, quantidade):
        self.nome = nome
        self.quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, novo_valor):
        if not isinstance(novo_valor, int):
            raise TypeError("Quantidade deve ser um número inteiro")
        if novo_valor < 0:
            raise ValueError("Quantidade não pode ser negativa")

        self._quantidade = novo_valor
    
    @property
    def status(self):
        if self._quantidade < 10:
            return 'Baixo'
        else:
            return 'Suficiente'

iphones = ItemEstoque('iphone', 30)
print(iphones.quantidade)
