class Item():


    def __init__(self, nome_item, valor_item):
        self.nome_item = nome_item
        self.valor_item = valor_item
        self.quantidade = 0    

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
 
    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, nova_quantidade):
        if not isinstance(nova_quantidade, int) or nova_quantidade <= 0:
            raise ValueError("A quantidade deve ser um número inteiro positivo.")
        self._quantidade = nova_quantidade

    def adicionar_quantidade(self, quantidade):
        self.quantidade = quantidade
    
    def listar_itens(self):
        return f'QUANTIDADE - NOME DO ITEM\n{self._quantidade} | {self.nome_item}'