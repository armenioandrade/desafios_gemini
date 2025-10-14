# As Generator Expressions (Geração por Expressão) são visualmente idênticas às List Comprehensions, 
# mas usam parênteses () em vez de colchetes [].

# A diferença: Elas não criam a lista inteira na memória; elas geram os valores sob demanda (lazy evaluation).

# Seu desafio é transformar uma List Comprehension que calcula o 
# quadrado dos números em uma Generator Expression e, em seguida, 
# calcular a soma total desses números gerados.
# 1. Lista Inicial
# Python

# numeros = [1, 2, 3, 4, 5]
# 2. Criação do Gerador
# Crie uma Generator Expression para calcular o quadrado de cada número (numero * numero).

# Armazene-a na variável quadrados_gerador.

# 3. Execução
# Use a função sum() para forçar o gerador a calcular e somar todos os valores.

# Avise-me quando tiver a solução!

numeros = [1, 2, 3, 4, 5]

quadrados_gerador = (item_numero * item_numero for item_numero in numeros)

print(sum(quadrados_gerador))
