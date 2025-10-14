# Crie duas classes: Pessoa (que usa propriedades) e Gerenciador (que usa Composição).

# 1. Classe Componente: Pessoa
# O foco é garantir que o construtor use o setter.

# Construtor (__init__): Recebe nome_inicial e idade_inicial.

# Regra: Você deve usar o @property setter para inicializar ambos os atributos. (Isso é uma ótima prática de segurança).

# Propriedade: nome (@property e @setter)

# Setter: Garante que o nome tenha mais de 2 caracteres. Se não, lance ValueError. Atribua a self._nome.

# Propriedade: idade (@property e @setter)

# Setter: Garante que a idade seja maior que 0. Se não, lance ValueError. Atribua a self._idade.

# 2. Classe Principal: Gerenciador
# O foco é na Composição e no acesso correto.

# Construtor (__init__):

# Cria uma instância de Pessoa com valores iniciais válidos (ex: "Alex", 25). Armazene-a em self.usuario.

# Método de Instância: mudar_dados(novo_nome, nova_idade)

# Este método deve:

# Usar o setter de nome do objeto Pessoa para aplicar novo_nome.

# Usar o setter de idade do objeto Pessoa para aplicar nova_idade.

class Pessoa():

    def __init__(self, nome_inicial, idade_inicial):
        # CORRETO: Chama os setters para validar na inicialização
        self.nome = nome_inicial
        self.idade = idade_inicial
    
    # --- PROPRIEDADE NOME ---
    @property
    def nome(self):
        # Retorna o valor armazenado
        return self._nome 
    
    @nome.setter
    def nome(self, novo_valor):
        # CORREÇÃO 1: Lança erro se a regra for FALHA (<= 2 caracteres)
        if len(novo_valor) <= 2:
            raise ValueError("Nome muito pequeno. Deve ter mais de 2 caracteres.")
        else:
            self._nome = novo_valor # Atribuição segura
    
    # --- PROPRIEDADE IDADE ---
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, novo_valor):
        if novo_valor < 0:
            raise ValueError("Idade não pode ser menor que zero.")
        else:
            self._idade = novo_valor # Atribuição segura

class Gerenciador():

    def __init__(self):
        # Cria a instância Pessoa (Composição)
        self.usuario = Pessoa('Alex', 25)
    
    def mudar_dados(self, nome, idade):
        # CORREÇÃO 2: Usa o NOME DA PROPRIEDADE para chamar o SETTER (validação)
        self.usuario.nome = nome 
        self.usuario.idade = idade 
        
        # Leitura via GETTER da propriedade
        return f'Sucesso! Nome: {self.usuario.nome}, Idade: {self.usuario.idade}'

# --- Teste de Uso ---
gerenciador = Gerenciador()

# Teste 1: Mudança bem-sucedida (SETTER é chamado)
print(gerenciador.mudar_dados("Armenio", 36))

# Teste 2: Falha na validação do NOME (SETTER lança erro)
try:
    gerenciador.mudar_dados("A", 40)
except ValueError as e:
    print(f"Erro capturado (Esperado): {e}")

# Teste 3: Falha na validação da IDADE (SETTER lança erro)
try:
    gerenciador.mudar_dados("Armenio", -5)
except ValueError as e:
    print(f"Erro capturado (Esperado): {e}")

