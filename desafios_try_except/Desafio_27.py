# Você precisa de uma classe Pedido (com @property e raise) e uma função registrar_compra (com try/except).

# 1. Classe Componente: Pedido
# Setter de quantidade: Deve lançar TypeError (se não for int) ou ValueError (se for ≤0).

# 2. Função Principal: registrar_compra(valor_entrada)
# Deve usar try/except para capturar o TypeError e o ValueError lançados pelo setter.

class Pedido():

    def __init__(self, quantidade):
        # CORRETO: Chama o setter para validar na inicialização
        self.quantidade = quantidade
    
    @property
    def quantidade(self):
        return self._quantidade
    
    @quantidade.setter
    def quantidade(self, nova_quantidade):
        
        # CORREÇÃO 1: Validação de TIPO PRIMEIRO
        if not isinstance(nova_quantidade, int):
            raise TypeError("A quantidade deve ser um número inteiro.")
            
        # Validação de VALOR
        if nova_quantidade <= 0:
            # Melhor Prática: Incluir mensagem no raise
            raise ValueError("A quantidade deve ser maior que zero.") 
            
        self._quantidade = nova_quantidade


# CORREÇÃO 2: Função externa para simular o uso na aplicação
def registrar_compra(valor_entrada):
    try:
        # Tenta criar a instância, o que chama o setter e pode lançar erro
        pedido = Pedido(valor_entrada) 
        
        # Bloco ELSE implícito: Se o código acima rodar sem erro, ele continua aqui
        print(f"Pedido registrado com sucesso. Quantidade: {pedido.quantidade}")
        
    except (ValueError, TypeError):
        # Captura os dois tipos de exceção lançados pelo setter
        # Mensagem genérica pedida no desafio:
        print("Falha ao registrar pedido: O valor fornecido é inválido ou de um tipo incorreto.")


# --- Testes de Cenário ---

print("--- Teste 1: Sucesso ---")
registrar_compra(5)

print("\n--- Teste 2: Falha por Valor (-2) ---")
registrar_compra(-2) # Setter lança ValueError -> except

print("\n--- Teste 3: Falha por Tipo (Float) ---")
registrar_compra(10.5) # Setter lança TypeError -> except

print("\n--- Teste 4: Falha por Tipo (String) ---")
# O construtor recebe "dez", o setter lança TypeError -> except
registrar_compra("dez")
