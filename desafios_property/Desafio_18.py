# Crie uma classe chamada SistemaUsuario.

# Construtor: Recebe e inicializa _username e _senha.

# Getter (@property): Crie um método username que retorna self._username.

# Propriedade de Segurança: Crie um método senha e decore-o com @property.

# Ele deve retornar uma string oculta, como por exemplo: "******".

# Não crie um setter para a senha.

# Objetivo: Qualquer tentativa de ler usuario.senha retorna uma string genérica e qualquer tentativa de escrever usuario.senha = 'nova' resultará em um erro de Python, garantindo a segurança de leitura.

class SistemaUsuario():

    def __init__(self, username, senha):
        # Chama o @username.setter (para fins de boa prática, caso haja validação futura)
        self.username = username 
        
        # Armazena a senha no atributo privado, sem passar pelo getter/setter, 
        # pois não queremos que a leitura/escrita acione lógica complexa.
        self._senha = senha 
    
    # --- PROPRIEDADE USERNAME (Permite Leitura/Escrita) ---
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, novo_username):
        # Aqui poderia haver validação. Apenas atribuímos ao privado.
        self._username = novo_username
    
    # --- PROPRIEDADE SENHA (Somente Leitura) ---
    @property
    def senha(self):
        # Retorna o valor criptografado/mascarado sem expor o self._senha real.
        return f'*******' 
    
# --- Teste de Uso ---
user_armenio = SistemaUsuario('armenio', '1234')

# 1. Leitura de username (GETTER):
print(f"Username: {user_armenio.username}") 

# 2. Leitura de senha (GETTER, mas retorna mascarado):
print(f"Senha (mascarada): {user_armenio.senha}") 

# 3. Tenta escrever na senha (lança erro, como esperado):
try:
    user_armenio.senha = 'nova_senha'
except AttributeError as e:
    print(f"\nErro esperado: {e}")