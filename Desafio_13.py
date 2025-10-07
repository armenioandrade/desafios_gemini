# Crie uma classe chamada Mensagem com um construtor que recebe texto e autor.

# Método Estático (@staticmethod):

# Crie formatar_data().

# Ele deve retornar uma string simulada de data/hora, por exemplo: "Enviado em 15:00h".

# Método de Classe (@classmethod):

# Crie criar_mensagem_anonima(cls, texto).

# Este método deve chamar o construtor padrão, passando o texto fornecido e definindo o autor como "Anônimo".

# Deve retornar a nova instância.

# Método de Instância:

# Crie detalhes().

# Deve retornar uma string combinando o texto, o autor e o resultado do método estático formatar_data().

class Mensagem():

    def __init__(self, texto, autor):
        self.texto = texto
        self.autor = autor
    
    @staticmethod
    def formatar_data():
        return 'enviado em 15:00h'
    
    @classmethod
    def criar_mensagem_anonima(cls, texto):
        return cls(texto, 'Anônimo')

    def detalhes(self):
        return f'texto: "{self.texto}" , autor {self.autor}, {self.formatar_data()}'

msg = Mensagem('aprendizado deve ser constante', 'armenio')
print(msg.detalhes())

msg_2 = Mensagem.criar_mensagem_anonima('não acredite em tudo que dizem')
print(msg_2.detalhes())
