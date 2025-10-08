# Produto com Validação de Preço
# Crie uma classe chamada Produto.

# Construtor: Recebe e inicializa nome e a propriedade preco (lembre-se de chamar o setter na inicialização).

# Getter (@property): Crie um método preco que retorna self._preco.

# Setter (@preco.setter): Crie um método preco que recebe novo_valor.

# Regra de Validação: Se novo_valor for menor ou igual a zero, lance um erro (raise ValueError("O preço deve ser maior que zero.")).

# Se for válido, atribua a self._preco.

class Produto():
    
    def __init__(self, preco):
        self.preco = preco
    
    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_valor):
        if novo_valor <= 0:
            raise ValueError("O preço deve ser maior que zero")
        else:
            self._preco = novo_valor